"""
Moduł Modulator: README Generator Pro v2.2
polsoft.ITS™ Group – Automatyczny generator plików README.md

Analizuje strukturę projektu, wyciąga metadane z kodu źródłowego,
analizuje Git, testy, jakość dokumentacji i generuje spójny README.md.

Nowości v2.0:
  • GitAnalyzer – branch, ostatni commit, status repo
  • TestAnalyzer – wykrywanie frameworka + komenda uruchomienia
  • DocQualityAnalyzer – raport brakujących docstringów
  • BadgeGenerator – rozszerzone odznaki shields.io
  • ChangelogGenerator – sekcja changelog z CHANGELOG.md / git log
  • UsageExampleGenerator – przykłady użycia z publicznych funkcji
  • WatchMode – monitorowanie zmian i auto-regeneracja
  • Sekcja API z typami (type hints z AST)
  • Tryb drzewa compact / full z konfigurowalną głębokością
  • readmegen.json – konfiguracja projektu
  • Panel zakładkowy GUI: Analiza / Jakość / Git / Ustawienia

Nowości v2.1:
  • UnusedFunctionDetector – wykrywanie nieużywanych publicznych symboli
  • TodoRoadmapExtractor – skanowanie TODO/FIXME → sekcja Roadmap
  • ContributingGenerator – sekcja Contributing z wykrywaniem stylu commitów
  • ModuleDependencyAnalyzer – diagram zależności między modułami Python
  • PluginManager – system pluginów analizatorów, generatorów i szablonów
  • DebugInspector – tryb debugowania z podglądem metadanych + walidacja szablonów
  • Sekcje: Roadmap, Contributing, Nieużywane symbole, Zależności modułów
  • ConfigManager – rozszerzony o disabled_sections, ignore_dirs, custom_fields

Nowości v2.2:
  • ProjectTypeDetector – auto-wykrywanie typu (CLI/web/lib/desktop/enterprise)
  • ProjectSummaryGenerator – auto-streszczenie projektu z analizy kodu
  • ApiChangeDetector – snapshot + diff publicznego API, wykrywanie breaking changes
  • ConventionalChangelogGenerator – pełny CHANGELOG.md z Conventional Commits
  • ExtendedDocsGenerator – generowanie docs/api.md, docs/usage.md, docs/configuration.md
  • ArchitectureDocGenerator – auto-dokumentacja architektury z warstw, deps, entry points
  • PreCommitHookGenerator – instalacja pre-commit hook auto-regenerującego README
  • Nowe sekcje README: Architektura, Zmiany API, type badge
  • GUI: przyciski Generuj docs / Snapshot API / Hook install / Changelog

─────────────────────────────────────────────────────────────
  Autor:    Sebastian Januchowski
  Firma:    polsoft.ITS™ Group
  E-mail:   polsoft.its@fastservice.com
  GitHub:   https://github.com/seb07uk
  Licencja: 2026 © Sebastian Januchowski & polsoft.ITS™ Group
─────────────────────────────────────────────────────────────
"""

__version__   = "2.2.0"
__author__    = "Sebastian Januchowski"
__company__   = "polsoft.ITS™ Group"
__email__     = "polsoft.its@fastservice.com"
__github__    = "https://github.com/seb07uk"
__copyright__ = "2026 © Sebastian Januchowski & polsoft.ITS™ Group"

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os, re, json, ast, threading, subprocess, time, hashlib
from pathlib import Path
from datetime import datetime
from main import BaseModule


# ══════════════════════════════════════════════════════════════════════
#  1. ProjectAnalyzer
# ══════════════════════════════════════════════════════════════════════
class ProjectAnalyzer:
    """Skanuje katalog projektu i zwraca słownik metadanych."""

    LANG_MAP = {
        ".py":"Python", ".js":"JavaScript", ".ts":"TypeScript",
        ".cs":"C#", ".go":"Go", ".rs":"Rust", ".java":"Java",
        ".cpp":"C++", ".c":"C", ".rb":"Ruby", ".php":"PHP",
        ".kt":"Kotlin", ".swift":"Swift", ".html":"HTML", ".css":"CSS",
        ".vue":"Vue", ".jsx":"React", ".tsx":"React/TS",
    }
    ENTRY_POINTS = [
        "main.py","app.py","run.py","server.py","index.js","index.ts",
        "Program.cs","main.go","main.rs","App.java","index.php","src/main.py",
    ]
    DEP_FILES = {
        "requirements.txt":"pip", "package.json":"npm",
        "pyproject.toml":"poetry/pip", "Cargo.toml":"cargo",
        "go.mod":"go mod", "Gemfile":"bundler",
        "pom.xml":"maven", "build.gradle":"gradle",
    }
    LICENSE_NAMES = {
        "mit":"MIT", "apache":"Apache 2.0", "gpl":"GPL",
        "lgpl":"LGPL", "bsd":"BSD", "mozilla":"MPL",
        "isc":"ISC", "cc0":"CC0",
    }
    IGNORE = {"__pycache__","node_modules","venv",".git",".idea",
               ".vscode","dist","build","target","bin","obj"}

    def analyze(self, root: str, tree_mode: str = "compact", tree_depth: int = 2) -> dict:
        root = Path(root)
        ext_count = {}
        files_list, dirs_set = [], set()

        for p in root.rglob("*"):
            if any(part.startswith(".") or part in self.IGNORE for part in p.parts):
                continue
            if p.is_file():
                ext_count[p.suffix] = ext_count.get(p.suffix, 0) + 1
                files_list.append(p)
            elif p.is_dir():
                rel = p.relative_to(root).parts
                if rel:
                    dirs_set.add(rel[0])

        lang = "Nieznany"
        best = 0
        lang_stats = {}
        for ext, cnt in ext_count.items():
            name = self.LANG_MAP.get(ext)
            if name:
                lang_stats[name] = lang_stats.get(name, 0) + cnt
                if cnt > best:
                    best, lang = cnt, name

        entry = next((ep for ep in self.ENTRY_POINTS if (root / ep).exists()), None)

        deps_info = {}
        for df, mgr in self.DEP_FILES.items():
            fp = root / df
            if fp.exists():
                deps_info[df] = {"manager": mgr, "content": self._read_deps(fp, df)}

        license_name = self._detect_license(root)
        has_tests, test_files = self._detect_tests(files_list)
        configs = [f.name for f in files_list
                   if f.name in (".env.example","config.json",".env","settings.py",
                                 "config.yaml","config.yml","appsettings.json",".readmegen.json")]

        tree = self._build_tree(root, max_depth=tree_depth, compact=(tree_mode == "compact"))

        total_bytes = sum(f.stat().st_size for f in files_list if f.exists())
        repo_size_kb = round(total_bytes / 1024, 1)

        return {
            "root": str(root), "name": root.name,
            "language": lang, "lang_stats": lang_stats,
            "entry": entry or "brak",
            "deps": deps_info, "license": license_name,
            "has_tests": has_tests, "test_files": test_files,
            "configs": configs, "tree": tree,
            "file_count": len(files_list), "dir_count": len(dirs_set),
            "repo_size_kb": repo_size_kb,
        }

    def _read_deps(self, fp, filename):
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            if filename == "requirements.txt":
                return [l.strip() for l in text.splitlines()
                        if l.strip() and not l.startswith("#")][:20]
            if filename == "package.json":
                data = json.loads(text)
                return (list(data.get("dependencies", {}).keys()) +
                        list(data.get("devDependencies", {}).keys()))[:20]
            if filename == "pyproject.toml":
                return [l.strip() for l in text.splitlines()
                        if "=" in l and not l.startswith("[") and not l.startswith("#")][:15]
        except Exception:
            pass
        return []

    def _detect_license(self, root):
        for name in ("LICENSE", "LICENSE.txt", "LICENSE.md", "LICENCE"):
            fp = root / name
            if fp.exists():
                content = fp.read_text(errors="ignore").lower()
                for key, val in self.LICENSE_NAMES.items():
                    if key in content:
                        return val
                return "Własna"
        return "Brak"

    def _detect_tests(self, files):
        test_files = [f for f in files
                      if f.name.startswith("test") or f.name.endswith("_test.py")
                      or "tests" in str(f).lower() or "spec" in f.name.lower()]
        return bool(test_files), [str(f.name) for f in test_files[:10]]

    def _build_tree(self, root, max_depth=2, compact=True):
        lines = [f"{root.name}/"]
        self._tree_walk(root, "", lines, 0, max_depth, compact)
        return "\n".join(lines)

    def _tree_walk(self, path, prefix, lines, depth, max_depth, compact):
        if depth >= max_depth:
            return
        limit = 12 if compact else 40
        children = sorted(
            [p for p in path.iterdir()
             if not p.name.startswith(".") and p.name not in self.IGNORE],
            key=lambda p: (p.is_file(), p.name.lower())
        )[:limit]
        for i, child in enumerate(children):
            connector = "└── " if i == len(children) - 1 else "├── "
            icon = "📁 " if child.is_dir() else "📄 "
            lines.append(f"{prefix}{connector}{icon}{child.name}{'/' if child.is_dir() else ''}")
            if child.is_dir():
                ext = "    " if i == len(children) - 1 else "│   "
                self._tree_walk(child, prefix + ext, lines, depth + 1, max_depth, compact)


# ══════════════════════════════════════════════════════════════════════
#  2. MetadataExtractor – z typami z AST
# ══════════════════════════════════════════════════════════════════════
class MetadataExtractor:
    """Czyta metadane, docstringi, type hints i manifesty."""

    def extract(self, root: str) -> dict:
        root = Path(root)
        meta = {"version": "", "author": "", "description": "",
                "functions": [], "classes": [], "missing_docs": []}

        for candidate in ("main.py", "app.py", "__init__.py", "run.py"):
            fp = root / candidate
            if fp.exists():
                meta.update(self._parse_python(fp))
                break

        pj = root / "package.json"
        if pj.exists():
            try:
                data = json.loads(pj.read_text(encoding="utf-8"))
                if not meta["version"]:     meta["version"]     = data.get("version", "")
                if not meta["author"]:      meta["author"]      = str(data.get("author", ""))
                if not meta["description"]: meta["description"] = data.get("description", "")
            except Exception:
                pass
        return meta

    def _parse_python(self, fp):
        result = {"version": "", "author": "", "description": "",
                  "functions": [], "classes": [], "missing_docs": []}
        try:
            source = fp.read_text(encoding="utf-8", errors="ignore")
            tree   = ast.parse(source)

            mod_doc = ast.get_docstring(tree)
            if mod_doc:
                result["description"] = mod_doc.strip().splitlines()[0][:120]

            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    for t in node.targets:
                        if isinstance(t, ast.Name) and isinstance(node.value, ast.Constant):
                            val = str(node.value.value)
                            if t.id == "__version__" and not result["version"]:
                                result["version"] = val
                            if t.id == "__author__" and not result["author"]:
                                result["author"] = val

                if isinstance(node, ast.FunctionDef) and not node.col_offset:
                    doc  = ast.get_docstring(node) or ""
                    args = self._extract_args(node)
                    ret  = self._extract_return(node)
                    result["functions"].append({
                        "name": node.name, "args": args, "return": ret,
                        "doc": doc.splitlines()[0][:80] if doc else "",
                    })
                    if not doc:
                        result["missing_docs"].append(f"def {node.name}()")

                if isinstance(node, ast.ClassDef) and not node.col_offset:
                    doc     = ast.get_docstring(node) or ""
                    methods = []
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            m_doc  = ast.get_docstring(item) or ""
                            m_args = self._extract_args(item)
                            m_ret  = self._extract_return(item)
                            methods.append({
                                "name": item.name, "args": m_args,
                                "return": m_ret, "doc": m_doc.splitlines()[0][:80] if m_doc else "",
                            })
                            if not m_doc and not item.name.startswith("_"):
                                result["missing_docs"].append(f"{node.name}.{item.name}()")
                    result["classes"].append({
                        "name": node.name,
                        "doc":  doc.splitlines()[0][:80] if doc else "",
                        "methods": methods,
                    })
                    if not doc:
                        result["missing_docs"].append(f"class {node.name}")
        except Exception:
            pass
        return result

    def _extract_args(self, node):
        args = []
        for a in node.args.args:
            if a.arg == "self":
                continue
            ann = ""
            if a.annotation:
                try:
                    ann = ast.unparse(a.annotation)
                except Exception:
                    pass
            args.append(f"{a.arg}: {ann}" if ann else a.arg)
        return args

    def _extract_return(self, node):
        if node.returns:
            try:
                return ast.unparse(node.returns)
            except Exception:
                pass
        return ""


# ══════════════════════════════════════════════════════════════════════
#  3. GitAnalyzer
# ══════════════════════════════════════════════════════════════════════
class GitAnalyzer:
    """Pobiera informacje z repozytorium Git (subprocess, brak zależności)."""

    def analyze(self, root: str) -> dict:
        result = {
            "is_git": False, "branch": "", "last_commit_hash": "",
            "last_commit_msg": "", "last_commit_date": "",
            "last_commit_author": "", "commits_count": 0,
            "remote_url": "", "status_clean": True,
            "changelog_entries": [],
        }
        git_dir = Path(root) / ".git"
        if not git_dir.exists():
            return result

        result["is_git"] = True

        def git(args):
            try:
                r = subprocess.run(["git"] + args, cwd=root,
                                   capture_output=True, text=True, timeout=5)
                return r.stdout.strip()
            except Exception:
                return ""

        result["branch"]             = git(["rev-parse", "--abbrev-ref", "HEAD"])
        result["last_commit_hash"]   = git(["log", "-1", "--format=%h"])
        result["last_commit_msg"]    = git(["log", "-1", "--format=%s"])
        result["last_commit_date"]   = git(["log", "-1", "--format=%ci"])[:10]
        result["last_commit_author"] = git(["log", "-1", "--format=%an"])
        count = git(["rev-list", "--count", "HEAD"])
        result["commits_count"]      = int(count) if count.isdigit() else 0
        result["remote_url"]         = git(["remote", "get-url", "origin"])
        result["status_clean"]       = (git(["status", "--porcelain"]) == "")
        log = git(["log", "--oneline", "-10", "--pretty=format:%h %s (%ci)"])
        result["changelog_entries"]  = [l for l in log.splitlines() if l][:10]
        return result


# ══════════════════════════════════════════════════════════════════════
#  4. TestAnalyzer
# ══════════════════════════════════════════════════════════════════════
class TestAnalyzer:
    """Wykrywa framework testów i generuje komendę uruchomienia."""

    FRAMEWORKS = {
        "pytest":     {"files": ["pytest.ini", "setup.cfg", "pyproject.toml"],
                       "imports": ["pytest"], "cmd": "pytest"},
        "unittest":   {"files": [], "imports": ["unittest"],
                       "cmd": "python -m unittest discover"},
        "jest":       {"files": ["jest.config.js", "jest.config.ts"],
                       "imports": [], "cmd": "npm test"},
        "mocha":      {"files": [".mocharc.js", ".mocharc.yml"],
                       "imports": [], "cmd": "npm test"},
        "go test":    {"files": [], "imports": [], "cmd": "go test ./..."},
        "cargo test": {"files": ["Cargo.toml"], "imports": [], "cmd": "cargo test"},
    }

    def analyze(self, root: str, test_files: list) -> dict:
        root = Path(root)
        result = {"framework": "", "command": "", "test_count": len(test_files),
                  "test_files": test_files}

        for fw, info in self.FRAMEWORKS.items():
            for cfg in info["files"]:
                if (root / cfg).exists():
                    result["framework"] = fw
                    result["command"]   = info["cmd"]
                    return result

        for tf in test_files:
            fp = root / tf
            if not fp.exists():
                continue
            try:
                src = fp.read_text(errors="ignore")
                for fw, info in self.FRAMEWORKS.items():
                    for imp in info.get("imports", []):
                        if imp in src:
                            result["framework"] = fw
                            result["command"]   = info["cmd"]
                            return result
            except Exception:
                pass

        if test_files:
            result["framework"] = "pytest"
            result["command"]   = "pytest"
        return result


