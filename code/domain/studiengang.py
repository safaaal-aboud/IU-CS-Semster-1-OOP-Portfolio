"""
Studiengang-Klasse für das Studien-Dashboard.

Diese Klasse repräsentiert einen Studiengang mit Semestern (Komposition).
"""

from datetime import date, timedelta
from typing import List
from .enums import Abschluss
from .semester import Semester
from .modul import Modul


class Studiengang:
    """
    Repräsentiert einen Studiengang.
    
    Attributes:
        _name: Der Name des Studiengangs
        _abschluss: Der Abschlusstyp (Bachelor, Master, Diplom)
        _gesamtdauer: Die Gesamtdauer in Semestern
        _ziel_notendurchschnitt: Der angestrebte Notendurchschnitt
        _ziel_abschlussdauer: Die angestrebte Abschlussdauer in Semestern
        _semester: Liste der Semester (Komposition)
    """
    
    def __init__(self, name: str, abschluss: Abschluss, gesamtdauer: int, 
                 ziel_notendurchschnitt: float, ziel_abschlussdauer: int):
        """
        Initialisiert einen neuen Studiengang.
        
        Die Semester werden automatisch erstellt (Komposition).
        
        Args:
            name: Der Name des Studiengangs
            abschluss: Der Abschlusstyp
            gesamtdauer: Die Gesamtdauer in Semestern
            ziel_notendurchschnitt: Der angestrebte Notendurchschnitt
            ziel_abschlussdauer: Die angestrebte Abschlussdauer
            
        Raises:
            ValueError: Wenn die Werte ungültig sind
        """
        self._name = name
        self._abschluss = abschluss
        self._gesamtdauer = gesamtdauer
        self._ziel_notendurchschnitt = ziel_notendurchschnitt
        self._ziel_abschlussdauer = ziel_abschlussdauer
        
        # Validierung
        if gesamtdauer < 1:
            raise ValueError("Gesamtdauer muss mindestens 1 Semester sein")
        if not 1.0 <= ziel_notendurchschnitt <= 4.0:
            raise ValueError("Ziel-Notendurchschnitt muss zwischen 1.0 und 4.0 liegen")
        if ziel_abschlussdauer < 1 or ziel_abschlussdauer > gesamtdauer:
            raise ValueError("Ziel-Abschlussdauer muss zwischen 1 und Gesamtdauer liegen")
        
        # Semester erstellen (Komposition)
        self._semester: List[Semester] = self.erstelle_semester()
    
    @property
    def name(self) -> str:
        """Getter für den Namen."""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """Setter für den Namen."""
        if not value:
            raise ValueError("Name darf nicht leer sein")
        self._name = value
    
    @property
    def abschluss(self) -> Abschluss:
        """Getter für den Abschluss."""
        return self._abschluss
    
    @abschluss.setter
    def abschluss(self, value: Abschluss):
        """Setter für den Abschluss."""
        self._abschluss = value
    
    @property
    def gesamtdauer(self) -> int:
        """Getter für die Gesamtdauer."""
        return self._gesamtdauer
    
    @gesamtdauer.setter
    def gesamtdauer(self, value: int):
        """Setter für die Gesamtdauer."""
        if value < 1:
            raise ValueError("Gesamtdauer muss mindestens 1 Semester sein")
        self._gesamtdauer = value
    
    @property
    def ziel_notendurchschnitt(self) -> float:
        """Getter für den Ziel-Notendurchschnitt."""
        return self._ziel_notendurchschnitt
    
    @ziel_notendurchschnitt.setter
    def ziel_notendurchschnitt(self, value: float):
        """Setter für den Ziel-Notendurchschnitt."""
        if not 1.0 <= value <= 4.0:
            raise ValueError("Ziel-Notendurchschnitt muss zwischen 1.0 und 4.0 liegen")
        self._ziel_notendurchschnitt = value
    
    @property
    def ziel_abschlussdauer(self) -> int:
        """Getter für die Ziel-Abschlussdauer."""
        return self._ziel_abschlussdauer
    
    @ziel_abschlussdauer.setter
    def ziel_abschlussdauer(self, value: int):
        """Setter für die Ziel-Abschlussdauer."""
        if value < 1 or value > self._gesamtdauer:
            raise ValueError("Ziel-Abschlussdauer muss zwischen 1 und Gesamtdauer liegen")
        self._ziel_abschlussdauer = value
    
    @property
    def semester(self) -> List[Semester]:
        """Getter für die Semester (gibt eine Kopie zurück)."""
        return self._semester.copy()
    
    def erstelle_semester(self) -> List[Semester]:
        """
        Erstellt die Semester für den Studiengang (Komposition).
        
        Die Semester werden automatisch mit sinnvollen Start- und Enddaten erstellt.
        
        Returns:
            Liste der erstellten Semester
        """
        semester_liste = []
        startdatum = date.today()
        
        for i in range(1, self._gesamtdauer + 1):
            # Semester dauert ca. 6 Monate
            enddatum = startdatum + timedelta(days=180)
            
            # Bezeichnung erstellen (WiSe/SoSe)
            if startdatum.month >= 10 or startdatum.month <= 3:
                bezeichnung = f"WiSe {startdatum.year}/{startdatum.year + 1}"
            else:
                bezeichnung = f"SoSe {startdatum.year}"
            
            semester = Semester(i, bezeichnung, startdatum, enddatum)
            semester_liste.append(semester)
            
            # Nächstes Semester startet einen Tag nach Ende des aktuellen
            startdatum = enddatum + timedelta(days=1)
        
        return semester_liste
    
    def hole_alle_modulen(self) -> List[Modul]:
        """
        Gibt alle Module aus allen Semestern zurück.
        
        Returns:
            Liste aller Module
        """
        alle_module = []
        for semester in self._semester:
            alle_module.extend(semester.hole_modulen())
        return alle_module
    
    def hole_abgeschlossene_modulen(self) -> List[Modul]:
        """
        Gibt alle abgeschlossenen Module zurück.
        
        Returns:
            Liste der abgeschlossenen Module
        """
        return [m for m in self.hole_alle_modulen() if m.ist_abgeschlossen()]
    
    def berechne_durchschnitt(self) -> float:
        """
        Berechnet den gewichteten Notendurchschnitt über alle bestandenen Module.
        
        Returns:
            Der gewichtete Notendurchschnitt oder 0.0 wenn keine Noten vorhanden
        """
        bestandene_module = [m for m in self.hole_alle_modulen() if m.ist_bestanden()]
        
        if not bestandene_module:
            return 0.0
        
        gewichtete_summe = sum(m.hole_note() * m.ects for m in bestandene_module if m.hole_note())
        gesamt_ects = sum(m.ects for m in bestandene_module)
        
        if gesamt_ects == 0:
            return 0.0
        
        return round(gewichtete_summe / gesamt_ects, 2)
    
    def berechne_fortschritt(self) -> float:
        """
        Berechnet den Studienfortschritt in Prozent basierend auf ECTS.
        
        Annahme: Ein Bachelor hat 180 ECTS, ein Master 120 ECTS.
        
        Returns:
            Der Fortschritt in Prozent (0.0 - 100.0)
        """
        # Gesamt-ECTS je nach Abschluss
        if self._abschluss == Abschluss.BACHELOR:
            gesamt_ects_ziel = 180
        elif self._abschluss == Abschluss.MASTER:
            gesamt_ects_ziel = 120
        else:  # DIPLOM
            gesamt_ects_ziel = 240
        
        # Erreichte ECTS aus bestandenen Modulen
        erreichte_ects = sum(m.ects for m in self.hole_alle_modulen() if m.ist_bestanden())
        
        fortschritt = (erreichte_ects / gesamt_ects_ziel) * 100
        return round(min(fortschritt, 100.0), 2)
    
    def berechne_verbleibende_ects(self) -> int:
        """
        Berechnet die verbleibenden ECTS bis zum Abschluss.
        
        Returns:
            Die Anzahl der verbleibenden ECTS
        """
        # Gesamt-ECTS je nach Abschluss
        if self._abschluss == Abschluss.BACHELOR:
            gesamt_ects_ziel = 180
        elif self._abschluss == Abschluss.MASTER:
            gesamt_ects_ziel = 120
        else:  # DIPLOM
            gesamt_ects_ziel = 240
        
        erreichte_ects = sum(m.ects for m in self.hole_alle_modulen() if m.ist_bestanden())
        return max(0, gesamt_ects_ziel - erreichte_ects)
    
    def __str__(self) -> str:
        """String-Repräsentation des Studiengangs."""
        return f"{self._name} ({self._abschluss.value}, {self._gesamtdauer} Semester)"
    
    def __repr__(self) -> str:
        """Repr-Repräsentation des Studiengangs."""
        return f"Studiengang(name='{self._name}', abschluss={self._abschluss}, gesamtdauer={self._gesamtdauer})"
