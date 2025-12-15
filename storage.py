"""
Módulo de persistencia de datos en JSON.
"""

import json
from pathlib import Path

DATA_FILE = Path("tareas.json")


def load_data() -> list:
    """Carga las tareas desde el archivo."""
    if not DATA_FILE.exists():
        DATA_FILE.write_text("[]")
    return json.loads(DATA_FILE.read_text())


def save_data(tareas: list) -> None:
    """Guarda las tareas en el archivo."""
    DATA_FILE.write_text(json.dumps(tareas, indent=4))