# ══════════════════════════════════════════════════════════════════════
#  5. DocQualityAnalyzer
# ══════════════════════════════════════════════════════════════════════
class DocQualityAnalyzer:
    """Analizuje jakość dokumentacji — brakujące docstringi, raport."""

    IGNORE = {"__pycache__", "venv", ".git", "node_modules", "dist", "build"}

    def analyze(self, root: str) -> dict:
        root        = Path(root)
        total_items = 0
        missing     = []
        has_readme   = (root / "README.md").exists() or (root / "README.rst").exists()
        has_license  = any((root / n).exists() for n in
                           ("LICENSE", "LICENSE.txt", "LICENSE.md", "LICENCE"))
        has_changelog = any((root / n).exists() for n in
                            ("CHANGELOG.md", "CHANGELOG.txt", "CHANGES.md", "HISTORY.md"))

        for fp in root.rglob("*.py"):
            if any(p in self.IGNORE for p in fp.parts):
                continue
            try:
                src  = fp.read_text(encoding="utf-8", errors="ignore")
                tree = ast.parse(src)
                rel  = fp.relative_to(root)

                if not ast.get_docstring(tree):
                    missing.append(f"📄 {rel} — brak docstringa modułu")
                    total_items += 1

                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                        total_items += 1
                        if not ast.get_docstring(node):
                            name = getattr(node, "name", "?")
                            if not name.startswith("_"):
                                kind = type(node).__name__.replace("Def", "")
                                missing.append(f"  ↳ {rel}:{node.lineno} — {kind} `{name}`")
            except Exception:
                pass

        score = max(0, 100 - int(len(missing) / max(total_items, 1) * 100)) if total_items else 100
        return {
            "score": score, "missing": missing[:40],
            "total_items": total_items, "missing_count": len(missing),
            "has_readme": has_readme, "has_license": has_license,
            "has_changelog": has_changelog,
        }


# ══════════════════════════════════════════════════════════════════════
#  6. BadgeGenerator
# ══════════════════════════════════════════════════════════════════════
class BadgeGenerator:
    """Generuje odznaki shields.io dla różnych metadanych projektu."""

    LANG_COLORS = {
        "Python": "3776AB", "JavaScript": "F7DF1E", "TypeScript": "3178C6",
        "Go": "00ADD8", "Rust": "000000", "C#": "239120", "Java": "007396",
        "C++": "00599C", "Ruby": "CC342D", "PHP": "777BB4", "Kotlin": "7F52FF",
    }

    def generate(self, project: dict, meta: dict, git: dict,
                 tests: dict, style: str = "flat") -> list:
        badges  = []
        ver     = meta.get("version") or "1.0.0"
        lang    = project.get("language", "")
        lic     = project.get("license", "Brak").replace(" ", "-")
        size_kb = project.get("repo_size_kb", 0)
        size    = f"{size_kb}KB" if size_kb < 1024 else f"{round(size_kb/1024,1)}MB"
        lc      = self.LANG_COLORS.get(lang, "blue")

        badges.append(f"![Version](https://img.shields.io/badge/version-{ver}-brightgreen?style={style})")
        badges.append(f"![Language](https://img.shields.io/badge/language-{lang}-{lc}?style={style})")
        badges.append(f"![License](https://img.shields.io/badge/license-{lic}-blue?style={style})")
        badges.append(f"![Size](https://img.shields.io/badge/size-{size}-lightgrey?style={style})")
        badges.append(f"![Files](https://img.shields.io/badge/files-{project.get('file_count',0)}-informational?style={style})")

        if project.get("has_tests"):
            fw = tests.get("framework", "") or "tests"
            badges.append(f"![Tests](https://img.shields.io/badge/tests-{fw}-success?style={style})")
        else:
            badges.append(f"![Tests](https://img.shields.io/badge/tests-none-critical?style={style})")

        if git.get("is_git"):
            branch = git.get("branch", "main")
            clean  = "clean" if git.get("status_clean") else "dirty"
            color  = "success" if git.get("status_clean") else "yellow"
            badges.append(f"![Branch](https://img.shields.io/badge/branch-{branch}-{color}?style={style})")
            badges.append(f"![Commits](https://img.shields.io/badge/commits-{git.get('commits_count',0)}-blue?style={style})")
            badges.append(f"![Repo](https://img.shields.io/badge/repo-{clean}-{color}?style={style})")

        return badges


# ══════════════════════════════════════════════════════════════════════
#  7. ChangelogGenerator
# ══════════════════════════════════════════════════════════════════════
class ChangelogGenerator:
    """Generuje sekcję CHANGELOG z pliku lub git log."""

    def generate(self, root: str, git: dict) -> str:
        root = Path(root)
        for fname in ("CHANGELOG.md", "CHANGELOG.txt", "CHANGES.md", "HISTORY.md"):
            fp = root / fname
            if fp.exists():
                try:
                    lines = fp.read_text(encoding="utf-8", errors="ignore").splitlines()
                    excerpt = "\n".join(lines[:30])
                    if len(lines) > 30:
                        excerpt += f"\n\n*... ({len(lines)-30} więcej linii w {fname})*"
                    return excerpt
                except Exception:
                    pass

        entries = git.get("changelog_entries", [])
        if entries:
            lines = ["### Ostatnie zmiany (git log)\n"]
            for e in entries:
                lines.append(f"- `{e}`")
            return "\n".join(lines)

        return "_Brak pliku CHANGELOG.md i historii git._"


# ══════════════════════════════════════════════════════════════════════
#  8. UsageExampleGenerator
# ══════════════════════════════════════════════════════════════════════
class UsageExampleGenerator:
    """Generuje przykłady użycia z publicznych funkcji i klas."""

    def generate(self, meta: dict, project: dict) -> str:
        lang    = project.get("language", "Python")
        name    = project.get("name", "projekt")
        classes = meta.get("classes", [])
        funcs   = meta.get("functions", [])
        examples = []

        if lang == "Python":
            if classes:
                cls = classes[0]
                methods = [m for m in cls.get("methods", [])
                           if not m["name"].startswith("_")][:2]
                ex = f"```python\nfrom {name.lower()} import {cls['name']}\n\n"
                ex += f"obj = {cls['name']}()\n"
                for m in methods:
                    args = ", ".join(
                        f'"{a.split(":")[0].strip()}"' for a in m["args"][:2]
                    )
                    ex += f"result = obj.{m['name']}({args})\n"
                ex += "```"
                examples.append(ex)

            if funcs:
                fn = funcs[0]
                args = ", ".join(
                    f'"{a.split(":")[0].strip()}"' for a in fn["args"][:2]
                )
                ex = (f"```python\nfrom {name.lower()} import {fn['name']}\n\n"
                      f"result = {fn['name']}({args})\nprint(result)\n```")
                examples.append(ex)

            if not examples:
                entry = project.get("entry", "main.py")
                examples.append(f"```bash\npython {entry}\n```")
        else:
            entry = project.get("entry", "main")
            examples.append(f"```bash\n# Uruchom projekt\npython {entry}\n```")

        return "\n\n".join(examples)


# ══════════════════════════════════════════════════════════════════════
#  9. WatchMode – polling bez zależności zewnętrznych
# ══════════════════════════════════════════════════════════════════════
class WatchMode:
    """Monitoruje zmiany w plikach projektu (polling co N sekund)."""

    IGNORE = {"__pycache__", "node_modules", "venv", ".git"}

    def __init__(self, path: str, callback, interval: float = 3.0):
        self.path     = Path(path)
        self.callback = callback
        self.interval = interval
        self._running = False
        self._thread  = None
        self._hashes  = {}

    def start(self):
        if self._running:
            return
        self._running = True
        self._hashes  = self._snapshot()
        self._thread  = threading.Thread(target=self._loop,
                                         daemon=True, name="WatchMode")
        self._thread.start()

    def stop(self):
        self._running = False

    def is_running(self):
        return self._running

    def _snapshot(self):
        snap = {}
        try:
            for fp in self.path.rglob("*"):
                if fp.is_file() and not any(p in self.IGNORE for p in fp.parts):
                    try:
                        snap[str(fp)] = hashlib.md5(fp.read_bytes()).hexdigest()
                    except Exception:
                        pass
        except Exception:
            pass
        return snap

    def _loop(self):
        while self._running:
            time.sleep(self.interval)
            new_snap = self._snapshot()
            changed  = [k for k, v in new_snap.items() if self._hashes.get(k) != v]
            added    = [k for k in new_snap if k not in self._hashes]
            removed  = [k for k in self._hashes if k not in new_snap]
            if changed or added or removed:
                self._hashes = new_snap
                try:
                    self.callback(changed=changed, added=added, removed=removed)
                except Exception:
                    pass


# ══════════════════════════════════════════════════════════════════════
#  10a. UnusedFunctionDetector – wykrywanie nieużywanych funkcji
# ══════════════════════════════════════════════════════════════════════
class UnusedFunctionDetector:
    """Wykrywa nieużywane funkcje i klasy w projekcie Python."""

    IGNORE = {"__pycache__", "venv", ".git", "node_modules", "dist", "build"}

    def analyze(self, root: str) -> dict:
        root = Path(root)
        defined = {}   # name -> (file, lineno)
        calls   = set()

        for fp in root.rglob("*.py"):
            if any(p in self.IGNORE for p in fp.parts):
                continue
            try:
                src  = fp.read_text(encoding="utf-8", errors="ignore")
                tree = ast.parse(src)
                rel  = str(fp.relative_to(root))

                for node in ast.walk(tree):
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if not node.name.startswith("_"):
                            defined[node.name] = (rel, node.lineno)
                    if isinstance(node, ast.ClassDef):
                        if not node.name.startswith("_"):
                            defined[node.name] = (rel, node.lineno)
                    if isinstance(node, ast.Call):
                        if isinstance(node.func, ast.Name):
                            calls.add(node.func.id)
                        elif isinstance(node.func, ast.Attribute):
                            calls.add(node.func.attr)
            except Exception:
                pass

        unused = [
            {"name": name, "file": info[0], "lineno": info[1]}
            for name, info in defined.items()
            if name not in calls
        ]
        return {
            "unused": unused[:30],
            "unused_count": len(unused),
            "defined_count": len(defined),
        }


