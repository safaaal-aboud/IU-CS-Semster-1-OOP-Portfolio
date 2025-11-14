"""
Hauptprogramm für das Studien-Dashboard.

Dieses Programm startet das Studien-Dashboard und ermöglicht die Verwaltung
eines Studiengangs mit Semestern, Modulen und Prüfungsleistungen.
"""

from datetime import date
from domain import Studiengang, Semester, Modul, Pruefungsleistung
from domain.enums import Abschluss, Pruefungsart, ModulStatus
from persistence import DatenManager
from gui import DashboardView, InputHandler


def erstelle_beispiel_studiengang() -> Studiengang:
    """
    Erstellt einen Beispiel-Studiengang mit echten Modulen aus dem Cybersecurity-Studiengang.
    
    Returns:
        Ein Studiengang mit Beispieldaten basierend auf dem echten Studienplan
    """
    # Studiengang erstellen
    studiengang = Studiengang(
        name="Cybersecurity",
        abschluss=Abschluss.BACHELOR,
        gesamtdauer=6,
        ziel_notendurchschnitt=2.0,
        ziel_abschlussdauer=6
    )
    
    # ===== SEMESTER 1 =====
    # Modul 1: OOP mit Python (aktuell - mit Note)
    modul1 = Modul("DLBDSOOFPP01_D", "Objektorientierte und funktionale Programmierung mit Python", 5, 1)
    pruefung1 = Pruefungsleistung(1.7, date(2024, 11, 15), 1, Pruefungsart.PORTFOLIO)
    modul1.setze_pruefungsleistung(pruefung1)
    
    # Modul 2: Einführung Cybersecurity (bestanden)
    modul2 = Modul("DLBCSICS01", "Einführung in Cybersecurity und IT-Sicherheit", 5, 1)
    pruefung2 = Pruefungsleistung(2.3, date(2024, 10, 20), 1, Pruefungsart.KLAUSUR)
    modul2.setze_pruefungsleistung(pruefung2)
    
    # Modul 3: Betriebssysteme (bestanden)
    modul3 = Modul("DLBINGWBS01", "Betriebssysteme, Rechnernetze und verteilte Systeme", 5, 1)
    pruefung3 = Pruefungsleistung(2.0, date(2024, 10, 15), 1, Pruefungsart.KLAUSUR)
    modul3.setze_pruefungsleistung(pruefung3)
    
    # Modul 4: Wissenschaftliches Arbeiten (offen)
    modul4 = Modul("DLBINGIT01", "Einführung in das Wissenschaftliche Arbeiten für IT- und Technik", 5, 1)
    modul4.status = ModulStatus.OFFEN
    
    # Modul 5: Projekt OOP (angemeldet)
    modul5 = Modul("DLBDSOOFPP01_P", "Projekt: Objektorientierte und funktionale Programmierung mit Python", 5, 1)
    modul5.status = ModulStatus.ANGEMELDET
    
    studiengang.semester[0].fuege_modul_hinzu(modul1)
    studiengang.semester[0].fuege_modul_hinzu(modul2)
    studiengang.semester[0].fuege_modul_hinzu(modul3)
    studiengang.semester[0].fuege_modul_hinzu(modul4)
    studiengang.semester[0].fuege_modul_hinzu(modul5)
    
    # ===== SEMESTER 2 =====
    # Modul 6: Netzwerksicherheit (angemeldet)
    modul6 = Modul("DLBCSENFSI_D", "Einführung in die Netzwerksicherheit", 5, 2)
    modul6.status = ModulStatus.ANGEMELDET
    
    # Modul 7: Mathematik Grundlagen (angemeldet)
    modul7 = Modul("IMT101", "Mathematik Grundlagen I", 5, 2)
    modul7.status = ModulStatus.ANGEMELDET
    
    # Modul 8: Statistik (offen)
    modul8 = Modul("DLBDSPGDS01_D", "Statistik - Wahrscheinlichkeit und deskriptive Statistik", 5, 2)
    modul8.status = ModulStatus.OFFEN
    
    # Modul 9: Requirements Engineering (offen)
    modul9 = Modul("IREM01", "Requirements Engineering", 5, 2)
    modul9.status = ModulStatus.OFFEN
    
    # Modul 10: Projekt Agiles PM (offen)
    modul10 = Modul("DLBCSAPM01", "Projekt: Agiles Projektmanagement", 5, 2)
    modul10.status = ModulStatus.OFFEN
    
    studiengang.semester[1].fuege_modul_hinzu(modul6)
    studiengang.semester[1].fuege_modul_hinzu(modul7)
    studiengang.semester[1].fuege_modul_hinzu(modul8)
    studiengang.semester[1].fuege_modul_hinzu(modul9)
    studiengang.semester[1].fuege_modul_hinzu(modul10)
    
    # ===== SEMESTER 3 =====
    # Modul 11: System-Pentesting (offen)
    modul11 = Modul("DLBCSESPKI_D", "Grundlage des System-Pentestings", 5, 3)
    modul11.status = ModulStatus.OFFEN
    
    # Modul 12: Theoretische Informatik (offen)
    modul12 = Modul("DLBITIM01", "Theoretische Informatik und Mathematische Logik", 5, 3)
    modul12.status = ModulStatus.OFFEN
    
    # Modul 13: Social Engineering (offen)
    modul13 = Modul("DLBCSESEIT_D", "Social Engineering und Insider Threats", 5, 3)
    modul13.status = ModulStatus.OFFEN
    
    # Modul 14: IT-Sicherheitskonzeptionen (offen)
    modul14 = Modul("DLBCSESCSI_D", "Technische und betriebliche IT-Sicherheitskonzeptionen", 5, 3)
    modul14.status = ModulStatus.OFFEN
    
    studiengang.semester[2].fuege_modul_hinzu(modul11)
    studiengang.semester[2].fuege_modul_hinzu(modul12)
    studiengang.semester[2].fuege_modul_hinzu(modul13)
    studiengang.semester[2].fuege_modul_hinzu(modul14)
    
    # ===== SEMESTER 4 =====
    # Modul 15: DevSecOps (offen)
    modul15 = Modul("DLBCSECSPRS01_D", "DevSecOps und gängige Software-Schwachstellen", 5, 4)
    modul15.status = ModulStatus.OFFEN
    
    # Modul 16: Kryptografie (offen)
    modul16 = Modul("DLBCSCS_01", "Kryptografische Verfahren", 5, 4)
    modul16.status = ModulStatus.OFFEN
    
    # Modul 17: Softwareforensik (offen)
    modul17 = Modul("DLBCSENSFI01_D", "Host- und Softwareforensik", 5, 4)
    modul17.status = ModulStatus.OFFEN
    
    # Modul 18: Seminar Computer Science (offen)
    modul18 = Modul("DLBCSATCSI01_D", "Seminar: Aktuelle Themen in Computer Science", 5, 4)
    modul18.status = ModulStatus.OFFEN
    
    studiengang.semester[3].fuege_modul_hinzu(modul15)
    studiengang.semester[3].fuege_modul_hinzu(modul16)
    studiengang.semester[3].fuege_modul_hinzu(modul17)
    studiengang.semester[3].fuege_modul_hinzu(modul18)
    
    # ===== SEMESTER 5 =====
    # Modul 19: Threat Modeling (offen)
    modul19 = Modul("DLBCSEETSI_D", "Threat Modeling", 5, 5)
    modul19.status = ModulStatus.OFFEN
    
    # Modul 20: Standards Informationssicherheit (offen)
    modul20 = Modul("DLBCSEISS01_D", "Standards der Informationssicherheit", 5, 5)
    modul20.status = ModulStatus.OFFEN
    
    studiengang.semester[4].fuege_modul_hinzu(modul19)
    studiengang.semester[4].fuege_modul_hinzu(modul20)
    
    # ===== SEMESTER 6 =====
    # Modul 21: C/C++ Programmierung (offen)
    modul21 = Modul("DLBINMAPCCS01", "Projekt: Allgemeine Programmierung mit C/C++", 5, 6)
    modul21.status = ModulStatus.OFFEN
    
    studiengang.semester[5].fuege_modul_hinzu(modul21)
    
    return studiengang


