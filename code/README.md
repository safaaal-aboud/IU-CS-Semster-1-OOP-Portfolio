# Studien-Dashboard

Ein Python-basiertes Dashboard zur Verwaltung und Überwachung eines Studiengangs mit Semestern, Modulen und Prüfungsleistungen.

## Projektbeschreibung

Dieses Projekt wurde im Rahmen des Kurses **DLBDSOOFPP01 - Objektorientierte und funktionale Programmierung mit Python** an der IU Internationale Hochschule entwickelt.

Das Studien-Dashboard ermöglicht:
- ✅ Verwaltung von Studiengang, Semestern und Modulen
- ✅ Erfassung von Prüfungsleistungen
- ✅ Berechnung von Notendurchschnitt und Studienfortschritt
- ✅ Persistierung der Daten (Pickle, CSV)
- ✅ CLI-basierte Benutzeroberfläche

---

## Architektur

Das Projekt folgt einer **3-Schichten-Architektur**:

```
code/
├── domain/              # Anwendungslogikschicht
│   ├── studiengang.py   # Hauptklasse für Studiengang
│   ├── semester.py      # Semester-Verwaltung
│   ├── modul.py         # Modul-Verwaltung
│   ├── pruefungsleistung.py  # Prüfungsleistungen
│   └── enums.py         # Enumerationen (Abschluss, Status, Prüfungsart)
│
├── persistence/         # Datenhaltungsschicht
│   └── daten_manager.py # Speichern/Laden (Pickle, CSV)
│
├── gui/                 # Präsentationsschicht
│   ├── dashboard_view.py    # Dashboard-Anzeige
│   └── input_handler.py     # Benutzereingaben
│
└── main.py             # Hauptprogramm
```

---

## OOP-Konzepte

Das Projekt demonstriert folgende OOP-Konzepte:

### Encapsulation (Kapselung)
- Private Attribute (mit `_` Präfix)
- Properties (`@property`) für kontrollierten Zugriff
- Setter (`@<name>.setter`) für validierte Änderungen

### Komposition
- `Studiengang` **besitzt** `Semester` (starke Abhängigkeit)
- Semester werden im Konstruktor erstellt
- Semester können nicht ohne Studiengang existieren

### Aggregation
- `Semester` **verwaltet** `Module` (schwache Abhängigkeit)
- Module werden über `fuege_modul_hinzu()` hinzugefügt
- Module können unabhängig von Semester existieren

### Enums
- `Abschluss`: BACHELOR, MASTER, DIPLOM
- `ModulStatus`: OFFEN, ANGEMELDET, BESTANDEN, NICHT_BESTANDEN
- `Pruefungsart`: 11 verschiedene Prüfungsarten

---

## Installation

### Systemanforderungen
- **Python 3.11 oder höher**
- **Betriebssystem:** Windows, macOS, Linux
- **Keine externen Bibliotheken erforderlich** (nur Python Standard Library)

### Schritt 1: Projekt herunterladen

1. Öffne das GitHub-Repository: [https://github.com/safaaal-aboud/IU-CS-Semster-1-OOP-Portfolio]
2. Klicke auf den grünen **`< > Code`** Button
3. Wähle **`Download ZIP`**
4. Entpacke die heruntergeladene ZIP-Datei in einen Ordner deiner Wahl

### Schritt 2: Python-Version prüfen
```bash
python --version
# oder
python3 --version
```

---

## Verwendung

### Programm starten

**Windows:**
```bash
cd IU-CS-Semster-1-OOP-Portfolio/code
python main.py
```

**macOS/Linux:**
```bash
cd IU-CS-Semster-1-OOP-Portfolio/code
python3 main.py
```


### Beim ersten Start

Das Programm fragt, ob Sie einen Beispiel-Studiengang erstellen möchten:
- **j** = Beispieldaten werden geladen (Cybersecurity Bachelor mit Modulen)
- **n** = Leerer Studiengang wird erstellt

### Hauptmenü

```
1. Dashboard anzeigen          # Übersicht über Studienfortschritt
2. Modul hinzufügen            # Neues Modul anlegen
3. Prüfungsleistung hinzufügen # Note für Modul eintragen
4. Modulstatus ändern          # Status aktualisieren
5. Daten speichern             # Als Pickle speichern
6. Daten als CSV exportieren   # CSV-Export
7. Beenden                     # Programm beenden
```

### Daten speichern

- **Automatisch:** Beim Beenden werden Sie gefragt, ob gespeichert werden soll
- **Manuell:** Option 5 im Hauptmenü
- **Speicherort:** `code/studiengang.pkl`

### Daten exportieren

- CSV-Export über Option 6
- Erstellt separate CSV-Dateien für Module und Prüfungsleistungen

---

## Projektstruktur

```
studien_dashboard/
├── code/
│   ├── main.py                    # Hauptprogramm
│   ├── domain/                    # Geschäftslogik
│   │   ├── studiengang.py
│   │   ├── semester.py
│   │   ├── modul.py
│   │   ├── pruefungsleistung.py
│   │   └── enums.py
│   ├── persistence/               # Datenverwaltung
│   │   └── daten_manager.py
│   └── gui/                       # Benutzeroberfläche
│       ├── dashboard_view.py
│       └── input_handler.py
├── UML/                           # UML-Diagramme
│   ├── Dashboard_UML_PH_3.png
│   └── Dashboard_UML_PH_3.mdj
├── tests/                         # Tests
│   ├── test_properties.py
│   └── test_komposition_aggregation.py
├── .gitignore
└── README.md
```

---

## Tests

### Properties testen
```bash
cd code
python test_properties.py
```

### Komposition/Aggregation testen
```bash
cd code
python test_komposition_aggregation.py
```

---

## UML-Diagramm

Das vollständige UML-Klassendiagramm finden Sie in:
- `UML/Dashboard_UML_PH_3.png` (Bild)
- `UML/Dashboard_UML_PH_3.mdj` (StarUML-Projekt)

---

## Autor

**Safaa Al-Aboud**
- Matrikelnummer: IU14124768
- Kurs: DLBDSOOFPP01 - Objektorientierte und funktionale Programmierung mit Python
- Hochschule: IU Internationale Hochschule

---

## Lizenz

Dieses Projekt wurde zu Bildungszwecken erstellt.

---

## Links

- **GitHub Repository:** https://github.com/safaaal-aboud/IU-CS-Semster-1-OOP-Portfolio
- **IU Internationale Hochschule:** https://www.iu.de

---

## Hinweise

- Beim ersten Start werden Beispieldaten angeboten
- Daten werden als `.pkl` Datei gespeichert
- CSV-Export für externe Analyse verfügbar
- CLI-basiert (keine grafische Oberfläche erforderlich)

---

**Version:** 1.0  
**Datum:** November 2025

