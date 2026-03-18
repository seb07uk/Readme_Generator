<img width="1182" height="895" alt="Screenshot" src="https://github.com/user-attachments/assets/47e7e24b-ca9f-4aee-b044-15eb978f16fb" />


# README Generator Pro v2.2

> **polsoft.ITS™ Group** — Standalone GUI application for automatic README.md generation

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/customtkinter-%E2%89%A55.2-orange?style=flat)](https://github.com/TomSchimansky/CustomTkinter)
[![Version](https://img.shields.io/badge/version-2.2.0-brightgreen?style=flat)](https://github.com/seb07uk)
[![License](https://img.shields.io/badge/license-%C2%A9%202026%20polsoft.ITS%E2%84%A2-lightgrey?style=flat)](https://github.com/seb07uk)

---

## Description

**README Generator Pro** is a professional desktop application built with CustomTkinter that automatically analyzes software projects and generates complete, ready-to-publish `README.md` documentation. It inspects source code, Git history, test coverage, and documentation quality, then synthesizes a coherent, well-structured README without any manual editing.

The application can operate in two modes: a full-featured GUI mode and a headless CLI mode for use inside pre-commit Git hooks.

---

## Features

- **Project Analysis** — scans files, detects the primary language, entry point, dependencies, directory structure, and project size
- **Git Integration** — reads branch, last commit hash/message/author/date, commit count, remote URL, and working-tree status
- **Metadata Extraction** — parses Python AST to extract `__version__`, `__author__`, module docstring, functions, classes, and missing docstrings
- **README Generation** — produces a full `README.md` from four built-in templates: *Minimalist*, *Open-Source*, *Enterprise*, *polsoft.ITS™*
- **Badge Styles** — supports multiple shield.io badge styles (flat, flat-square, plastic, for-the-badge, social)
- **Configurable Sections** — enable or disable individual sections (Badges, Description, Features, Installation, Usage, Structure, API, Tests, Configuration, Changelog, License, Author)
- **Directory Tree** — renders a compact or full ASCII tree of the project with configurable depth
- **Documentation Quality Report** — scores docstring coverage, detects missing docs, and exports a quality report as TXT
- **API Change Tracking** — saves a public-API snapshot and detects breaking changes on subsequent runs
- **Changelog Generation** — generates `CHANGELOG.md` from Conventional Commits
- **Extended Docs** — generates `docs/` folder with additional documentation pages
- **Pre-commit Git Hook** — installs a hook that automatically regenerates `README.md` before every commit
- **Watch Mode** — monitors the project directory and regenerates the README on file changes
- **Bilingual UI** — full English and Polish interface with a single-click language toggle
- **Theme Support** — Dark, Light, Dark-Blue, and Green themes
- **CLI Mode** — headless generation via `--cli <path>` for CI/CD pipelines and Git hooks
- **Plugin System** — extensible architecture with additional analyser/generator modules (Unused Symbol Detector, TODO→Roadmap, Contributing Generator, Module Dependency Diagram, Architecture Docs, API Diff, Conventional Changelog, Pre-commit Hook)
- **Configuration Persistence** — saves/loads project settings to `.readmegen.json`

---

## Requirements

| Requirement | Version |
|---|---|
| Python | 3.10 or higher |
| customtkinter | ≥ 5.2 |

> The application ships a built-in fallback backend so it runs standalone. Placing `readme_generator.py` in the same directory activates the full-featured backend automatically.

---

## Installation

```bash
pip install customtkinter
```

Clone or download the repository, then run:

```bash
python readme_generator_app.py
```

---

## Usage

### GUI Mode

Launch the application and use the toolbar to:

1. **📂 Open project** — select a project directory (supports drag-and-drop)
2. **🔍 Analyze** — scan the project (language, Git, tests, docstrings)
3. **⚡ Generate README** — produce the `README.md` preview
4. **💾 Save .md** — save the result to disk
5. **📋 Copy** — copy the raw Markdown to the clipboard
6. **📤 Export TXT** — export a documentation-quality report
7. **📚 Generate docs/** — generate an extended `docs/` folder
8. **📜 Changelog** — generate `CHANGELOG.md` from commit history
9. **🪝 Git hook** — install/remove the pre-commit hook
10. **👁 Watch** — enable live-reload on file changes

### CLI Mode

```bash
python readme_generator_app.py --cli /path/to/project
```

Reads `.readmegen.json` from the project root (if present) and writes `README.md` to the same directory. Ideal for use inside a pre-commit hook.

---

## Structure

```
readme_generator_app.py   # Main GUI application (standalone + GUI + CLI)
readme_generator.py       # Optional full backend module
.readmegen.json           # Per-project configuration (auto-generated)
```

---

## Configuration

Project settings are persisted in `.readmegen.json` inside the project directory. The file stores:

- `template` — active README template key
- `badge_style` — shield.io badge style
- `sections` — per-section enabled/disabled flags
- `name`, `desc`, `version`, `author`, `github_url` — metadata overrides

Save and load configurations from the **⚙️ Config** tab using the **💾 Save .readmegen.json** and **📂 Load** buttons.

---

## API

Key internal classes exposed by the backend:

| Class | Responsibility |
|---|---|
| `ProjectAnalyzer` | File tree, language detection, dependency parsing, size |
| `GitAnalyzer` | Branch, commits, remote URL, working-tree status |
| `MetadataExtractor` | Python AST parsing, version/author/docstring extraction |
| `ReadmeGenerator` | Markdown synthesis from all collected data |
| `DocQualityAnalyzer` | Docstring coverage scoring and missing-doc detection |
| `ChangelogGenerator` | CHANGELOG.md from Git log |
| `ApiChangeDetector` | Public API snapshot and diff |
| `WatchMode` | File-system watcher for live regeneration |

---

## License

**2026 © Sebastian Januchowski & polsoft.ITS™ Group**

All rights reserved. This software and its source code are the property of Sebastian Januchowski and polsoft.ITS™ Group.

---

## Author

| | |
|---|---|
| **Author** | Sebastian Januchowski |
| **Company** | polsoft.ITS™ Group |
| **E-mail** | polsoft.its@fastservice.com |
| **GitHub** | https://github.com/seb07uk |
| **Version** | 2.2.0 |

---

*Generated by README Generator Pro v2.2 — Sebastian Januchowski · polsoft.ITS™ Group*