def main():
    """Hauptfunktion der Anwendung."""
    print("\n" + "=" * 80)
    print("  WILLKOMMEN ZUM STUDIEN-DASHBOARD")
    print("=" * 80)
    
    # DatenManager initialisieren
    daten_manager = DatenManager("studiengang.pkl")
    
    # Versuchen, gespeicherten Studiengang zu laden
    studiengang = daten_manager.lade_studiengang()
    
    if studiengang is None:
        print("\nKeine gespeicherten Daten gefunden.")
        antwort = input("Möchten Sie einen Beispiel-Studiengang erstellen? (j/n): ").strip().lower()
        
        if antwort == 'j':
            studiengang = erstelle_beispiel_studiengang()
            print("\n✓ Beispiel-Studiengang erstellt!")
            print("  → Basierend auf dem echten B.Sc. Cybersecurity Studienplan")
            print("  → Mit Ihren aktuellen Modulen und Noten")
        else:
            print("\nErstelle leeren Studiengang...")
            studiengang = Studiengang(
                name="Mein Studiengang",
                abschluss=Abschluss.BACHELOR,
                gesamtdauer=6,
                ziel_notendurchschnitt=2.5,
                ziel_abschlussdauer=6
            )
            print("✓ Leerer Studiengang erstellt!")
    
    # Dashboard und InputHandler initialisieren
    dashboard_view = DashboardView(studiengang)
    input_handler = InputHandler(studiengang, daten_manager, dashboard_view)
    
    # Anwendung starten
    input_handler.starten()
    
    # Beim Beenden fragen, ob gespeichert werden soll
    antwort = input("\nMöchten Sie die Änderungen speichern? (j/n): ").strip().lower()
    if antwort == 'j':
        daten_manager.speichere_studiengang(studiengang)
        print("✓ Daten gespeichert!")
    
    print("\n👋 Auf Wiedersehen!\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programm beendet.")
    except Exception as e:
        print(f"\n❌ Unerwarteter Fehler: {e}")
        import traceback
        traceback.print_exc()
