"""
Modul-Klasse für das Studien-Dashboard.

Diese Klasse repräsentiert ein Studienmodul mit allen relevanten Informationen.
"""

from typing import Optional
from .enums import ModulStatus, Pruefungsart
from .pruefungsleistung import Pruefungsleistung


class Modul:
    """
    Repräsentiert ein Studienmodul.
    
    Attributes:
        _modulcode: Der eindeutige Code des Moduls
        _name: Der Name des Moduls
        _ects: Die Anzahl der ECTS-Punkte
        _semester_empfehlung: Das empfohlene Semester
        _status: Der aktuelle Status des Moduls
        _pruefungsleistung: Die zugehörige Prüfungsleistung (optional)
    """
    
    def __init__(self, modulcode: str, name: str, ects: int, semester_empfehlung: int):
        """
        Initialisiert ein neues Modul.
        
        Args:
            modulcode: Der eindeutige Code des Moduls
            name: Der Name des Moduls
            ects: Die Anzahl der ECTS-Punkte
            semester_empfehlung: Das empfohlene Semester
            
        Raises:
            ValueError: Wenn ECTS oder Semester-Empfehlung ungültig sind
        """
        self._modulcode = modulcode
        self._name = name
        self._ects = ects
        self._semester_empfehlung = semester_empfehlung
        self._status = ModulStatus.OFFEN
        self._pruefungsleistung: Optional[Pruefungsleistung] = None
        
        # Validierung
        if ects <= 0:
            raise ValueError("ECTS müssen größer als 0 sein")
        if semester_empfehlung < 1:
            raise ValueError("Semester-Empfehlung muss mindestens 1 sein")
    
    @property
    def modulcode(self) -> str:
        """Getter für den Modulcode."""
        return self._modulcode
    
    @modulcode.setter
    def modulcode(self, value: str):
        """Setter für den Modulcode."""
        if not value:
            raise ValueError("Modulcode darf nicht leer sein")
        self._modulcode = value
    
    @property
    def name(self) -> str:
        """Getter für den Modulnamen."""
        return self._name
    
    @name.setter
    def name(self, value: str):
        """
        Setter für den Modulnamen mit Validierung.
        
        Args:
            value: Der neue Name
            
        Raises:
            ValueError: Wenn der Name leer ist
        """
        if not value:
            raise ValueError("Der Name darf nicht leer sein")
        self._name = value
    
    @property
    def ects(self) -> int:
        """Getter für die ECTS-Punkte."""
        return self._ects
    
    @ects.setter
    def ects(self, value: int):
        """
        Setter für die ECTS-Punkte mit Validierung.
        
        Args:
            value: Die neuen ECTS-Punkte
            
        Raises:
            ValueError: Wenn ECTS <= 0
        """
        if value <= 0:
            raise ValueError("ECTS müssen größer als 0 sein")
        self._ects = value
    
    @property
    def semester_empfehlung(self) -> int:
        """Getter für die Semester-Empfehlung."""
        return self._semester_empfehlung
    
    @semester_empfehlung.setter
    def semester_empfehlung(self, value: int):
        """
        Setter für die Semester-Empfehlung mit Validierung.
        
        Args:
            value: Die neue Semester-Empfehlung
            
        Raises:
            ValueError: Wenn Semester-Empfehlung < 1
        """
        if value < 1:
            raise ValueError("Semester-Empfehlung muss mindestens 1 sein")
        self._semester_empfehlung = value
    
    @property
    def status(self) -> ModulStatus:
        """Getter für den Modulstatus."""
        return self._status
    
    @status.setter
    def status(self, value: ModulStatus):
        """Setter für den Modulstatus."""
        self._status = value
    
    @property
    def pruefungsleistung(self) -> Optional[Pruefungsleistung]:
        """Getter für die Prüfungsleistung."""
        return self._pruefungsleistung
    
    def setze_pruefungsleistung(self, pruefungsleistung: Pruefungsleistung) -> None:
        """
        Setzt die Prüfungsleistung für dieses Modul (Komposition).
        
        Args:
            pruefungsleistung: Die Prüfungsleistung
        """
        self._pruefungsleistung = pruefungsleistung
        # Status automatisch aktualisieren
        if pruefungsleistung.ist_bestanden():
            self._status = ModulStatus.BESTANDEN
        else:
            self._status = ModulStatus.NICHT_BESTANDEN
    
    def hole_pruefungsleistung(self) -> Optional[Pruefungsleistung]:
        """
        Gibt die Prüfungsleistung zurück.
        
        Returns:
            Die Prüfungsleistung oder None
        """
        return self._pruefungsleistung
    
    def ist_bestanden(self) -> bool:
        """
        Prüft, ob das Modul bestanden wurde.
        
        Returns:
            True wenn das Modul bestanden wurde, sonst False
        """
        return self._status == ModulStatus.BESTANDEN
    
    def ist_abgeschlossen(self) -> bool:
        """
        Prüft, ob das Modul abgeschlossen ist (bestanden oder nicht bestanden).
        
        Returns:
            True wenn das Modul abgeschlossen ist, sonst False
        """
        return self._status in [ModulStatus.BESTANDEN, ModulStatus.NICHT_BESTANDEN]
    
    def hole_note(self) -> Optional[float]:
        """
        Gibt die Note des Moduls zurück.
        
        Returns:
            Die Note oder None wenn keine Prüfungsleistung vorhanden ist
        """
        if self._pruefungsleistung:
            return self._pruefungsleistung.hole_note()
        return None
    
    def __str__(self) -> str:
        """String-Repräsentation des Moduls."""
        status_str = f", Status: {self._status.value}"
        note_str = f", Note: {self.hole_note()}" if self.hole_note() else ""
        return f"{self._modulcode}: {self._name} ({self._ects} ECTS){status_str}{note_str}"
    
    def __repr__(self) -> str:
        """Repr-Repräsentation des Moduls."""
        return f"Modul(modulcode='{self._modulcode}', name='{self._name}', ects={self._ects}, semester_empfehlung={self._semester_empfehlung})"
