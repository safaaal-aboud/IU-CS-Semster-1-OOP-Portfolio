# IU-CS-Semster-1-OOP-Portfolio
Code und Dokumentation für OOP – IU-Portfolio-Projekt.
# Studien-Dashboard - Phase 3

## 1. Überblick

Dieses Projekt ist eine professionelle Implementierung eines Studien-Dashboards in Python, basierend auf dem UML-Klassendiagramm für Phase 3. Es handelt sich um eine Konsolenanwendung, die eine 3-Schichten-Architektur verwendet, um die Verwaltung eines Studiengangs, inklusive Semester, Module und Prüfungsleistungen, zu ermöglichen.

Die Anwendung demonstriert zentrale objektorientierte Konzepte wie **Kapselung**, **Komposition** und **Aggregation** und folgt dabei den Best Practices von Python.

---

## 2. Features

- **3-Schichten-Architektur**: Klare Trennung von Anwendungslogik, Datenpersistenz und Benutzeroberfläche.
- **OOP-Konzepte**: 
  - **Kapselung**: Verwendung von `@property`-Dekoratoren für kontrollierten Attributzugriff.
  - **Komposition**: Die `Studiengang`-Klasse "besitzt" `Semester`-Objekte.
  - **Aggregation**: `Semester`-Objekte "enthalten" `Modul`-Objekte, die unabhängig existieren.
- **Datenpersistenz**: Speichern und Laden des gesamten Studiengang-Objekts mittels `pickle`.
- **CSV-Export**: Exportieren der Modul- und Notenübersicht in eine CSV-Datei.
- **Interaktive Konsole**: Menügesteuerte Bedienung zum Anzeigen des Dashboards, Hinzufügen von Modulen und Prüfungsleistungen.
- **Dynamisches Dashboard**: Visualisierung von Studienfortschritt, Notendurchschnitt und Semester-Übersichten.
- **Test-Suite**: Separate Test-Skripte zur Demonstration der OOP-Konzepte aus Phase 2.

---

## 3. Projektstruktur

Das Projekt ist in drei Hauptschichten unterteilt, die in separaten Paketen organisiert sind:

```
studien_dashboard/
├── domain/                 # Anwendungslogik-Schicht (Entities)
│   ├── __init__.py
│   ├── enums.py            # Alle Enum-Klassen (Abschluss, Pruefungsart, etc.)
│   ├── pruefungsleistung.py
│   ├── modul.py
│   ├── semester.py
│   └── studiengang.py
├── persistence/            # Datenspeicher-Schicht
│   ├── __init__.py
│   └── daten_manager.py    # Speichern, Laden, CSV-Export
├── gui/                    # GUI-Schicht (Konsolen-UI)
│   ├── __init__.py
│   ├── dashboard_view.py   # Visualisierung des Dashboards
│   └── input_handler.py    # Menüführung und Benutzereingaben
├── tests/                  # Test-Skripte
│   ├── __init__.py
│   ├── test_komposition_aggregation.py
│   └── test_properties.py
├── main.py                 # Haupteinstiegspunkt der Anwendung
├── requirements.txt        # Projekt-Abhängigkeiten (keine externen benötigt)
└── README.md               # Diese Datei
```

---

## 4. Installation

Das Projekt erfordert **Python 3.14** oder höher. Es werden keine externen Bibliotheken benötigt, da ausschließlich die Python Standard Library verwendet wird.

1.  **Klonen Sie das Projekt** (oder laden Sie die ZIP-Datei herunter und entpacken Sie sie).
2.  Navigieren Sie in das Hauptverzeichnis `studien_dashboard/`.

---

## 5. Anwendung starten

Um das Studien-Dashboard zu starten, führen Sie die `main.py`-Datei aus:

```bash
cd studien_dashboard
python main.py
```

Beim ersten Start werden Sie gefragt, ob Sie einen Beispiel-Studiengang mit vordefinierten Daten erstellen möchten. Dies wird empfohlen, um die Features der Anwendung schnell zu sehen.

### Menüführung

Nach dem Start erscheint das Hauptmenü:

```
================================================================================
  HAUPTMENÜ
================================================================================
  1. Dashboard anzeigen
  2. Modul hinzufügen
  3. Prüfungsleistung hinzufügen
  4. Modulstatus ändern
  5. Daten speichern
  6. Daten als CSV exportieren
  7. Beenden
================================================================================
```

- **Dashboard anzeigen**: Zeigt eine vollständige Übersicht über Fortschritt, Noten und Module.
- **Modul hinzufügen**: Ermöglicht das Hinzufügen eines neuen Moduls zu einem bestimmten Semester.
- **Prüfungsleistung hinzufügen**: Ermöglicht das Hinzufügen einer Note zu einem Modul.
- **Daten speichern**: Speichert den aktuellen Stand des Studiengangs in der Datei `studiengang.pkl`.
- **Daten als CSV exportieren**: Erstellt eine `studiengang.csv`-Datei mit einer detaillierten Übersicht aller Module.
- **Beenden**: Beendet die Anwendung und fragt, ob die Änderungen gespeichert werden sollen.

---

## 6. Tests ausführen

Die `tests/`-Verzeichnis enthält Skripte, die die in Phase 2 diskutierten OOP-Konzepte demonstrieren.

### Test für Kapselung (@property)

Dieser Test zeigt, wie `@property` und `@<name>.setter` für kontrollierten Attributzugriff verwendet werden.

```bash
cd studien_dashboard
python tests/test_properties.py
```

### Test für Komposition und Aggregation

Dieser Test demonstriert den Unterschied im Lebenszyklus von Objekten in Kompositions- und Aggregationsbeziehungen.

```bash
cd studien_dashboard
python tests/test_komposition_aggregation.py
```

---

## 7. Architektonische Konzepte

### 3-Schichten-Architektur

- **Domain (Anwendungslogik)**: Enthält die Kernlogik und die Entity-Klassen (`Studiengang`, `Semester`, `Modul`). Diese Schicht ist unabhängig von den anderen Schichten.
- **Persistence (Datenspeicher)**: Verantwortlich für das Speichern und Laden der Domain-Objekte. Sie kennt die Domain-Schicht, aber nicht die GUI-Schicht.
- **GUI (Benutzeroberfläche)**: Verantwortlich für die Darstellung der Daten und die Interaktion mit dem Benutzer. Sie verwendet die Domain- und Persistence-Schichten.

### Objektorientierte Konzepte

- **Kapselung**: Alle Attribute der Klassen sind als "protected" (`_attribut`) deklariert. Der Zugriff erfolgt ausschließlich über `@property`-Dekoratoren, die bei Bedarf Validierungslogik enthalten.
- **Komposition**: Die Beziehung zwischen `Studiengang` und `Semester` ist eine Komposition. Die `Semester`-Objekte werden innerhalb des `Studiengang`-Konstruktors erstellt und sind von dessen Lebenszyklus abhängig.
- **Aggregation**: Die Beziehung zwischen `Semester` und `Modul` ist eine Aggregation. `Modul`-Objekte werden unabhängig erstellt und können einem `Semester` hinzugefügt oder daraus entfernt werden, ohne zerstört zu werden.

---

## 8. Datenpersistenz

Die Anwendung verwendet das `pickle`-Modul von Python, um das gesamte `Studiengang`-Objekt inklusive aller zugehörigen `Semester`-, `Modul`- und `Pruefungsleistung`-Objekte zu serialisieren und in einer einzigen Binärdatei (`studiengang.pkl`) zu speichern. Dies ermöglicht ein einfaches und schnelles Speichern und Laden des gesamten Anwendungszustands.
