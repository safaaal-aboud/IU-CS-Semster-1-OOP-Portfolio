"""
DashboardView-Klasse für die Visualisierung des Dashboards.

Diese Klasse ist verantwortlich für die Darstellung des Studien-Dashboards.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain import Studiengang


class DashboardView:
    """
    Visualisiert das Studien-Dashboard.
    
    Attributes:
        _studiengang: Der anzuzeigende Studiengang
    """
    
    def __init__(self, studiengang: 'Studiengang'):
        """
        Initialisiert die DashboardView.
        
        Args:
            studiengang: Der Studiengang der angezeigt werden soll
        """
        self._studiengang = studiengang
    
    @property
    def studiengang(self) -> 'Studiengang':
        """Getter für den Studiengang."""
        return self._studiengang
    
    @studiengang.setter
    def studiengang(self, value: 'Studiengang'):
        """Setter für den Studiengang."""
        self._studiengang = value
    
    def zeige_dashboard(self) -> None:
        """Zeigt das komplette Dashboard an."""
        self.zeige_header()
        print()
        self.zeige_studienfortschritt()
        print()
        self.zeige_notendurchschnitt()
        print()
        self.zeige_quartal_uebersicht()
        print()
        self.zeige_modul_uebersicht()
    
    def zeige_header(self) -> None:
        """Zeigt den Header des Dashboards an."""
        print("=" * 80)
        print(f"  STUDIEN-DASHBOARD: {self._studiengang.name}")
        print(f"  Abschluss: {self._studiengang.abschluss.value}")
        print("=" * 80)
    
    def zeige_studienfortschritt(self) -> None:
        """Zeigt den Studienfortschritt an."""
        fortschritt = self._studiengang.berechne_fortschritt()
        verbleibende_ects = self._studiengang.berechne_verbleibende_ects()
        
        print("📊 STUDIENFORTSCHRITT")
        print("-" * 80)
        print(f"  Fortschritt: {fortschritt}%")
        
        # Fortschrittsbalken
        balken_laenge = 50
        gefuellt = int((fortschritt / 100) * balken_laenge)
        balken = "█" * gefuellt + "░" * (balken_laenge - gefuellt)
        print(f"  [{balken}]")
        
        print(f"  Verbleibende ECTS: {verbleibende_ects}")
    
    def zeige_notendurchschnitt(self) -> None:
        """Zeigt den Notendurchschnitt an."""
        durchschnitt = self._studiengang.berechne_durchschnitt()
        ziel = self._studiengang.ziel_notendurchschnitt
        
        print("📈 NOTENDURCHSCHNITT")
        print("-" * 80)
        print(f"  Aktueller Durchschnitt: {durchschnitt:.2f}")
        print(f"  Ziel-Durchschnitt: {ziel:.2f}")
        
        if durchschnitt > 0:
            if durchschnitt <= ziel:
                print(f"  Status: ✓ Ziel erreicht! (Differenz: {abs(durchschnitt - ziel):.2f})")
            else:
                print(f"  Status: ⚠ Ziel noch nicht erreicht (Differenz: {abs(durchschnitt - ziel):.2f})")
        else:
            print("  Status: Noch keine Noten vorhanden")
    
    def zeige_quartal_uebersicht(self) -> None:
        """Zeigt eine Übersicht der Semester/Quartale an."""
        print("📅 SEMESTER-ÜBERSICHT")
        print("-" * 80)
        
        for semester in self._studiengang.semester:
            anzahl_module = semester.anzahl_module()
            bestandene = sum(1 for m in semester.hole_modulen() if m.ist_bestanden())
            durchschnitt = semester.berechne_semester_durchschnitt()
            
            status_icon = "🟢" if semester.ist_aktuell() else "⚪"
            
            print(f"  {status_icon} Semester {semester.nummer}: {semester.bezeichnung}")
            print(f"     Module: {bestandene}/{anzahl_module} bestanden", end="")
            if durchschnitt > 0:
                print(f" | Durchschnitt: {durchschnitt:.2f}")
            else:
                print()
    
    def zeige_modul_uebersicht(self) -> None:
        """Zeigt eine detaillierte Modul-Übersicht an."""
        print("📚 MODUL-ÜBERSICHT")
        print("-" * 80)
        
        alle_module = self._studiengang.hole_alle_modulen()
        
        if not alle_module:
            print("  Noch keine Module vorhanden.")
            return
        
        # Gruppierung nach Status
        from domain.enums import ModulStatus
        
        for status in ModulStatus:
            module_mit_status = [m for m in alle_module if m.status == status]
            
            if module_mit_status:
                print(f"\n  {status.value}:")
                for modul in module_mit_status:
                    note_str = f" - Note: {modul.hole_note():.2f}" if modul.hole_note() else ""
                    print(f"    • {modul.modulcode}: {modul.name} ({modul.ects} ECTS){note_str}")
