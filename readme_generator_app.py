"""
README Generator Pro v2.2 — polsoft.ITS™ Group
Standalone GUI Application (CustomTkinter)

Uruchomienie:
    pip install customtkinter
    python readme_generator_app.py

Wymagania: Python 3.10+, customtkinter>=5.2

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

# ══════════════════════════════════════════════════════════════════════════════
#   INTERNATIONALISATION  (EN first, PL second)
# ══════════════════════════════════════════════════════════════════════════════

_LANG = "en"   # default language — EN

_T: dict[str, dict[str, str]] = {
    # ── Generic ──────────────────────────────────────────────────────────────
    "ok":                          {"en": "OK",               "pl": "OK"},
    "error":                       {"en": "Error",            "pl": "Błąd"},
    "close":                       {"en": "Close",            "pl": "Zamknij"},
    "cancel":                      {"en": "Cancel",           "pl": "Anuluj"},
    "yes":                         {"en": "Yes",              "pl": "Tak"},
    "no":                          {"en": "No",               "pl": "Nie"},
    "lang_switch":                 {"en": "🇵🇱 PL",           "pl": "🇬🇧 EN"},

    # ── App / window ─────────────────────────────────────────────────────────
    "app_title":                   {"en": "README Generator Pro v2.2 — polsoft.ITS™ Group",
                                    "pl": "README Generator Pro v2.2 — polsoft.ITS™ Group"},
    "titlebar_name":               {"en": "README Generator Pro", "pl": "README Generator Pro"},
    "titlebar_company":            {"en": "polsoft.ITS™ Group",   "pl": "polsoft.ITS™ Group"},
    "titlebar_author":             {"en": "Sebastian Januchowski","pl": "Sebastian Januchowski"},
    "theme_label":                 {"en": "Theme:",              "pl": "Motyw:"},
    "status_ready":                {"en": "Ready.",              "pl": "Gotowy."},
    "status_backend_full":         {"en": "✅ Full backend loaded (readme_generator.py)",
                                    "pl": "✅ Pełny backend załadowany (readme_generator.py)"},
    "status_backend_standalone":   {"en": "ℹ️  Standalone mode — built-in backend",
                                    "pl": "ℹ️  Tryb standalone — wbudowany backend"},

    # ── Toolbar buttons ───────────────────────────────────────────────────────
    "btn_open":                    {"en": "📂 Open project",   "pl": "📂 Otwórz projekt"},
    "btn_analyze":                 {"en": "🔍 Analyze",        "pl": "🔍 Analizuj"},
    "btn_generate":                {"en": "⚡ Generate README","pl": "⚡ Generuj README"},
    "btn_save_md":                 {"en": "💾 Save .md",       "pl": "💾 Zapisz .md"},
    "btn_copy":                    {"en": "📋 Copy",           "pl": "📋 Kopiuj"},
    "btn_export":                  {"en": "📤 Export TXT",     "pl": "📤 Eksport TXT"},
    "btn_gen_docs":                {"en": "📚 Generate docs/", "pl": "📚 Generuj docs/"},
    "btn_changelog":               {"en": "📜 Changelog",      "pl": "📜 Changelog"},
    "btn_hook":                    {"en": "🪝 Git hook",        "pl": "🪝 Hook git"},
    "btn_watch":                   {"en": "👁 Watch",           "pl": "👁 Watch"},

    # ── Left panel tabs ───────────────────────────────────────────────────────
    "tab_config":                  {"en": "⚙️ Config",          "pl": "⚙️ Konf."},
    "tab_analysis":                {"en": "🔎 Analysis",        "pl": "🔎 Analiza"},
    "tab_sections":                {"en": "📑 Sections",        "pl": "📑 Sekcje"},
    "tab_plugins":                 {"en": "🔌 Plugins",         "pl": "🔌 Pluginy"},

    # ── Config tab ────────────────────────────────────────────────────────────
    "drop_title":                  {"en": "Drag project folder", "pl": "Przeciągnij folder projektu"},
    "drop_hint":                   {"en": "or click to choose",  "pl": "lub kliknij, żeby wybrać"},
    "no_project":                  {"en": "— none selected —",   "pl": "— nie wybrano —"},
    "card_template":               {"en": "🎨 README Template",  "pl": "🎨 Szablon README"},
    "card_badge":                  {"en": "🏷️ Badge style",      "pl": "🏷️ Styl odznak (badges)"},
    "card_tree":                   {"en": "🌲 Directory tree",   "pl": "🌲 Drzewo katalogów"},
    "tree_mode_label":             {"en": "Mode:",               "pl": "Tryb:"},
    "tree_depth_label":            {"en": "Depth:",              "pl": "Głęb.:"},
    "card_metadata":               {"en": "✏️ Metadata (optional)", "pl": "✏️ Metadane (opcjonalne)"},
    "field_name":                  {"en": "Name:",               "pl": "Nazwa:"},
    "field_desc":                  {"en": "Desc:",               "pl": "Opis:"},
    "field_version":               {"en": "Version:",            "pl": "Wersja:"},
    "field_author":                {"en": "Author:",             "pl": "Autor:"},
    "field_github":                {"en": "GitHub:",             "pl": "GitHub:"},
    "btn_save_cfg":                {"en": "💾 Save .readmegen.json", "pl": "💾 Zapisz .readmegen.json"},
    "btn_load_cfg":                {"en": "📂 Load",             "pl": "📂 Wczytaj"},

    # ── Analysis tab ──────────────────────────────────────────────────────────
    "card_stats":                  {"en": "📊 Project statistics", "pl": "📊 Statystyki projektu"},
    "stat_files":                  {"en": "Files",                "pl": "Pliki"},
    "stat_dirs":                   {"en": "Directories",          "pl": "Katalogi"},
    "stat_size":                   {"en": "Size",                 "pl": "Rozmiar"},
    "stat_lang":                   {"en": "Language",             "pl": "Język"},
    "stat_classes":                {"en": "Classes",              "pl": "Klasy"},
    "stat_funcs":                  {"en": "Functions",            "pl": "Funkcje"},
    "card_quality":                {"en": "📈 Documentation quality", "pl": "📈 Jakość dokumentacji"},
    "bar_docstrings":              {"en": "Docstrings",           "pl": "Docstringi"},
    "bar_tests":                   {"en": "Test coverage",        "pl": "Pokrycie testami"},
    "card_details":                {"en": "🔎 Project details",   "pl": "🔎 Szczegóły projektu"},

    # ── Sections tab ──────────────────────────────────────────────────────────
    "card_sections":               {"en": "📑 README sections — enable/disable",
                                    "pl": "📑 Sekcje README — włącz/wyłącz i sortuj"},
    "sections_hint":               {"en": "Select sections to generate:",
                                    "pl": "Zaznacz sekcje do wygenerowania:"},
    "btn_all":                     {"en": "✅ All",               "pl": "✅ Wszystkie"},
    "btn_clear":                   {"en": "❌ Clear",             "pl": "❌ Wyczyść"},
    "card_api_track":              {"en": "🔀 API change tracking","pl": "🔀 Śledzenie zmian API"},
    "api_track_hint":              {"en": "Save a public API snapshot\nto detect breaking changes.",
                                    "pl": "Zapisz snapshot publicznego API,\naby wykrywać breaking changes."},
    "btn_api_snapshot":            {"en": "📸 Save API snapshot", "pl": "📸 Zapisz snapshot API"},

    # ── Section names (used as keys in the generator) ─────────────────────────
    "sec_Badges":                  {"en": "Badges",               "pl": "Odznaki"},
    "sec_Description":             {"en": "Description",          "pl": "Opis"},
    "sec_Features":                {"en": "Features",             "pl": "Funkcje"},
    "sec_Installation":            {"en": "Installation",         "pl": "Instalacja"},
    "sec_Usage":                   {"en": "Usage",                "pl": "Użycie"},
    "sec_Structure":               {"en": "Structure",            "pl": "Struktura"},
    "sec_API":                     {"en": "API",                  "pl": "API"},
    "sec_Tests":                   {"en": "Tests",                "pl": "Testy"},
    "sec_Config":                  {"en": "Configuration",        "pl": "Konfiguracja"},
    "sec_Changelog":               {"en": "Changelog",            "pl": "Changelog"},
    "sec_License":                 {"en": "License",              "pl": "Licencja"},
    "sec_Author":                  {"en": "Author",               "pl": "Autor"},

    # ── Template names ────────────────────────────────────────────────────────
    "tpl_Minimal":                 {"en": "Minimalist",           "pl": "Minimalistyczny"},
    "tpl_OpenSource":              {"en": "Open-Source",          "pl": "Open-Source"},
    "tpl_Enterprise":              {"en": "Enterprise",           "pl": "Enterprise"},
    "tpl_polsoft":                 {"en": "polsoft.ITS™",         "pl": "polsoft.ITS™"},

    # ── Plugins tab ───────────────────────────────────────────────────────────
    "card_plugins":                {"en": "🔌 Plugins — analysers & generators",
                                    "pl": "🔌 Pluginy — analizatory i generatory"},
    "plugins_hint":                {"en": "Enable additional analysis modules:",
                                    "pl": "Włącz dodatkowe moduły analizy:"},
    "card_plugin_info":            {"en": "ℹ️ About the plugin system",
                                    "pl": "ℹ️ O systemie pluginów"},
    "plugin_info_text":            {"en": "Plugins extend the generator's capabilities.\n"
                                         "Installed add-ons will appear here\nautomatically upon detection.",
                                    "pl": "Pluginy rozszerzają możliwości generatora.\n"
                                         "Zainstalowane dodatki pojawią się tu\nautomatycznie po wykryciu."},

    # Plugin descriptions
    "plugin_unused_desc":          {"en": "Detect unused public symbols",
                                    "pl": "Wykrywa nieużywane publiczne symbole"},
    "plugin_todo_desc":            {"en": "Scan TODO/FIXME → Roadmap section",
                                    "pl": "Skanuje TODO/FIXME → sekcja Roadmap"},
    "plugin_contrib_desc":         {"en": "Auto Contributing section + commit style",
                                    "pl": "Auto-sekcja Contributing + styl commitów"},
    "plugin_moddeps_desc":         {"en": "Module dependency diagram",
                                    "pl": "Diagram zależności między modułami"},
    "plugin_arch_desc":            {"en": "Project architecture documentation",
                                    "pl": "Dokumentacja architektury projektu"},
    "plugin_apidet_desc":          {"en": "Snapshot and diff of public API",
                                    "pl": "Snapshot i diff publicznego API"},
    "plugin_convch_desc":          {"en": "CHANGELOG.md from Conventional Commits",
                                    "pl": "CHANGELOG.md z Conventional Commits"},
    "plugin_prehook_desc":         {"en": "Install pre-commit git hook",
                                    "pl": "Instaluje pre-commit hook git"},

    # ── Center panel ─────────────────────────────────────────────────────────
    "preview_header":              {"en": "👁 README.md Preview",  "pl": "👁 Podgląd README.md"},
    "preview_raw":                 {"en": "📄 RAW",                "pl": "📄 RAW"},
    "preview_rendered":            {"en": "🎨 Preview",            "pl": "🎨 Podgląd"},
    "preview_placeholder":         {"en": "← Select a project and click ⚡ Generate README",
                                    "pl": "← Wybierz projekt i kliknij ⚡ Generuj README"},
    "line_count":                  {"en": "lines",                 "pl": "linii"},
    "word_count":                  {"en": "words",                 "pl": "słów"},

    # ── Right panel ───────────────────────────────────────────────────────────
    "right_header":                {"en": "🌿 Git & Status",       "pl": "🌿 Git & Status"},
    "card_git":                    {"en": "🌿 Git repository",     "pl": "🌿 Repozytorium Git"},
    "git_branch":                  {"en": "Branch",                "pl": "Branch"},
    "git_hash":                    {"en": "Hash",                  "pl": "Hash"},
    "git_commit":                  {"en": "Commit",                "pl": "Commit"},
    "git_date":                    {"en": "Date",                  "pl": "Data"},
    "git_author":                  {"en": "Author",                "pl": "Autor"},
    "git_commits":                 {"en": "Commits",               "pl": "Commity"},
    "git_status":                  {"en": "Status",                "pl": "Status"},
    "git_clean":                   {"en": "✅ Clean",              "pl": "✅ Czyste"},
    "git_dirty":                   {"en": "⚠️ Changes",            "pl": "⚠️ Zmiany"},
    "card_commits":                {"en": "📋 Recent commits",     "pl": "📋 Ostatnie commity"},
    "card_hook":                   {"en": "🪝 Pre-commit Hook",    "pl": "🪝 Pre-commit Hook"},
    "hook_not_installed":          {"en": "❌ Not installed",      "pl": "❌ Nie zainstalowany"},
    "hook_installed":              {"en": "✅ Installed (README Generator)",
                                    "pl": "✅ Zainstalowany (README Generator)"},
    "card_api_changes":            {"en": "🔀 API Changes",        "pl": "🔀 Zmiany API"},
    "api_no_snapshot":             {"en": "📸 No API snapshot",    "pl": "📸 Brak snapshotu API"},

    # ── Status bar ────────────────────────────────────────────────────────────
    "about_btn":                   {"en": "ℹ️ About",              "pl": "ℹ️ About"},
    "statusbar_info":              {"en": "Sebastian Januchowski  ·  polsoft.ITS™ Group  ·  v2.2",
                                    "pl": "Sebastian Januchowski  ·  polsoft.ITS™ Group  ·  v2.2"},

    # ── Messages / dialogs ────────────────────────────────────────────────────
    "msg_no_project_title":        {"en": "No project",            "pl": "Brak projektu"},
    "msg_no_project":              {"en": "Select a project first.", "pl": "Najpierw wybierz katalog projektu."},
    "msg_no_project_short":        {"en": "Select a project.",      "pl": "Wybierz projekt."},
    "msg_no_data_title":           {"en": "No data",               "pl": "Brak danych"},
    "msg_no_data":                 {"en": "Run analysis first.",    "pl": "Najpierw wykonaj analizę."},
    "msg_no_analysis_title":       {"en": "No analysis",           "pl": "Brak analizy"},
    "msg_no_content_title":        {"en": "No content",            "pl": "Brak treści"},
    "msg_no_content":              {"en": "Generate README first.", "pl": "Najpierw wygeneruj README."},
    "msg_no_git_title":            {"en": "No git",                "pl": "Brak git"},
    "msg_no_git":                  {"en": "Project is not a Git repository.",
                                    "pl": "Projekt nie jest repozytorium Git."},
    "msg_saved_title":             {"en": "Saved",                 "pl": "Zapisano"},
    "msg_saved":                   {"en": "README.md saved:\n",    "pl": "README.md zapisany:\n"},
    "msg_copied":                  {"en": "📋 Copied to clipboard.","pl": "📋 Skopiowano do schowka."},
    "msg_cfg_saved":               {"en": "💾 Saved .readmegen.json", "pl": "💾 Zapisano .readmegen.json"},
    "msg_cfg_loaded":              {"en": "📂 Loaded .readmegen.json","pl": "📂 Wczytano .readmegen.json"},
    "msg_hook_dir_err_title":      {"en": "Error",                 "pl": "Błąd"},
    "msg_hook_dir_err":            {"en": "Directory .git/hooks does not exist.\nIs this a git repository?",
                                    "pl": "Katalog .git/hooks nie istnieje.\nCzy to jest repozytorium git?"},
    "msg_hook_removed_title":      {"en": "Hook removed",          "pl": "Hook usunięty"},
    "msg_hook_removed":            {"en": "Pre-commit hook has been removed.",
                                    "pl": "Pre-commit hook został usunięty."},
    "msg_hook_installed_title":    {"en": "Hook installed",        "pl": "Hook zainstalowany"},
    "msg_hook_installed":          {"en": "Pre-commit hook installed:\n{path}\n\n"
                                         "README.md will be regenerated before every git commit.",
                                    "pl": "Pre-commit hook zainstalowany:\n{path}\n\n"
                                         "README.md będzie regenerowane przed każdym git commit."},
    "msg_hook_install_err_title":  {"en": "Installation error",    "pl": "Błąd instalacji"},
    "msg_api_title":               {"en": "API Snapshot",          "pl": "Snapshot API"},
    "msg_api_saved":               {"en": "Saved snapshot of {n} public API symbols.\n"
                                         "Future analyses will detect changes.",
                                    "pl": "Zapisano snapshot {n} publicznych symboli API.\n"
                                         "Kolejne analizy będą wykrywać zmiany."},
    "msg_docs_title":              {"en": "Documentation",         "pl": "Dokumentacja"},
    "msg_docs_saved":              {"en": "Files saved to:\n",     "pl": "Zapisano pliki w katalogu:\n"},
    "msg_changelog_title":         {"en": "Changelog",             "pl": "Changelog"},
    "msg_changelog_saved":         {"en": "CHANGELOG.md generated and saved.",
                                    "pl": "CHANGELOG.md wygenerowany i zapisany."},
    "msg_export_title":            {"en": "Export",                "pl": "Eksport"},
    "msg_export_saved":            {"en": "Quality report saved.", "pl": "Raport jakości zapisany."},
    "msg_watch_no_project":        {"en": "Select a project before enabling Watch.",
                                    "pl": "Wybierz projekt przed włączeniem Watch."},

    # ── Status messages ───────────────────────────────────────────────────────
    "status_selected":             {"en": "Selected: ",            "pl": "Wybrano: "},
    "status_analyzing":            {"en": "⏳ Analysing project…", "pl": "⏳ Analizuję projekt…"},
    "status_analyzing_generating": {"en": "⏳ Analysing and generating…",
                                    "pl": "⏳ Analizuję i generuję…"},
    "status_analyze_ok":           {"en": "✅ Analysis: {files} files | Language: {lang} | Quality: {q}% | Git: {git}",
                                    "pl": "✅ Analiza: {files} plików | Język: {lang} | Jakość: {q}% | Git: {git}"},
    "status_analyze_err":          {"en": "❌ Analysis error: ",   "pl": "❌ Błąd analizy: "},
    "status_gen_ok":               {"en": "✅ Generated — {lines} lines | Template: {tpl}",
                                    "pl": "✅ Wygenerowano — {lines} linii | Szablon: {tpl}"},
    "status_gen_err":              {"en": "❌ Generation error: ", "pl": "❌ Błąd generowania: "},
    "status_gen_err_short":        {"en": "❌ Error: ",            "pl": "❌ Błąd: "},
    "status_saved":                {"en": "💾 Saved: ",            "pl": "💾 Zapisano: "},
    "status_hook_removed":         {"en": "🪝 Pre-commit hook uninstalled.", "pl": "🪝 Pre-commit hook odinstalowany."},
    "status_hook_installed":       {"en": "🪝 Pre-commit hook installed.", "pl": "🪝 Pre-commit hook zainstalowany."},
    "status_api_saved":            {"en": "📸 API snapshot saved ({n} symbols).",
                                    "pl": "📸 Snapshot API zapisany ({n} symboli)."},
    "status_api_saved_lbl":        {"en": "✅ Snapshot: {n} symbols","pl": "✅ Snapshot: {n} symboli"},
    "status_docs_ok":              {"en": "📚 Generated docs/api.md, docs/usage.md, docs/configuration.md",
                                    "pl": "📚 Wygenerowano docs/api.md, docs/usage.md, docs/configuration.md"},
    "status_changelog_saved":      {"en": "📜 CHANGELOG.md saved in {path}",
                                    "pl": "📜 CHANGELOG.md zapisany w {path}"},
    "status_export_saved":         {"en": "📤 Report saved: ",     "pl": "📤 Raport zapisany: "},
    "status_watch_on":             {"en": "👁 Watch mode ON — monitoring changes…",
                                    "pl": "👁 Watch mode WŁĄCZONY — monitoruję zmiany…"},
    "status_watch_off":            {"en": "👁 Watch mode OFF.",     "pl": "👁 Watch mode WYŁĄCZONY."},
    "status_watch_change":         {"en": "👁 File changed — regenerating…",
                                    "pl": "👁 Zmiana pliku — regeneruję…"},

    # ── About dialog ─────────────────────────────────────────────────────────
    "about_title":                 {"en": "About — README Generator Pro v2.2",
                                    "pl": "O programie — README Generator Pro v2.2"},
    "about_subtitle":              {"en": "Version 2.2.0  ·  polsoft.ITS™ Group",
                                    "pl": "Version 2.2.0  ·  polsoft.ITS™ Group"},
    "about_row_author":            {"en": "👤 Author",             "pl": "👤 Autor"},
    "about_row_company":           {"en": "🏢 Company",            "pl": "🏢 Firma"},
    "about_row_email":             {"en": "📧 E-mail",             "pl": "📧 E-mail"},
    "about_row_github":            {"en": "🐙 GitHub",             "pl": "🐙 GitHub"},
    "about_row_year":              {"en": "📅 Year",               "pl": "📅 Rok"},
    "about_row_license":           {"en": "📜 License",            "pl": "📜 Licencja"},
    "about_row_python":            {"en": "🐍 Python",             "pl": "🐍 Python"},
    "about_row_version":           {"en": "📦 Version",            "pl": "📦 Wersja"},
    "about_desc":                  {"en": "Automatic README.md generator for software projects.\n"
                                         "Analyses source code, Git, tests,\n"
                                         "documentation quality and produces consistent docs.",
                                    "pl": "Automatyczny generator plików README.md dla projektów\n"
                                         "programistycznych. Analizuje kod źródłowy, Git, testy,\n"
                                         "jakość dokumentacji i generuje spójną dokumentację."},

    # ── Info text panel ───────────────────────────────────────────────────────
    "info_project":                {"en": "📁 Project:  ",         "pl": "📁 Projekt:  "},
    "info_langs":                  {"en": "🗣  Languages:",        "pl": "🗣  Języki:   "},
    "info_entry":                  {"en": "🚪 Entry:    ",         "pl": "🚪 Wejście:  "},
    "info_license":                {"en": "📜 License:  ",         "pl": "📜 Licencja: "},
    "info_tests":                  {"en": "🧪 Tests:    ",         "pl": "🧪 Testy:    "},
    "info_configs":                {"en": "⚙  Configs:  ",         "pl": "⚙  Konfigi:  "},
    "info_version":                {"en": "📌 Version:  ",         "pl": "📌 Wersja:   "},
    "info_author":                 {"en": "👤 Author:   ",         "pl": "👤 Autor:    "},
    "info_description":            {"en": "📝 Desc:     ",         "pl": "📝 Opis:     "},
    "info_qual_header":            {"en": "── Doc quality ───────────────",
                                    "pl": "── Jakość dokumentacji ───────"},
    "info_qual_score":             {"en": "📊 Score:    ",         "pl": "📊 Wynik:    "},
    "info_qual_missing":           {"en": "❗ Missing:  ",         "pl": "❗ Braki:    "},
    "info_readme":                 {"en": "📄 README:   ",         "pl": "📄 README:   "},
    "info_license2":               {"en": "📜 LICENSE:  ",         "pl": "📜 LICENSE:  "},
    "info_changelog":              {"en": "📋 CHANGELOG:",         "pl": "📋 CHANGELOG:"},
    "info_deps_header":            {"en": "── Dependencies ─────────────",
                                    "pl": "── Zależności ───────────────"},
    "info_packages":               {"en": " packages",             "pl": " pakietów"},

    # ── Dialog titles / file pickers ─────────────────────────────────────────
    "dlg_pick_folder":             {"en": "Select project directory",
                                    "pl": "Wybierz katalog projektu"},
    "dlg_save_readme":             {"en": "Save README.md",        "pl": "Zapisz README.md"},
    "dlg_export":                  {"en": "Export report",         "pl": "Eksportuj raport"},
    "dlg_export_default":          {"en": "quality_report.txt",    "pl": "raport_jakosci.txt"},
    "ft_markdown":                 {"en": "Markdown",              "pl": "Markdown"},
    "ft_text":                     {"en": "Text",                  "pl": "Tekst"},
    "ft_all":                      {"en": "All",                   "pl": "Wszystkie"},

    # ── Export report ─────────────────────────────────────────────────────────
    "rpt_title":                   {"en": "DOCUMENTATION QUALITY REPORT",
                                    "pl": "RAPORT JAKOŚCI DOKUMENTACJI"},
    "rpt_author_lbl":              {"en": "Author: ",              "pl": "Autor:  "},
    "rpt_project_lbl":             {"en": "Project:",              "pl": "Projekt:"},
    "rpt_date_lbl":                {"en": "Date:   ",              "pl": "Data:   "},
    "rpt_overall":                 {"en": "Overall score:",        "pl": "Wynik ogólny:  "},
    "rpt_elements":                {"en": "Elements:    ",         "pl": "Elementy:      "},
    "rpt_missing":                 {"en": "Missing:     ",         "pl": "Braki:         "},
    "rpt_readme":                  {"en": "README:      ",         "pl": "README:        "},
    "rpt_license":                 {"en": "LICENSE:     ",         "pl": "LICENSE:       "},
    "rpt_changelog":               {"en": "CHANGELOG:   ",         "pl": "CHANGELOG:     "},
    "rpt_language":                {"en": "Language:    ",         "pl": "Język:         "},
    "rpt_files":                   {"en": "Files:       ",         "pl": "Pliki:         "},
    "rpt_size":                    {"en": "Size:        ",         "pl": "Rozmiar:       "},
    "rpt_tests":                   {"en": "Tests:       ",         "pl": "Testy:         "},
    "rpt_git":                     {"en": "GIT:",                  "pl": "GIT:"},
    "rpt_branch":                  {"en": "Branch:         ",      "pl": "Branch:        "},
    "rpt_last_commit":             {"en": "Last commit:    ",      "pl": "Ostatni commit:"},
    "rpt_commit_author":           {"en": "Commit author:  ",      "pl": "Autor commita: "},
    "rpt_commit_date":             {"en": "Date:           ",      "pl": "Data:          "},
    "rpt_commit_count":            {"en": "Commit count:   ",      "pl": "Liczba commitów:"},
    "rpt_git_status":              {"en": "Status:         ",      "pl": "Status:        "},
    "rpt_git_clean":               {"en": "✅ Clean",              "pl": "✅ Czyste"},
    "rpt_git_dirty":               {"en": "⚠️ Uncommitted changes","pl": "⚠️ Niezacommitowane zmiany"},
    "rpt_missing_hdr":             {"en": "MISSING DOCSTRINGS:",   "pl": "BRAKUJĄCE DOCSTRINGI:"},
    "rpt_all_ok":                  {"en": "✅ All elements documented!",
                                    "pl": "✅ Wszystkie elementy udokumentowane!"},
    "rpt_qual_excellent":          {"en": "✅ Excellent",          "pl": "✅ Doskonały"},
    "rpt_qual_improve":            {"en": "⚠️ Needs improvement",  "pl": "⚠️ Do poprawy"},
    "rpt_qual_attention":          {"en": "❌ Needs attention",    "pl": "❌ Wymaga uwagi"},
    "rpt_footer1":                 {"en": "Generated by README Generator Pro v2.2",
                                    "pl": "Wygenerowano przez README Generator Pro v2.2"},
    "rpt_footer2":                 {"en": "Sebastian Januchowski  |  polsoft.ITS™ Group",
                                    "pl": "Sebastian Januchowski  |  polsoft.ITS™ Group"},
}


def T(key: str, **kwargs) -> str:
    """Return translated string for current language, with optional .format() kwargs."""
    entry = _T.get(key)
    if entry is None:
        return key
    text = entry.get(_LANG) or entry.get("en") or key
    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError:
            pass
    return text


def set_lang(lang: str):
    """Switch active language ('en' or 'pl')."""
    global _LANG
    _LANG = lang if lang in ("en", "pl") else "en"


import os
import sys
import json
import threading
import subprocess
import ast
import re
import hashlib
import time
from pathlib import Path
from datetime import datetime

import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import customtkinter as ctk

# ── Backend: dynamiczny import lub wbudowany fallback ─────────────────────────
# Gdy readme_generator.py istnieje obok tego pliku, używamy jego pełnych klas.
# W przeciwnym razie działają uproszczone klasy zdefiniowane poniżej.
_BACKEND_FILE = Path(__file__).parent / "readme_generator.py"
_USING_FULL_BACKEND = False

if _BACKEND_FILE.exists():
    try:
        import importlib.util as _ilu
        _spec = _ilu.spec_from_file_location("readme_generator_full", str(_BACKEND_FILE))
        _mod  = _ilu.module_from_spec(_spec)
        # Podaj fałszywy BaseModule żeby uniknąć ImportError z 'from main import BaseModule'
        import types as _types
        _fake_main = _types.ModuleType("main")
        class _FakeBase:
            def __init__(self, app=None): self.app = app
            bus = type("bus", (), {"publish": lambda *a, **k: None})()
            theme = {}
        _fake_main.BaseModule = _FakeBase
        sys.modules.setdefault("main", _fake_main)
        _spec.loader.exec_module(_mod)
        # Importuj klasy backendu z pełnego modułu
        ProjectAnalyzer           = _mod.ProjectAnalyzer
        GitAnalyzer               = _mod.GitAnalyzer
        MetadataExtractor         = _mod.MetadataExtractor
        ReadmeGenerator           = _mod.ReadmeGenerator
        DocQualityAnalyzer        = _mod.DocQualityAnalyzer
        TestAnalyzer              = _mod.TestAnalyzer
        BadgeGenerator            = _mod.BadgeGenerator
        ChangelogGenerator        = _mod.ChangelogGenerator
        TodoRoadmapExtractor      = _mod.TodoRoadmapExtractor
        UnusedFunctionDetector    = _mod.UnusedFunctionDetector
        ContributingGenerator     = _mod.ContributingGenerator
        ModuleDependencyAnalyzer  = _mod.ModuleDependencyAnalyzer
        ProjectTypeDetector       = _mod.ProjectTypeDetector
        ProjectSummaryGenerator   = _mod.ProjectSummaryGenerator
        ApiChangeDetector         = _mod.ApiChangeDetector
        ConventionalChangelogGenerator = _mod.ConventionalChangelogGenerator
        ExtendedDocsGenerator     = _mod.ExtendedDocsGenerator
        ArchitectureDocGenerator  = _mod.ArchitectureDocGenerator
        PreCommitHookGenerator    = _mod.PreCommitHookGenerator
        ConfigManager             = _mod.ConfigManager
        WatchMode                 = _mod.WatchMode
        _USING_FULL_BACKEND = True
        print(f"[ReadmeGeneratorApp] Załadowano pełny backend: {_BACKEND_FILE.name}")
    except Exception as _e:
        print(f"[ReadmeGeneratorApp] Fallback do wbudowanego backendu: {_e}")

# ── Wbudowany uproszczony backend (działa bez readme_generator.py) ────────────
class ProjectAnalyzer:
    LANG_MAP = {
        ".py":"Python",".js":"JavaScript",".ts":"TypeScript",".cs":"C#",
        ".go":"Go",".rs":"Rust",".java":"Java",".cpp":"C++",".c":"C",
        ".rb":"Ruby",".php":"PHP",".kt":"Kotlin",".swift":"Swift",
        ".html":"HTML",".css":"CSS",".vue":"Vue",".jsx":"React",".tsx":"React/TS",
    }
    ENTRY_POINTS = ["main.py","app.py","run.py","server.py","index.js",
                    "index.ts","Program.cs","main.go","main.rs","index.php"]
    DEP_FILES = {
        "requirements.txt":"pip","package.json":"npm",
        "pyproject.toml":"poetry/pip","Cargo.toml":"cargo",
        "go.mod":"go mod","Gemfile":"bundler",
    }
    LICENSE_NAMES = {"mit":"MIT","apache":"Apache 2.0","gpl":"GPL","bsd":"BSD","isc":"ISC"}
    IGNORE = {"__pycache__","node_modules","venv",".git",".idea",".vscode",
              "dist","build","target","bin","obj"}

    def analyze(self, root: str, tree_mode: str = "compact", tree_depth: int = 2) -> dict:
        root = Path(root)
        ext_count, files_list, dirs_set = {}, [], set()
        for p in root.rglob("*"):
            if any(part.startswith(".") or part in self.IGNORE for part in p.parts):
                continue
            if p.is_file():
                ext_count[p.suffix] = ext_count.get(p.suffix, 0) + 1
                files_list.append(p)
            elif p.is_dir():
                rel = p.relative_to(root).parts
                if rel: dirs_set.add(rel[0])

        lang, best, lang_stats = "Nieznany", 0, {}
        for ext, cnt in ext_count.items():
            name = self.LANG_MAP.get(ext)
            if name:
                lang_stats[name] = lang_stats.get(name, 0) + cnt
                if cnt > best: best, lang = cnt, name

        entry = next((ep for ep in self.ENTRY_POINTS if (root/ep).exists()), None)
        deps_info = {}
        for df, mgr in self.DEP_FILES.items():
            fp = root / df
            if fp.exists():
                deps_info[df] = {"manager": mgr, "content": self._read_deps(fp, df)}

        license_name = self._detect_license(root)
        has_tests, test_files = self._detect_tests(files_list)
        configs = [f.name for f in files_list
                   if f.name in (".env.example","config.json",".env","settings.py",
                                 "config.yaml","config.yml","appsettings.json")]
        tree = self._build_tree(root, max_depth=tree_depth, compact=(tree_mode=="compact"))
        total_bytes = sum(f.stat().st_size for f in files_list if f.exists())

        return {
            "root": str(root), "name": root.name,
            "language": lang, "lang_stats": lang_stats,
            "entry": entry or "brak",
            "deps": deps_info, "license": license_name,
            "has_tests": has_tests, "test_files": test_files,
            "configs": configs, "tree": tree,
            "file_count": len(files_list), "dir_count": len(dirs_set),
            "repo_size_kb": round(total_bytes/1024, 1),
        }

    def _read_deps(self, fp, filename):
        try:
            text = fp.read_text(encoding="utf-8", errors="ignore")
            if filename == "requirements.txt":
                return [l.strip() for l in text.splitlines()
                        if l.strip() and not l.startswith("#")][:20]
            if filename == "package.json":
                data = json.loads(text)
                return (list(data.get("dependencies",{}).keys()) +
                        list(data.get("devDependencies",{}).keys()))[:20]
        except Exception:
            pass
        return []

    def _detect_license(self, root):
        for name in ("LICENSE","LICENSE.txt","LICENSE.md","LICENCE"):
            fp = root/name
            if fp.exists():
                content = fp.read_text(errors="ignore").lower()
                for key, val in self.LICENSE_NAMES.items():
                    if key in content: return val
                return "Własna"
        return "Brak"

    def _detect_tests(self, files):
        test_files = [f for f in files
                      if f.name.startswith("test") or "tests" in str(f).lower()]
        return bool(test_files), [str(f.name) for f in test_files[:10]]

    def _build_tree(self, root, max_depth=2, compact=True):
        lines = [f"{root.name}/"]
        self._walk(root, "", lines, 0, max_depth, compact)
        return "\n".join(lines)

    def _walk(self, path, prefix, lines, depth, max_depth, compact):
        if depth >= max_depth: return
        limit = 12 if compact else 40
        try:
            children = sorted(
                [p for p in path.iterdir()
                 if not p.name.startswith(".") and p.name not in self.IGNORE],
                key=lambda p: (p.is_file(), p.name.lower())
            )[:limit]
        except PermissionError:
            return
        for i, child in enumerate(children):
            con = "└── " if i == len(children)-1 else "├── "
            icon = "📁 " if child.is_dir() else "📄 "
            lines.append(f"{prefix}{con}{icon}{child.name}{'/' if child.is_dir() else ''}")
            if child.is_dir():
                ext = "    " if i == len(children)-1 else "│   "
                self._walk(child, prefix+ext, lines, depth+1, max_depth, compact)


class GitAnalyzer:
    def analyze(self, root: str) -> dict:
        result = {"is_git":False,"branch":"","last_commit_hash":"",
                  "last_commit_msg":"","last_commit_date":"",
                  "last_commit_author":"","commits_count":0,
                  "remote_url":"","status_clean":True,"changelog_entries":[]}
        if not (Path(root)/".git").exists(): return result
        result["is_git"] = True
        def git(args):
            try:
                r = subprocess.run(["git"]+args, cwd=root,
                                   capture_output=True, text=True, timeout=5)
                return r.stdout.strip()
            except Exception: return ""
        result["branch"]             = git(["rev-parse","--abbrev-ref","HEAD"])
        result["last_commit_hash"]   = git(["log","-1","--format=%h"])
        result["last_commit_msg"]    = git(["log","-1","--format=%s"])
        result["last_commit_date"]   = git(["log","-1","--format=%ci"])[:10]
        result["last_commit_author"] = git(["log","-1","--format=%an"])
        count = git(["rev-list","--count","HEAD"])
        result["commits_count"] = int(count) if count.isdigit() else 0
        result["remote_url"]    = git(["remote","get-url","origin"])
        result["status_clean"]  = (git(["status","--porcelain"]) == "")
        log = git(["log","--oneline","-10","--pretty=format:%h %s (%ci)"])
        result["changelog_entries"] = [l for l in log.splitlines() if l][:10]
        return result


class MetadataExtractor:
    def extract(self, root: str) -> dict:
        root = Path(root)
        meta = {"version":"","author":"","description":"",
                "functions":[],"classes":[],"missing_docs":[]}
        for candidate in ("main.py","app.py","__init__.py","run.py"):
            fp = root/candidate
            if fp.exists():
                meta.update(self._parse_python(fp))
                break
        pj = root/"package.json"
        if pj.exists():
            try:
                data = json.loads(pj.read_text(encoding="utf-8"))
                if not meta["version"]:     meta["version"]     = data.get("version","")
                if not meta["author"]:      meta["author"]      = str(data.get("author",""))
                if not meta["description"]: meta["description"] = data.get("description","")
            except Exception: pass
        return meta

    def _parse_python(self, fp):
        result = {"version":"","author":"","description":"",
                  "functions":[],"classes":[],"missing_docs":[]}
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
                            if t.id == "__version__" and not result["version"]: result["version"] = val
                            if t.id == "__author__"  and not result["author"]:  result["author"]  = val
                if isinstance(node, ast.FunctionDef) and not node.col_offset:
                    doc  = ast.get_docstring(node) or ""
                    args = self._args(node)
                    ret  = self._ret(node)
                    result["functions"].append({"name":node.name,"args":args,"return":ret,
                                                "doc":doc.splitlines()[0][:80] if doc else ""})
                    if not doc: result["missing_docs"].append(f"def {node.name}()")
                if isinstance(node, ast.ClassDef) and not node.col_offset:
                    doc = ast.get_docstring(node) or ""
                    methods = []
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef):
                            m_doc = ast.get_docstring(item) or ""
                            methods.append({"name":item.name,"args":self._args(item),
                                            "return":self._ret(item),
                                            "doc":m_doc.splitlines()[0][:80] if m_doc else ""})
                    result["classes"].append({"name":node.name,
                                              "doc":doc.splitlines()[0][:80] if doc else "",
                                              "methods":methods})
        except Exception: pass
        return result

    def _args(self, node):
        args = []
        for a in node.args.args:
            if a.arg == "self": continue
            ann = ""
            if a.annotation:
                try: ann = ast.unparse(a.annotation)
                except Exception: pass
            args.append(f"{a.arg}: {ann}" if ann else a.arg)
        return args

    def _ret(self, node):
        if node.returns:
            try: return ast.unparse(node.returns)
            except Exception: pass
        return ""


class ReadmeGenerator:
    TEMPLATES = {
        "Minimalist":  "minimal",
        "Open-Source": "opensource",
        "Enterprise":  "enterprise",
        "polsoft.ITS™":"polsoft",
    }
    # Polish aliases kept for backwards compat with saved configs
    TEMPLATES_ALIAS = {
        "Minimalistyczny": "minimal",
        "Minimalist":      "minimal",
        "Open-Source":     "opensource",
        "Enterprise":      "enterprise",
        "polsoft.ITS™":    "polsoft",
    }

    def generate(self, project, meta, git, custom, template="opensource",
                 badge_style="flat", sections=None) -> str:
        sections = sections or {s: True for s in self._all_sections()}
        name    = custom.get("name")    or project["name"]
        desc    = custom.get("desc")    or meta.get("description") or f"Projekt {name}"
        version = custom.get("version") or meta.get("version")     or "1.0.0"
        author  = custom.get("author")  or meta.get("author")      or "Autor"
        github  = custom.get("github")  or git.get("remote_url")   or ""
        now     = datetime.now().strftime("%Y-%m-%d")

        badges = self._badges(project, meta, git, badge_style)
        deps   = self._deps_block(project)
        tree   = f"\n```\n{project.get('tree','')}\n```" if sections.get("Structure") else ""
        api    = self._api_block(meta)       if sections.get("API")            else ""
        tests  = self._tests_block(project)  if sections.get("Tests")          else ""
        cl     = self._changelog_block(git)  if sections.get("Changelog")      else ""
        feats  = self._features_block(meta)  if sections.get("Features")       else ""

        if template == "minimal":
            return self._minimal(name, desc, badges, deps, tree, now, project, author, sections)
        if template == "enterprise":
            return self._enterprise(name, desc, version, author, github, badges, deps,
                                    tree, api, tests, cl, feats, now, project, meta, git, sections)
        if template == "polsoft":
            return self._polsoft(name, desc, version, author, github, badges, deps,
                                 tree, api, tests, cl, feats, now, project, meta, git, sections)
        return self._opensource(name, desc, version, author, github, badges, deps,
                                tree, api, tests, cl, feats, now, project, meta, git, sections)

    def _all_sections(self):
        return ["Badges","Description","Features","Installation","Usage",
                "Structure","API","Tests","Configuration","Changelog",
                "License","Author"]

    def _badges(self, p, m, g, style):
        ver = m.get("version") or "1.0.0"
        lang = p.get("language","")
        lic  = p.get("license","Brak").replace(" ","-")
        lines = [
            f"![Version](https://img.shields.io/badge/version-{ver}-brightgreen?style={style})",
            f"![Language](https://img.shields.io/badge/language-{lang}-blue?style={style})",
            f"![License](https://img.shields.io/badge/license-{lic}-informational?style={style})",
        ]
        if p.get("has_tests"):
            lines.append(f"![Tests](https://img.shields.io/badge/tests-passing-success?style={style})")
        if g.get("is_git"):
            branch = g.get("branch","main")
            lines.append(f"![Branch](https://img.shields.io/badge/branch-{branch}-lightgrey?style={style})")
        return "\n".join(lines)

    def _deps_block(self, p):
        if not p.get("deps"): return "```bash\n# Brak pliku zależności\n```"
        lines = []
        cmd_map = {"pip":"pip install -r requirements.txt","npm":"npm install",
                   "poetry/pip":"poetry install","cargo":"cargo build","go mod":"go mod download"}
        for fname, info in p["deps"].items():
            cmd = cmd_map.get(info["manager"], f"# {info['manager']}")
            lines.append(f"```bash\n{cmd}\n```")
        return "\n".join(lines)

    def _api_block(self, m):
        rows = []
        for cls in m.get("classes",[])[:6]:
            for mth in cls.get("methods",[])[:4]:
                if mth["name"].startswith("_"): continue
                args = ", ".join(mth["args"]) or "—"
                ret  = mth.get("return") or "—"
                doc  = mth.get("doc") or "—"
                rows.append(f"| `{cls['name']}.{mth['name']}` | `{args}` | `{ret}` | {doc} |")
        for fn in m.get("functions",[])[:6]:
            args = ", ".join(fn["args"]) or "—"
            ret  = fn.get("return") or "—"
            doc  = fn.get("doc") or "—"
            rows.append(f"| `{fn['name']}` | `{args}` | `{ret}` | {doc} |")
        if not rows: return "\nBrak publicznego API.\n"
        header = ["\n| Metoda/Funkcja | Argumenty | Zwraca | Opis |",
                  "|----------------|-----------|--------|------|"]
        return "\n".join(header + rows)

    def _tests_block(self, p):
        if p.get("has_tests"):
            files = ", ".join(p.get("test_files",[])[:5])
            return f"✅ Wykryto testy: `{files}`\n\n```bash\npytest\n```"
        return "❌ Brak testów."

    def _changelog_block(self, g):
        entries = g.get("changelog_entries",[])
        if not entries: return "_Brak historii git._"
        lines = ["### Ostatnie zmiany\n"]
        for e in entries: lines.append(f"- `{e}`")
        return "\n".join(lines)

    def _features_block(self, m):
        items = []
        for cls in m.get("classes",[])[:4]:
            doc = f" — {cls['doc']}" if cls.get("doc") else ""
            items.append(f"- 🔷 **{cls['name']}**{doc}")
        for fn in m.get("functions",[])[:4]:
            doc = f" — {fn['doc']}" if fn.get("doc") else ""
            items.append(f"- 🔹 `{fn['name']}()`{doc}")
        if not items:
            items = ["- ✅ Modular architecture","- ✅ Easy configuration","- ✅ Built-in documentation"]
        return "\n".join(items)

    def _minimal(self, name, desc, badges, deps, tree, now, p, author, s):
        parts = [f"# {name}\n\n> {desc}\n"]
        if s.get("Badges"):       parts.append(badges)
        if s.get("Installation"): parts.append(f"\n## Installation\n\n{deps}")
        if s.get("Structure"):    parts.append(f"\n## Project structure\n{tree}")
        if s.get("License"):      parts.append(f"\n## License\n\n{p['license']}")
        parts.append(f"\n---\n*Generated {now} by [README Generator Pro v2.2](https://github.com/seb07uk) — [Sebastian Januchowski](https://github.com/seb07uk) @ [polsoft.ITS™ Group](https://github.com/seb07uk)*")
        return "\n".join(parts)

    def _opensource(self, name, desc, version, author, github, badges, deps,
                    tree, api, tests, cl, feats, now, p, m, g, s):
        gh = f"\n\n🔗 [GitHub]({github})" if github else ""
        score = self._quality_score(m)
        parts = [f"# {name}{gh}\n"]
        if s.get("Badges"):        parts.append(badges)
        if s.get("Description"):   parts.append(f"\n## 📖 Description\n\n{desc}")
        if s.get("Features"):      parts.append(f"\n## ✨ Features\n\n{feats}")
        if s.get("Installation"):  parts.append(f"\n## 🚀 Installation\n\n{deps}")
        if s.get("Structure"):     parts.append(f"\n## 📁 Directory structure\n{tree}")
        if s.get("API"):           parts.append(f"\n## 🔧 API\n{api}")
        if s.get("Tests"):         parts.append(f"\n## 🧪 Tests\n\n{tests}")
        if s.get("Configuration"): parts.append(f"\n## ⚙️ Configuration\n\nFiles: {', '.join(p['configs']) if p['configs'] else 'none'}")
        if s.get("Changelog"):     parts.append(f"\n## 📋 Changelog\n\n{cl}")
        if s.get("License"):       parts.append(f"\n## 📄 License\n\n{p['license']} — © {datetime.now().year} {author}")
        if s.get("Author"):        parts.append(f"\n## 👤 Author\n\n{author}")
        parts.append(f"\n---\n*Generated {now} by [README Generator Pro v2.2](https://github.com/seb07uk) — [Sebastian Januchowski](https://github.com/seb07uk) @ [polsoft.ITS™ Group](https://github.com/seb07uk)*")
        return "\n".join(parts)

    def _enterprise(self, name, desc, version, author, github, badges, deps,
                    tree, api, tests, cl, feats, now, p, m, g, s):
        return f"""# {name} — Technical Documentation

