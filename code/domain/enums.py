"""
Enumerationen für das Studien-Dashboard.

Dieses Modul enthält alle Enum-Klassen, die im Domain-Modell verwendet werden.
"""

from enum import Enum


class Abschluss(Enum):
    """Enum für Studienabschlüsse."""
    BACHELOR = "Bachelor"
    MASTER = "Master"
    DIPLOM = "Diplom"


class Pruefungsart(Enum):
    """Enum für verschiedene Prüfungsarten."""
    KLAUSUR = "Klausur"
    HAUSARBEIT = "Hausarbeit"
    PORTFOLIO = "Portfolio"
    PROJEKTARBEIT = "Projektarbeit"
    MUENDLICH = "Mündliche Prüfung"
    ADVANCED_WORKBOOK = "Advanced Workbook"
    FALLSTUDIE = "Fallstudie"
    GRUPPENPRAESENTATION = "Gruppenpräsentation"
    PROJEKTBERICHT = "Projektbericht"
    SEMINARARBEIT = "Seminararbeit"
    PRAKTIKUM = "Praktikum"


class ModulStatus(Enum):
    """Enum für den Status eines Moduls."""
    OFFEN = "Offen"
    ANGEMELDET = "Angemeldet"
    BESTANDEN = "Bestanden"
    NICHT_BESTANDEN = "Nicht bestanden"