# ══════════════════════════════════════════════════════════════════════
#  10b. TodoRoadmapExtractor – wykrywanie TODO/FIXME → Roadmap
# ══════════════════════════════════════════════════════════════════════
class TodoRoadmapExtractor:
    """Skanuje komentarze TODO/FIXME/HACK/NOTE w kodzie i buduje sekcję Roadmap."""

    PATTERNS = re.compile(
        r"#\s*(TODO|FIXME|HACK|NOTE|XXX|IDEA|FEATURE)[:\s]+(.+)",
        re.IGNORECASE
    )
    IGNORE = {"__pycache__", "venv", ".git", "node_modules", "dist", "build"}

    def analyze(self, root: str) -> dict:
        root  = Path(root)
        items = []

        for fp in root.rglob("*"):
            if any(p in self.IGNORE for p in fp.parts):
                continue
            if fp.suffix not in (".py", ".js", ".ts", ".cs", ".go", ".rs",
                                  ".java", ".rb", ".php", ".kt", ".swift"):
                continue
            try:
                for i, line in enumerate(
                        fp.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                    m = self.PATTERNS.search(line)
                    if m:
                        items.append({
                            "kind":    m.group(1).upper(),
                            "text":    m.group(2).strip()[:120],
                            "file":    str(fp.relative_to(root)),
                            "lineno":  i,
                        })
            except Exception:
                pass

        grouped = {}
        for item in items[:60]:
            grouped.setdefault(item["kind"], []).append(item)

        return {
            "items":   items[:60],
            "grouped": grouped,
            "count":   len(items),
        }

    def generate_section(self, data: dict) -> str:
        if not data.get("items"):
            return "_Brak zaplanowanych zadań (TODO/FIXME) w kodzie._"
        lines = []
        for kind, entries in data["grouped"].items():
            emoji = {"TODO": "🔲", "FIXME": "🐛", "HACK": "⚠️",
                     "NOTE": "📝", "IDEA": "💡", "FEATURE": "✨"}.get(kind, "•")
            lines.append(f"\n**{emoji} {kind}**\n")
            for e in entries[:8]:
                lines.append(f"- {e['text']}  *(_{e['file']}:{e['lineno']}_)*")
        total = data["count"]
        if total > 60:
            lines.append(f"\n*... i {total - 60} więcej w kodzie.*")
        return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════
#  10c. ContributingGenerator – sekcja Contributing
# ══════════════════════════════════════════════════════════════════════
class ContributingGenerator:
    """Generuje sekcję Contributing, wykrywając styl commitów i środowisko."""

    CONVENTIONAL_PATTERN = re.compile(
        r"^(feat|fix|docs|style|refactor|perf|test|chore|ci|build|revert)(\(.+\))?:",
        re.IGNORECASE
    )

    def analyze(self, root: str, git_data: dict) -> dict:
        style = self._detect_commit_style(git_data)
        env   = self._detect_env_setup(root)
        has_contributing = (Path(root) / "CONTRIBUTING.md").exists()
        return {
            "commit_style":      style,
            "env_setup":         env,
            "has_contributing":  has_contributing,
        }

    def _detect_commit_style(self, git_data: dict) -> str:
        entries = git_data.get("changelog_entries", [])
        conventional = sum(
            1 for e in entries
            if self.CONVENTIONAL_PATTERN.search(e)
        )
        if conventional >= len(entries) * 0.5 and entries:
            return "conventional"
        return "free"

    def _detect_env_setup(self, root: str) -> list:
        root  = Path(root)
        steps = []
        if (root / "requirements.txt").exists():
            steps.append("pip install -r requirements.txt")
        elif (root / "pyproject.toml").exists():
            steps.append("poetry install")
        if (root / "package.json").exists():
            steps.append("npm install")
        if (root / "Cargo.toml").exists():
            steps.append("cargo build")
        if (root / "go.mod").exists():
            steps.append("go mod download")
        if not steps:
            steps.append("# Brak pliku zależności — skonfiguruj ręcznie")
        return steps

    def generate_section(self, data: dict) -> str:
        if data.get("has_contributing"):
            return "_Szczegóły w pliku [CONTRIBUTING.md](CONTRIBUTING.md)._"

        style = data.get("commit_style", "free")
        env   = data.get("env_setup", [])

        commit_guide = (
            "Używamy **Conventional Commits**:\n"
            "```\n"
            "feat: dodaj nową funkcję\n"
            "fix: napraw błąd\n"
            "docs: aktualizacja dokumentacji\n"
            "refactor: refaktoryzacja kodu\n"
            "test: dodaj testy\n"
            "```"
        ) if style == "conventional" else (
            "Commit message powinien być krótki i opisowy."
        )

        env_block = "\n".join(f"```bash\n{cmd}\n```" for cmd in env)

        return f"""1. Fork repozytorium
2. Stwórz branch: `git checkout -b feature/moja-funkcja`
3. Skonfiguruj środowisko:

{env_block}

4. Wprowadź zmiany i napisz testy
5. Utwórz Pull Request

### Konwencja commitów

{commit_guide}"""


# ══════════════════════════════════════════════════════════════════════
#  10d. ModuleDependencyAnalyzer – diagram zależności modułów
# ══════════════════════════════════════════════════════════════════════
class ModuleDependencyAnalyzer:
    """Analizuje importy między modułami Python i generuje diagram zależności."""

    IGNORE = {"__pycache__", "venv", ".git", "node_modules", "dist", "build"}

    def analyze(self, root: str) -> dict:
        root  = Path(root)
        edges = []       # (from_module, to_module)
        nodes = set()

        py_files = [
            fp for fp in root.rglob("*.py")
            if not any(p in self.IGNORE for p in fp.parts)
        ]
        local_modules = {fp.stem for fp in py_files}

        for fp in py_files:
            mod = fp.stem
            nodes.add(mod)
            try:
                src  = fp.read_text(encoding="utf-8", errors="ignore")
                tree = ast.parse(src)
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for alias in node.names:
                            name = alias.name.split(".")[0]
                            if name in local_modules and name != mod:
                                edges.append((mod, name))
                                nodes.add(name)
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            name = node.module.split(".")[0]
                            if name in local_modules and name != mod:
                                edges.append((mod, name))
                                nodes.add(name)
            except Exception:
                pass

        # Deduplicate
        edges = list(dict.fromkeys(edges))
        return {
            "nodes": sorted(nodes),
            "edges": edges[:50],
            "has_deps": bool(edges),
        }

    def generate_section(self, data: dict) -> str:
        if not data.get("has_deps"):
            return "_Brak wykrytych zależności między modułami lokalnymi._"

        lines = ["```"]
        by_source = {}
        for src, dst in data["edges"]:
            by_source.setdefault(src, []).append(dst)

        for src in sorted(by_source):
            targets = by_source[src]
            lines.append(f"{src}")
            for t in targets:
                lines.append(f"  └── {t}")
        lines.append("```")
        return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════
#  10e. PluginManager – system pluginów analizatorów i generatorów
# ══════════════════════════════════════════════════════════════════════
class PluginManager:
    """Rejestr pluginów: analizatory, generatory sekcji, szablony."""

    def __init__(self):
        self._analyzers:  dict[str, object] = {}
        self._generators: dict[str, object] = {}
        self._templates:  dict[str, object] = {}

    # ── Rejestracja ──────────────────────────────────────────────────

    def register_analyzer(self, name: str, analyzer) -> None:
        """Rejestruje analizator z metodą analyze(root) -> dict."""
        self._analyzers[name] = analyzer

    def register_generator(self, name: str, generator) -> None:
        """Rejestruje generator sekcji z metodą generate_section(data) -> str."""
        self._generators[name] = generator

    def register_template(self, name: str, template_fn) -> None:
        """Rejestruje funkcję szablonu (context_dict) -> str."""
        self._templates[name] = template_fn

    # ── Uruchamianie ─────────────────────────────────────────────────

    def run_analyzers(self, root: str) -> dict:
        """Uruchamia wszystkie zarejestrowane analizatory i zwraca wyniki."""
        results = {}
        for name, analyzer in self._analyzers.items():
            try:
                results[name] = analyzer.analyze(root)
            except Exception as e:
                results[name] = {"error": str(e)}
        return results

    def run_generator(self, name: str, data: dict) -> str:
        """Generuje sekcję README dla wskazanego generatora."""
        gen = self._generators.get(name)
        if not gen:
            return f"_Plugin '{name}' nie znaleziony._"
        try:
            return gen.generate_section(data)
        except Exception as e:
            return f"_Błąd pluginu '{name}': {e}_"

    def render_template(self, name: str, context: dict) -> str:
        """Renderuje niestandardowy szablon."""
        fn = self._templates.get(name)
        if not fn:
            return f"_Szablon '{name}' nie znaleziony._"
        try:
            return fn(context)
        except Exception as e:
            return f"_Błąd szablonu '{name}': {e}_"

    # ── Metadane ─────────────────────────────────────────────────────

    @property
    def analyzer_names(self) -> list:
        return list(self._analyzers.keys())

    @property
    def generator_names(self) -> list:
        return list(self._generators.keys())

    @property
    def template_names(self) -> list:
        return list(self._templates.keys())


# ══════════════════════════════════════════════════════════════════════
#  10f. DebugInspector – tryb debugowania / walidacja szablonów
# ══════════════════════════════════════════════════════════════════════
class DebugInspector:
    """Tryb debugowania: podgląd metadanych i walidacja szablonów README."""

    REQUIRED_KEYS = ["name", "desc", "version", "author", "badges",
                     "changelog", "usage"]

    def inspect(self, project, meta, git, tests, quality, todo,
                unused, contrib, moddeps) -> str:
        lines = ["=" * 60, "  DEBUG — README Generator Pro v2.0", "=" * 60, ""]

        # ProjectAnalyzer
        lines += [
            "── ProjectAnalyzer ──────────────────────────────────",
            f"  name:         {project.get('name')}",
            f"  language:     {project.get('language')}",
            f"  lang_stats:   {project.get('lang_stats')}",
            f"  file_count:   {project.get('file_count')}",
            f"  dir_count:    {project.get('dir_count')}",
            f"  repo_size:    {project.get('repo_size_kb')} KB",
            f"  entry:        {project.get('entry')}",
            f"  license:      {project.get('license')}",
            f"  has_tests:    {project.get('has_tests')}",
            f"  deps:         {list(project.get('deps', {}).keys())}",
            f"  configs:      {project.get('configs')}",
            "",
        ]

        # MetadataExtractor
        lines += [
            "── MetadataExtractor ────────────────────────────────",
            f"  version:      {meta.get('version')}",
            f"  author:       {meta.get('author')}",
            f"  description:  {str(meta.get('description',''))[:60]}",
            f"  classes:      {len(meta.get('classes', []))}",
            f"  functions:    {len(meta.get('functions', []))}",
            f"  missing_docs: {len(meta.get('missing_docs', []))}",
            "",
        ]

        # GitAnalyzer
        lines += [
            "── GitAnalyzer ──────────────────────────────────────",
            f"  is_git:       {git.get('is_git')}",
            f"  branch:       {git.get('branch')}",
            f"  last_commit:  {git.get('last_commit_hash')} — {git.get('last_commit_msg')}",
            f"  commits:      {git.get('commits_count')}",
            f"  status_clean: {git.get('status_clean')}",
            f"  remote:       {git.get('remote_url')}",
            "",
        ]

        # TestAnalyzer
        lines += [
            "── TestAnalyzer ─────────────────────────────────────",
            f"  framework:    {tests.get('framework')}",
            f"  command:      {tests.get('command')}",
            f"  test_count:   {tests.get('test_count')}",
            "",
        ]

        # DocQualityAnalyzer
        lines += [
            "── DocQualityAnalyzer ───────────────────────────────",
            f"  score:        {quality.get('score')}%",
            f"  total_items:  {quality.get('total_items')}",
            f"  missing_count:{quality.get('missing_count')}",
            f"  has_readme:   {quality.get('has_readme')}",
            f"  has_license:  {quality.get('has_license')}",
            f"  has_changelog:{quality.get('has_changelog')}",
            "",
        ]

        # TODO / Roadmap
        lines += [
            "── TodoRoadmapExtractor ─────────────────────────────",
            f"  items_found:  {todo.get('count', 0)}",
            f"  kinds:        {list(todo.get('grouped', {}).keys())}",
            "",
        ]

        # Unused functions
        lines += [
            "── UnusedFunctionDetector ───────────────────────────",
            f"  defined:      {unused.get('defined_count', 0)}",
            f"  unused:       {unused.get('unused_count', 0)}",
        ]
        for u in unused.get("unused", [])[:5]:
            lines.append(f"    ↳ {u['name']}  ({u['file']}:{u['lineno']})")
        lines.append("")

        # Contributing style
        lines += [
            "── ContributingGenerator ────────────────────────────",
            f"  commit_style: {contrib.get('commit_style')}",
            f"  env_steps:    {contrib.get('env_setup')}",
            "",
        ]

        # Module deps
        lines += [
            "── ModuleDependencyAnalyzer ─────────────────────────",
            f"  nodes:        {len(moddeps.get('nodes', []))}",
            f"  edges:        {len(moddeps.get('edges', []))}",
            "",
        ]

        # Template validation
        lines += ["── Walidacja szablonu ────────────────────────────────"]
        missing_keys = [k for k in self.REQUIRED_KEYS
                        if not project.get(k) and not meta.get(k)]
        if missing_keys:
            lines.append(f"  ⚠️  Brakujące klucze szablonu: {missing_keys}")
        else:
            lines.append("  ✅ Wszystkie klucze szablonu obecne.")
        lines += ["", "=" * 60]
        return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════
#  10g. ProjectTypeDetector – auto-wykrywanie typu projektu
# ══════════════════════════════════════════════════════════════════════
class ProjectTypeDetector:
    """Wykrywa typ projektu (CLI / web / lib / desktop / enterprise) i rekomenduje szablon."""

    SIGNALS = {
        "cli": {
            "files":   ["cli.py", "commands.py", "__main__.py", "setup.cfg"],
            "deps":    ["click", "typer", "argparse", "docopt", "fire"],
            "entries": ["__main__.py", "cli.py"],
        },
        "web": {
            "files":   ["app.py", "server.py", "wsgi.py", "asgi.py",
                        "manage.py", "routes.py", "index.js", "index.ts"],
            "deps":    ["flask", "django", "fastapi", "express", "koa",
                        "starlette", "aiohttp", "tornado", "uvicorn"],
            "entries": ["app.py", "server.py", "manage.py", "index.js"],
        },
        "lib": {
            "files":   ["__init__.py", "setup.py", "pyproject.toml",
                        "package.json", "Cargo.toml", "go.mod"],
            "deps":    [],
            "entries": ["__init__.py"],
        },
        "desktop": {
            "files":   [],
            "deps":    ["tkinter", "PyQt5", "PyQt6", "PySide6", "wxPython",
                        "kivy", "electron", "tauri"],
            "entries": ["main.py", "app.py"],
        },
        "enterprise": {
            "files":   ["docker-compose.yml", "Dockerfile", "kubernetes.yaml",
                        "helm", ".github/workflows"],
            "deps":    ["celery", "kafka", "rabbitmq", "redis", "sqlalchemy",
                        "alembic", "grpc"],
            "entries": [],
        },
    }

    TEMPLATE_MAP = {
        "cli":        "opensource",
        "web":        "opensource",
        "lib":        "opensource",
        "desktop":    "polsoft",
        "enterprise": "enterprise",
    }

    def detect(self, root: str, project: dict) -> dict:
        root  = Path(root)
        scores = {t: 0 for t in self.SIGNALS}

        all_deps: list = []
        for info in project.get("deps", {}).values():
            all_deps.extend(info.get("content", []))
        all_deps_lower = [d.lower() for d in all_deps]

        entry = project.get("entry", "")

        for ptype, signals in self.SIGNALS.items():
            for f in signals["files"]:
                if (root / f).exists():
                    scores[ptype] += 2
            for dep in signals["deps"]:
                if any(dep in d for d in all_deps_lower):
                    scores[ptype] += 3
            if entry in signals["entries"]:
                scores[ptype] += 1

        detected = max(scores, key=lambda k: scores[k])
        if scores[detected] == 0:
            detected = "lib"

        return {
            "type":             detected,
            "scores":           scores,
            "recommended_tpl":  self.TEMPLATE_MAP[detected],
            "confidence":       scores[detected],
        }


# ══════════════════════════════════════════════════════════════════════
#  10h. ProjectSummaryGenerator – auto-streszczenie projektu
# ══════════════════════════════════════════════════════════════════════
class ProjectSummaryGenerator:
    """Generuje krótkie i długie streszczenie projektu z analizy kodu i struktury."""

    def generate(self, project: dict, meta: dict, git: dict,
                 project_type: dict) -> dict:
        name    = project.get("name", "Projekt")
        lang    = project.get("language", "")
        version = meta.get("version", "")
        author  = meta.get("author", "")
        ptype   = project_type.get("type", "lib")
        classes = meta.get("classes", [])
        funcs   = meta.get("functions", [])
        desc    = meta.get("description", "")

        # Słowa kluczowe z nazw klas i funkcji
        symbols = (
            [c["name"] for c in classes[:6]] +
            [f["name"] for f in funcs[:8]]
        )
        keywords = self._extract_keywords(symbols, name)

        # Krótkie streszczenie (1 zdanie)
        type_labels = {
            "cli": "narzędzie CLI", "web": "aplikacja webowa",
            "lib": "biblioteka/moduł", "desktop": "aplikacja desktopowa",
            "enterprise": "system enterprise",
        }
        type_label = type_labels.get(ptype, "projekt")
        if desc:
            short = desc[:200]
        else:
            short = (
                f"{name} to {type_label} napisana w {lang}"
                + (f" przez {author}" if author else "")
                + (f" (v{version})" if version else "")
                + "."
            )

        # Długie streszczenie
        long_parts = [short]
        if classes:
            cls_names = ", ".join(f"`{c['name']}`" for c in classes[:5])
            long_parts.append(f"Projekt zawiera {len(classes)} klas: {cls_names}.")
        if funcs:
            fn_names = ", ".join(f"`{f['name']}`" for f in funcs[:5])
            long_parts.append(f"Eksportuje {len(funcs)} funkcji publicznych: {fn_names}.")
        if git.get("is_git"):
            long_parts.append(
                f"Repozytorium git: branch `{git.get('branch', 'main')}`, "
                f"{git.get('commits_count', 0)} commitów."
            )

        return {
            "short":    short,
            "long":     " ".join(long_parts),
            "keywords": keywords,
            "type":     ptype,
        }

    def _extract_keywords(self, symbols: list, project_name: str) -> list:
        """Wyciąga słowa kluczowe z nazw symboli (camelCase / snake_case)."""
        words = set()
        for sym in symbols:
            # snake_case
            parts = re.split(r"[_\-]", sym)
            # camelCase
            for p in parts:
                sub = re.findall(r"[A-Z][a-z]+|[a-z]+", p)
                words.update(w.lower() for w in sub if len(w) > 3)
        words.discard(project_name.lower())
        return sorted(words)[:15]


# ══════════════════════════════════════════════════════════════════════
#  10i. ApiChangeDetector – wykrywanie zmian w publicznym API
# ══════════════════════════════════════════════════════════════════════
class ApiChangeDetector:
    """Porównuje bieżące API z zapisanym snapshotem i raportuje zmiany."""

    SNAPSHOT_FILE = ".readmegen_api_snapshot.json"

    def take_snapshot(self, root: str, meta: dict) -> None:
        """Zapisuje snapshot aktualnego publicznego API do pliku."""
        snapshot = self._build_snapshot(meta)
        fp = Path(root) / self.SNAPSHOT_FILE
        try:
            fp.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False),
                          encoding="utf-8")
        except Exception:
            pass

    def detect_changes(self, root: str, meta: dict) -> dict:
        """Wykrywa zmiany API względem ostatniego snapshotu."""
        current  = self._build_snapshot(meta)
        fp       = Path(root) / self.SNAPSHOT_FILE
        if not fp.exists():
            return {
                "has_snapshot": False,
                "added": [], "removed": [], "changed": [],
                "breaking": [], "outdated": False,
            }
        try:
            previous = json.loads(fp.read_text(encoding="utf-8"))
        except Exception:
            return {"has_snapshot": False, "added": [], "removed": [],
                    "changed": [], "breaking": [], "outdated": False}

        prev_keys = set(previous.keys())
        curr_keys = set(current.keys())

        added   = sorted(curr_keys - prev_keys)
        removed = sorted(prev_keys - curr_keys)
        changed = []
        for key in curr_keys & prev_keys:
            if current[key] != previous[key]:
                changed.append({
                    "symbol": key,
                    "before": previous[key],
                    "after":  current[key],
                })

        # Breaking changes: usunięte publiczne symbole lub zmienione sygnatury
        breaking = removed + [c["symbol"] for c in changed]

        return {
            "has_snapshot": True,
            "added":    added,
            "removed":  removed,
            "changed":  changed,
            "breaking": breaking,
            "outdated": bool(added or removed or changed),
        }

    def generate_section(self, changes: dict) -> str:
        if not changes.get("has_snapshot"):
            return "_Brak snapshotu API. Kliknij 'Zapisz snapshot API' aby zacząć śledzić zmiany._"
        if not changes.get("outdated"):
            return "✅ API nie zmieniło się od ostatniego snapshotu."

        lines = []
        if changes["added"]:
            lines.append("**➕ Dodane symbole:**")
            for s in changes["added"]:
                lines.append(f"- `{s}`")
        if changes["removed"]:
            lines.append("\n**➖ Usunięte symbole (⚠️ breaking change):**")
            for s in changes["removed"]:
                lines.append(f"- `{s}`")
        if changes["changed"]:
            lines.append("\n**🔄 Zmienione sygnatury:**")
            for c in changes["changed"][:10]:
                lines.append(
                    f"- `{c['symbol']}`: `{c['before']}` → `{c['after']}`"
                )
        return "\n".join(lines)

    def _build_snapshot(self, meta: dict) -> dict:
        snap = {}
        for fn in meta.get("functions", []):
            key = fn["name"]
            snap[key] = {"args": fn.get("args", []), "return": fn.get("return", "")}
        for cls in meta.get("classes", []):
            for m in cls.get("methods", []):
                if not m["name"].startswith("_"):
                    key = f"{cls['name']}.{m['name']}"
                    snap[key] = {"args": m.get("args", []), "return": m.get("return", "")}
        return snap


