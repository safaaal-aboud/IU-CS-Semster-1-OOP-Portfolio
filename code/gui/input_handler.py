"""
InputHandler-Klasse für die Benutzerinteraktion.

Diese Klasse verarbeitet Benutzereingaben und steuert die Anwendung.
"""

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain import Studiengang
    from persistence import DatenManager
    from .dashboard_view import DashboardView

from domain.enums import Pruefungsart, ModulStatus
from domain import Pruefungsleistung, Modul


class InputHandler:
    """
    Verarbeitet Benutzereingaben und steuert die Anwendung.
    
    Attributes:
        _studiengang: Der aktuelle Studiengang
        _daten_manager: Der DatenManager für Persistierung
        _dashboard_view: Die DashboardView für Visualisierung
    """
    
    def __init__(self, studiengang: 'Studiengang', daten_manager: 'DatenManager', 
                 dashboard_view: 'DashboardView'):
        """
        Initialisiert den InputHandler.
        
        Args:
            studiengang: Der Studiengang
            daten_manager: Der DatenManager
            dashboard_view: Die DashboardView
        """
        self._studiengang = studiengang
        self._daten_manager = daten_manager
        self._dashboard_view = dashboard_view
    
    @property
    def studiengang(self) -> 'Studiengang':
        """Getter für den Studiengang."""
        return self._studiengang
    
    @studiengang.setter
    def studiengang(self, value: 'Studiengang'):
        """Setter für den Studiengang."""
        self._studiengang = value
        self._dashboard_view.studiengang = value
    
    def starten(self) -> None:
        """Startet die Hauptschleife der Anwendung."""
        while True:
            try:
                self.zeige_menu()
                auswahl = input("\nIhre Auswahl: ").strip()
                
                if auswahl == "1":
                    self._dashboard_view.zeige_dashboard()
                elif auswahl == "2":
                    self._modul_hinzufuegen()
                elif auswahl == "3":
                    self._pruefungsleistung_hinzufuegen()
                elif auswahl == "4":
                    self._modul_status_aendern()
                elif auswahl == "5":
                    self._daten_manager.speichere_studiengang(self._studiengang)
                elif auswahl == "6":
                    self._daten_manager.exportiere_csv(self._studiengang)
                elif auswahl == "7":
                    print("\n👋 Auf Wiedersehen!")
                    break
                else:
                    print("\n❌ Ungültige Auswahl. Bitte versuchen Sie es erneut.")
                
                input("\nDrücken Sie Enter um fortzufahren...")
                print("\n" * 2)
                
            except KeyboardInterrupt:
                print("\n\n👋 Programm beendet.")
                break
            except Exception as e:
                print(f"\n❌ Fehler: {e}")
                input("\nDrücken Sie Enter um fortzufahren...")
    
    def zeige_menu(self) -> None:
        """Zeigt das Hauptmenü an."""
        print("\n" + "=" * 80)
        print("  HAUPTMENÜ")
        print("=" * 80)
        print("  1. Dashboard anzeigen")
        print("  2. Modul hinzufügen")
        print("  3. Prüfungsleistung hinzufügen")
        print("  4. Modulstatus ändern")
        print("  5. Daten speichern")
        print("  6. Daten als CSV exportieren")
        print("  7. Beenden")
        print("=" * 80)
    
    def _modul_hinzufuegen(self) -> None:
        """Fügt ein neues Modul hinzu."""
        print("\n" + "=" * 80)
        print("  MODUL HINZUFÜGEN")
        print("=" * 80)
        
        # Semester auswählen
        print("\nVerfügbare Semester:")
        for i, semester in enumerate(self._studiengang.semester, 1):
            print(f"  {i}. {semester}")
        
        try:
            semester_nr = int(input("\nSemester-Nummer: "))
            if semester_nr < 1 or semester_nr > len(self._studiengang.semester):
                print("❌ Ungültige Semester-Nummer")
                return
            
            semester = self._studiengang.semester[semester_nr - 1]
            
            # Modul-Daten eingeben
            modulcode = input("Modulcode: ").strip()
            name = input("Modulname: ").strip()
            ects = int(input("ECTS: "))
            semester_empfehlung = int(input("Semester-Empfehlung: "))
            
            # Modul erstellen und hinzufügen
            modul = Modul(modulcode, name, ects, semester_empfehlung)
            semester.fuege_modul_hinzu(modul)
            
            print(f"\n✓ Modul '{name}' erfolgreich zu Semester {semester_nr} hinzugefügt!")
            
        except ValueError as e:
            print(f"❌ Ungültige Eingabe: {e}")
        except Exception as e:
            print(f"❌ Fehler: {e}")
    
    def _pruefungsleistung_hinzufuegen(self) -> None:
        """Fügt eine Prüfungsleistung zu einem Modul hinzu."""
        print("\n" + "=" * 80)
        print("  PRÜFUNGSLEISTUNG HINZUFÜGEN")
        print("=" * 80)
        
        # Alle Module anzeigen
        alle_module = self._studiengang.hole_alle_modulen()
        
        if not alle_module:
            print("\n❌ Keine Module vorhanden. Bitte fügen Sie zuerst Module hinzu.")
            return
        
        print("\nVerfügbare Module:")
        for i, modul in enumerate(alle_module, 1):
            print(f"  {i}. {modul}")
        
        try:
            modul_nr = int(input("\nModul-Nummer: "))
            if modul_nr < 1 or modul_nr > len(alle_module):
                print("❌ Ungültige Modul-Nummer")
                return
            
            modul = alle_module[modul_nr - 1]
            
            # Prüfungsdaten eingeben
            note = float(input("Note (1.0 - 5.0): "))
            
            print("\nVerfügbare Prüfungsarten:")
            for i, art in enumerate(Pruefungsart, 1):
                print(f"  {i}. {art.value}")
            
            art_nr = int(input("Prüfungsart-Nummer: "))
            pruefungsart = list(Pruefungsart)[art_nr - 1]
            
            versuch = int(input("Versuch (1, 2, 3, ...): "))
            
            # Datum (Standard: heute)
            datum_input = input("Datum (YYYY-MM-DD, Enter für heute): ").strip()
            if datum_input:
                jahr, monat, tag = map(int, datum_input.split('-'))
                datum = date(jahr, monat, tag)
            else:
                datum = date.today()
            
            # Prüfungsleistung erstellen und setzen
            pruefungsleistung = Pruefungsleistung(note, datum, versuch, pruefungsart)
            modul.setze_pruefungsleistung(pruefungsleistung)
            
            print(f"\n✓ Prüfungsleistung erfolgreich zu Modul '{modul.name}' hinzugefügt!")
            print(f"  Note: {note} ({pruefungsleistung.hole_bewertung()})")
            print(f"  Status: {'✓ Bestanden' if pruefungsleistung.ist_bestanden() else '✗ Nicht bestanden'}")
            
        except ValueError as e:
            print(f"❌ Ungültige Eingabe: {e}")
        except Exception as e:
            print(f"❌ Fehler: {e}")
    
    def _modul_status_aendern(self) -> None:
        """Ändert den Status eines Moduls."""
        print("\n" + "=" * 80)
        print("  MODULSTATUS ÄNDERN")
        print("=" * 80)
        
        alle_module = self._studiengang.hole_alle_modulen()
        
        if not alle_module:
            print("\n❌ Keine Module vorhanden.")
            return
        
        print("\nVerfügbare Module:")
        for i, modul in enumerate(alle_module, 1):
            print(f"  {i}. {modul}")
        
        try:
            modul_nr = int(input("\nModul-Nummer: "))
            if modul_nr < 1 or modul_nr > len(alle_module):
                print("❌ Ungültige Modul-Nummer")
                return
            
            modul = alle_module[modul_nr - 1]
            
            print("\nVerfügbare Status:")
            for i, status in enumerate(ModulStatus, 1):
                print(f"  {i}. {status.value}")
            
            status_nr = int(input("Status-Nummer: "))
            neuer_status = list(ModulStatus)[status_nr - 1]
            
            modul.status = neuer_status
            
            print(f"\n✓ Status von Modul '{modul.name}' erfolgreich geändert zu: {neuer_status.value}")
            
        except ValueError as e:
            print(f"❌ Ungültige Eingabe: {e}")
        except Exception as e:
            print(f"❌ Fehler: {e}")
