"""
Prüfungsleistung-Klasse für das Studien-Dashboard.

Diese Klasse repräsentiert eine Prüfungsleistung mit Note, Datum, Versuch und Art.
"""

from datetime import date
from .enums import Pruefungsart


class Pruefungsleistung:
    """
    Repräsentiert eine Prüfungsleistung eines Moduls.
    
    Attributes:
        _note: Die erreichte Note (1.0 - 5.0)
        _datum: Das Datum der Prüfung
        _versuch: Der Versuch (1, 2, 3, ...)
        _art: Die Art der Prüfung (aus Pruefungsart Enum)
    """
    
    def __init__(self, note: float, datum: date, versuch: int, art: Pruefungsart):
        """
        Initialisiert eine neue Prüfungsleistung.
        
        Args:
            note: Die erreichte Note (1.0 - 5.0)
            datum: Das Datum der Prüfung
            versuch: Der Versuch (1, 2, 3, ...)
            art: Die Art der Prüfung
            
        Raises:
            ValueError: Wenn die Note außerhalb des gültigen Bereichs liegt
            ValueError: Wenn der Versuch kleiner als 1 ist
        """
        self._note = note
        self._datum = datum
        self._versuch = versuch
        self._art = art
        
        # Validierung
        if not 1.0 <= note <= 5.0:
            raise ValueError("Note muss zwischen 1.0 und 5.0 liegen")
        if versuch < 1:
            raise ValueError("Versuch muss mindestens 1 sein")
    
    @property
    def note(self) -> float:
        """Getter für die Note."""
        return self._note
    
    @note.setter
    def note(self, value: float):
        """
        Setter für die Note mit Validierung.
        
        Args:
            value: Die neue Note
            
        Raises:
            ValueError: Wenn die Note außerhalb des gültigen Bereichs liegt
        """
        if not 1.0 <= value <= 5.0:
            raise ValueError("Note muss zwischen 1.0 und 5.0 liegen")
        self._note = value
    
    @property
    def datum(self) -> date:
        """Getter für das Datum."""
        return self._datum
    
    @datum.setter
    def datum(self, value: date):
        """Setter für das Datum."""
        self._datum = value
    
    @property
    def versuch(self) -> int:
        """Getter für den Versuch."""
        return self._versuch
    
    @versuch.setter
    def versuch(self, value: int):
        """
        Setter für den Versuch mit Validierung.
        
        Args:
            value: Der neue Versuch
            
        Raises:
            ValueError: Wenn der Versuch kleiner als 1 ist
        """
        if value < 1:
            raise ValueError("Versuch muss mindestens 1 sein")
        self._versuch = value
    
    @property
    def art(self) -> Pruefungsart:
        """Getter für die Prüfungsart."""
        return self._art
    
    @art.setter
    def art(self, value: Pruefungsart):
        """Setter für die Prüfungsart."""
        self._art = value
    
    def ist_bestanden(self) -> bool:
        """
        Prüft, ob die Prüfungsleistung bestanden wurde.
        
        Returns:
            True wenn die Note 4.0 oder besser ist, sonst False
        """
        return self._note <= 4.0
    
    def hole_note(self) -> float:
        """
        Gibt die Note zurück.
        
        Returns:
            Die Note als float
        """
        return self._note
    
    def hole_bewertung(self) -> str:
        """
        Gibt eine textuelle Bewertung der Note zurück.
        
        Returns:
            Eine Bewertung wie "Sehr gut", "Gut", etc.
        """
        if self._note <= 1.5:
            return "Sehr gut"
        elif self._note <= 2.5:
            return "Gut"
        elif self._note <= 3.5:
            return "Befriedigend"
        elif self._note <= 4.0:
            return "Ausreichend"
        else:
            return "Nicht bestanden"
    
    def __str__(self) -> str:
        """String-Repräsentation der Prüfungsleistung."""
        return f"Prüfungsleistung: {self._art.value}, Note: {self._note}, Datum: {self._datum}, Versuch: {self._versuch}"
    
    def __repr__(self) -> str:
        """Repr-Repräsentation der Prüfungsleistung."""
        return f"Pruefungsleistung(note={self._note}, datum={self._datum}, versuch={self._versuch}, art={self._art})"