# ══════════════════════════════════════════════════════════════════════
#  10j. ConventionalChangelogGenerator – CHANGELOG.md z Conventional Commits
# ══════════════════════════════════════════════════════════════════════
class ConventionalChangelogGenerator:
    """Generuje pełny CHANGELOG.md z commitów wg Conventional Commits."""

    TYPES = {
        "feat":     ("✨ Nowe funkcje",    False),
        "fix":      ("🐛 Naprawione błędy", False),
        "docs":     ("📚 Dokumentacja",    False),
        "refactor": ("♻️  Refaktoryzacja",  False),
        "perf":     ("⚡ Wydajność",        False),
        "test":     ("🧪 Testy",           False),
        "chore":    ("🔧 Narzędzia/CI",    False),
        "build":    ("📦 Build",           False),
        "ci":       ("🤖 CI/CD",           False),
        "style":    ("💄 Styl kodu",       False),
        "revert":   ("⏪ Revert",          False),
        "BREAKING": ("💥 Breaking Changes", True),
    }

    PATTERN = re.compile(
        r"^([a-f0-9]+)\s+"
        r"(feat|fix|docs|refactor|perf|test|chore|build|ci|style|revert)"
        r"(\([^)]+\))?(!)?:\s*(.+?)(?:\s+\(\d{4}-\d{2}-\d{2}.*\))?$",
        re.IGNORECASE,
    )
    BREAKING_PATTERN = re.compile(r"BREAKING[- ]CHANGE", re.IGNORECASE)

    def generate_from_git(self, root: str, git_data: dict,
                          version: str = "") -> str:
        """Buduje changelog z git log. Zwraca Markdown."""
        entries = git_data.get("changelog_entries", [])
        if not entries:
            return "_Brak historii git._"

        grouped:  dict[str, list] = {k: [] for k in self.TYPES}
        ungrouped: list = []

        for entry in entries:
            m = self.PATTERN.match(entry)
            if m:
                commit_hash = m.group(1)
                ctype       = m.group(2).lower()
                scope       = (m.group(3) or "").strip("()")
                breaking    = bool(m.group(4)) or self.BREAKING_PATTERN.search(entry)
                message     = m.group(5).strip()
                scope_str   = f"**{scope}**: " if scope else ""
                line = f"- {scope_str}{message} (`{commit_hash}`)"
                if breaking:
                    grouped["BREAKING"].append(line)
                else:
                    grouped.get(ctype, ungrouped).append(line)
            else:
                # nie-conventional commit — dodaj do sekcji ogólnej
                ungrouped.append(f"- {entry}")

        now = datetime.now().strftime("%Y-%m-%d")
        ver_header = f"## [{version or 'Unreleased'}] — {now}"
        lines = [ver_header, ""]

        # Breaking Changes zawsze na górze
        breaking_entries = grouped.pop("BREAKING", [])
        if breaking_entries:
            lines.append("### 💥 Breaking Changes\n")
            lines.extend(breaking_entries)
            lines.append("")

        for ctype, (label, _) in self.TYPES.items():
            if ctype == "BREAKING":
                continue
            items = grouped.get(ctype, [])
            if items:
                lines.append(f"### {label}\n")
                lines.extend(items)
                lines.append("")

        if ungrouped:
            lines.append("### 📝 Pozostałe zmiany\n")
            lines.extend(ungrouped[:10])
            lines.append("")

        return "\n".join(lines)

    def save_changelog(self, root: str, content: str) -> bool:
        """Zapisuje/aktualizuje CHANGELOG.md w katalogu projektu."""
        fp = Path(root) / "CHANGELOG.md"
        try:
            header = "# Changelog\n\nWszystkie zmiany w projekcie są dokumentowane tutaj.\n\n"
            if fp.exists():
                existing = fp.read_text(encoding="utf-8")
                # Wstaw nowy blok po nagłówku
                if "# Changelog" in existing:
                    existing = existing.replace(
                        "# Changelog\n\n",
                        f"# Changelog\n\nWszystkie zmiany w projekcie są dokumentowane tutaj.\n\n{content}\n\n",
                        1,
                    )
                    fp.write_text(existing, encoding="utf-8")
                else:
                    fp.write_text(header + content + "\n\n" + existing,
                                  encoding="utf-8")
            else:
                fp.write_text(header + content, encoding="utf-8")
            return True
        except Exception:
            return False


# ══════════════════════════════════════════════════════════════════════
#  10k. ExtendedDocsGenerator – docs/api.md, docs/usage.md, docs/configuration.md
# ══════════════════════════════════════════════════════════════════════
class ExtendedDocsGenerator:
    """Generuje rozszerzone pliki dokumentacji w katalogu docs/."""

    def generate_api_doc(self, meta: dict, project: dict) -> str:
        """Generuje docs/api.md z pełnym opisem klas i funkcji."""
        name = project.get("name", "Projekt")
        now  = datetime.now().strftime("%Y-%m-%d")
        lines = [
            f"# {name} — Dokumentacja API",
            f"\n> Wygenerowano automatycznie {now} przez README Generator Pro\n",
            "---\n",
        ]

        for cls in meta.get("classes", []):
            lines.append(f"## Klasa `{cls['name']}`\n")
            if cls.get("doc"):
                lines.append(f"{cls['doc']}\n")
            methods = [m for m in cls.get("methods", [])
                       if not m["name"].startswith("_")]
            if methods:
                lines.append("### Metody\n")
                lines.append("| Metoda | Argumenty | Zwraca | Opis |")
                lines.append("|--------|-----------|--------|------|")
                for m in methods:
                    args = ", ".join(m.get("args", [])) or "—"
                    ret  = m.get("return") or "—"
                    doc  = m.get("doc") or "—"
                    lines.append(f"| `{m['name']}` | `{args}` | `{ret}` | {doc} |")
            lines.append("")

        if meta.get("functions"):
            lines.append("## Funkcje publiczne\n")
            lines.append("| Funkcja | Argumenty | Zwraca | Opis |")
            lines.append("|---------|-----------|--------|------|")
            for fn in meta["functions"]:
                args = ", ".join(fn.get("args", [])) or "—"
                ret  = fn.get("return") or "—"
                doc  = fn.get("doc") or "—"
                lines.append(f"| `{fn['name']}` | `{args}` | `{ret}` | {doc} |")

        return "\n".join(lines)

    def generate_usage_doc(self, meta: dict, project: dict) -> str:
        """Generuje docs/usage.md z przykładami użycia."""
        name = project.get("name", "Projekt")
        lang = project.get("language", "Python")
        now  = datetime.now().strftime("%Y-%m-%d")

        examples = UsageExampleGenerator().generate(meta, project)
        install  = self._install_block(project)

        return f"""# {name} — Przewodnik użytkowania

> Wygenerowano automatycznie {now} przez README Generator Pro

---

## Instalacja

{install}

## Szybki start

{examples}

## Język projektu

Projekt napisany w **{lang}**.

## Punkt wejścia

`{project.get('entry', 'brak')}`
"""

    def generate_configuration_doc(self, project: dict, cfg_data: dict) -> str:
        """Generuje docs/configuration.md z opisem plików konfiguracyjnych."""
        name = project.get("name", "Projekt")
        now  = datetime.now().strftime("%Y-%m-%d")
        configs = project.get("configs", [])

        lines = [
            f"# {name} — Konfiguracja",
            f"\n> Wygenerowano automatycznie {now} przez README Generator Pro\n",
            "---\n",
            "## Pliki konfiguracyjne\n",
        ]

        if configs:
            lines.append("| Plik | Opis |")
            lines.append("|------|------|")
            desc_map = {
                ".env":              "Zmienne środowiskowe (nie commitować!)",
                ".env.example":      "Przykładowe zmienne środowiskowe",
                "config.json":       "Główna konfiguracja aplikacji",
                "config.yaml":       "Główna konfiguracja aplikacji (YAML)",
                "config.yml":        "Główna konfiguracja aplikacji (YAML)",
                "settings.py":       "Ustawienia Django / aplikacji Python",
                "appsettings.json":  "Ustawienia .NET",
                ".readmegen.json":   "Konfiguracja generatora README",
            }
            for c in configs:
                lines.append(f"| `{c}` | {desc_map.get(c, 'Plik konfiguracyjny')} |")
        else:
            lines.append("_Nie wykryto plików konfiguracyjnych._")

        lines += [
            "\n## Konfiguracja .readmegen.json\n",
            "Plik `.readmegen.json` umieszczony w katalogu projektu steruje "
            "generatorem dokumentacji.\n",
            "```json",
            json.dumps({
                k: v for k, v in cfg_data.items()
                if not isinstance(v, (list, dict)) or v
            }, indent=2, ensure_ascii=False)[:800],
            "```",
        ]
        return "\n".join(lines)

    def save_docs(self, root: str, api: str, usage: str, config: str) -> dict:
        """Zapisuje wszystkie pliki docs/ w katalogu projektu."""
        docs_dir = Path(root) / "docs"
        saved = {}
        try:
            docs_dir.mkdir(exist_ok=True)
            for filename, content in [("api.md", api),
                                       ("usage.md", usage),
                                       ("configuration.md", config)]:
                fp = docs_dir / filename
                fp.write_text(content, encoding="utf-8")
                saved[filename] = str(fp)
        except Exception as e:
            saved["error"] = str(e)
        return saved

    def _install_block(self, project: dict) -> str:
        deps = project.get("deps", {})
        if not deps:
            return "```bash\n# Brak pliku zależności\n```"
        lines = []
        cmd_map = {
            "pip":        "pip install -r requirements.txt",
            "npm":        "npm install",
            "poetry/pip": "poetry install",
            "cargo":      "cargo build",
            "go mod":     "go mod download",
            "bundler":    "bundle install",
            "maven":      "mvn install",
            "gradle":     "gradle build",
        }
        for fname, info in deps.items():
            cmd = cmd_map.get(info["manager"], f"# {info['manager']}")
            lines.append(f"```bash\n{cmd}\n```")
        return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════
#  10l. ArchitectureDocGenerator – auto-dokumentacja architektury
# ══════════════════════════════════════════════════════════════════════
class ArchitectureDocGenerator:
    """Generuje sekcję i plik dokumentacji architektury projektu."""

    def generate(self, project: dict, meta: dict, moddeps: dict,
                 project_type: dict, summary: dict) -> str:
        name   = project.get("name", "Projekt")
        lang   = project.get("language", "")
        ptype  = project_type.get("type", "lib")
        entry  = project.get("entry", "brak")
        tree   = project.get("tree", "")

        type_labels = {
            "cli": "Narzędzie linii komend (CLI)",
            "web": "Aplikacja webowa",
            "lib": "Biblioteka / Moduł",
            "desktop": "Aplikacja desktopowa",
            "enterprise": "System enterprise",
        }

        lines = [
            f"## 🏗️ Architektura — {name}\n",
            f"**Typ projektu:** {type_labels.get(ptype, ptype)}  ",
            f"**Język:** {lang}  ",
            f"**Punkt wejścia:** `{entry}`\n",
        ]

        # Streszczenie
        if summary.get("long"):
            lines += ["\n### Opis\n", summary["long"], ""]

        # Słowa kluczowe
        if summary.get("keywords"):
            kws = ", ".join(f"`{k}`" for k in summary["keywords"])
            lines.append(f"**Słowa kluczowe:** {kws}\n")

        # Klasy i warstwy
        classes = meta.get("classes", [])
        if classes:
            lines.append("\n### Warstwy i komponenty\n")
            lines.append("| Komponent | Typ | Opis |")
            lines.append("|-----------|-----|------|")
            for cls in classes[:15]:
                doc = cls.get("doc") or "—"
                lines.append(f"| `{cls['name']}` | Klasa | {doc} |")

        # Diagram zależności
        if moddeps.get("has_deps"):
            lines.append("\n### Zależności między modułami\n")
            lines.append(ModuleDependencyAnalyzer().generate_section(moddeps))

        # Struktura katalogów
        if tree:
            lines.append("\n### Struktura katalogów\n")
            lines.append(f"```\n{tree}\n```")

        return "\n".join(lines)


