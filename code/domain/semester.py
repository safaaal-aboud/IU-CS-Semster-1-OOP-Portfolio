"""
Semester-Klasse für das Studien-Dashboard.

Diese Klasse repräsentiert ein Semester mit Modulen (Aggregation).
"""

from datetime import date
from typing import List
from .modul import Modul


class Semester:
    """
    Repräsentiert ein Semester im Studiengang.
    
    Attributes:
        _nummer: Die Semesternummer (1, 2, 3, ...)
        _bezeichnung: Die Bezeichnung (z.B. "WiSe 2024/25")
        _startdatum: Das Startdatum des Semesters
        _enddatum: Das Enddatum des Semesters
        _module: Liste der Module in diesem Semester (Aggregation)
    """
    
    def __init__(self, nummer: int, bezeichnung: str, startdatum: date, enddatum: date):
        """
        Initialisiert ein neues Semester.
        
        Args:
            nummer: Die Semesternummer
            bezeichnung: Die Bezeichnung des Semesters
            startdatum: Das Startdatum
            enddatum: Das Enddatum
            
        Raises:
            ValueError: Wenn die Nummer ungültig ist oder Enddatum vor Startdatum liegt
        """
        self._nummer = nummer
        self._bezeichnung = bezeichnung
        self._startdatum = startdatum
        self._enddatum = enddatum
        self._module: List[Modul] = []
        
        # Validierung
        if nummer < 1:
            raise ValueError("Semesternummer muss mindestens 1 sein")
        if enddatum < startdatum:
            raise ValueError("Enddatum muss nach Startdatum liegen")
    
    @property
    def nummer(self) -> int:
        """Getter für die Semesternummer."""
        return self._nummer
    
    @nummer.setter
    def nummer(self, value: int):
        """Setter für die Semesternummer mit Validierung."""
        if value < 1:
            raise ValueError("Semesternummer muss mindestens 1 sein")
        self._nummer = value
    
    @property
    def bezeichnung(self) -> str:
        """Getter für die Bezeichnung."""
        return self._bezeichnung
    
    @bezeichnung.setter
    def bezeichnung(self, value: str):
        """Setter für die Bezeichnung."""
        if not value:
            raise ValueError("Bezeichnung darf nicht leer sein")
        self._bezeichnung = value
    
    @property
    def startdatum(self) -> date:
        """Getter für das Startdatum."""
        return self._startdatum
    
    @startdatum.setter
    def startdatum(self, value: date):
        """Setter für das Startdatum."""
        if self._enddatum and value >= self._enddatum:
            raise ValueError("Startdatum muss vor Enddatum liegen")
        self._startdatum = value
    
    @property
    def enddatum(self) -> date:
        """Getter für das Enddatum."""
        return self._enddatum
    
    @enddatum.setter
    def enddatum(self, value: date):
        """Setter für das Enddatum."""
        if value <= self._startdatum:
            raise ValueError("Enddatum muss nach Startdatum liegen")
        self._enddatum = value
    
    @property
    def module(self) -> List[Modul]:
        """Getter für die Module (gibt eine Kopie zurück)."""
        return self._module.copy()
    
    def fuege_modul_hinzu(self, modul: Modul) -> None:
        """
        Fügt ein Modul zum Semester hinzu (Aggregation).
        
        Das Modul existiert unabhängig vom Semester und kann
        zwischen Semestern verschoben werden.
        
        Args:
            modul: Das hinzuzufügende Modul
            
        Raises:
            ValueError: Wenn das Modul bereits im Semester ist
        """
        if modul in self._module:
            raise ValueError(f"Modul {modul.name} ist bereits im Semester")
        self._module.append(modul)
    
    def entferne_modul(self, modul: Modul) -> None:
        """
        Entfernt ein Modul aus dem Semester.
        
        Das Modul wird nur aus der Liste entfernt, existiert aber weiterhin.
        Dies demonstriert die Aggregation.
        
        Args:
            modul: Das zu entfernende Modul
            
        Raises:
            ValueError: Wenn das Modul nicht im Semester ist
        """
        if modul not in self._module:
            raise ValueError(f"Modul {modul.name} ist nicht im Semester")
        self._module.remove(modul)
    
    def hole_modulen(self) -> List[Modul]:
        """
        Gibt alle Module des Semesters zurück.
        
        Returns:
            Liste aller Module
        """
        return self._module.copy()
    
    def berechne_semester_durchschnitt(self) -> float:
        """
        Berechnet den Notendurchschnitt des Semesters.
        
        Returns:
            Der gewichtete Notendurchschnitt oder 0.0 wenn keine Noten vorhanden
        """
        bestandene_module = [m for m in self._module if m.ist_bestanden()]
        
        if not bestandene_module:
            return 0.0
        
        gewichtete_summe = sum(m.hole_note() * m.ects for m in bestandene_module if m.hole_note())
        gesamt_ects = sum(m.ects for m in bestandene_module)
        
        if gesamt_ects == 0:
            return 0.0
        
        return round(gewichtete_summe / gesamt_ects, 2)
    
    def ist_aktuell(self) -> bool:
        """
        Prüft, ob das Semester aktuell läuft.
        
        Returns:
            True wenn das aktuelle Datum zwischen Start- und Enddatum liegt
        """
        heute = date.today()
        return self._startdatum <= heute <= self._enddatum
    
    def anzahl_module(self) -> int:
        """
        Gibt die Anzahl der Module im Semester zurück.
        
        Returns:
            Die Anzahl der Module
        """
        return len(self._module)
    
    def __str__(self) -> str:
        """String-Repräsentation des Semesters."""
        return f"Semester {self._nummer}: {self._bezeichnung} ({self.anzahl_module()} Module)"
    
    def __repr__(self) -> str:
        """Repr-Repräsentation des Semesters."""
        return f"Semester(nummer={self._nummer}, bezeichnung='{self._bezeichnung}', startdatum={self._startdatum}, enddatum={self._enddatum})"
