# Pimp my Python Environment

## Visual Studio Code Settings

- Eigene Templates und Snippets in [.vscode\python.code-snippets](.vscode\python.code-snippets) ermöglichen standardisierte Vorlagen.
- Projekt-Einstellungen in [settings.json](.vscode/settings.json) definieren wichtige Projekteinstellungen unabhängig von Benutzer

## Dependency & Environment Management - [uv](https://docs.astral.sh/uv/)

- Installation mit `winget install --exact --id astral-sh.uv` oder gemäss https://docs.astral.sh/uv/getting-started/installation/
- Dokumentation der Projekt-Abhängigkeiten und Metadaten in [pyproject.toml](pyproject.toml)
- Fixierte Versionen von Abhängigkeiten und deren Abhängigkeiten in [uv.lock](uv.lock)
- Nicht kompatibel mit arcpy und conda da ArcGIS diverse Anforderungen an die Python-Umgebung stellt.

### Anwendungsbeispiel

```cmd
rem Projekt initialisieren mit bestimmter Python-Version
uv init -p 3.12

rem Python Skript ausführen (erstellt auch virtuelle Umgebung)
uv run main.py

rem Virtuelle Umgebung erstellen mit Abhängigkeiten / Modulen
uv sync

rem Modul / Abhängigkeit zu Projekt hinzufügen
uv add duckdb

rem Modul / Abhängigkeit für Entwicklung hinzufügen
uv add --dev ruff
uv add --dev ty
uv add --dev pre-commit

rem Verwendung von pip wie gewohnt
uv pip install requirements.txt
```

## Formatter - [ruff](https://docs.astral.sh/ruff/)

- Installation mit `uv add --dev ruff` plus Visual Studio Code Extension [charliermarsh.ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- Konfiguration in [pyproject.toml](pyproject.toml) gemäss https://docs.astral.sh/ruff/settings/#top-level und https://docs.astral.sh/ruff/settings/#format


### Anwendungsbeispiel

Automatische Formatierung in Editor bei aktiviertem `editor.formatOnSave` in [settings.json](.vscode/settings.json)

```cmd
rem Alle Dateien im aktuellen Verzeichnis formatieren
ruff format                   
rem Alle Dateien in `Pfad/zum/Code` (und allen Unterverzeichnissen) formatieren.
ruff format ./path/to/code/     
rem Eine einzelne Datei formatieren.
ruff format path/to/file.py   
```

## Linter - [ruff](https://docs.astral.sh/ruff/)

- Installation mit `uv add --dev ruff` plus Visual Studio Code Extension [charliermarsh.ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- Auswahl und Ausschluss der zu verwendenden [Regeln](https://docs.astral.sh/ruff/rules/) in [pyproject.toml](pyproject.toml)

### Anwendungsbeispiel

Problems-Tab in Visual Studio Code

```cmd
rem Alle Dateien im aktuellen Verzeichnis prüfen
ruff check
rem Alle Dateien im aktuellen Verzeichnis prüfen und behebbare Fehler / Unstimmigkeiten korrigieren
ruff check --fix
```

## Type-Checking - [ty](https://docs.astral.sh/ty/)

- Installation mit `uv add --dev ty`
- Ergänzende Problem-Hinweise zu Linter bezüglich Variablen und Typen.
- Präzisere Autovervollständigung
- Prüfen von Typen-Kompatiblität vor Ausführung

### Anwendungsbeispiel

```cmd
rem Prüft Dateien im aktuellen Verzeichnis
ty check
```

## Qualitätssicherung vor Commit oder Push - [pre-commit](https://pre-commit.com/)

- Installation mit `uv add --dev pre-comnmit`
- Konfiguration in [.pre-commit-config.yaml](.pre-commit-config.yaml)
- **Funktioniert aktuell nicht auf Sandbox**

### Anwendungsbeispiel

```cmd
rem Erstellen einer neuen Konfiguration
pre-commit sample-config > .pre-commit-config.yaml

rem Installation der Konfiguration
pre-commit install

rem Ausführen der konfigurierten pre-commit-hooks
pre-commit run
```