# ══════════════════════════════════════════════════════════════════════
#  10m. PreCommitHookGenerator – generowanie pre-commit hook
# ══════════════════════════════════════════════════════════════════════
class PreCommitHookGenerator:
    """Generuje i instaluje pre-commit hook automatycznie aktualizujący README."""

    HOOK_TEMPLATE = """#!/bin/sh
# pre-commit hook — README Generator Pro v2.2
# Autor:  Sebastian Januchowski <polsoft.its@fastservice.com>
# Firma:  polsoft.ITS™ Group  |  https://github.com/seb07uk
# Licencja: 2026 © Sebastian Januchowski & polsoft.ITS™ Group
# Automatycznie regeneruje README.md przed każdym commitem.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(git rev-parse --show-toplevel)"

echo "🔄 README Generator: sprawdzam zmiany w kodzie..."

# Sprawdź czy Python jest dostępny
if ! command -v python3 &> /dev/null; then
    echo "⚠️  Python3 niedostępny — pomijam regenerację README"
    exit 0
fi

# Uruchom generator w trybie CLI (jeśli dostępny)
if [ -f "$ROOT_DIR/readme_generator.py" ]; then
    python3 "$ROOT_DIR/readme_generator.py" --cli --output "$ROOT_DIR/README.md" 2>/dev/null || true
    git add "$ROOT_DIR/README.md" 2>/dev/null || true
    echo "✅ README.md zaktualizowany i dodany do commita."
else
    echo "ℹ️  readme_generator.py nie znaleziony — pomijam."
fi
"""

    def install(self, root: str) -> dict:
        """Instaluje pre-commit hook w .git/hooks/."""
        git_hooks = Path(root) / ".git" / "hooks"
        if not git_hooks.exists():
            return {"success": False, "error": "Katalog .git/hooks nie istnieje."}
        hook_path = git_hooks / "pre-commit"
        try:
            hook_path.write_text(self.HOOK_TEMPLATE, encoding="utf-8")
            # chmod +x
            hook_path.chmod(hook_path.stat().st_mode | 0o111)
            return {"success": True, "path": str(hook_path)}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def uninstall(self, root: str) -> dict:
        """Usuwa pre-commit hook jeśli był zainstalowany przez generator."""
        hook_path = Path(root) / ".git" / "hooks" / "pre-commit"
        if not hook_path.exists():
            return {"success": False, "error": "Hook nie istnieje."}
        try:
            content = hook_path.read_text(encoding="utf-8", errors="ignore")
            if "README Generator Pro" not in content:
                return {"success": False,
                        "error": "Hook nie pochodzi z README Generator — nie usunięto."}
            hook_path.unlink()
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def is_installed(self, root: str) -> bool:
        hook_path = Path(root) / ".git" / "hooks" / "pre-commit"
        if not hook_path.exists():
            return False
        try:
            return "README Generator Pro" in hook_path.read_text(
                encoding="utf-8", errors="ignore")
        except Exception:
            return False

    def get_hook_script(self) -> str:
        return self.HOOK_TEMPLATE


# ══════════════════════════════════════════════════════════════════════
#  10. ConfigManager – .readmegen.json
# ══════════════════════════════════════════════════════════════════════
class ConfigManager:
    """Czyta i zapisuje .readmegen.json w katalogu projektu."""

    DEFAULT = {
        "template": "opensource", "tree_mode": "compact", "tree_depth": 2,
        "badge_style": "flat", "name": "", "version": "", "author": "",
        "description": "", "github_url": "", "watch_interval": 3.0,
        # v2.1
        "disabled_sections": [],
        "ignore_dirs":        [],
        "custom_fields":      {},
        "show_unused":        True,
        "show_roadmap":       True,
        "show_contributing":  True,
        "show_module_deps":   True,
        # v2.2 – nowe opcje automatyzacji
        "auto_detect_type":   True,   # auto-wykrywanie typu projektu
        "show_api_changes":   True,   # sekcja zmian API
        "show_architecture":  True,   # sekcja architektury
        "generate_docs_dir":  False,  # generuj docs/api.md, docs/usage.md itd.
        "precommit_hook":     False,  # czy hook pre-commit jest aktywny
    }

    def load(self, root: str) -> dict:
        fp  = Path(root) / ".readmegen.json"
        cfg = dict(self.DEFAULT)
        if fp.exists():
            try:
                cfg.update(json.loads(fp.read_text(encoding="utf-8")))
            except Exception:
                pass
        return cfg

    def save(self, root: str, cfg: dict):
        fp = Path(root) / ".readmegen.json"
        try:
            fp.write_text(json.dumps(cfg, indent=2, ensure_ascii=False),
                          encoding="utf-8")
        except Exception:
            pass


# ══════════════════════════════════════════════════════════════════════
#  11. ReadmeGenerator v2
# ══════════════════════════════════════════════════════════════════════
class ReadmeGenerator:
    """Generuje README.md z pełnymi sekcjami v2.0."""

    TEMPLATES = {
        "Minimalistyczny": "minimal",
        "Open-Source":     "opensource",
        "Enterprise":      "enterprise",
        "polsoft.ITS™":    "polsoft",
    }

    def generate(self, project, meta, git, tests, quality,
                 template, custom, badge_style="flat",
                 todo=None, unused=None, contrib=None, moddeps=None, cfg=None,
                 project_type=None, summary=None, api_changes=None):
        name    = custom.get("name")    or project["name"]
        desc    = custom.get("desc")    or meta.get("description") or f"Projekt {name}"
        version = custom.get("version") or meta.get("version")     or "1.0.0"
        author  = custom.get("author")  or meta.get("author")      or "Autor"
        github  = custom.get("github")  or git.get("remote_url")   or ""
        now     = datetime.now().strftime("%Y-%m-%d")
        cfg     = cfg or {}

        badges_str = "\n".join(BadgeGenerator().generate(project, meta, git, tests, badge_style))
        changelog  = ChangelogGenerator().generate(project["root"], git)
        usage      = UsageExampleGenerator().generate(meta, project)

        # v2.1 sekcje
        todo_data    = todo    or {"items": [], "grouped": {}, "count": 0}
        unused_data  = unused  or {"unused": [], "unused_count": 0, "defined_count": 0}
        contrib_data = contrib or {"commit_style": "free", "env_setup": [], "has_contributing": False}
        moddeps_data = moddeps or {"nodes": [], "edges": [], "has_deps": False}

        roadmap_s      = (TodoRoadmapExtractor().generate_section(todo_data)
                          if cfg.get("show_roadmap", True) else "")
        contributing_s = (ContributingGenerator().generate_section(contrib_data)
                          if cfg.get("show_contributing", True) else "")
        moddeps_s      = (ModuleDependencyAnalyzer().generate_section(moddeps_data)
                          if cfg.get("show_module_deps", True) else "")
        unused_s       = self._unused_block(unused_data) if cfg.get("show_unused", True) else ""

        # v2.2 sekcje
        ptype_data   = project_type or {"type": "lib", "recommended_tpl": template,
                                        "confidence": 0, "scores": {}}
        summary_data = summary or {"short": desc, "long": desc, "keywords": [], "type": "lib"}
        api_chg_data = api_changes or {"has_snapshot": False, "added": [], "removed": [],
                                       "changed": [], "breaking": [], "outdated": False}

        arch_s     = (ArchitectureDocGenerator().generate(
                          project, meta, moddeps_data, ptype_data, summary_data)
                      if cfg.get("show_architecture", True) else "")
        api_chg_s  = (ApiChangeDetector().generate_section(api_chg_data)
                      if cfg.get("show_api_changes", True) else "")
        summary_s  = summary_data.get("long", desc)
        type_badge = self._type_badge(ptype_data)

        c = dict(name=name, desc=desc, version=version, author=author,
                 github=github, now=now, badges=badges_str,
                 changelog=changelog, usage=usage,
                 p=project, m=meta, g=git, t=tests, q=quality,
                 roadmap=roadmap_s, contributing=contributing_s,
                 moddeps=moddeps_s, unused=unused_s, cfg=cfg,
                 arch=arch_s, api_changes=api_chg_s,
                 summary=summary_s, type_badge=type_badge,
                 ptype=ptype_data)

        if template == "minimal":    return self._tpl_minimal(c)
        if template == "opensource": return self._tpl_opensource(c)
        if template == "enterprise": return self._tpl_enterprise(c)
        return self._tpl_polsoft(c)

    # ── Szablony ────────────────────────────────────────────────────

    def _tpl_minimal(self, c):
        p = c["p"]
        tree = f"\n```\n{p['tree']}\n```" if p.get("tree") else ""
        return f"""# {c['name']}

> {c['desc']}

{c['badges']}

## Instalacja
{self._deps_block(p)}

## Użycie

{c['usage']}

## Struktura projektu
{tree}

## Licencja

{p['license']}

---
*Wygenerowano {c['now']} przez [README Generator Pro v2.2](https://github.com/seb07uk) — [Sebastian Januchowski](https://github.com/seb07uk) @ [polsoft.ITS™ Group](https://github.com/seb07uk)*
"""

    def _tpl_opensource(self, c):
        p, m, g, t, q = c["p"], c["m"], c["g"], c["t"], c["q"]
        tree    = f"\n```\n{p['tree']}\n```" if p.get("tree") else ""
        tests_s = (f"**Framework:** `{t['framework']}`\n\n**Komenda:** `{t['command']}`"
                   f"\n\n**Pliki testów:** {t['test_count']}"
                   if t.get("framework") else "❌ Brak testów")
        gh_link = f"\n\n🔗 [GitHub]({c['github']})" if c["github"] else ""
        score_s = f"📊 Jakość dokumentacji: **{q['score']}%** ({q['missing_count']} brakujących docstringów)"

        return f"""# {c['name']}{gh_link}

{c['badges']}

## 📖 Opis

{c['desc']}

## ✨ Funkcje

{self._features_block(m)}

## 🚀 Instalacja

{self._deps_block(p)}

## 💡 Przykłady użycia

{c['usage']}

## 📁 Struktura katalogów
{tree}

## 🔧 API — Klasy
{self._classes_block(m)}

## 🔩 API — Funkcje
{self._api_block(m)}

## 🧪 Testy

{tests_s}

## ⚙️ Konfiguracja

Pliki: {', '.join(p['configs']) if p['configs'] else 'brak'}

## 📋 Changelog

{c['changelog']}

## 🗺️ Roadmap

{c['roadmap']}

## 🔗 Zależności modułów

{c['moddeps']}

## 🤝 Contributing

{c['contributing']}

## 🔍 Nieużywane symbole

{c['unused']}

## 🏗️ Architektura

{c['arch']}

## 🔀 Zmiany API

{c['api_changes']}

## 📊 Jakość kodu

{score_s}

## 📄 Licencja

{p['license']} — © {datetime.now().year} {c['author']}

## 👤 Autor

{c['author']}

---
*Wygenerowano {c['now']} przez [README Generator Pro v2.2](https://github.com/seb07uk) — [Sebastian Januchowski](https://github.com/seb07uk) @ [polsoft.ITS™ Group](https://github.com/seb07uk)*
"""

    def _tpl_enterprise(self, c):
        p, m, g, t, q = c["p"], c["m"], c["g"], c["t"], c["q"]
        tree   = f"\n```\n{p['tree']}\n```" if p.get("tree") else ""
        tests_s = (f"**Framework:** `{t['framework']}`\n\n**Komenda:** `{t['command']}`"
                   f"\n\nLiczba plików testów: {t['test_count']}"
                   if t.get("framework") else "⚠️ Brak pokrycia testami")

        return f"""# {c['name']} — Dokumentacja Techniczna

**Wersja:** {c['version']}
**Autor / Zespół:** {c['author']}
**Język:** {p['language']}
**Licencja:** {p['license']}
**Data generacji:** {c['now']}

---

## 1. Streszczenie

{c['desc']}

---

## 2. Wymagania systemowe

| Parametr | Wartość |
|----------|---------|
| Język | **{p['language']}** |
| Punkt wejścia | `{p['entry']}` |
| Pliki | {p['file_count']} |
| Katalogi | {p['dir_count']} |
| Rozmiar | {p['repo_size_kb']} KB |

---

## 3. Instalacja

{self._deps_block(p)}

---

## 4. Architektura projektu
{tree}

---

## 5. Dokumentacja klas
{self._classes_block(m)}

---

## 6. Dokumentacja API
{self._api_block(m)}

---

## 7. Przykłady użycia

{c['usage']}

---

## 8. Testy

{tests_s}

---

## 9. Integracja z Git

{self._git_section(g)}

---

## 10. Konfiguracja

| Plik | Opis |
|------|------|
{self._config_table(p['configs'])}

---

## 11. Changelog

{c['changelog']}

---

## 12. Roadmap

{c['roadmap']}

---

## 13. Zależności modułów

{c['moddeps']}

---

## 14. Wkład w projekt (Contributing)

{c['contributing']}

---

## 15. Nieużywane symbole

{c['unused']}

---

## 16. Architektura

{c['arch']}

---

## 17. Zmiany API

{c['api_changes']}

---

## 18. Jakość dokumentacji

Wynik: **{q['score']}%** ({q['missing_count']} / {q['total_items']} elementów bez docstringów)

---

## 19. Licencja

**{p['license']}** — © {datetime.now().year} {c['author']}

---
*Wygenerowano przez [README Generator Pro v2.2](https://github.com/seb07uk) — [Sebastian Januchowski](https://github.com/seb07uk) @ [polsoft.ITS™ Group](https://github.com/seb07uk)*
"""

    def _tpl_polsoft(self, c):
        p, m, g, t, q = c["p"], c["m"], c["g"], c["t"], c["q"]
        tree   = f"\n```\n{p['tree']}\n```" if p.get("tree") else ""
        gh_btn = (f"[![GitHub](https://img.shields.io/badge/GitHub-repo-black"
                  f"?style=for-the-badge&logo=github)]({c['github']})" if c["github"] else "")
        tests_s = (f"✅ **Framework:** `{t['framework']}` | **Komenda:** `{t['command']}`"
                   if t.get("framework") else "⚠️ Brak testów — zalecane dodanie.")
        score_emoji = "🟢" if q["score"] >= 90 else ("🟡" if q["score"] >= 60 else "🔴")

        return f"""<div align="center">

# 🚀 {c['name']}

**{c['desc']}**

{c['badges']}
{gh_btn}

</div>

---

## 🎯 O projekcie

{c['desc']}

Projekt stworzony przez **{c['author']}** w technologii **{p['language']}**.
Wersja: `{c['version']}` | Licencja: `{p['license']}` | Data: `{c['now']}`

---

## ✨ Możliwości

{self._features_block(m)}

---

## ⚡ Szybki start

{self._deps_block(p)}

---

## 💡 Przykłady użycia

{c['usage']}

---

## 📂 Struktura projektu
{tree}

---

## 🧩 Architektura kodu
{self._classes_block(m)}

---

## 🔩 API Publiczne
{self._api_block(m)}

---

## 🧪 Testy

{tests_s}

---

## 📋 Changelog

{c['changelog']}

---

## 🗺️ Roadmap

{c['roadmap']}

---

## 🔗 Zależności modułów

{c['moddeps']}

---

## 🤝 Contributing

{c['contributing']}

---

## 🔍 Nieużywane symbole

{c['unused']}

---

## 🏗️ Architektura

{c['arch']}

---

## 🔀 Zmiany API

{c['api_changes']}

---

## 🌿 Git

{self._git_section(g)}

---

## {score_emoji} Jakość dokumentacji

Wynik: **{q['score']}%** ({q['missing_count']} elementów bez docstringów)

---

## ⚙️ Konfiguracja

Pliki: `{'`, `'.join(p['configs']) if p['configs'] else 'brak'}`

---

## 📜 Licencja

**{p['license']}** — © {datetime.now().year} **{c['author']}** | [polsoft.ITS™ Group](https://github.com/seb07uk)

---

<div align="center">

*Wygenerowano przez **[README Generator Pro v2.2](https://github.com/seb07uk)** — [Sebastian Januchowski](https://github.com/seb07uk) @ [polsoft.ITS™ Group](https://github.com/seb07uk)*

</div>
"""

    # ── Pomocnicze bloki ──────────────────────────────────────────────

    def _deps_block(self, p):
        if not p.get("deps"):
            return "\n```bash\n# Brak pliku zależności\n```"
        lines = []
        for fname, info in p["deps"].items():
            mgr, deps = info["manager"], info["content"]
            cmd_map = {"pip": f"pip install -r {fname}",
                       "npm": "npm install",
                       "poetry/pip": f"pip install .\n# lub\npoetry install",
                       "cargo": "cargo build",
                       "go mod": "go mod download",
                       "bundler": "bundle install",
                       "maven": "mvn install",
                       "gradle": "gradle build"}
            cmd = cmd_map.get(mgr, f"# {mgr} — patrz {fname}")
            lines.append(f"\n```bash\n{cmd}\n```")
            if deps:
                short = deps[:8]
                lines.append(f"\nZależności: `{'`, `'.join(short)}`" +
                              (f" *(+{len(deps)-8} więcej)*" if len(deps) > 8 else ""))
        return "\n".join(lines)

    def _features_block(self, m):
        items = []
        for cls in m.get("classes", [])[:5]:
            doc = f" — {cls['doc']}" if cls.get("doc") else ""
            items.append(f"- 🔷 **{cls['name']}**{doc}")
        for fn in m.get("functions", [])[:5]:
            doc = f" — {fn['doc']}" if fn.get("doc") else ""
            items.append(f"- 🔹 `{fn['name']}({', '.join(fn['args'])})`{doc}")
        if not items:
            items = ["- ✅ Modularna architektura",
                     "- ✅ Łatwa konfiguracja",
                     "- ✅ Dokumentacja wbudowana"]
        return "\n".join(items)

    def _classes_block(self, m):
        if not m.get("classes"):
            return "\nBrak wykrytych klas.\n"
        lines = ["\n| Klasa | Opis |", "|-------|------|"]
        for cls in m["classes"][:12]:
            lines.append(f"| `{cls['name']}` | {cls.get('doc') or '—'} |")
        return "\n".join(lines)

    def _api_block(self, m):
        """Tabela API z typami argumentów i wartością zwracaną."""
        rows = []
        for cls in m.get("classes", [])[:8]:
            for mth in cls.get("methods", [])[:5]:
                if mth["name"].startswith("_"):
                    continue
                args = ", ".join(mth["args"]) or "—"
                ret  = mth.get("return") or "—"
                doc  = mth.get("doc") or "—"
                rows.append(f"| `{cls['name']}.{mth['name']}` | `{args}` | `{ret}` | {doc} |")
        for fn in m.get("functions", [])[:8]:
            args = ", ".join(fn["args"]) or "—"
            ret  = fn.get("return") or "—"
            doc  = fn.get("doc") or "—"
            rows.append(f"| `{fn['name']}` | `{args}` | `{ret}` | {doc} |")
        if not rows:
            return "\nBrak publicznego API.\n"
        header = ["\n| Metoda/Funkcja | Argumenty | Zwraca | Opis |",
                  "|----------------|-----------|--------|------|"]
        return "\n".join(header + rows)

    def _git_section(self, g):
        if not g.get("is_git"):
            return "_Projekt nie jest repozytorium Git._"
        clean = "✅ Czyste" if g.get("status_clean") else "⚠️ Niezacommitowane zmiany"
        lines = [
            f"- **Branch:** `{g.get('branch','—')}`",
            f"- **Ostatni commit:** `{g.get('last_commit_hash','—')}` — {g.get('last_commit_msg','—')}",
            f"- **Data:** {g.get('last_commit_date','—')}",
            f"- **Autor:** {g.get('last_commit_author','—')}",
            f"- **Liczba commitów:** {g.get('commits_count',0)}",
            f"- **Status:** {clean}",
        ]
        if g.get("remote_url"):
            lines.append(f"- **Remote:** [{g['remote_url']}]({g['remote_url']})")
        return "\n".join(lines)

    def _config_table(self, configs):
        if not configs:
            return "| — | Brak plików konfiguracyjnych |"
        return "\n".join(f"| `{c}` | Plik konfiguracyjny |" for c in configs)

    def _unused_block(self, unused_data: dict) -> str:
        """Sekcja nieużywanych publicznych symboli."""
        items = unused_data.get("unused", [])
        if not items:
            return "_✅ Nie wykryto nieużywanych publicznych symboli._"
        lines = [
            f"Wykryto **{unused_data.get('unused_count', 0)}** "
            f"potencjalnie nieużywanych symboli "
            f"(spośród {unused_data.get('defined_count', 0)} zdefiniowanych):\n"
        ]
        for u in items[:15]:
            lines.append(f"- `{u['name']}` — _{u['file']}:{u['lineno']}_")
        if unused_data.get("unused_count", 0) > 15:
            lines.append(f"\n*... i więcej — uruchom pełną analizę.*")
        return "\n".join(lines)

    def _type_badge(self, ptype_data: dict) -> str:
        """Zwraca odznakę typu projektu."""
        label_map = {
            "cli":        ("CLI",        "blueviolet"),
            "web":        ("Web+App",    "blue"),
            "lib":        ("Library",    "green"),
            "desktop":    ("Desktop",    "orange"),
            "enterprise": ("Enterprise", "red"),
        }
        ptype = ptype_data.get("type", "lib")
        label, color = label_map.get(ptype, ("Unknown", "grey"))
        return f"![Type](https://img.shields.io/badge/type-{label}-{color}?style=flat)"