**Version:** {version}  **Author:** {author}  **Language:** {p['language']}  **License:** {p['license']}  **Date:** {now}

---

## 1. Summary

{desc}

---

## 2. Requirements

| Parameter | Value |
|-----------|-------|
| Language | **{p['language']}** |
| Entry point | `{p['entry']}` |
| Files | {p['file_count']} |
| Size | {p['repo_size_kb']} KB |

---

## 3. Installation

{deps}

---

## 4. Project architecture
{tree}

---

## 5. API documentation
{api}

---

## 6. Tests

{tests}

---

## 7. Changelog

{cl}

---

## 8. License

**{p['license']}** — © {datetime.now().year} {author}

---
*Generated by [README Generator Pro v2.2](https://github.com/seb07uk) — [Sebastian Januchowski](https://github.com/seb07uk) @ [polsoft.ITS™ Group](https://github.com/seb07uk)*
"""

    def _polsoft(self, name, desc, version, author, github, badges, deps,
                 tree, api, tests, cl, feats, now, p, m, g, s):
        gh_btn = (f"[![GitHub](https://img.shields.io/badge/GitHub-repo-black"
                  f"?style=for-the-badge&logo=github)]({github})") if github else ""
        score_e = "🟢" if self._quality_score(m) >= 90 else ("🟡" if self._quality_score(m) >= 60 else "🔴")
        return f"""<div align="center">

# 🚀 {name}

**{desc}**

{badges}
{gh_btn}

</div>

---

## 🎯 About

{desc}

Project created by **{author}** using **{p['language']}**.
Version: `{version}` | License: `{p['license']}` | Date: `{now}`

---

## ✨ Features

{feats}

---

## ⚡ Quick start

{deps}

---

## 📂 Project structure
{tree}

---

## 🧩 API
{api}

---

## 🧪 Tests

{tests}

---

## 📋 Changelog

{cl}

---

## {score_e} Documentation quality

Classes: {len(m.get('classes',[]))} | Functions: {len(m.get('functions',[]))} | Missing docstrings: {len(m.get('missing_docs',[]))}

---

## 📜 License

**{p['license']}** — © {datetime.now().year} **{author}** | [polsoft.ITS™ Group](https://github.com/seb07uk)

---

<div align="center">

*Generated by **[README Generator Pro v2.2](https://github.com/seb07uk)** — [Sebastian Januchowski](https://github.com/seb07uk) @ [polsoft.ITS™ Group](https://github.com/seb07uk)*

</div>
"""

    def _quality_score(self, m):
        total = len(m.get("functions",[])) + len(m.get("classes",[]))
        missing = len(m.get("missing_docs",[]))
        if not total: return 100
        return max(0, 100 - int(missing/total*100))


# ── Fallback: DocQualityAnalyzer i TestAnalyzer (gdy pełny backend niedostępny)
if not _USING_FULL_BACKEND:

    class DocQualityAnalyzer:
        """Uproszczona analiza jakości dokumentacji (fallback)."""
        IGNORE = {"__pycache__","venv",".git","node_modules","dist","build"}

        def analyze(self, root: str) -> dict:
            root = Path(root)
            total_items, missing = 0, []
            has_readme    = (root/"README.md").exists() or (root/"README.rst").exists()
            has_license   = any((root/n).exists() for n in ("LICENSE","LICENSE.txt","LICENCE"))
            has_changelog = any((root/n).exists() for n in ("CHANGELOG.md","CHANGES.md"))
            for fp in root.rglob("*.py"):
                if any(p in self.IGNORE for p in fp.parts): continue
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
                                    missing.append(f"  ↳ {rel}:{node.lineno} — `{name}`")
                except Exception: pass
            score = max(0, 100 - int(len(missing)/max(total_items,1)*100))
            return {
                "score": score, "missing": missing[:40],
                "total_items": total_items, "missing_count": len(missing),
                "has_readme": has_readme, "has_license": has_license,
                "has_changelog": has_changelog,
            }

    class TestAnalyzer:
        """Uproszczone wykrywanie testów (fallback)."""
        FRAMEWORKS = {
            "pytest":  {"files":["pytest.ini","pyproject.toml"],"cmd":"pytest"},
            "unittest":{"files":[],"imports":["unittest"],"cmd":"python -m unittest discover"},
            "jest":    {"files":["jest.config.js"],"cmd":"npm test"},
        }
        def analyze(self, root: str, test_files: list) -> dict:
            root = Path(root)
            for fw, info in self.FRAMEWORKS.items():
                for cfg in info.get("files",[]):
                    if (root/cfg).exists():
                        return {"framework":fw,"command":info["cmd"],"test_count":len(test_files),"test_files":test_files}
            if test_files:
                return {"framework":"pytest","command":"pytest","test_count":len(test_files),"test_files":test_files}
            return {"framework":"","command":"","test_count":0,"test_files":[]}

    class WatchMode:
        """Stub WatchMode (fallback — watch obsługuje wątek w GUI)."""
        def __init__(self, *a, **kw): pass
        def start(self): pass
        def stop(self): pass


# ══════════════════════════════════════════════════════════════════════════════
#   COLOUR PALETTE
# ══════════════════════════════════════════════════════════════════════════════
BG      = "#0a0c10"
BG2     = "#0f1218"
CARD    = "#141820"
CARD2   = "#1a2030"
BORDER  = "#1e2535"
BORDER2 = "#2a3550"

FG      = "#e2e8f8"
FG2     = "#8892b0"
FG3     = "#4a5570"

ACC     = "#00d4ff"
ACC2    = "#0099cc"
GRN     = "#00ff88"
YLW     = "#ffcc00"
RED     = "#ff4466"
PURPLE  = "#aa66ff"
ORANGE  = "#ff8844"

FONT_MONO = ("JetBrains Mono", 10)
FONT_UI   = ("Segoe UI",       10)
FONT_BOLD = ("Segoe UI",       10, "bold")
FONT_H1   = ("Segoe UI",       14, "bold")
FONT_H2   = ("Segoe UI",       12, "bold")
FONT_TINY = ("Segoe UI",        9)
FONT_MONO_SMALL = ("JetBrains Mono", 9)


def hex_to_rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


# ══════════════════════════════════════════════════════════════════════════════
#   CUSTOM WIDGETS
# ══════════════════════════════════════════════════════════════════════════════

class NeonButton(ctk.CTkButton):
    """Przycisk z neonową obwódką i efektem glow."""
    def __init__(self, master, accent=ACC, **kw):
        kw.setdefault("corner_radius", 8)
        kw.setdefault("border_width", 1)
        kw.setdefault("border_color", accent)
        kw.setdefault("fg_color", CARD)
        kw.setdefault("hover_color", CARD2)
        kw.setdefault("text_color", accent)
        kw.setdefault("font", FONT_BOLD)
        kw.setdefault("height", 30)
        super().__init__(master, **kw)


class PrimaryButton(ctk.CTkButton):
    """Gradient primary button."""
    def __init__(self, master, **kw):
        kw.setdefault("corner_radius", 8)
        kw.setdefault("fg_color", ACC)
        kw.setdefault("hover_color", ACC2)
        kw.setdefault("text_color", "#000000")
        kw.setdefault("font", ("Segoe UI", 11, "bold"))
        kw.setdefault("height", 34)
        super().__init__(master, **kw)


class SectionCard(ctk.CTkFrame):
    """Karta sekcji z tytułem."""
    def __init__(self, master, title: str, accent=ACC, **kw):
        kw.setdefault("fg_color", CARD)
        kw.setdefault("border_color", BORDER)
        kw.setdefault("border_width", 1)
        kw.setdefault("corner_radius", 10)
        super().__init__(master, **kw)
        hdr = ctk.CTkFrame(self, fg_color=CARD2, corner_radius=0,
                           border_width=0, height=24)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)
        self._hdr_lbl = ctk.CTkLabel(hdr, text=title, text_color=accent,
                     font=("Segoe UI", 10, "bold"),
                     anchor="w")
        self._hdr_lbl.pack(side="left", padx=10, pady=4)

    def body(self) -> ctk.CTkFrame:
        f = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        f.pack(fill="both", expand=True, padx=6, pady=6)
        return f


class StatBadge(ctk.CTkFrame):
    def __init__(self, master, label: str, value: str, color=ACC, **kw):
        kw.setdefault("fg_color", BG)
        kw.setdefault("border_color", BORDER)
        kw.setdefault("border_width", 1)
        kw.setdefault("corner_radius", 8)
        super().__init__(master, **kw)
        ctk.CTkLabel(self, text=label, text_color=FG3,
                     font=("Segoe UI", 8), anchor="w").pack(padx=8, pady=(5,0), anchor="w")
        self._val_lbl = ctk.CTkLabel(self, text=value, text_color=color,
                                     font=("JetBrains Mono", 15, "bold"), anchor="w")
        self._val_lbl.pack(padx=8, pady=(0,5), anchor="w")

    def set(self, value: str, color=None):
        self._val_lbl.configure(text=value)
        if color: self._val_lbl.configure(text_color=color)


class ProgressBar(ctk.CTkFrame):
    def __init__(self, master, label: str, **kw):
        kw.setdefault("fg_color", "transparent")
        super().__init__(master, **kw)
        hdr = ctk.CTkFrame(self, fg_color="transparent")
        hdr.pack(fill="x")
        self._label = ctk.CTkLabel(hdr, text=label, text_color=FG2,
                                   font=FONT_TINY, anchor="w")
        self._label.pack(side="left")
        self._pct_lbl = ctk.CTkLabel(hdr, text="0%", text_color=ACC,
                                     font=FONT_MONO_SMALL, anchor="e")
        self._pct_lbl.pack(side="right")
        self._bar = ctk.CTkProgressBar(self, height=5,
                                       progress_color=GRN,
                                       fg_color=BORDER)
        self._bar.pack(fill="x", pady=(3,0))
        self._bar.set(0)

    def set_value(self, pct: int):
        self._bar.set(pct/100)
        self._pct_lbl.configure(text=f"{pct}%")
        color = GRN if pct >= 80 else (YLW if pct >= 50 else RED)
        self._bar.configure(progress_color=color)
        self._pct_lbl.configure(text_color=color)


class DraggableSectionRow(ctk.CTkFrame):
    """Wiersz sekcji z checkboxem i uchwytem do przeciągania."""
    def __init__(self, master, name: str, enabled: bool = True,
                 on_toggle=None, **kw):
        kw.setdefault("fg_color", BG)
        kw.setdefault("border_color", BORDER)
        kw.setdefault("border_width", 1)
        kw.setdefault("corner_radius", 7)
        super().__init__(master, **kw)
        self.name = name
        self._on_toggle = on_toggle
        self._enabled = ctk.BooleanVar(value=enabled)

        ctk.CTkLabel(self, text="⠿", text_color=FG3,
                     font=("Segoe UI", 14), width=20).pack(side="left", padx=(6,2))

        cb = ctk.CTkCheckBox(self, text=name, variable=self._enabled,
                             text_color=FG2, font=FONT_UI,
                             checkbox_width=16, checkbox_height=16,
                             border_color=BORDER2, fg_color=ACC,
                             hover_color=ACC2,
                             command=self._toggled)
        cb.pack(side="left", padx=4, pady=6)

    def _toggled(self):
        if self._on_toggle:
            self._on_toggle(self.name, self._enabled.get())

    @property
    def is_enabled(self) -> bool:
        return self._enabled.get()


# ══════════════════════════════════════════════════════════════════════════════
#   MAIN APPLICATION
# ══════════════════════════════════════════════════════════════════════════════

class ReadmeGeneratorApp(ctk.CTk):

    APP_TITLE  = "README Generator Pro v2.2 — polsoft.ITS™ Group"
    APP_AUTHOR = "Sebastian Januchowski"
    APP_COMPANY= "polsoft.ITS™ Group"
    APP_EMAIL  = "polsoft.its@fastservice.com"
    APP_GITHUB = "https://github.com/seb07uk"
    APP_COPY   = "2026 © Sebastian Januchowski & polsoft.ITS™ Group"
    WIN_SIZE   = "1180x720"
    MIN_SIZE   = (860, 560)

    ALL_SECTIONS = [
        "Badges","Description","Features","Installation","Usage",
        "Structure","API","Tests","Configuration","Changelog",
        "License","Author",
    ]

    BADGE_STYLES = ["flat","flat-square","for-the-badge","plastic","social"]
    THEMES      = ["dark","light","dark-blue","green"]

    PLUGINS = [
        {"icon":"🔍","name":"UnusedDetector",   "desc_key":"plugin_unused_desc",   "enabled":True},
        {"icon":"🗺️", "name":"TodoRoadmap",      "desc_key":"plugin_todo_desc",     "enabled":True},
        {"icon":"🤝","name":"Contributing",     "desc_key":"plugin_contrib_desc",  "enabled":True},
        {"icon":"🔗","name":"ModuleDeps",       "desc_key":"plugin_moddeps_desc",  "enabled":False},
        {"icon":"🏗️", "name":"Architecture",    "desc_key":"plugin_arch_desc",     "enabled":False},
        {"icon":"🔀","name":"ApiChangeDetector","desc_key":"plugin_apidet_desc",   "enabled":False},
        {"icon":"📜","name":"ConvChangelog",    "desc_key":"plugin_convch_desc",   "enabled":True},
        {"icon":"🪝","name":"PreCommitHook",    "desc_key":"plugin_prehook_desc",  "enabled":False},
    ]

    def __init__(self):
        super().__init__()

        # ── Backend
        self._analyzer  = ProjectAnalyzer()
        self._git       = GitAnalyzer()
        self._extractor = MetadataExtractor()
        self._gen       = ReadmeGenerator()
        self._quality   = DocQualityAnalyzer()
        self._tests     = TestAnalyzer()

        # ── Language registry  (key → list of (widget, attr))
        # Populated during _build_ui; _apply_lang() iterates it to update texts
        self._i18n: dict[str, list[tuple]] = {}

        # ── State
        self._project_path: str | None = None
        self._project_data: dict | None = None
        self._meta_data:    dict | None = None
        self._git_data:     dict | None = None
        self._quality_data: dict | None = None
        self._readme_text:  str  = ""
        self._section_states: dict = {s: True for s in self.ALL_SECTIONS}
        self._plugin_vars: list[ctk.BooleanVar] = []
        self._busy = False
        self._watcher_active = False
        self._watcher_hashes: dict = {}

        # ── Window setup
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.title(self.APP_TITLE)
        self.geometry(self.WIN_SIZE)
        self.minsize(*self.MIN_SIZE)
        self.configure(fg_color=BG)

        self._build_ui()
        backend_info = (
            T("status_backend_full") if _USING_FULL_BACKEND
            else T("status_backend_standalone")
        )
        self._set_status(f"{T('status_ready')} {backend_info}", "idle")

    # ══════════════════════════════════════════════════════════════════
    #  LANGUAGE SWITCH  (stable: only updates text, never rebuilds UI)
    # ══════════════════════════════════════════════════════════════════

    def _reg(self, key: str, widget, attr: str = "text"):
        """Register a widget+attribute under translation key for later update."""
        self._i18n.setdefault(key, []).append((widget, attr))

    def _switch_language(self):
        """Toggle EN ↔ PL by updating every registered widget text in-place."""
        new_lang = "pl" if _LANG == "en" else "en"
        set_lang(new_lang)
        self._apply_lang()

    def _apply_lang(self):
        """Push current language strings to all registered widgets."""
        for key, entries in self._i18n.items():
            text = T(key)
            for widget, attr in entries:
                try:
                    widget.configure(**{attr: text})
                except Exception:
                    pass
        # Git field key labels have ":" appended
        if hasattr(self, "_git_key_lbls"):
            for label_key, lbl in self._git_key_lbls.items():
                try:
                    lbl.configure(text=T(label_key) + ":")
                except Exception:
                    pass
        # Plugin description labels
        if hasattr(self, "_plugin_desc_lbls"):
            for desc_key, lbl in self._plugin_desc_lbls.items():
                try:
                    lbl.configure(text=T(desc_key))
                except Exception:
                    pass
        # Update lang-switch button to show the *other* language
        if hasattr(self, "_lang_btn"):
            self._lang_btn.configure(text=T("lang_switch"))
        # Refresh status bar
        backend_info = (
            T("status_backend_full") if _USING_FULL_BACKEND
            else T("status_backend_standalone")
        )
        self._set_status(f"{T('status_ready')} {backend_info}", "idle")
        # Refresh counts if readme already generated
        if self._readme_text:
            lines = len(self._readme_text.splitlines())
            self._line_lbl.configure(text=f"{lines} {T('line_count')}")
            self._word_count_lbl.configure(
                text=f"{len(self._readme_text.split())} {T('word_count')}  "
                     f"{lines} {T('line_count')}")
        # Refresh hook / api status labels
        if self._project_path:
            self._update_hook_status()

    def _lbl(self, parent, key: str, **kw) -> ctk.CTkLabel:
        """Create a CTkLabel with translated text and register it for live updates."""
        w = ctk.CTkLabel(parent, text=T(key), **kw)
        self._reg(key, w)
        return w

    def _card(self, parent, title_key: str, accent=ACC, **kw) -> "SectionCard":
        """Create a SectionCard whose header is registered for live translation."""
        card = SectionCard(parent, T(title_key), accent=accent, **kw)
        self._reg(title_key, card._hdr_lbl)
        return card



    def _build_ui(self):
        self._build_titlebar()
        self._build_toolbar()

        # ── Main paned area
        body = ctk.CTkFrame(self, fg_color="transparent")
        body.pack(fill="both", expand=True)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        self._build_left_panel(body)
        self._build_center_panel(body)
        self._build_right_panel(body)

        self._build_statusbar()

    # ── Titlebar ──────────────────────────────────────────────────────
    def _build_titlebar(self):
        tb = ctk.CTkFrame(self, fg_color=CARD, height=40, corner_radius=0)
        tb.pack(fill="x")
        tb.pack_propagate(False)

        # Logo mark
        logo = ctk.CTkFrame(tb, fg_color=ACC, width=30, height=30,
                            corner_radius=7)
        logo.pack(side="left", padx=(12,8), pady=8)
        logo.pack_propagate(False)
        ctk.CTkLabel(logo, text="R", text_color="#000",
                     font=("Segoe UI",14,"bold")).place(relx=.5,rely=.5,anchor="center")

        ctk.CTkLabel(tb, text="README Generator Pro",
                     text_color=FG, font=("Segoe UI",13,"bold")).pack(side="left")
        ctk.CTkLabel(tb, text="v2.2",
                     text_color=ACC, font=("JetBrains Mono",10)).pack(side="left", padx=6)
        ctk.CTkLabel(tb, text="polsoft.ITS™ Group",
                     text_color=FG3, font=("Segoe UI",9)).pack(side="left", padx=4)
        ctk.CTkLabel(tb, text="·",
                     text_color=FG3, font=("Segoe UI",9)).pack(side="left")
        ctk.CTkLabel(tb, text="Sebastian Januchowski",
                     text_color=FG2, font=("Segoe UI",9)).pack(side="left", padx=4)

        # Theme selector (packed right-to-left: label → menu → lang button)
        # Language switcher — rightmost
        self._lang_btn = ctk.CTkButton(
            tb, text=T("lang_switch"), width=58, height=26,
            fg_color=CARD2, hover_color=BORDER2,
            border_color=BORDER2, border_width=1,
            text_color=ACC, font=("Segoe UI", 10, "bold"),
            corner_radius=6,
            command=self._switch_language,
        )
        self._lang_btn.pack(side="right", padx=(4, 8), pady=8)

        # Theme OptionMenu — must create StringVar first
        self._theme_var = ctk.StringVar(value="dark")
        theme_menu = ctk.CTkOptionMenu(
            tb, variable=self._theme_var,
            values=self.THEMES,
            fg_color=CARD2, button_color=BORDER2,
            button_hover_color=BORDER, text_color=FG2,
            dropdown_fg_color=CARD, dropdown_hover_color=CARD2,
            font=FONT_TINY, width=110, height=26,
            command=self._change_theme,
        )
        theme_menu.pack(side="right", padx=(0, 4), pady=8)
        _theme_lbl = ctk.CTkLabel(tb, text=T("theme_label"), text_color=FG3, font=FONT_TINY)
        _theme_lbl.pack(side="right", padx=(0, 4))
        self._reg("theme_label", _theme_lbl)

    # ── Toolbar ───────────────────────────────────────────────────────
    def _build_toolbar(self):
        bar = ctk.CTkFrame(self, fg_color=BG2, height=40, corner_radius=0)
        bar.pack(fill="x")
        bar.pack_propagate(False)

        inner = ctk.CTkFrame(bar, fg_color="transparent")
        inner.pack(side="left", padx=8, pady=6)

        actions = [
            ("btn_open",     self._pick_folder,   ACC,    False),
            ("btn_analyze",  self._run_analyze,   ACC,    False),
            ("btn_generate", self._run_generate,  "#000", True),
            (None, None, None, None),   # separator
            ("btn_save_md",  self._save_readme,   GRN,    False),
            ("btn_copy",     self._copy_clip,     GRN,    False),
            ("btn_export",   self._export_txt,    YLW,    False),
            (None, None, None, None),
            ("btn_gen_docs", self._gen_docs,      PURPLE, False),
            ("btn_changelog",self._gen_changelog, ORANGE, False),
            ("btn_hook",     self._toggle_hook,   RED,    False),
        ]

        for item in actions:
            key, cmd, color, is_primary = item
            if key is None:
                ctk.CTkFrame(inner, fg_color=BORDER, width=1,
                             height=22, corner_radius=0).pack(side="left", padx=6)
                continue
            if is_primary:
                btn = PrimaryButton(inner, text=T(key), command=cmd)
            else:
                btn = ctk.CTkButton(
                    inner, text=T(key), command=cmd,
                    fg_color=CARD, hover_color=CARD2,
                    border_color=BORDER, border_width=1,
                    text_color=color, font=FONT_BOLD,
                    height=26, corner_radius=8,
                )
            btn.pack(side="left", padx=3)
            self._reg(key, btn)

        # Watch toggle
        self._watch_var = ctk.BooleanVar(value=False)
        watch_sw = ctk.CTkSwitch(
            bar, text=T("btn_watch"),
            variable=self._watch_var,
            command=self._toggle_watch,
            progress_color=ACC, button_color=ACC2,
            text_color=FG2, font=FONT_BOLD,
        )
        watch_sw.pack(side="right", padx=16)
        self._reg("btn_watch", watch_sw)

    # ── Left panel ────────────────────────────────────────────────────
    def _build_left_panel(self, parent):
        panel = ctk.CTkFrame(parent, fg_color=BG2, width=255,
                             corner_radius=0, border_color=BORDER,
                             border_width=0)
        panel.grid(row=0, column=0, sticky="nsew")
        panel.grid_propagate(False)
        panel.grid_rowconfigure(1, weight=1)
        panel.grid_columnconfigure(0, weight=1)

        # Tab bar
        tab_bar = ctk.CTkFrame(panel, fg_color=CARD, height=30, corner_radius=0)
        tab_bar.grid(row=0, column=0, sticky="ew")
        tab_bar.pack_propagate(False)

        self._left_tabs: dict[str, ctk.CTkFrame] = {}
        self._left_tab_btns: dict[str, ctk.CTkButton] = {}
        # stable internal keys → (translation key, frame)
        tab_keys = ["tab_config", "tab_analysis", "tab_sections", "tab_plugins"]

        tab_inner = ctk.CTkFrame(tab_bar, fg_color="transparent")
        tab_inner.pack(fill="both", expand=True, padx=4)

        for key in tab_keys:
            btn = ctk.CTkButton(
                tab_inner, text=T(key),
                fg_color="transparent", hover_color=CARD2,
                text_color=FG3, font=("Segoe UI",10,"bold"),
                height=28, corner_radius=0,
                command=lambda k=key: self._switch_left_tab(k),
            )
            btn.pack(side="left", padx=1)
            self._left_tab_btns[key] = btn
            self._reg(key, btn)

        # Content area
        content = ctk.CTkScrollableFrame(panel, fg_color="transparent",
                                          scrollbar_button_color=BORDER2,
                                          scrollbar_button_hover_color=BORDER)
        content.grid(row=1, column=0, sticky="nsew")

        for key in tab_keys:
            f = ctk.CTkFrame(content, fg_color="transparent")
            self._left_tabs[key] = f

        self._build_tab_config(self._left_tabs["tab_config"])
        self._build_tab_analysis(self._left_tabs["tab_analysis"])
        self._build_tab_sections(self._left_tabs["tab_sections"])
        self._build_tab_plugins(self._left_tabs["tab_plugins"])

        self._switch_left_tab("tab_config")

    def _switch_left_tab(self, key: str):
        for k, f in self._left_tabs.items():
            f.pack_forget()
        for k, btn in self._left_tab_btns.items():
            btn.configure(text_color=FG3 if k != key else ACC,
                          fg_color="transparent" if k != key else CARD2)
        self._left_tabs[key].pack(fill="both", expand=True)

    # ── Config tab ────────────────────────────────────────────────────
    def _build_tab_config(self, parent):
        pad = {"padx":6,"pady":3}

        # Drop zone
        drop = ctk.CTkFrame(parent, fg_color=CARD, border_color=BORDER2,
                            border_width=2, corner_radius=12)
        drop.pack(fill="x", **pad)
        drop.bind("<Button-1>", lambda e: self._pick_folder())
        drop.bind("<Enter>",    lambda e: drop.configure(border_color=ACC))
        drop.bind("<Leave>",    lambda e: drop.configure(border_color=BORDER2))

        # Enable drag-and-drop
        try:
            drop.drop_target_register("DND_Files")
            drop.dnd_bind("<<Drop>>", self._on_dnd_drop)
        except Exception:
            pass

        ctk.CTkLabel(drop, text="📂", font=("Segoe UI",28)).pack(pady=(8,3))
        _drop_title = ctk.CTkLabel(drop, text=T("drop_title"), text_color=FG2, font=FONT_BOLD)
        _drop_title.pack()
        self._reg("drop_title", _drop_title)
        _drop_hint = ctk.CTkLabel(drop, text=T("drop_hint"), text_color=FG3, font=FONT_TINY)
        _drop_hint.pack(pady=(1,8))
        self._reg("drop_hint", _drop_hint)

        self._path_label = ctk.CTkLabel(parent, text=T("no_project"),
                                        text_color=FG3, font=FONT_MONO_SMALL,
                                        wraplength=235, anchor="w")
        self._path_label.pack(fill="x", padx=10, pady=2)

        # Template
        card = self._card(parent, "card_template")
        card.pack(fill="x", **pad)
        body = card.body()

        self._template_var = ctk.StringVar(value="Open-Source")
        for tname in ReadmeGenerator.TEMPLATES:
            rb = ctk.CTkRadioButton(body, text=tname,
                                    variable=self._template_var, value=tname,
                                    text_color=FG2, font=FONT_UI,
                                    radiobutton_width=16, radiobutton_height=16,
                                    border_color=BORDER2, fg_color=ACC,
                                    hover_color=ACC2,
                                    command=self._on_option_change)
            rb.pack(anchor="w", padx=8, pady=2)

        # Badge style
        card2 = self._card(parent, "card_badge")
        card2.pack(fill="x", **pad)
        body2 = card2.body()

        self._badge_var = ctk.StringVar(value="flat")
        seg = ctk.CTkSegmentedButton(
            body2, values=self.BADGE_STYLES[:4],
            variable=self._badge_var,
            fg_color=BG, selected_color=ACC,
            selected_hover_color=ACC2,
            unselected_color=CARD, unselected_hover_color=CARD2,
            text_color=FG, font=FONT_TINY,
            command=lambda v: self._on_option_change(),
        )
        seg.pack(fill="x", padx=4, pady=4)

        # Tree depth
        card3 = self._card(parent, "card_tree")
        card3.pack(fill="x", **pad)
        body3 = card3.body()

        mode_row = ctk.CTkFrame(body3, fg_color="transparent")
        mode_row.pack(fill="x")
        _w_tree_mode_label = ctk.CTkLabel(mode_row, text=T("tree_mode_label"),
                     text_color=FG3, font=FONT_TINY, width=50)
        _w_tree_mode_label.pack(side="left", padx=6)
        self._reg("tree_mode_label", _w_tree_mode_label)
        self._tree_mode_var = ctk.StringVar(value="compact")
        for v, lbl in [("compact","Compact"),("full","Full")]:
            ctk.CTkRadioButton(mode_row, text=lbl,
                               variable=self._tree_mode_var, value=v,
                               text_color=FG2, font=FONT_UI,
                               radiobutton_width=14, radiobutton_height=14,
                               border_color=BORDER2, fg_color=ACC,
                               command=self._on_option_change).pack(side="left", padx=6, pady=4)

        depth_row = ctk.CTkFrame(body3, fg_color="transparent")
        depth_row.pack(fill="x")
        _w_tree_depth_label = ctk.CTkLabel(depth_row, text=T("tree_depth_label"),
                     text_color=FG3, font=FONT_TINY, width=50)
        _w_tree_depth_label.pack(side="left", padx=6)
        self._reg("tree_depth_label", _w_tree_depth_label)
        self._tree_depth_var = ctk.IntVar(value=2)
        sl = ctk.CTkSlider(depth_row, from_=1, to=5, number_of_steps=4,
                           variable=self._tree_depth_var,
                           progress_color=ACC, button_color=ACC,
                           button_hover_color=ACC2,
                           command=lambda v: self._on_option_change())
        sl.pack(side="left", fill="x", expand=True, padx=6, pady=4)
        self._depth_lbl = ctk.CTkLabel(depth_row, text="2", text_color=ACC,
                                       font=FONT_MONO_SMALL, width=16)
        self._depth_lbl.pack(side="left", padx=(0,6))
        self._tree_depth_var.trace_add("write",
            lambda *_: self._depth_lbl.configure(text=str(self._tree_depth_var.get())))

        # Metadata overrides
        card4 = self._card(parent, "card_metadata")
        card4.pack(fill="x", **pad)
        body4 = card4.body()

        fields = [
            (T("field_name"),    "_inp_name"),
            (T("field_desc"),    "_inp_desc"),
            (T("field_version"), "_inp_version"),
            (T("field_author"),  "_inp_author"),
            (T("field_github"),  "_inp_github"),
        ]
        for lbl, attr in fields:
            row = ctk.CTkFrame(body4, fg_color="transparent")
            row.pack(fill="x", pady=1)
            ctk.CTkLabel(row, text=lbl, text_color=FG3,
                         font=FONT_TINY, width=52, anchor="w").pack(side="left", padx=4)
            entry = ctk.CTkEntry(row, fg_color=BG, border_color=BORDER2,
                                 text_color=FG, font=FONT_MONO_SMALL,
                                 height=26, corner_radius=5)
            entry.pack(side="left", fill="x", expand=True, padx=4)
            setattr(self, attr, entry)

        btn_row = ctk.CTkFrame(parent, fg_color="transparent")
        btn_row.pack(fill="x", padx=6, pady=4)
        _btn_save_cfg = NeonButton(btn_row, text=T("btn_save_cfg"), command=self._save_config)
        _btn_save_cfg.pack(side="left", padx=2)
        self._reg("btn_save_cfg", _btn_save_cfg)
        _btn_load_cfg = NeonButton(btn_row, text=T("btn_load_cfg"), command=self._load_config)
        _btn_load_cfg.pack(side="left", padx=2)
        self._reg("btn_load_cfg", _btn_load_cfg)

    # ── Analysis tab ──────────────────────────────────────────────────
    def _build_tab_analysis(self, parent):
        pad = {"padx":6,"pady":3}

        # Stats grid
        stats_card = self._card(parent, "card_stats")
        stats_card.pack(fill="x", **pad)
        body = stats_card.body()

        grid = ctk.CTkFrame(body, fg_color="transparent")
        grid.pack(fill="x")
        grid.columnconfigure((0,1), weight=1)

        self._stat_files  = StatBadge(grid, T("stat_files"),   "—", ACC)
        self._stat_dirs   = StatBadge(grid, T("stat_dirs"),    "—", PURPLE)
        self._stat_size   = StatBadge(grid, T("stat_size"),    "—", GRN)
        self._stat_lang   = StatBadge(grid, T("stat_lang"),    "—", YLW)
        self._stat_cls    = StatBadge(grid, T("stat_classes"), "—", ACC)
        self._stat_fns    = StatBadge(grid, T("stat_funcs"),   "—", ORANGE)

        for i, sb in enumerate([self._stat_files, self._stat_dirs,
                                 self._stat_size,  self._stat_lang,
                                 self._stat_cls,   self._stat_fns]):
            sb.grid(row=i//2, column=i%2, padx=2, pady=2, sticky="ew")

        # Quality bars
        qual_card = self._card(parent, "card_quality")
        qual_card.pack(fill="x", **pad)
        qbody = qual_card.body()
        self._bar_docs  = ProgressBar(qbody, T("bar_docstrings"))
        self._bar_tests = ProgressBar(qbody, T("bar_tests"))
        for b in [self._bar_docs, self._bar_tests]:
            b.pack(fill="x", padx=4, pady=3)

        # Project info text
        info_card = self._card(parent, "card_details")
        info_card.pack(fill="both", expand=True, **pad)
        ibody = info_card.body()
        self._info_text = ctk.CTkTextbox(
            ibody, fg_color=BG, text_color=FG2,
            font=FONT_MONO_SMALL, corner_radius=6,
            border_color=BORDER, border_width=1,
            state="disabled", wrap="word",
        )
        self._info_text.pack(fill="both", expand=True)

    # ── Sections tab ──────────────────────────────────────────────────
    def _build_tab_sections(self, parent):
        pad = {"padx":6,"pady":3}

        card = self._card(parent, "card_sections")
        card.pack(fill="x", **pad)
        body = card.body()

        _w_sections_hint = ctk.CTkLabel(body, text=T("sections_hint"),
                     text_color=FG3, font=FONT_TINY, anchor="w")
        _w_sections_hint.pack(fill="x", padx=4, pady=(0,4))
        self._reg("sections_hint", _w_sections_hint)

        self._section_rows: list[DraggableSectionRow] = []
        for sec_name in self.ALL_SECTIONS:
            row = DraggableSectionRow(body, name=sec_name,
                                      enabled=True,
                                      on_toggle=self._on_section_toggle)
            row.pack(fill="x", pady=2, padx=2)
            self._section_rows.append(row)

        btn_row = ctk.CTkFrame(parent, fg_color="transparent")
        btn_row.pack(fill="x", padx=6, pady=3)
        _btn_all = NeonButton(btn_row, text=T("btn_all"), command=lambda: self._set_all_sections(True))
        _btn_all.pack(side="left", padx=2)
        self._reg("btn_all", _btn_all)
        _btn_clr = NeonButton(btn_row, text=T("btn_clear"), command=lambda: self._set_all_sections(False))
        _btn_clr.pack(side="left", padx=2)
        self._reg("btn_clear", _btn_clr)

        # API snapshot
        api_card = self._card(parent, "card_api_track")
        api_card.pack(fill="x", padx=8, pady=4)
        api_body = api_card.body()
        _w_api_track_hint = ctk.CTkLabel(api_body, text=T("api_track_hint"),
                     text_color=FG3, font=FONT_TINY, justify="left")
        _w_api_track_hint.pack(padx=6, pady=(2,6))
        self._reg("api_track_hint", _w_api_track_hint)
        _btn_snap = NeonButton(api_body, text=T("btn_api_snapshot"),
                   command=self._save_api_snapshot,
                   accent=PURPLE)
        _btn_snap.pack(fill="x", padx=4, pady=4)
        self._reg("btn_api_snapshot", _btn_snap)

    # ── Plugins tab ───────────────────────────────────────────────────
    def _build_tab_plugins(self, parent):
        pad = {"padx":6,"pady":3}
        card = self._card(parent, "card_plugins")
        card.pack(fill="x", **pad)
        body = card.body()

        _w_plugins_hint = ctk.CTkLabel(body, text=T("plugins_hint"),
                     text_color=FG3, font=FONT_TINY, anchor="w")
        _w_plugins_hint.pack(fill="x", padx=4, pady=(0,4))
        self._reg("plugins_hint", _w_plugins_hint)

        self._plugin_vars = []
        self._plugin_desc_lbls: dict[str, ctk.CTkLabel] = {}
        for plugin in self.PLUGINS:
            var = ctk.BooleanVar(value=plugin["enabled"])
            self._plugin_vars.append(var)

            row = ctk.CTkFrame(body, fg_color=BG, border_color=BORDER,
                               border_width=1, corner_radius=7)
            row.pack(fill="x", pady=2, padx=2)

            ctk.CTkLabel(row, text=plugin["icon"],
                         font=("Segoe UI",16), width=28).pack(side="left", padx=6, pady=6)

            info_f = ctk.CTkFrame(row, fg_color="transparent")
            info_f.pack(side="left", fill="x", expand=True, pady=4)
            ctk.CTkLabel(info_f, text=plugin["name"],
                         text_color=FG, font=FONT_BOLD, anchor="w").pack(anchor="w")
            _dl = ctk.CTkLabel(info_f, text=T(plugin["desc_key"]),
                         text_color=FG3, font=FONT_TINY, anchor="w")
            _dl.pack(anchor="w")
            self._plugin_desc_lbls[plugin["desc_key"]] = _dl

            sw = ctk.CTkSwitch(row, text="", variable=var,
                               width=44, progress_color=ACC,
                               button_color=ACC2)
            sw.pack(side="right", padx=10)

        # Plugin status info
        info_card = self._card(parent, "card_plugin_info")
        info_card.pack(fill="x", **pad)
        ibody = info_card.body()
        ctk.CTkLabel(
            ibody,
            text=T("plugin_info_text"),
            text_color=FG3, font=FONT_TINY, justify="left",
        ).pack(padx=8, pady=8)

    # ── Center panel (preview) ────────────────────────────────────────
    def _build_center_panel(self, parent):
        panel = ctk.CTkFrame(parent, fg_color=BG, corner_radius=0)
        panel.grid(row=0, column=1, sticky="nsew")
        panel.grid_rowconfigure(1, weight=1)
        panel.grid_columnconfigure(0, weight=1)

        # Preview header
        hdr = ctk.CTkFrame(panel, fg_color=CARD, height=32, corner_radius=0)
        hdr.grid(row=0, column=0, sticky="ew")
        hdr.grid_propagate(False)
        hdr.grid_columnconfigure(1, weight=1)

        _preview_hdr_lbl = ctk.CTkLabel(hdr, text=T("preview_header"),
                     text_color=FG2, font=FONT_BOLD)
        _preview_hdr_lbl.grid(row=0, column=0, padx=14, pady=6)
        self._reg("preview_header", _preview_hdr_lbl)

        self._word_count_lbl = ctk.CTkLabel(
            hdr, text="", text_color=FG3, font=FONT_MONO_SMALL)
        self._word_count_lbl.grid(row=0, column=1, padx=8, sticky="w")

        # Preview mode tabs
        tab_f = ctk.CTkFrame(hdr, fg_color="transparent")
        tab_f.grid(row=0, column=2, padx=12, sticky="e")
        self._preview_mode = ctk.StringVar(value="raw")
        for val, lbl_key in [("raw", "preview_raw"), ("rendered", "preview_rendered")]:
            btn = ctk.CTkButton(
                tab_f, text=T(lbl_key), width=88, height=24,
                corner_radius=5,
                fg_color=ACC if val=="raw" else "transparent",
                hover_color=ACC2, text_color="#000" if val=="raw" else FG2,
                font=("Segoe UI",10,"bold"),
                command=lambda v=val: self._switch_preview(v),
            )
            btn.pack(side="left", padx=2)
            setattr(self, f"_preview_btn_{val}", btn)
            self._reg(lbl_key, btn)

        # Preview textbox
        self._preview_text = ctk.CTkTextbox(
            panel, fg_color=BG2, text_color=FG2,
            font=("JetBrains Mono",11), corner_radius=0,
            border_width=0, wrap="word",
            scrollbar_button_color=BORDER2,
        )
        self._preview_text.grid(row=1, column=0, sticky="nsew")
        self._preview_text.insert("end", T("preview_placeholder"))

        # Line counter sidebar
        self._line_lbl = ctk.CTkLabel(
            panel, text=f"0 {T('line_count')}", text_color=FG3,
            font=FONT_MONO_SMALL)
        self._line_lbl.grid(row=2, column=0, sticky="w", padx=14, pady=4)

    # ── Right panel (git + info) ──────────────────────────────────────
    def _build_right_panel(self, parent):
        panel = ctk.CTkFrame(parent, fg_color=BG2, width=220,
                             corner_radius=0, border_color=BORDER,
                             border_width=0)
        panel.grid(row=0, column=2, sticky="nsew")
        panel.grid_propagate(False)
        panel.grid_columnconfigure(0, weight=1)
        panel.grid_rowconfigure(1, weight=1)

        hdr = ctk.CTkFrame(panel, fg_color=CARD, height=30, corner_radius=0)
        hdr.grid(row=0, column=0, sticky="ew")
        hdr.pack_propagate(False)
        _w_right_header = ctk.CTkLabel(hdr, text=T("right_header"),
                     text_color=FG2, font=FONT_BOLD)
        _w_right_header.pack(side="left", padx=12, pady=6)
        self._reg("right_header", _w_right_header)

        scroll = ctk.CTkScrollableFrame(
            panel, fg_color="transparent",
            scrollbar_button_color=BORDER2)
        scroll.grid(row=1, column=0, sticky="nsew")

        # Git info section
        git_card = self._card(scroll, "card_git")
        git_card.pack(fill="x", padx=6, pady=6)
        gbody = git_card.body()

        self._git_fields: dict[str, ctk.CTkLabel] = {}
        self._git_key_lbls: dict[str, ctk.CTkLabel] = {}
        for key, label_key, color in [
            ("branch",            "git_branch",  ACC),
            ("last_commit_hash",  "git_hash",    FG2),
            ("last_commit_msg",   "git_commit",  FG),
            ("last_commit_date",  "git_date",    FG3),
            ("last_commit_author","git_author",  FG2),
            ("commits_count",     "git_commits", YLW),
            ("status",            "git_status",  GRN),
        ]:
            row = ctk.CTkFrame(gbody, fg_color="transparent")
            row.pack(fill="x", pady=1)
            _kl = ctk.CTkLabel(row, text=T(label_key)+":",
                         text_color=FG3, font=FONT_MONO_SMALL,
                         width=60, anchor="w")
            _kl.pack(side="left", padx=4)
            self._git_key_lbls[label_key] = _kl
            lbl = ctk.CTkLabel(row, text="—", text_color=color,
                               font=FONT_MONO_SMALL, anchor="w",
                               wraplength=120)
            lbl.pack(side="left", fill="x", expand=True, padx=2)
            self._git_fields[key] = lbl

        # Commit history
        commits_card = self._card(scroll, "card_commits")
        commits_card.pack(fill="x", padx=6, pady=6)
        cbody = commits_card.body()
        self._commits_text = ctk.CTkTextbox(
            cbody, fg_color=BG, text_color=FG3,
            font=("JetBrains Mono",9), height=120,
            border_color=BORDER, border_width=1,
            corner_radius=6, state="disabled", wrap="word",
        )
        self._commits_text.pack(fill="x", padx=2, pady=2)

        # Hook status
        hook_card = self._card(scroll, "card_hook")
        hook_card.pack(fill="x", padx=6, pady=6)
        hkbody = hook_card.body()
        self._hook_status_lbl = ctk.CTkLabel(
            hkbody, text=T("hook_not_installed"),
            text_color=RED, font=FONT_TINY, anchor="w")
        self._hook_status_lbl.pack(fill="x", padx=8, pady=4)

        # API change status
        api_card = self._card(scroll, "card_api_changes")
        api_card.pack(fill="x", padx=6, pady=6)
        apibody = api_card.body()
        self._api_status_lbl = ctk.CTkLabel(
            apibody, text=T("api_no_snapshot"),
            text_color=FG3, font=FONT_TINY, anchor="w")
        self._api_status_lbl.pack(fill="x", padx=8, pady=4)

    # ── Status bar ────────────────────────────────────────────────────
    def _build_statusbar(self):
        bar = ctk.CTkFrame(self, fg_color=CARD, height=22, corner_radius=0)
        bar.pack(fill="x", side="bottom")
        bar.pack_propagate(False)

        self._status_dot = ctk.CTkLabel(bar, text="●", width=18,
                                         text_color=FG3, font=("Segoe UI",10))
        self._status_dot.pack(side="left", padx=(10,4), pady=4)

        self._status_lbl = ctk.CTkLabel(bar, text=T("status_ready"),
                                         text_color=FG3, font=FONT_MONO_SMALL,
                                         anchor="w")
        self._status_lbl.pack(side="left", fill="x", expand=True, padx=2)

        # About button
        _about_btn = ctk.CTkButton(
            bar, text=T("about_btn"), width=72, height=18,
            fg_color="transparent", hover_color=CARD2,
            text_color=FG3, font=("Segoe UI",9),
            corner_radius=4, border_width=0,
            command=self._show_about,
        )
        _about_btn.pack(side="right", padx=4)
        self._reg("about_btn", _about_btn)

        _sb_info = ctk.CTkLabel(
            bar,
            text=T("statusbar_info"),
            text_color=FG3, font=FONT_MONO_SMALL,
        )
        _sb_info.pack(side="right", padx=12)
        self._reg("statusbar_info", _sb_info)

    # ══════════════════════════════════════════════════════════════════
    #  STATUS HELPERS
    # ══════════════════════════════════════════════════════════════════

    def _set_status(self, msg: str, state: str = "idle"):
        colors = {"idle": FG3, "ok": GRN, "busy": YLW, "error": RED}
        self._status_lbl.configure(text=msg)
        self._status_dot.configure(text_color=colors.get(state, FG3))

    def _set_busy(self, busy: bool):
        self._busy = busy
        dot_color = YLW if busy else FG3
        self._status_dot.configure(text_color=dot_color)

    # ══════════════════════════════════════════════════════════════════
    #  PROJECT ACTIONS
    # ══════════════════════════════════════════════════════════════════

    def _pick_folder(self):
        path = filedialog.askdirectory(title=T("dlg_pick_folder"))
        if path:
            self._set_project_path(path)

    def _on_dnd_drop(self, event):
        path = event.data.strip().strip("{}")
        if Path(path).is_dir():
            self._set_project_path(path)

    def _set_project_path(self, path: str):
        self._project_path = path
        short = Path(path).name
        self._path_label.configure(text=f"📁 {short}", text_color=ACC)
        self._set_status(f"{T('status_selected')}{path}", "idle")
        self._load_config()
        self._update_hook_status()

    def _run_analyze(self):
        if not self._project_path:
            messagebox.showwarning(T("msg_no_project_title"), T("msg_no_project"))
            return
        self._set_status(T("status_analyzing"), "busy")
        self._set_busy(True)
        threading.Thread(target=self._analyze_task, daemon=True).start()

    def _analyze_task(self):
        try:
            mode  = self._tree_mode_var.get()
            depth = int(self._tree_depth_var.get())
            self._project_data = self._analyzer.analyze(self._project_path, mode, depth)
            self._meta_data    = self._extractor.extract(self._project_path)
            self._git_data     = self._git.analyze(self._project_path)
            self._quality_data = self._quality.analyze(self._project_path)
            test_files = self._project_data.get("test_files", [])
            self._test_data    = self._tests.analyze(self._project_path, test_files)
            self.after(0, self._update_all_panels)
            self.after(0, lambda: self._set_status(
                T("status_analyze_ok",
                  files=self._project_data['file_count'],
                  lang=self._project_data['language'],
                  q=self._quality_data.get('score',0),
                  git='✅' if self._git_data['is_git'] else '❌'),
                "ok"))
        except Exception as e:
            self.after(0, lambda: self._set_status(f"{T('status_analyze_err')}{e}", "error"))
        finally:
            self.after(0, lambda: self._set_busy(False))

    def _run_generate(self):
        if not self._project_path:
            messagebox.showwarning(T("msg_no_project_title"), T("msg_no_project_short"))
            return
        if not self._project_data:
            self._set_status(T("status_analyzing_generating"), "busy")
            self._set_busy(True)
            threading.Thread(target=self._analyze_and_generate_task, daemon=True).start()
        else:
            self._do_generate()

    def _analyze_and_generate_task(self):
        try:
            mode  = self._tree_mode_var.get()
            depth = int(self._tree_depth_var.get())
            self._project_data = self._analyzer.analyze(self._project_path, mode, depth)
            self._meta_data    = self._extractor.extract(self._project_path)
            self._git_data     = self._git.analyze(self._project_path)
            self._quality_data = self._quality.analyze(self._project_path)
            test_files = self._project_data.get("test_files", [])
            self._test_data    = self._tests.analyze(self._project_path, test_files)
            self.after(0, self._update_all_panels)
            self.after(0, self._do_generate)
        except Exception as e:
            self.after(0, lambda: self._set_status(f"{T('status_gen_err_short')}{e}", "error"))
        finally:
            self.after(0, lambda: self._set_busy(False))

    def _do_generate(self):
        try:
            template_key = ReadmeGenerator.TEMPLATES_ALIAS.get(
                self._template_var.get(), "opensource")
            custom = {
                "name":    self._inp_name.get().strip(),
                "desc":    self._inp_desc.get().strip(),
                "version": self._inp_version.get().strip(),
                "author":  self._inp_author.get().strip(),
                "github":  self._inp_github.get().strip(),
            }
            sections = {row.name: row.is_enabled for row in self._section_rows}
            text = self._gen.generate(
                self._project_data, self._meta_data or {}, self._git_data or {},
                custom, template=template_key,
                badge_style=self._badge_var.get(),
                sections=sections,
            )
            self._readme_text = text
            self._show_preview(text)
            lines = len(text.splitlines())
            self._set_status(T("status_gen_ok", lines=lines, tpl=self._template_var.get()), "ok")
            self._line_lbl.configure(text=f"{lines} {T('line_count')}")
            self._word_count_lbl.configure(
                text=f"{len(text.split())} {T('word_count')}  {lines} {T('line_count')}")
        except Exception as e:
            self._set_status(f"{T('status_gen_err')}{e}", "error")

    def _on_option_change(self):
        """Auto-regeneruj przy zmianie opcji jeśli projekt jest załadowany."""
        if self._project_data and self._readme_text:
            self._do_generate()

    def _on_section_toggle(self, name: str, enabled: bool):
        self._section_states[name] = enabled
        self._on_option_change()

    # ══════════════════════════════════════════════════════════════════
    #  PREVIEW
    # ══════════════════════════════════════════════════════════════════

    def _show_preview(self, text: str):
        self._preview_text.configure(state="normal")
        self._preview_text.delete("1.0", "end")
        self._preview_text.insert("end", text)
        # Syntax highlighting (simple)
        self._highlight_preview()

    def _highlight_preview(self):
        """Kolorowanie składni Markdown w podglądzie RAW."""
        tb = self._preview_text
        # Headings
        for tag, pattern, color, font_sz in [
            ("h1", r"^#\s+.+$",    ACC,    ("JetBrains Mono",13,"bold")),
            ("h2", r"^##\s+.+$",   FG,     ("JetBrains Mono",12,"bold")),
            ("h3", r"^###\s+.+$",  FG2,    ("JetBrains Mono",11,"bold")),
            ("badge", r"!\[.+?\]", PURPLE, ("JetBrains Mono",10)),
            ("code_fence", r"^```.*$", GRN, ("JetBrains Mono",10)),
        ]:
            try:
                tb.tag_config(tag, foreground=color, font=font_sz)
                start = "1.0"
                while True:
                    pos = tb.search(pattern, start, stopindex="end", regexp=True)
                    if not pos: break
                    end = f"{pos} lineend"
                    tb.tag_add(tag, pos, end)
                    start = end
            except Exception:
                pass

    def _switch_preview(self, mode: str):
        self._preview_mode.set(mode)
        # Update tab button appearance
        for v in ["raw","rendered"]:
            btn = getattr(self, f"_preview_btn_{v}", None)
            if btn:
                btn.configure(
                    fg_color=ACC if v == mode else "transparent",
                    text_color="#000" if v == mode else FG2,
                )

    # ══════════════════════════════════════════════════════════════════
    #  PANEL UPDATES
    # ══════════════════════════════════════════════════════════════════

    def _update_all_panels(self):
        self._update_stats_panel()
        self._update_git_panel()

    def _update_stats_panel(self):
        if not self._project_data: return
        p = self._project_data
        m = self._meta_data or {}
        q = self._quality_data or {}
        t = getattr(self, "_test_data", {}) or {}

        self._stat_files.set(str(p["file_count"]))
        self._stat_dirs.set(str(p["dir_count"]))
        self._stat_size.set(f"{p['repo_size_kb']} KB")
        self._stat_lang.set(p["language"])
        self._stat_cls.set(str(len(m.get("classes",[]))))
        self._stat_fns.set(str(len(m.get("functions",[]))))

        # Quality bars — prefer DocQualityAnalyzer data if available
        if q:
            doc_score = q.get("score", 0)
        else:
            total   = len(m.get("functions",[])) + len(m.get("classes",[]))
            missing = len(m.get("missing_docs",[]))
            doc_score = max(0, 100 - int(missing/max(total,1)*100))

        test_score = 85 if p.get("has_tests") else 5
        if t.get("framework"):
            test_score = 85

        self._bar_docs.set_value(doc_score)
        self._bar_tests.set_value(test_score)

        # Info text — show quality details if available
        lang_bar = " | ".join(
            f"{l}: {c}"
            for l, c in sorted(p.get("lang_stats",{}).items(), key=lambda x: -x[1])[:4]
        )
        lines = [
            f"{T('info_project')}{p['name']}",
            f"{T('info_langs')}{lang_bar}",
            f"{T('info_entry')}{p['entry']}",
            f"{T('info_license')}{p['license']}",
            f"{T('info_tests')}{T('yes') if p.get('has_tests') else T('no')}"
            + (f" ({t['framework']})" if t.get("framework") else ""),
            f"{T('info_configs')}{', '.join(p['configs']) if p['configs'] else '—'}",
            "",
            f"{T('info_version')}{m.get('version') or '—'}",
            f"{T('info_author')}{m.get('author') or '—'}",
            f"{T('info_description')}{(m.get('description') or '—')[:55]}",
            "",
            T("info_qual_header"),
            f"{T('info_qual_score')}{doc_score}%"
            + (" ✅" if doc_score >= 80 else (" ⚠️" if doc_score >= 50 else " ❌")),
        ]
        if q.get("missing_count"):
            lines.append(f"{T('info_qual_missing')}{q['missing_count']}")
        lines += [
            f"{T('info_readme')}{'✅' if q.get('has_readme', (p.get('root','') and (Path(p['root'])/'README.md').exists())) else '❌'}",
            f"{T('info_license2')}{'✅' if q.get('has_license') else '❌'}",
            f"{T('info_changelog')}{'✅' if q.get('has_changelog') else '❌'}",
            "",
            T("info_deps_header"),
        ]
        for fname, info in p.get("deps",{}).items():
            lines.append(f"📦 {fname}: {len(info['content'])}{T('info_packages')}")

        self._info_text.configure(state="normal")
        self._info_text.delete("1.0","end")
        self._info_text.insert("end", "\n".join(lines))
        self._info_text.configure(state="disabled")

    def _update_git_panel(self):
        if not self._git_data: return
        g = self._git_data
        if not g.get("is_git"):
            for key, lbl in self._git_fields.items():
                lbl.configure(text="—", text_color=FG3)
            return

        self._git_fields["branch"].configure(text=g.get("branch","—"), text_color=ACC)
        self._git_fields["last_commit_hash"].configure(text=g.get("last_commit_hash","—"))
        self._git_fields["last_commit_msg"].configure(text=g.get("last_commit_msg","—")[:40])
        self._git_fields["last_commit_date"].configure(text=g.get("last_commit_date","—"))
        self._git_fields["last_commit_author"].configure(text=g.get("last_commit_author","—"))
        self._git_fields["commits_count"].configure(text=str(g.get("commits_count",0)), text_color=YLW)
        clean = g.get("status_clean", True)
        self._git_fields["status"].configure(
            text=T("git_clean") if clean else T("git_dirty"),
            text_color=GRN if clean else YLW,
        )

        # Commits log
        self._commits_text.configure(state="normal")
        self._commits_text.delete("1.0","end")
        for entry in g.get("changelog_entries",[]):
            self._commits_text.insert("end", f"• {entry}\n")
        self._commits_text.configure(state="disabled")

    def _update_hook_status(self):
        if not self._project_path: return
        hook_path = Path(self._project_path) / ".git" / "hooks" / "pre-commit"
        if hook_path.exists():
            try:
                content = hook_path.read_text(encoding="utf-8", errors="ignore")
                if "README Generator" in content:
                    self._hook_status_lbl.configure(
                        text=T("hook_installed"),
                        text_color=GRN)
                    return
            except Exception:
                pass
        self._hook_status_lbl.configure(
            text=T("hook_not_installed"), text_color=RED)

    # ══════════════════════════════════════════════════════════════════
    #  FILE ACTIONS
    # ══════════════════════════════════════════════════════════════════

    def _save_readme(self):
        content = self._preview_text.get("1.0","end").strip()
        placeholder = T("preview_placeholder")
        if not content or content == placeholder:
            messagebox.showinfo(T("msg_no_content_title"), T("msg_no_content"))
            return
        default_dir = self._project_path or os.path.expanduser("~")
        path = filedialog.asksaveasfilename(
            initialdir=default_dir, initialfile="README.md",
            defaultextension=".md",
            filetypes=[(T("ft_markdown"),"*.md"),(T("ft_text"),"*.txt"),(T("ft_all"),"*.*")],
            title=T("dlg_save_readme"),
        )
        if path:
            try:
                Path(path).write_text(content, encoding="utf-8")
                self._set_status(f"{T('status_saved')}{path}", "ok")
                messagebox.showinfo(T("msg_saved_title"), f"{T('msg_saved')}{path}")
            except Exception as e:
                messagebox.showerror(T("error"), str(e))

    def _copy_clip(self):
        content = self._preview_text.get("1.0","end").strip()
        placeholder = T("preview_placeholder")
        if content and content != placeholder:
            self.clipboard_clear()
            self.clipboard_append(content)
            self._set_status(T("msg_copied"), "ok")

    def _export_txt(self):
        if not self._project_data:
            messagebox.showinfo(T("msg_no_data_title"), T("msg_no_data"))
            return
        default_dir = self._project_path or os.path.expanduser("~")
        path = filedialog.asksaveasfilename(
            initialdir=default_dir, initialfile=T("dlg_export_default"),
            defaultextension=".txt",
            filetypes=[(T("ft_text"),"*.txt"),(T("ft_all"),"*.*")],
            title=T("dlg_export"),
        )
        if not path:
            return
        p = self._project_data
        m = self._meta_data or {}
        g = self._git_data or {}
        q = self._quality_data or {}
        t = getattr(self, "_test_data", {}) or {}

        if q:
            score   = q.get("score", 0)
            missing = q.get("missing", [])
            total   = q.get("total_items", 0)
        else:
            total_sym = len(m.get("functions",[])) + len(m.get("classes",[]))
            miss_cnt  = len(m.get("missing_docs",[]))
            score     = max(0, 100 - int(miss_cnt/max(total_sym,1)*100))
            missing   = m.get("missing_docs",[])
            total     = total_sym

        qual_label = (T("rpt_qual_excellent") if score >= 90
                      else (T("rpt_qual_improve") if score >= 60 else T("rpt_qual_attention")))
        lines = [
            "=" * 64,
            f"  {T('rpt_title')}",
            "  README Generator Pro v2.2 — polsoft.ITS™ Group",
            f"  {T('rpt_author_lbl')} Sebastian Januchowski",
            f"  {T('rpt_project_lbl')} {p['name']}",
            f"  {T('rpt_date_lbl')} {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "=" * 64, "",
            f"{T('rpt_overall')} {score}%  ({qual_label})",
            f"{T('rpt_elements')} {total}",
            f"{T('rpt_missing')} {q.get('missing_count', len(missing))}",
            f"{T('rpt_readme')} {'✅ ' + T('yes') if q.get('has_readme') else '❌ ' + T('no')}",
            f"{T('rpt_license')} {'✅ ' + T('yes') if q.get('has_license') else '❌ ' + T('no')}",
            f"{T('rpt_changelog')} {'✅ ' + T('yes') if q.get('has_changelog') else '❌ ' + T('no')}",
            "",
            f"{T('rpt_language')} {p.get('language','—')}",
            f"{T('rpt_files')} {p.get('file_count','—')}",
            f"{T('rpt_size')} {p.get('repo_size_kb','—')} KB",
            f"{T('rpt_tests')} {T('yes') if p.get('has_tests') else T('no')}"
            + (f" ({t['framework']})" if t.get("framework") else ""),
            "",
            "─" * 64,
            T("rpt_git"),
            "─" * 64,
            f"{T('rpt_branch')} {g.get('branch','—')}",
            f"{T('rpt_last_commit')} {g.get('last_commit_hash','—')} — {g.get('last_commit_msg','—')}",
            f"{T('rpt_commit_author')} {g.get('last_commit_author','—')}",
            f"{T('rpt_commit_date')} {g.get('last_commit_date','—')}",
            f"{T('rpt_commit_count')} {g.get('commits_count',0)}",
            f"{T('rpt_git_status')} {T('rpt_git_clean') if g.get('status_clean') else T('rpt_git_dirty')}",
            "",
            "─" * 64,
            T("rpt_missing_hdr"),
            "─" * 64, "",
        ]
        lines += missing or [T("rpt_all_ok")]
        lines += [
            "", "─" * 64,
            T("rpt_footer1"),
            T("rpt_footer2"),
            "polsoft.its@fastservice.com  |  https://github.com/seb07uk",
            "2026 © Sebastian Januchowski & polsoft.ITS™ Group",
        ]
        try:
            Path(path).write_text("\n".join(lines), encoding="utf-8")
            self._set_status(f"{T('status_export_saved')}{path}", "ok")
            messagebox.showinfo(T("msg_export_title"), T("msg_export_saved"))
        except Exception as e:
            messagebox.showerror(T("error"), str(e))

    # ══════════════════════════════════════════════════════════════════
    #  ADVANCED ACTIONS
    # ══════════════════════════════════════════════════════════════════

    def _gen_docs(self):
        if not self._project_data:
            messagebox.showinfo(T("msg_no_data_title"), T("msg_no_data"))
            return
        docs_dir = Path(self._project_path) / "docs"
        try:
            docs_dir.mkdir(exist_ok=True)
            p, m = self._project_data, self._meta_data or {}
            now = datetime.now().strftime("%Y-%m-%d")
            name = p["name"]

            api_lines = [f"# {name} — API\n\n> Generated {now}\n\n---\n"]
            for cls in m.get("classes",[]):
                api_lines.append(f"## `{cls['name']}`\n\n{cls.get('doc') or ''}\n")
                pub = [mt for mt in cls.get("methods",[]) if not mt["name"].startswith("_")]
                if pub:
                    api_lines.append("| Method | Arguments | Returns | Description |")
                    api_lines.append("|--------|-----------|---------|-------------|")
                    for mt in pub:
                        args = ", ".join(mt.get("args",[])[:3]) or "—"
                        api_lines.append(f"| `{mt['name']}` | `{args}` | `{mt.get('return') or '—'}` | {mt.get('doc') or '—'} |")
                api_lines.append("")

            usage_content = f"# {name} — Usage\n\n> Generated {now}\n\n## Installation\n\n{self._gen._deps_block(p)}\n\n## Run\n\n```bash\npython {p['entry']}\n```\n"
            cfg_content = f"# {name} — Configuration\n\n> Generated {now}\n\n## Config files\n\n"
            cfg_content += "\n".join(f"- `{c}`" for c in p.get("configs",[])) or "_No configuration files._"

            for fname, content in [("api.md", "\n".join(api_lines)),
                                    ("usage.md", usage_content),
                                    ("configuration.md", cfg_content)]:
                (docs_dir / fname).write_text(content, encoding="utf-8")

            self._set_status(T("status_docs_ok"), "ok")
            messagebox.showinfo(T("msg_docs_title"), f"{T('msg_docs_saved')}{docs_dir}")
        except Exception as e:
            messagebox.showerror(T("error"), str(e))

    def _gen_changelog(self):
        if not self._git_data or not self._git_data.get("is_git"):
            messagebox.showinfo(T("msg_no_git_title"), T("msg_no_git"))
            return
        g = self._git_data
        version = self._inp_version.get().strip() or (self._meta_data or {}).get("version","")
        now = datetime.now().strftime("%Y-%m-%d")
        ver_header = f"## [{version or 'Unreleased'}] — {now}"

        CONV_RE = re.compile(
            r"^([a-f0-9]+)\s+(feat|fix|docs|refactor|perf|test|chore|build|ci|style|revert)"
            r"(\([^)]+\))?(!)?:\s*(.+?)(?:\s+\(\d{4}-\d{2}-\d{2}.*\))?$",
            re.IGNORECASE)

        grouped: dict[str,list] = {}
        ungrouped = []
        labels = {"feat":"✨ New features","fix":"🐛 Bug fixes",
                  "docs":"📚 Documentation","refactor":"♻️ Refactoring",
                  "perf":"⚡ Performance","test":"🧪 Tests",
                  "chore":"🔧 Tooling","build":"📦 Build",
                  "ci":"🤖 CI/CD","style":"💄 Style","revert":"⏪ Revert"}

        for entry in g.get("changelog_entries",[]):
            m = CONV_RE.match(entry)
            if m:
                ctype = m.group(2).lower()
                scope = (m.group(3) or "").strip("()")
                msg   = m.group(5).strip()
                hash_ = m.group(1)
                scope_s = f"**{scope}**: " if scope else ""
                grouped.setdefault(ctype,[]).append(f"- {scope_s}{msg} (`{hash_}`)")
            else:
                ungrouped.append(f"- {entry}")

        lines = [ver_header,""]
        for ctype, label in labels.items():
            items = grouped.get(ctype,[])
            if items:
                lines.append(f"\n### {label}\n")
                lines.extend(items)
        if ungrouped:
            lines.append("\n### 📝 Other\n")
            lines.extend(ungrouped[:10])

        content = "\n".join(lines)
        fp = Path(self._project_path) / "CHANGELOG.md"
        header = "# Changelog\n\nAll project changes are documented here.\n\n"
        try:
            if fp.exists():
                existing = fp.read_text(encoding="utf-8")
                fp.write_text(header + content + "\n\n---\n\n" + existing, encoding="utf-8")
            else:
                fp.write_text(header + content, encoding="utf-8")
            self._set_status(T("status_changelog_saved", path=self._project_path), "ok")
            messagebox.showinfo(T("msg_changelog_title"), T("msg_changelog_saved"))
        except Exception as e:
            messagebox.showerror(T("error"), str(e))

    def _toggle_hook(self):
        if not self._project_path:
            messagebox.showwarning(T("msg_no_project_title"), T("msg_no_project_short"))
            return
        hook_path = Path(self._project_path) / ".git" / "hooks" / "pre-commit"
        HOOK_SCRIPT = """#!/bin/sh
# pre-commit hook — README Generator Pro v2.2
# Autor:  Sebastian Januchowski <polsoft.its@fastservice.com>
# Firma:  polsoft.ITS™ Group  |  https://github.com/seb07uk
# Licencja: 2026 © Sebastian Januchowski & polsoft.ITS™ Group
set -e
ROOT_DIR="$(git rev-parse --show-toplevel)"
echo "🔄 README Generator: regeneruję README.md..."
if [ -f "$ROOT_DIR/readme_generator_app.py" ]; then
    python3 "$ROOT_DIR/readme_generator_app.py" --cli "$ROOT_DIR" 2>/dev/null || true
    git add "$ROOT_DIR/README.md" 2>/dev/null || true
    echo "✅ README.md zaktualizowany."
fi
"""
        hooks_dir = Path(self._project_path) / ".git" / "hooks"
        if not hooks_dir.exists():
            messagebox.showerror(T("msg_hook_dir_err_title"), T("msg_hook_dir_err"))
            return

        if hook_path.exists():
            try:
                content = hook_path.read_text(encoding="utf-8", errors="ignore")
                if "README Generator" in content:
                    hook_path.unlink()
                    self._set_status(T("status_hook_removed"), "ok")
                    messagebox.showinfo(T("msg_hook_removed_title"), T("msg_hook_removed"))
                    self._update_hook_status()
                    return
            except Exception:
                pass
        try:
            hook_path.write_text(HOOK_SCRIPT, encoding="utf-8")
            hook_path.chmod(hook_path.stat().st_mode | 0o111)
            self._set_status(T("status_hook_installed"), "ok")
            messagebox.showinfo(T("msg_hook_installed_title"),
                                T("msg_hook_installed", path=hook_path))
            self._update_hook_status()
        except Exception as e:
            messagebox.showerror(T("msg_hook_install_err_title"), str(e))

    def _save_api_snapshot(self):
        if not self._meta_data:
            messagebox.showinfo(T("msg_no_analysis_title"), T("msg_no_data"))
            return
        m = self._meta_data
        snap = {}
        for fn in m.get("functions",[]):
            snap[fn["name"]] = {"args": fn.get("args",[]), "return": fn.get("return","")}
        for cls in m.get("classes",[]):
            for mt in cls.get("methods",[]):
                if not mt["name"].startswith("_"):
                    snap[f"{cls['name']}.{mt['name']}"] = {
                        "args": mt.get("args",[]), "return": mt.get("return","")}
        fp = Path(self._project_path) / ".readmegen_api_snapshot.json"
        try:
            fp.write_text(json.dumps(snap, indent=2, ensure_ascii=False), encoding="utf-8")
            self._set_status(T("status_api_saved", n=len(snap)), "ok")
            self._api_status_lbl.configure(
                text=T("status_api_saved_lbl", n=len(snap)), text_color=GRN)
            messagebox.showinfo(T("msg_api_title"), T("msg_api_saved", n=len(snap)))
        except Exception as e:
            messagebox.showerror(T("error"), str(e))

    # ══════════════════════════════════════════════════════════════════
    #  WATCH MODE
    # ══════════════════════════════════════════════════════════════════

    def _toggle_watch(self):
        if self._watch_var.get():
            if not self._project_path:
                messagebox.showwarning(T("msg_no_project_title"), T("msg_watch_no_project"))
                self._watch_var.set(False)
                return
            self._watcher_thread = threading.Thread(
                target=self._watch_loop, daemon=True)
            self._watcher_active = True
            self._watcher_hashes = self._snapshot_dir()
            self._watcher_thread.start()
            self._set_status(T("status_watch_on"), "busy")
        else:
            self._watcher_active = False
            self._set_status(T("status_watch_off"), "idle")

    def _watch_loop(self):
        IGNORE = {"__pycache__","node_modules","venv",".git","dist","build"}
        while getattr(self,"_watcher_active", False):
            time.sleep(3)
            try:
                new_hashes = self._snapshot_dir()
                if new_hashes != self._watcher_hashes:
                    self._watcher_hashes = new_hashes
                    self.after(0, self._on_files_changed)
            except Exception:
                pass

    def _snapshot_dir(self) -> dict:
        snap = {}
        IGNORE = {"__pycache__","node_modules","venv",".git","dist","build"}
        try:
            for fp in Path(self._project_path).rglob("*"):
                if any(p in IGNORE for p in fp.parts): continue
                if fp.is_file():
                    try:
                        snap[str(fp)] = hashlib.md5(fp.read_bytes()).hexdigest()
                    except Exception:
                        pass
        except Exception:
            pass
        return snap

    def _on_files_changed(self):
        self._set_status(T("status_watch_change"), "busy")
        self._analyze_and_generate_task_bg()

    def _analyze_and_generate_task_bg(self):
        threading.Thread(target=self._analyze_and_generate_task, daemon=True).start()

    # ══════════════════════════════════════════════════════════════════
    #  CONFIG
    # ══════════════════════════════════════════════════════════════════

    def _save_config(self):
        if not self._project_path:
            messagebox.showwarning(T("msg_no_project_title"), T("msg_no_project_short"))
            return
        cfg = {
            "template":    ReadmeGenerator.TEMPLATES_ALIAS.get(self._template_var.get(),"opensource"),
            "tree_mode":   self._tree_mode_var.get(),
            "tree_depth":  self._tree_depth_var.get(),
            "badge_style": self._badge_var.get(),
            "name":        self._inp_name.get().strip(),
            "version":     self._inp_version.get().strip(),
            "author":      self._inp_author.get().strip(),
            "description": self._inp_desc.get().strip(),
            "github_url":  self._inp_github.get().strip(),
            "sections":    {row.name: row.is_enabled for row in self._section_rows},
        }
        fp = Path(self._project_path) / ".readmegen.json"
        try:
            fp.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
            self._set_status(T("msg_cfg_saved"), "ok")
        except Exception as e:
            messagebox.showerror(T("error"), str(e))

    def _load_config(self):
        if not self._project_path: return
        fp = Path(self._project_path) / ".readmegen.json"
        if not fp.exists(): return
        try:
            cfg = json.loads(fp.read_text(encoding="utf-8"))
            rev = {v: k for k, v in ReadmeGenerator.TEMPLATES.items()}
            self._template_var.set(rev.get(cfg.get("template","opensource"),"Open-Source"))
            self._tree_mode_var.set(cfg.get("tree_mode","compact"))
            self._tree_depth_var.set(cfg.get("tree_depth",2))
            self._badge_var.set(cfg.get("badge_style","flat"))
            for attr, key in [("_inp_name","name"),("_inp_version","version"),
                               ("_inp_author","author"),("_inp_desc","description"),
                               ("_inp_github","github_url")]:
                entry = getattr(self, attr, None)
                if entry and cfg.get(key):
                    entry.delete(0,"end")
                    entry.insert(0, cfg[key])
            # Sections
            sec_cfg = cfg.get("sections",{})
            for row in self._section_rows:
                if row.name in sec_cfg:
                    row._enabled.set(sec_cfg[row.name])
            self._set_status(T("msg_cfg_loaded"), "ok")
        except Exception:
            pass

    def _set_all_sections(self, value: bool):
        for row in self._section_rows:
            row._enabled.set(value)
        self._on_option_change()

    # ══════════════════════════════════════════════════════════════════
    #  THEME
    # ══════════════════════════════════════════════════════════════════

    def _change_theme(self, theme: str):
        mode_map = {"dark":"dark","light":"light","dark-blue":"dark","green":"dark"}
        ctk.set_appearance_mode(mode_map.get(theme,"dark"))

    def _show_about(self):
        """About dialog with author and program information."""
        win = ctk.CTkToplevel(self)
        win.title(T("about_title"))
        win.geometry("480x400")
        win.resizable(False, False)
        win.configure(fg_color=BG)
        win.grab_set()

        # Logo
        logo_f = ctk.CTkFrame(win, fg_color=CARD, corner_radius=0, height=80)
        logo_f.pack(fill="x")
        logo_f.pack_propagate(False)

        logo_mark = ctk.CTkFrame(logo_f, fg_color=ACC, width=48, height=48, corner_radius=12)
        logo_mark.pack(side="left", padx=20, pady=16)
        logo_mark.pack_propagate(False)
        ctk.CTkLabel(logo_mark, text="R", text_color="#000",
                     font=("Segoe UI",22,"bold")).place(relx=.5, rely=.5, anchor="center")

        title_f = ctk.CTkFrame(logo_f, fg_color="transparent")
        title_f.pack(side="left", pady=16)
        ctk.CTkLabel(title_f, text="README Generator Pro",
                     text_color=FG, font=("Segoe UI",16,"bold"), anchor="w").pack(anchor="w")
        ctk.CTkLabel(title_f, text=T("about_subtitle"),
                     text_color=FG3, font=("Segoe UI",10), anchor="w").pack(anchor="w")

        # Info
        body = ctk.CTkScrollableFrame(win, fg_color="transparent",
                                       scrollbar_button_color=BORDER2)
        body.pack(fill="both", expand=True, padx=16, pady=12)

        rows = [
            (T("about_row_author"),  "Sebastian Januchowski",                          FG),
            (T("about_row_company"), "polsoft.ITS™ Group",                             ACC),
            (T("about_row_email"),   "polsoft.its@fastservice.com",                    GRN),
            (T("about_row_github"),  "https://github.com/seb07uk",                     PURPLE),
            (T("about_row_year"),    "2026",                                            FG2),
            (T("about_row_license"),"2026 © Sebastian Januchowski & polsoft.ITS™ Group",YLW),
            (T("about_row_python"),  "3.10+  ·  customtkinter ≥ 5.2",                 FG2),
            (T("about_row_version"), "2.2.0",                                          ACC),
        ]

        for label, value, color in rows:
            row = ctk.CTkFrame(body, fg_color=CARD, border_color=BORDER,
                               border_width=1, corner_radius=7)
            row.pack(fill="x", pady=3)
            ctk.CTkLabel(row, text=label, text_color=FG3,
                         font=("Segoe UI",10,"bold"), width=90, anchor="w").pack(side="left", padx=10, pady=7)
            ctk.CTkLabel(row, text=value, text_color=color,
                         font=("JetBrains Mono",10), anchor="w").pack(side="left", padx=4)

        # Description
        desc_f = ctk.CTkFrame(body, fg_color=CARD, border_color=BORDER,
                              border_width=1, corner_radius=7)
        desc_f.pack(fill="x", pady=6)
        ctk.CTkLabel(
            desc_f,
            text=T("about_desc"),
            text_color=FG2, font=("Segoe UI",10),
            justify="left", anchor="w",
        ).pack(padx=14, pady=10)

        # Close
        ctk.CTkButton(win, text=T("close"), command=win.destroy,
                      fg_color=ACC, hover_color=ACC2,
                      text_color="#000", font=("Segoe UI",11,"bold"),
                      height=34, corner_radius=8).pack(pady=(4,14))


# ══════════════════════════════════════════════════════════════════════════════
#   CLI MODE (dla pre-commit hook)
# ══════════════════════════════════════════════════════════════════════════════

def cli_generate(project_path: str):
    """Generuje README.md w trybie CLI (bez GUI), używany przez pre-commit hook."""
    analyzer  = ProjectAnalyzer()
    extractor = MetadataExtractor()
    git_anal  = GitAnalyzer()
    gen       = ReadmeGenerator()

    project = analyzer.analyze(project_path)
    meta    = extractor.extract(project_path)
    git     = git_anal.analyze(project_path)

    cfg_file = Path(project_path) / ".readmegen.json"
    cfg = {}
    if cfg_file.exists():
        try: cfg = json.loads(cfg_file.read_text(encoding="utf-8"))
        except Exception: pass

    rev = {v: k for k, v in ReadmeGenerator.TEMPLATES.items()}
    template = cfg.get("template","opensource")
    custom = {k: cfg.get(k,"") for k in ["name","desc","version","author","github_url"]}
    custom["github"] = custom.pop("github_url","")

    text = gen.generate(project, meta, git, custom, template=template,
                        badge_style=cfg.get("badge_style","flat"))

    out = Path(project_path) / "README.md"
    out.write_text(text, encoding="utf-8")
    print(f"✅ README.md wygenerowany ({len(text.splitlines())} linii)")
    print(f"   README Generator Pro v2.2 — Sebastian Januchowski @ polsoft.ITS™ Group")


# ══════════════════════════════════════════════════════════════════════════════
#   ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--cli":
        # Tryb CLI: python readme_generator_app.py --cli /ścieżka/projektu
        cli_generate(sys.argv[2])
    else:
        app = ReadmeGeneratorApp()
        app.mainloop()
