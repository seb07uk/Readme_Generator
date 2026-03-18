# README Generator Pro v2.2

> Automatyczne generowanie `README.md` z analizy projektu — GUI + CLI.

[![Version](https://img.shields.io/badge/version-2.2.0-blue?style=flat)](https://github.com/seb07uk)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/license-©%20polsoft.ITS™-yellow?style=flat)](https://github.com/seb07uk)

---

## Wymagania

- Python 3.10+
- `customtkinter >= 5.2`

```bash
pip install customtkinter
```

---

## Uruchomienie

```bash
# GUI
python readme_generator_app.py

# CLI (bez GUI, np. jako pre-commit hook)
python readme_generator_app.py --cli /ścieżka/projektu
```

---

## Główne funkcje

- 🔍 Analiza projektu — język, pliki, klasy, funkcje, zależności, Git
- 🎨 Szablony README — Minimalist, Open-Source, Enterprise, polsoft.ITS™
- 📑 Wybór sekcji — włącz/wyłącz dowolne sekcje README
- 🪝 Pre-commit hook — auto-regeneracja przed każdym `git commit`
- 📸 Snapshot API — wykrywanie breaking changes
- 📜 Changelog — z Conventional Commits
- 🌍 Język UI — EN 🇬🇧 / PL 🇵🇱

---

## Autor

**Sebastian Januchowski** · [polsoft.ITS™ Group](https://github.com/seb07uk) · polsoft.its@fastservice.com

2026 © Sebastian Januchowski & polsoft.ITS™ Group
