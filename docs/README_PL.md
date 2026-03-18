# README Generator Pro v2.2

> **polsoft.ITS™ Group** — Samodzielna aplikacja GUI do automatycznego generowania plików README.md

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/customtkinter-%E2%89%A55.2-orange?style=flat)](https://github.com/TomSchimansky/CustomTkinter)
[![Wersja](https://img.shields.io/badge/wersja-2.2.0-brightgreen?style=flat)](https://github.com/seb07uk)
[![Licencja](https://img.shields.io/badge/licencja-%C2%A9%202026%20polsoft.ITS%E2%84%A2-lightgrey?style=flat)](https://github.com/seb07uk)

---

## Opis

**README Generator Pro** to profesjonalna aplikacja desktopowa zbudowana na CustomTkinter, która automatycznie analizuje projekty programistyczne i generuje kompletną, gotową do publikacji dokumentację `README.md`. Aplikacja analizuje kod źródłowy, historię Git, pokrycie testami oraz jakość dokumentacji, a następnie tworzy spójne, dobrze ustrukturyzowane pliki README — bez ręcznej edycji.

Aplikacja działa w dwóch trybach: pełnym trybie GUI oraz bezgłowym trybie CLI, który można wykorzystać wewnątrz hooków Git pre-commit.

---

## Funkcje

- **Analiza projektu** — skanuje pliki, wykrywa główny język programowania, punkt wejścia, zależności, strukturę katalogów i rozmiar projektu
- **Integracja z Git** — odczytuje branch, hash/wiadomość/autora/datę ostatniego commita, liczbę commitów, zdalny URL oraz status drzewa roboczego
- **Ekstrakcja metadanych** — parsuje AST Pythona w celu wyodrębnienia `__version__`, `__author__`, docstringu modułu, funkcji, klas i brakujących docstringów
- **Generowanie README** — tworzy pełny plik `README.md` na podstawie czterech wbudowanych szablonów: *Minimalistyczny*, *Open-Source*, *Enterprise*, *polsoft.ITS™*
- **Style odznak** — obsługuje wiele stylów shield.io (flat, flat-square, plastic, for-the-badge, social)
- **Konfigurowalne sekcje** — włączanie i wyłączanie poszczególnych sekcji (Odznaki, Opis, Funkcje, Instalacja, Użycie, Struktura, API, Testy, Konfiguracja, Changelog, Licencja, Autor)
- **Drzewo katalogów** — renderuje kompaktowe lub pełne drzewo ASCII projektu z konfigurowalną głębokością
- **Raport jakości dokumentacji** — ocenia pokrycie docstringami, wykrywa braki i eksportuje raport jakości do pliku TXT
- **Śledzenie zmian API** — zapisuje snapshot publicznego API i wykrywa breaking changes przy kolejnych uruchomieniach
- **Generowanie Changelogu** — tworzy `CHANGELOG.md` na podstawie Conventional Commits
- **Rozszerzona dokumentacja** — generuje folder `docs/` z dodatkowymi stronami dokumentacji
- **Hook Git pre-commit** — instaluje hook, który automatycznie regeneruje `README.md` przed każdym commitem
- **Tryb Watch** — monitoruje katalog projektu i regeneruje README przy zmianach plików
- **Dwujęzyczny interfejs** — pełny interfejs w języku angielskim i polskim z przełącznikiem języka jednym kliknięciem
- **Obsługa motywów** — motywy: Ciemny, Jasny, Ciemno-niebieski i Zielony
- **Tryb CLI** — bezgłowe generowanie przez `--cli <ścieżka>` dla potoków CI/CD i hooków Git
- **System pluginów** — rozszerzalna architektura z dodatkowymi modułami (Detektor nieużywanych symboli, TODO→Roadmap, Generator Contributing, Diagram zależności modułów, Dokumentacja architektury, Diff API, Conventional Changelog, Hook pre-commit)
- **Trwałość konfiguracji** — zapisuje i wczytuje ustawienia projektu do/z pliku `.readmegen.json`

---

## Wymagania

| Wymaganie | Wersja |
|---|---|
| Python | 3.10 lub wyższa |
| customtkinter | ≥ 5.2 |

> Aplikacja zawiera wbudowany backend zastępczy, dzięki czemu działa samodzielnie. Umieszczenie pliku `readme_generator.py` w tym samym katalogu automatycznie aktywuje pełny backend.

---

## Instalacja

```bash
pip install customtkinter
```

Sklonuj lub pobierz repozytorium, a następnie uruchom:

```bash
python readme_generator_app.py
```

---

## Użycie

### Tryb GUI

Uruchom aplikację i skorzystaj z paska narzędzi:

1. **📂 Otwórz projekt** — wybierz katalog projektu (obsługuje przeciąganie i upuszczanie)
2. **🔍 Analizuj** — przeskanuj projekt (język, Git, testy, docstringi)
3. **⚡ Generuj README** — wygeneruj podgląd pliku `README.md`
4. **💾 Zapisz .md** — zapisz wynik na dysk
5. **📋 Kopiuj** — skopiuj surowy Markdown do schowka
6. **📤 Eksport TXT** — eksportuj raport jakości dokumentacji
7. **📚 Generuj docs/** — wygeneruj rozszerzony folder `docs/`
8. **📜 Changelog** — wygeneruj `CHANGELOG.md` z historii commitów
9. **🪝 Hook git** — zainstaluj lub usuń hook pre-commit
10. **👁 Watch** — włącz automatyczne odświeżanie przy zmianach plików

### Tryb CLI

```bash
python readme_generator_app.py --cli /ścieżka/do/projektu
```

Odczytuje `.readmegen.json` z katalogu głównego projektu (jeśli istnieje) i zapisuje `README.md` w tym samym katalogu. Idealny do użycia wewnątrz hooka pre-commit.

---

## Struktura

```
readme_generator_app.py   # Główna aplikacja GUI (standalone + GUI + CLI)
readme_generator.py       # Opcjonalny pełny moduł backend
.readmegen.json           # Konfiguracja projektu (generowana automatycznie)
```

---

## Konfiguracja

Ustawienia projektu są zapisywane w pliku `.readmegen.json` w katalogu projektu. Plik przechowuje:

- `template` — klucz aktywnego szablonu README
- `badge_style` — styl odznak shield.io
- `sections` — flagi włączenia/wyłączenia poszczególnych sekcji
- `name`, `desc`, `version`, `author`, `github_url` — nadpisania metadanych

Zapisuj i wczytuj konfiguracje z zakładki **⚙️ Konf.** przy użyciu przycisków **💾 Zapisz .readmegen.json** i **📂 Wczytaj**.

---

## API

Główne klasy wewnętrzne udostępniane przez backend:

| Klasa | Odpowiedzialność |
|---|---|
| `ProjectAnalyzer` | Drzewo plików, wykrywanie języka, parsowanie zależności, rozmiar |
| `GitAnalyzer` | Branch, commity, zdalny URL, status drzewa roboczego |
| `MetadataExtractor` | Parsowanie AST Pythona, ekstrakcja wersji/autora/docstringów |
| `ReadmeGenerator` | Synteza Markdown ze wszystkich zebranych danych |
| `DocQualityAnalyzer` | Ocena pokrycia docstringami i wykrywanie braków |
| `ChangelogGenerator` | CHANGELOG.md z logu Git |
| `ApiChangeDetector` | Snapshot publicznego API i diff |
| `WatchMode` | Obserwator systemu plików do regeneracji na żywo |

---

## Licencja

**2026 © Sebastian Januchowski & polsoft.ITS™ Group**

Wszelkie prawa zastrzeżone. Niniejsze oprogramowanie i jego kod źródłowy są własnością Sebastiana Januchowskiego i polsoft.ITS™ Group.

---

## Autor

| | |
|---|---|
| **Autor** | Sebastian Januchowski |
| **Firma** | polsoft.ITS™ Group |
| **E-mail** | polsoft.its@fastservice.com |
| **GitHub** | https://github.com/seb07uk |
| **Wersja** | 2.2.0 |

---

*Wygenerowano przez README Generator Pro v2.2 — Sebastian Januchowski · polsoft.ITS™ Group*
