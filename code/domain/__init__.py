"""
Domain-Paket für das Studien-Dashboard.

Dieses Paket enthält alle Domänenklassen (Anwendungslogik).
"""

from .studiengang import Studiengang
from .semester import Semester
from .modul import Modul
from .pruefungsleistung import Pruefungsleistung
from .enums import Abschluss, Pruefungsart, ModulStatus

__all__ = [
    'Studiengang',
    'Semester',
    'Modul',
    'Pruefungsleistung',
    'Abschluss',
    'Pruefungsart',
    'ModulStatus'
]