# ══════════════════════════════════════════════════════════════════════
#  12. Module – klasa wtyczki Modulatora
# ══════════════════════════════════════════════════════════════════════
class Module(BaseModule):
    NAME         = "README Generator Pro"
    DESCRIPTION  = "Automatyczny generator README.md z analizy kodu, Git, testów i jakości"
    VERSION      = "2.2.0"
    AUTHOR       = "Sebastian Januchowski"
    COMPANY      = "polsoft.ITS™ Group"
    EMAIL        = "polsoft.its@fastservice.com"
    GITHUB       = "https://github.com/seb07uk"
    COPYRIGHT    = "2026 © Sebastian Januchowski & polsoft.ITS™ Group"
    ICON         = "📘"
    CAPABILITIES = ["file_read", "file_write", "subprocess"]

    def __init__(self, app):
        super().__init__(app)
        self._analyzer  = ProjectAnalyzer()
        self._extractor = MetadataExtractor()
        self._git       = GitAnalyzer()
        self._tests     = TestAnalyzer()
        self._quality   = DocQualityAnalyzer()
        self._gen       = ReadmeGenerator()
        self._cfg_mgr   = ConfigManager()
        self._watcher   = None
        # v2.1 – nowe analizatory
        self._unused_detector = UnusedFunctionDetector()
        self._todo_extractor  = TodoRoadmapExtractor()
        self._contrib_gen     = ContributingGenerator()
        self._moddep_analyzer = ModuleDependencyAnalyzer()
        self._debug_inspector = DebugInspector()
        self._plugin_manager  = PluginManager()
        # v2.2 – automatyzacja
        self._type_detector    = ProjectTypeDetector()
        self._summary_gen      = ProjectSummaryGenerator()
        self._api_change_det   = ApiChangeDetector()
        self._conv_changelog   = ConventionalChangelogGenerator()
        self._ext_docs_gen     = ExtendedDocsGenerator()
        self._arch_doc_gen     = ArchitectureDocGenerator()
        self._hook_gen         = PreCommitHookGenerator()

        self._project = self._meta = self._git_data = None
        self._test_data = self._quality_data = None
        self._todo_data = self._unused_data = None
        self._contrib_data = self._moddeps_data = None
        self._project_type = self._summary_data = None
        self._api_changes  = None
        self._preview_text = self._status_var = None
        self._watch_var = None
        self._quality_score_var = None

    def on_load(self):
        self.bus.publish("readme_generator", "loaded")

    def on_unload(self):
        if self._watcher:
            self._watcher.stop()
        self.bus.publish("readme_generator", "unloaded")

    # ── GUI ─────────────────────────────────────────────────────────

    def get_widget(self, parent):
        t = self.theme
        root_frame = tk.Frame(parent, bg=t["bg"])
        root_frame.pack(fill="both", expand=True)

        # ── Toolbar ──
        toolbar = tk.Frame(root_frame, bg=t["card"], pady=6, padx=8)
        toolbar.pack(fill="x")

        tk.Label(toolbar, text="📘 README Generator Pro v2.0",
                 font=("Segoe UI", 12, "bold"),
                 bg=t["card"], fg=t["acc"]).pack(side="left", padx=(0, 16))

        for label, cmd in [
            ("📂 Projekt",      self._pick_folder),
            ("🔍 Analizuj",     self._run_analyze),
            ("⚡ Generuj",      self._run_generate),
            ("💾 Zapisz",       self._save_readme),
            ("📋 Kopiuj",       self._copy_to_clipboard),
            ("📤 Eksport TXT",  self._export_txt),
            ("📚 Generuj docs", self._generate_extended_docs),
            ("📸 Snapshot API", self._save_api_snapshot),
            ("🔗 Hook install", self._toggle_precommit_hook),
            ("📜 Changelog",    self._generate_conventional_changelog),
        ]:
            ttk.Button(toolbar, text=label, command=cmd).pack(side="left", padx=3)

        self._watch_var = tk.BooleanVar(value=False)
        tk.Checkbutton(toolbar, text="👁 Watch", variable=self._watch_var,
                       command=self._toggle_watch,
                       bg=t["card"], fg=t["grn"], selectcolor=t["card"],
                       activebackground=t["card"],
                       font=("Segoe UI", 9)).pack(side="right", padx=8)

        # ── Ścieżka projektu ──
        path_f = tk.Frame(root_frame, bg=t["card2"], pady=4, padx=8)
        path_f.pack(fill="x")
        tk.Label(path_f, text="Projekt:", bg=t["card2"], fg=t["dim"],
                 font=("Segoe UI", 9)).pack(side="left")
        self._path_var = tk.StringVar(value="— nie wybrano —")
        tk.Label(path_f, textvariable=self._path_var,
                 bg=t["card2"], fg=t["fg"],
                 font=("Segoe UI", 9, "bold")).pack(side="left", padx=8)

        # ── PanedWindow ──
        paned = tk.PanedWindow(root_frame, orient=tk.HORIZONTAL,
                               bg=t["bg"], sashwidth=5)
        paned.pack(fill="both", expand=True, padx=6, pady=4)

        # ── LEWA: notebook zakładek ──
        left = tk.Frame(paned, bg=t["bg"])
        paned.add(left, minsize=285)

        left_nb = ttk.Notebook(left)
        left_nb.pack(fill="both", expand=True)

        tab_cfg  = tk.Frame(left_nb, bg=t["bg"])
        tab_info = tk.Frame(left_nb, bg=t["bg"])
        tab_qual = tk.Frame(left_nb, bg=t["bg"])
        tab_git  = tk.Frame(left_nb, bg=t["bg"])
        tab_dbg  = tk.Frame(left_nb, bg=t["bg"])

        left_nb.add(tab_cfg,  text="⚙️ Konfiguracja")
        left_nb.add(tab_info, text="🔎 Analiza")
        left_nb.add(tab_qual, text="📊 Jakość")
        left_nb.add(tab_git,  text="🌿 Git")
        left_nb.add(tab_dbg,  text="🐛 Debug")

        self._build_tab_config(tab_cfg, t)
        self._build_tab_info(tab_info, t)
        self._build_tab_quality(tab_qual, t)
        self._build_tab_git(tab_git, t)
        self._build_tab_debug(tab_dbg, t)

        # ── PRAWA: podgląd README ──
        right = tk.Frame(paned, bg=t["bg"])
        paned.add(right, minsize=420)

        ph = tk.Frame(right, bg=t["card2"], pady=4, padx=8)
        ph.pack(fill="x")
        tk.Label(ph, text="👁 Podgląd README.md",
                 font=("Segoe UI", 10, "bold"),
                 bg=t["card2"], fg=t["lav"]).pack(side="left")
        tk.Label(ph, text="(edytowalny)",
                 font=("Segoe UI", 8),
                 bg=t["card2"], fg=t["dim"]).pack(side="left", padx=6)

        self._preview_text = scrolledtext.ScrolledText(
            right, bg=t["card"], fg=t["fg"],
            font=("Consolas", 9), wrap="word",
            insertbackground=t["fg"], selectbackground=t["acc"],
            relief="flat"
        )
        self._preview_text.pack(fill="both", expand=True, padx=4, pady=4)
        self._preview_text.insert("end", "← Wybierz projekt i kliknij Generuj")

        # ── Pasek statusu ──
        self._status_var = tk.StringVar(value="Gotowy.")
        tk.Label(root_frame, textvariable=self._status_var,
                 bg=t["card"], fg=t["dim"],
                 font=("Segoe UI", 8), anchor="w", pady=3, padx=8
                 ).pack(fill="x", side="bottom")

        return root_frame

    def _build_tab_config(self, parent, t):
        canvas = tk.Canvas(parent, bg=t["bg"], highlightthickness=0)
        vsb    = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        scroll = tk.Frame(canvas, bg=t["bg"])
        canvas.create_window((0, 0), window=scroll, anchor="nw")
        scroll.bind("<Configure>",
                    lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Szablon
        tf = tk.LabelFrame(scroll, text=" 🎨 Szablon ",
                           bg=t["bg"], fg=t["acc"],
                           font=("Segoe UI", 9, "bold"), bd=1, relief="groove")
        tf.pack(fill="x", padx=6, pady=(6, 3))
        self._template_var = tk.StringVar(value="Open-Source")
        for tname in ReadmeGenerator.TEMPLATES:
            tk.Radiobutton(tf, text=tname, variable=self._template_var, value=tname,
                           bg=t["bg"], fg=t["fg"], selectcolor=t["card"],
                           activebackground=t["bg"],
                           font=("Segoe UI", 9)).pack(anchor="w", padx=10, pady=1)

        # Drzewo
        tree_f = tk.LabelFrame(scroll, text=" 🌲 Drzewo katalogów ",
                               bg=t["bg"], fg=t["acc"],
                               font=("Segoe UI", 9, "bold"), bd=1, relief="groove")
        tree_f.pack(fill="x", padx=6, pady=3)

        r1 = tk.Frame(tree_f, bg=t["bg"])
        r1.pack(fill="x", padx=8, pady=2)
        tk.Label(r1, text="Tryb:", width=10, anchor="w",
                 bg=t["bg"], fg=t["dim"], font=("Segoe UI", 8)).pack(side="left")
        self._tree_mode_var = tk.StringVar(value="compact")
        for val, lbl in [("compact", "Compact"), ("full", "Full")]:
            tk.Radiobutton(r1, text=lbl, variable=self._tree_mode_var, value=val,
                           bg=t["bg"], fg=t["fg"], selectcolor=t["card"],
                           activebackground=t["bg"],
                           font=("Segoe UI", 8)).pack(side="left", padx=4)

        r2 = tk.Frame(tree_f, bg=t["bg"])
        r2.pack(fill="x", padx=8, pady=2)
        tk.Label(r2, text="Głębokość:", width=10, anchor="w",
                 bg=t["bg"], fg=t["dim"], font=("Segoe UI", 8)).pack(side="left")
        self._tree_depth_var = tk.IntVar(value=2)
        tk.Spinbox(r2, from_=1, to=5, textvariable=self._tree_depth_var,
                   width=4, font=("Segoe UI", 9)).pack(side="left")

        # Styl odznak
        badge_f = tk.LabelFrame(scroll, text=" 🏷️ Badge style ",
                                bg=t["bg"], fg=t["acc"],
                                font=("Segoe UI", 9, "bold"), bd=1, relief="groove")
        badge_f.pack(fill="x", padx=6, pady=3)
        brow = tk.Frame(badge_f, bg=t["bg"])
        brow.pack(fill="x", padx=8, pady=2)
        self._badge_style_var = tk.StringVar(value="flat")
        for val in ["flat", "flat-square", "for-the-badge", "plastic"]:
            tk.Radiobutton(brow, text=val, variable=self._badge_style_var, value=val,
                           bg=t["bg"], fg=t["fg"], selectcolor=t["card"],
                           activebackground=t["bg"],
                           font=("Segoe UI", 8)).pack(side="left", padx=3)

        # Metadane
        mf = tk.LabelFrame(scroll, text=" ✏️ Metadane (opcjonalne) ",
                           bg=t["bg"], fg=t["acc"],
                           font=("Segoe UI", 9, "bold"), bd=1, relief="groove")
        mf.pack(fill="x", padx=6, pady=3)
        for label, attr in [("Nazwa:", "_inp_name"), ("Opis:", "_inp_desc"),
                             ("Wersja:", "_inp_version"), ("Autor:", "_inp_author"),
                             ("GitHub:", "_inp_github")]:
            row = tk.Frame(mf, bg=t["bg"])
            row.pack(fill="x", padx=8, pady=2)
            tk.Label(row, text=label, width=8, anchor="w",
                     bg=t["bg"], fg=t["dim"],
                     font=("Segoe UI", 8)).pack(side="left")
            entry = ttk.Entry(row, font=("Segoe UI", 9))
            entry.pack(side="left", fill="x", expand=True)
            setattr(self, attr, entry)

        # Sekcje README – przełączniki v2.1
        sec_f = tk.LabelFrame(scroll, text=" 📑 Sekcje README ",
                              bg=t["bg"], fg=t["acc"],
                              font=("Segoe UI", 9, "bold"), bd=1, relief="groove")
        sec_f.pack(fill="x", padx=6, pady=3)

        self._show_unused_var       = tk.BooleanVar(value=True)
        self._show_roadmap_var      = tk.BooleanVar(value=True)
        self._show_contributing_var = tk.BooleanVar(value=True)
        self._show_moddeps_var      = tk.BooleanVar(value=True)
        self._show_architecture_var = tk.BooleanVar(value=True)
        self._show_api_changes_var  = tk.BooleanVar(value=True)

        for label, var in [
            ("🔍 Nieużywane symbole",    self._show_unused_var),
            ("🗺️  Roadmap (TODO/FIXME)",  self._show_roadmap_var),
            ("🤝 Contributing",           self._show_contributing_var),
            ("🔗 Zależności modułów",     self._show_moddeps_var),
            ("🏗️  Architektura",           self._show_architecture_var),
            ("🔀 Zmiany API",             self._show_api_changes_var),
        ]:
            tk.Checkbutton(sec_f, text=label, variable=var,
                           bg=t["bg"], fg=t["fg"], selectcolor=t["card"],
                           activebackground=t["bg"],
                           font=("Segoe UI", 8)).pack(anchor="w", padx=10, pady=1)

        # Config buttons
        cfg_btns = tk.Frame(scroll, bg=t["bg"])
        cfg_btns.pack(fill="x", padx=6, pady=6)
        ttk.Button(cfg_btns, text="💾 Zapisz .readmegen.json",
                   command=self._save_config).pack(side="left", padx=3)
        ttk.Button(cfg_btns, text="📂 Wczytaj config",
                   command=self._load_config).pack(side="left", padx=3)

    def _build_tab_info(self, parent, t):
        self._info_text = tk.Text(parent, bg=t["card"], fg=t["fg"],
                                  font=("Consolas", 8), wrap="word",
                                  state="disabled", relief="flat",
                                  insertbackground=t["fg"])
        sb = ttk.Scrollbar(parent, orient="vertical", command=self._info_text.yview)
        self._info_text.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self._info_text.pack(fill="both", expand=True, padx=4, pady=4)

    def _build_tab_quality(self, parent, t):
        header = tk.Frame(parent, bg=t["card2"], pady=4, padx=8)
        header.pack(fill="x")
        self._quality_score_var = tk.StringVar(value="— nie przeanalizowano —")
        tk.Label(header, textvariable=self._quality_score_var,
                 font=("Segoe UI", 10, "bold"),
                 bg=t["card2"], fg=t["ylw"]).pack(side="left")

        self._quality_text = tk.Text(parent, bg=t["card"], fg=t["fg"],
                                     font=("Consolas", 8), wrap="word",
                                     state="disabled", relief="flat",
                                     insertbackground=t["fg"])
        sb2 = ttk.Scrollbar(parent, orient="vertical", command=self._quality_text.yview)
        self._quality_text.configure(yscrollcommand=sb2.set)
        sb2.pack(side="right", fill="y")
        self._quality_text.pack(fill="both", expand=True, padx=4, pady=4)

    def _build_tab_git(self, parent, t):
        self._git_text = tk.Text(parent, bg=t["card"], fg=t["fg"],
                                 font=("Consolas", 8), wrap="word",
                                 state="disabled", relief="flat",
                                 insertbackground=t["fg"])
        sb3 = ttk.Scrollbar(parent, orient="vertical", command=self._git_text.yview)
        self._git_text.configure(yscrollcommand=sb3.set)
        sb3.pack(side="right", fill="y")
        self._git_text.pack(fill="both", expand=True, padx=4, pady=4)

    def _build_tab_debug(self, parent, t):
        hdr = tk.Frame(parent, bg=t["card2"], pady=4, padx=8)
        hdr.pack(fill="x")
        tk.Label(hdr, text="🐛 Tryb debugowania",
                 font=("Segoe UI", 10, "bold"),
                 bg=t["card2"], fg=t["ylw"]).pack(side="left")
        ttk.Button(hdr, text="🔄 Odśwież",
                   command=self._refresh_debug_panel).pack(side="right", padx=4)

        self._debug_text = tk.Text(parent, bg=t["card"], fg=t["fg"],
                                   font=("Consolas", 8), wrap="word",
                                   state="disabled", relief="flat",
                                   insertbackground=t["fg"])
        sb4 = ttk.Scrollbar(parent, orient="vertical", command=self._debug_text.yview)
        self._debug_text.configure(yscrollcommand=sb4.set)
        sb4.pack(side="right", fill="y")
        self._debug_text.pack(fill="both", expand=True, padx=4, pady=4)
        self._write_text(self._debug_text, "← Wykonaj analizę (🔍 Analizuj) i kliknij 🔄 Odśwież.")

    # ── Akcje ────────────────────────────────────────────────────────

    def _pick_folder(self):
        path = filedialog.askdirectory(title="Wybierz katalog projektu")
        if path:
            self._path_var.set(path)
            self._project = self._meta = self._git_data = None
            self._test_data = self._quality_data = None
            self._set_status(f"Wybrano: {path}")
            self._load_config()

    def _run_analyze(self):
        path = self._path_var.get()
        if path == "— nie wybrano —":
            messagebox.showwarning("Brak projektu", "Najpierw wybierz katalog projektu.")
            return
        self._set_status("⏳ Analizuję projekt…")

        def task():
            try:
                mode  = self._tree_mode_var.get()
                depth = self._tree_depth_var.get()
                self._project      = self._analyzer.analyze(path, mode, depth)
                self._meta         = self._extractor.extract(path)
                self._git_data     = self._git.analyze(path)
                self._test_data    = self._tests.analyze(path, self._project["test_files"])
                self._quality_data = self._quality.analyze(path)
                # v2.1 – nowe analizatory
                self._todo_data    = self._todo_extractor.analyze(path)
                self._unused_data  = self._unused_detector.analyze(path)
                self._contrib_data = self._contrib_gen.analyze(path, self._git_data)
                self._moddeps_data = self._moddep_analyzer.analyze(path)
                # v2.2
                self._project_type = self._type_detector.detect(path, self._project)
                self._summary_data = self._summary_gen.generate(
                    self._project, self._meta, self._git_data, self._project_type)
                self._api_changes  = self._api_change_det.detect_changes(path, self._meta)
                self._update_info_panel()
                self._update_quality_panel()
                self._update_git_panel()
                self._set_status(
                    f"✅ Analiza: {self._project['file_count']} plików | "
                    f"Typ: {self._project_type['type']} | "
                    f"Git: {'✅' if self._git_data['is_git'] else '❌'} | "
                    f"Jakość: {self._quality_data['score']}% | "
                    f"TODO: {self._todo_data['count']} | "
                    f"Nieużywane: {self._unused_data['unused_count']}"
                )
            except Exception as e:
                self._set_status(f"❌ Błąd analizy: {e}")

        threading.Thread(target=task, daemon=True).start()

    def _run_generate(self):
        path = self._path_var.get()
        if path == "— nie wybrano —":
            messagebox.showwarning("Brak projektu", "Najpierw wybierz katalog projektu.")
            return

        if self._project is None:
            self._set_status("⏳ Analizuję i generuję…")
            mode  = self._tree_mode_var.get()
            depth = self._tree_depth_var.get()
            self._project      = self._analyzer.analyze(path, mode, depth)
            self._meta         = self._extractor.extract(path)
            self._git_data     = self._git.analyze(path)
            self._test_data    = self._tests.analyze(path, self._project["test_files"])
            self._quality_data = self._quality.analyze(path)
            self._todo_data    = self._todo_extractor.analyze(path)
            self._unused_data  = self._unused_detector.analyze(path)
            self._contrib_data = self._contrib_gen.analyze(path, self._git_data)
            self._moddeps_data = self._moddep_analyzer.analyze(path)
            # v2.2
            self._project_type = self._type_detector.detect(path, self._project)
            self._summary_data = self._summary_gen.generate(
                self._project, self._meta, self._git_data, self._project_type)
            self._api_changes  = self._api_change_det.detect_changes(path, self._meta)
            self._update_info_panel()
            self._update_quality_panel()
            self._update_git_panel()
        else:
            self._set_status("⏳ Generuję README…")

        template_key = ReadmeGenerator.TEMPLATES[self._template_var.get()]
        custom = {
            "name":    self._inp_name.get().strip(),
            "desc":    self._inp_desc.get().strip(),
            "version": self._inp_version.get().strip(),
            "author":  self._inp_author.get().strip(),
            "github":  self._inp_github.get().strip(),
        }
        badge_style = self._badge_style_var.get()
        cfg = self._cfg_mgr.load(path)

        def task():
            try:
                text = self._gen.generate(
                    self._project, self._meta, self._git_data,
                    self._test_data, self._quality_data,
                    template_key, custom, badge_style,
                    todo=self._todo_data,
                    unused=self._unused_data,
                    contrib=self._contrib_data,
                    moddeps=self._moddeps_data,
                    cfg=cfg,
                    project_type=self._project_type,
                    summary=self._summary_data,
                    api_changes=self._api_changes,
                )
                self._show_preview(text)
                self._set_status(
                    f"✅ Wygenerowano — {len(text.splitlines())} linii | "
                    f"Szablon: {self._template_var.get()} | "
                    f"Typ: {(self._project_type or {}).get('type', '?')}"
                )
                self.bus.publish("readme_generator", "generated",
                                 {"lines": len(text.splitlines()), "template": template_key})
            except Exception as e:
                self._set_status(f"❌ Błąd generowania: {e}")

        threading.Thread(target=task, daemon=True).start()

    def _save_readme(self):
        if not self._preview_text:
            return
        content = self._preview_text.get("1.0", "end").strip()
        if not content or content.startswith("← Wybierz"):
            messagebox.showinfo("Brak treści", "Najpierw wygeneruj README.")
            return
        path = self._path_var.get()
        default_dir = path if path != "— nie wybrano —" else os.path.expanduser("~")
        save_path = filedialog.asksaveasfilename(
            initialdir=default_dir, initialfile="README.md",
            defaultextension=".md",
            filetypes=[("Markdown", "*.md"), ("Tekst", "*.txt"), ("Wszystkie", "*.*")],
            title="Zapisz README.md",
        )
        if save_path:
            try:
                Path(save_path).write_text(content, encoding="utf-8")
                self._set_status(f"💾 Zapisano: {save_path}")
                self.bus.publish("readme_generator", "saved", {"path": save_path})
                messagebox.showinfo("Zapisano", f"README.md zapisany:\n{save_path}")
            except Exception as e:
                messagebox.showerror("Błąd zapisu", str(e))

    def _export_txt(self):
        """Eksportuje raport jakości dokumentacji do pliku TXT."""
        if not self._quality_data:
            messagebox.showinfo("Brak danych", "Najpierw wykonaj analizę (🔍 Analizuj).")
            return
        path = self._path_var.get()
        default_dir = path if path != "— nie wybrano —" else os.path.expanduser("~")
        save_path = filedialog.asksaveasfilename(
            initialdir=default_dir, initialfile="doc_quality_report.txt",
            defaultextension=".txt",
            filetypes=[("Tekst", "*.txt"), ("Wszystkie", "*.*")],
            title="Eksportuj raport jakości",
        )
        if save_path:
            q = self._quality_data
            p = self._project or {}
            g = self._git_data or {}
            lines = [
                "=" * 62,
                "  RAPORT JAKOŚCI DOKUMENTACJI — README Generator Pro v2.0",
                f"  Projekt:  {Path(path).name}",
                f"  Data:     {datetime.now().strftime('%Y-%m-%d %H:%M')}",
                "=" * 62, "",
                f"Wynik ogólny:    {q['score']}%  ({'✅ Doskonały' if q['score']>=90 else ('⚠️ Do poprawy' if q['score']>=60 else '❌ Wymaga uwagi')})",
                f"Elementy:        {q['total_items']}",
                f"Braki:           {q['missing_count']}",
                f"README:          {'✅ Tak' if q['has_readme'] else '❌ Brak'}",
                f"LICENSE:         {'✅ Tak' if q['has_license'] else '❌ Brak'}",
                f"CHANGELOG:       {'✅ Tak' if q['has_changelog'] else '❌ Brak'}",
                "",
                f"Język:           {p.get('language','—')}",
                f"Pliki:           {p.get('file_count','—')}",
                f"Rozmiar:         {p.get('repo_size_kb','—')} KB",
                f"Testy:           {'Tak' if p.get('has_tests') else 'Nie'}",
                "",
                "─" * 62,
                "GIT:",
                "─" * 62,
                f"Branch:          {g.get('branch','—')}",
                f"Ostatni commit:  {g.get('last_commit_hash','—')} — {g.get('last_commit_msg','—')}",
                f"Status:          {'✅ Czyste' if g.get('status_clean') else '⚠️ Zmiany'}",
                "",
                "─" * 62,
                "BRAKUJĄCE DOCSTRINGI:",
                "─" * 62, "",
            ]
            lines += q.get("missing", []) or ["✅ Brak braków!"]
            lines += ["", "─" * 62,
                      "Wygenerowano przez README Generator Pro v2.2 — Sebastian Januchowski @ polsoft.ITS™ Group | polsoft.its@fastservice.com"]
            try:
                Path(save_path).write_text("\n".join(lines), encoding="utf-8")
                self._set_status(f"📤 Raport wyeksportowany: {save_path}")
                messagebox.showinfo("Eksport", "Raport jakości zapisany.")
            except Exception as e:
                messagebox.showerror("Błąd", str(e))

    def _copy_to_clipboard(self):
        if not self._preview_text:
            return
        content = self._preview_text.get("1.0", "end").strip()
        if content and not content.startswith("← Wybierz"):
            self.app.clipboard_clear()
            self.app.clipboard_append(content)
            self._set_status("📋 Skopiowano do schowka.")

    def _toggle_watch(self):
        path = self._path_var.get()
        if self._watch_var.get():
            if path == "— nie wybrano —":
                messagebox.showwarning("Brak projektu", "Wybierz projekt przed włączeniem Watch.")
                self._watch_var.set(False)
                return
            self._watcher = WatchMode(path, self._on_watch_change, interval=3.0)
            self._watcher.start()
            self._set_status("👁 Watch mode WŁĄCZONY — monitoruję zmiany…")
        else:
            if self._watcher:
                self._watcher.stop()
                self._watcher = None
            self._set_status("👁 Watch mode WYŁĄCZONY.")

    def _on_watch_change(self, changed, added, removed):
        names = [Path(f).name for f in (changed + added + removed)[:3]]
        self._set_status(f"👁 Zmiana: {', '.join(names)} — regeneruję…")
        path = self._path_var.get()
        try:
            mode  = self._tree_mode_var.get()
            depth = self._tree_depth_var.get()
            self._project      = self._analyzer.analyze(path, mode, depth)
            self._meta         = self._extractor.extract(path)
            self._git_data     = self._git.analyze(path)
            self._test_data    = self._tests.analyze(path, self._project["test_files"])
            self._quality_data = self._quality.analyze(path)
            self._todo_data    = self._todo_extractor.analyze(path)
            self._unused_data  = self._unused_detector.analyze(path)
            self._contrib_data = self._contrib_gen.analyze(path, self._git_data)
            self._moddeps_data = self._moddep_analyzer.analyze(path)
            # v2.2
            self._project_type = self._type_detector.detect(path, self._project)
            self._summary_data = self._summary_gen.generate(
                self._project, self._meta, self._git_data, self._project_type)
            self._api_changes  = self._api_change_det.detect_changes(path, self._meta)
            self._update_info_panel()
            self._update_quality_panel()
            self._update_git_panel()

            template_key = ReadmeGenerator.TEMPLATES[self._template_var.get()]
            custom = {
                "name":    self._inp_name.get().strip(),
                "desc":    self._inp_desc.get().strip(),
                "version": self._inp_version.get().strip(),
                "author":  self._inp_author.get().strip(),
                "github":  self._inp_github.get().strip(),
            }
            cfg = self._cfg_mgr.load(path)
            text = self._gen.generate(
                self._project, self._meta, self._git_data,
                self._test_data, self._quality_data,
                template_key, custom, self._badge_style_var.get(),
                todo=self._todo_data,
                unused=self._unused_data,
                contrib=self._contrib_data,
                moddeps=self._moddeps_data,
                cfg=cfg,
                project_type=self._project_type,
                summary=self._summary_data,
                api_changes=self._api_changes,
            )
            self._show_preview(text)
            self._set_status(f"✅ Auto-regeneracja ({len(text.splitlines())} linii)")
        except Exception as e:
            self._set_status(f"❌ Błąd auto-regeneracji: {e}")

    def _refresh_debug_panel(self):
        """Odświeża zakładkę Debug z pełnym raportem analizy."""
        if not self._project:
            self._write_text(self._debug_text,
                             "← Najpierw wykonaj analizę (🔍 Analizuj).")
            return
        report = self._debug_inspector.inspect(
            self._project,
            self._meta         or {},
            self._git_data     or {},
            self._test_data    or {},
            self._quality_data or {},
            self._todo_data    or {},
            self._unused_data  or {},
            self._contrib_data or {},
            self._moddeps_data or {},
        )
        self._write_text(self._debug_text, report)

    # ── Akcje v2.2 ───────────────────────────────────────────────────

    def _generate_extended_docs(self):
        """Generuje docs/api.md, docs/usage.md, docs/configuration.md."""
        path = self._path_var.get()
        if path == "— nie wybrano —":
            messagebox.showwarning("Brak projektu", "Wybierz projekt.")
            return
        if not self._project:
            messagebox.showinfo("Brak analizy", "Najpierw wykonaj analizę (🔍 Analizuj).")
            return

        def task():
            try:
                cfg = self._cfg_mgr.load(path)
                api_doc   = self._ext_docs_gen.generate_api_doc(self._meta, self._project)
                usage_doc = self._ext_docs_gen.generate_usage_doc(self._meta, self._project)
                cfg_doc   = self._ext_docs_gen.generate_configuration_doc(self._project, cfg)
                saved     = self._ext_docs_gen.save_docs(path, api_doc, usage_doc, cfg_doc)
                if "error" in saved:
                    self._set_status(f"❌ Błąd zapisu docs/: {saved['error']}")
                else:
                    files = ", ".join(saved.keys())
                    self._set_status(f"📚 Wygenerowano docs/: {files}")
                    self.app.after(0, lambda: messagebox.showinfo(
                        "Dokumentacja zapisana",
                        f"Zapisano pliki:\n" + "\n".join(saved.values())
                    ))
            except Exception as e:
                self._set_status(f"❌ Błąd generowania docs/: {e}")

        threading.Thread(target=task, daemon=True).start()

    def _save_api_snapshot(self):
        """Zapisuje snapshot aktualnego API do pliku .readmegen_api_snapshot.json."""
        path = self._path_var.get()
        if path == "— nie wybrano —":
            messagebox.showwarning("Brak projektu", "Wybierz projekt.")
            return
        if not self._meta:
            messagebox.showinfo("Brak analizy", "Najpierw wykonaj analizę (🔍 Analizuj).")
            return
        try:
            self._api_change_det.take_snapshot(path, self._meta)
            # Odśwież wykrywanie zmian — po zapisie nie ma zmian
            self._api_changes = self._api_change_det.detect_changes(path, self._meta)
            self._set_status("📸 Snapshot API zapisany — zmiany będą wykrywane od teraz.")
            messagebox.showinfo("Snapshot API",
                                "Snapshot publicznego API zapisany.\n"
                                "Kolejne analizy będą porównywane z tym stanem.")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def _toggle_precommit_hook(self):
        """Instaluje lub odinstalowuje pre-commit hook."""
        path = self._path_var.get()
        if path == "— nie wybrano —":
            messagebox.showwarning("Brak projektu", "Wybierz projekt.")
            return
        if self._hook_gen.is_installed(path):
            result = self._hook_gen.uninstall(path)
            if result["success"]:
                self._set_status("🔗 Pre-commit hook odinstalowany.")
                messagebox.showinfo("Hook usunięty",
                                    "Pre-commit hook README Generator został usunięty.")
            else:
                messagebox.showerror("Błąd", result.get("error", "Nieznany błąd"))
        else:
            result = self._hook_gen.install(path)
            if result["success"]:
                self._set_status(f"🔗 Pre-commit hook zainstalowany: {result['path']}")
                messagebox.showinfo("Hook zainstalowany",
                                    f"Pre-commit hook zainstalowany:\n{result['path']}\n\n"
                                    "README.md będzie automatycznie aktualizowane przed każdym commitem.")
            else:
                messagebox.showerror("Błąd instalacji hooka", result.get("error", "Nieznany błąd"))

    def _generate_conventional_changelog(self):
        """Generuje CHANGELOG.md z Conventional Commits i zapisuje go w projekcie."""
        path = self._path_var.get()
        if path == "— nie wybrano —":
            messagebox.showwarning("Brak projektu", "Wybierz projekt.")
            return
        if not self._git_data:
            messagebox.showinfo("Brak analizy", "Najpierw wykonaj analizę (🔍 Analizuj).")
            return
        version = (self._inp_version.get().strip()
                   or (self._meta or {}).get("version", ""))

        def task():
            try:
                content = self._conv_changelog.generate_from_git(
                    path, self._git_data, version=version)
                ok = self._conv_changelog.save_changelog(path, content)
                if ok:
                    self._set_status("📜 CHANGELOG.md wygenerowany i zapisany.")
                    self.app.after(0, lambda: messagebox.showinfo(
                        "Changelog zapisany",
                        f"CHANGELOG.md zapisany w:\n{path}\n\n"
                        "Plik zawiera historię commitów wg Conventional Commits."
                    ))
                else:
                    self._set_status("❌ Błąd zapisu CHANGELOG.md")
            except Exception as e:
                self._set_status(f"❌ Błąd generowania changelog: {e}")

        threading.Thread(target=task, daemon=True).start()

    def _save_config(self):
        path = self._path_var.get()
        if path == "— nie wybrano —":
            messagebox.showwarning("Brak projektu", "Wybierz projekt.")
            return
        cfg = {
            "template":          ReadmeGenerator.TEMPLATES.get(self._template_var.get(), "opensource"),
            "tree_mode":         self._tree_mode_var.get(),
            "tree_depth":        self._tree_depth_var.get(),
            "badge_style":       self._badge_style_var.get(),
            "name":              self._inp_name.get().strip(),
            "version":           self._inp_version.get().strip(),
            "author":            self._inp_author.get().strip(),
            "description":       self._inp_desc.get().strip(),
            "github_url":        self._inp_github.get().strip(),
            # v2.1
            "show_unused":       self._show_unused_var.get(),
            "show_roadmap":      self._show_roadmap_var.get(),
            "show_contributing": self._show_contributing_var.get(),
            "show_module_deps":  self._show_moddeps_var.get(),
            # v2.2
            "show_architecture": getattr(self, "_show_architecture_var",
                                         tk.BooleanVar(value=True)).get(),
            "show_api_changes":  getattr(self, "_show_api_changes_var",
                                         tk.BooleanVar(value=True)).get(),
        }
        self._cfg_mgr.save(path, cfg)
        self._set_status("💾 Zapisano .readmegen.json")

    def _load_config(self):
        path = self._path_var.get()
        if path == "— nie wybrano —":
            return
        cfg = self._cfg_mgr.load(path)
        rev = {v: k for k, v in ReadmeGenerator.TEMPLATES.items()}
        self._template_var.set(rev.get(cfg.get("template", "opensource"), "Open-Source"))
        self._tree_mode_var.set(cfg.get("tree_mode", "compact"))
        self._tree_depth_var.set(cfg.get("tree_depth", 2))
        self._badge_style_var.set(cfg.get("badge_style", "flat"))
        for attr, key in [("_inp_name", "name"), ("_inp_version", "version"),
                          ("_inp_author", "author"), ("_inp_desc", "description"),
                          ("_inp_github", "github_url")]:
            entry = getattr(self, attr, None)
            if entry and cfg.get(key):
                entry.delete(0, "end")
                entry.insert(0, cfg[key])
        # v2.1 + v2.2 – przełączniki sekcji
        for var_attr, key, default in [
            ("_show_unused_var",       "show_unused",       True),
            ("_show_roadmap_var",      "show_roadmap",      True),
            ("_show_contributing_var", "show_contributing", True),
            ("_show_moddeps_var",      "show_module_deps",  True),
            ("_show_architecture_var", "show_architecture", True),
            ("_show_api_changes_var",  "show_api_changes",  True),
        ]:
            var = getattr(self, var_attr, None)
            if var is not None:
                var.set(cfg.get(key, default))

    # ── Panele informacyjne ──────────────────────────────────────────

    def _update_info_panel(self):
        if not self._project:
            return
        p, m = self._project, self._meta or {}
        td   = self._test_data or {}
        pt   = self._project_type or {}
        sm   = self._summary_data or {}
        ac   = self._api_changes or {}
        lang_stats = p.get("lang_stats", {})
        total_lf   = sum(lang_stats.values()) or 1
        lang_bar   = " | ".join(
            f"{l}: {c} ({int(c/total_lf*100)}%)"
            for l, c in sorted(lang_stats.items(), key=lambda x: -x[1])[:5]
        )
        lines = [
            f"📁 Projekt:    {p['name']}",
            f"🗣️  Język:      {p['language']}",
            f"📊 Języki:     {lang_bar}",
            f"📄 Pliki:      {p['file_count']}",
            f"📂 Katalogi:   {p['dir_count']}",
            f"💾 Rozmiar:    {p['repo_size_kb']} KB",
            f"🚪 Wejście:    {p['entry']}",
            f"📜 Licencja:   {p['license']}",
            f"🧪 Testy:      {'Tak' if p['has_tests'] else 'Nie'} ({td.get('framework','')})",
            f"⚙️  Konfigi:    {', '.join(p['configs']) if p['configs'] else 'brak'}",
            "",
            "── Metadane ─────────────────────",
            f"📌 Wersja:     {m.get('version') or '—'}",
            f"👤 Autor:      {m.get('author') or '—'}",
            f"📝 Opis:       {(m.get('description') or '—')[:60]}",
            f"🔷 Klas:       {len(m.get('classes', []))}",
            f"🔩 Funkcji:    {len(m.get('functions', []))}",
            "",
            "── Typ projektu (v2.2) ──────────",
            f"🏷️  Typ:        {pt.get('type', '—')} (pewność: {pt.get('confidence', 0)})",
            f"📐 Szablon:    {pt.get('recommended_tpl', '—')}",
            f"🔑 Słowa kl.:  {', '.join(sm.get('keywords', [])[:8]) or '—'}",
            "",
            "── Zmiany API ───────────────────",
            f"📸 Snapshot:   {'✅ Tak' if ac.get('has_snapshot') else '❌ Brak'}",
            f"🔀 Zmiany:     {'⚠️ Tak' if ac.get('outdated') else '✅ Brak'}",
            f"➕ Dodane:     {len(ac.get('added', []))}",
            f"➖ Usunięte:   {len(ac.get('removed', []))}",
            f"🔄 Zmienione:  {len(ac.get('changed', []))}",
            "",
            "── Zależności ───────────────────",
        ]
        for fname, info in p.get("deps", {}).items():
            lines.append(f"📦 {fname} ({info['manager']}): {len(info['content'])} pakietów")

        self._write_text(self._info_text, "\n".join(lines))

    def _update_quality_panel(self):
        if not self._quality_data:
            return
        q      = self._quality_data
        score  = q["score"]
        emoji  = "🟢" if score >= 90 else ("🟡" if score >= 60 else "🔴")
        self._quality_score_var.set(
            f"{emoji} Jakość: {score}%  "
            f"({q['missing_count']}/{q['total_items']} bez docstrings)"
        )
        lines = [
            f"README:     {'✅' if q['has_readme'] else '❌'}",
            f"LICENSE:    {'✅' if q['has_license'] else '❌'}",
            f"CHANGELOG:  {'✅' if q['has_changelog'] else '❌'}",
            "",
            "─" * 40,
            "Brakujące docstringi:",
            "─" * 40,
        ]
        lines += q.get("missing", []) or ["✅ Wszystko udokumentowane!"]
        self._write_text(self._quality_text, "\n".join(lines))

    def _update_git_panel(self):
        if not self._git_data:
            return
        g = self._git_data
        if not g.get("is_git"):
            self._write_text(self._git_text, "❌ Katalog nie jest repozytorium Git.")
            return
        lines = [
            f"🌿 Branch:        {g.get('branch','—')}",
            f"🔖 Ostatni hash:  {g.get('last_commit_hash','—')}",
            f"💬 Wiadomość:     {g.get('last_commit_msg','—')}",
            f"📅 Data:          {g.get('last_commit_date','—')}",
            f"👤 Autor:         {g.get('last_commit_author','—')}",
            f"🔢 Commity:       {g.get('commits_count',0)}",
            f"🌐 Remote:        {g.get('remote_url','—')}",
            f"✨ Status:        {'✅ Czyste' if g.get('status_clean') else '⚠️ Niezacommitowane zmiany'}",
            "",
            "─" * 40,
            "📋 Ostatnie commity:",
            "─" * 40,
        ]
        for entry in g.get("changelog_entries", []):
            lines.append(f"  • {entry}")
        self._write_text(self._git_text, "\n".join(lines))

    # ── Helpers ──────────────────────────────────────────────────────

    def _write_text(self, widget, content):
        try:
            widget.config(state="normal")
            widget.delete("1.0", "end")
            widget.insert("end", content)
            widget.config(state="disabled")
        except Exception:
            pass

    def _show_preview(self, text):
        if self._preview_text:
            self._preview_text.config(state="normal")
            self._preview_text.delete("1.0", "end")
            self._preview_text.insert("end", text)

    def _set_status(self, msg):
        try:
            self._status_var.set(msg)
        except Exception:
            pass
