"""
DatenManager-Klasse für die Persistierung von Daten.

Diese Klasse ist verantwortlich für das Speichern und Laden von Studiengang-Daten.
"""

import pickle
import csv
import os
from typing import Optional
from datetime import date


class DatenManager:
    """
    Verwaltet die Persistierung von Studiengang-Daten.
    
    Attributes:
        _datei_pfad: Der Pfad zur Datei für die Persistierung
    """
    
    def __init__(self, datei_pfad: str = "studiengang.pkl"):
        """
        Initialisiert den DatenManager.
        
        Args:
            datei_pfad: Der Pfad zur Datei (Standard: studiengang.pkl)
        """
        self._datei_pfad = datei_pfad
    
    @property
    def datei_pfad(self) -> str:
        """Getter für den Dateipfad."""
        return self._datei_pfad
    
    @datei_pfad.setter
    def datei_pfad(self, value: str):
        """Setter für den Dateipfad."""
        if not value:
            raise ValueError("Dateipfad darf nicht leer sein")
        self._datei_pfad = value
    
    def speichere_studiengang(self, studiengang) -> None:
        """
        Speichert einen Studiengang in einer Datei (Pickle).
        
        Args:
            studiengang: Der zu speichernde Studiengang
            
        Raises:
            IOError: Wenn das Speichern fehlschlägt
        """
        try:
            with open(self._datei_pfad, 'wb') as datei:
                pickle.dump(studiengang, datei)
            print(f"✓ Studiengang erfolgreich gespeichert in: {self._datei_pfad}")
        except Exception as e:
            raise IOError(f"Fehler beim Speichern: {e}")
    
    def lade_studiengang(self):
        """
        Lädt einen Studiengang aus einer Datei.
        
        Returns:
            Der geladene Studiengang oder None wenn die Datei nicht existiert
            
        Raises:
            IOError: Wenn das Laden fehlschlägt
        """
        if not os.path.exists(self._datei_pfad):
            print(f"ℹ Keine gespeicherten Daten gefunden: {self._datei_pfad}")
            return None
        
        try:
            with open(self._datei_pfad, 'rb') as datei:
                studiengang = pickle.load(datei)
            print(f"✓ Studiengang erfolgreich geladen aus: {self._datei_pfad}")
            return studiengang
        except Exception as e:
            raise IOError(f"Fehler beim Laden: {e}")
    
    def exportiere_csv(self, studiengang) -> None:
        """
        Exportiert die Modul-Daten eines Studiengangs in eine CSV-Datei.
        
        Args:
            studiengang: Der Studiengang dessen Daten exportiert werden sollen
            
        Raises:
            IOError: Wenn der Export fehlschlägt
        """
        csv_pfad = self._datei_pfad.replace('.pkl', '.csv')
        
        try:
            with open(csv_pfad, 'w', newline='', encoding='utf-8') as datei:
                writer = csv.writer(datei, delimiter=';')
                
                # Header
                writer.writerow([
                    'Semester',
                    'Modulcode',
                    'Modulname',
                    'ECTS',
                    'Status',
                    'Note',
                    'Prüfungsart',
                    'Prüfungsdatum',
                    'Versuch'
                ])
                
                # Daten
                for semester in studiengang.semester:
                    for modul in semester.hole_modulen():
                        pruefung = modul.hole_pruefungsleistung()
                        
                        row = [
                            f"Semester {semester.nummer}",
                            modul.modulcode,
                            modul.name,
                            modul.ects,
                            modul.status.value,
                            pruefung.note if pruefung else '',
                            pruefung.art.value if pruefung else '',
                            pruefung.datum if pruefung else '',
                            pruefung.versuch if pruefung else ''
                        ]
                        writer.writerow(row)
            
            print(f"✓ Daten erfolgreich exportiert nach: {csv_pfad}")
        except Exception as e:
            raise IOError(f"Fehler beim CSV-Export: {e}")
    
    def datei_existiert(self) -> bool:
        """
        Prüft, ob die Datei existiert.
        
        Returns:
            True wenn die Datei existiert, sonst False
        """
        return os.path.exists(self._datei_pfad)
    
    def loesche_datei(self) -> None:
        """
        Löscht die gespeicherte Datei.
        
        Raises:
            IOError: Wenn das Löschen fehlschlägt
        """
        if self.datei_existiert():
            try:
                os.remove(self._datei_pfad)
                print(f"✓ Datei erfolgreich gelöscht: {self._datei_pfad}")
            except Exception as e:
                raise IOError(f"Fehler beim Löschen: {e}")
        else:
            print(f"ℹ Keine Datei zum Löschen gefunden: {self._datei_pfad}")
