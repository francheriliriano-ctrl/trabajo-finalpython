"""Módulo personalizado con funciones de ayuda."""

import json

def cargar_tareas(ruta):
    """Carga tareas desde un archivo JSON."""
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def mostrar_tareas(tareas):
    """Imprime las tareas cargadas."""
    for t in tareas:
        print(f"- {t['titulo']}: {t['descripcion']}")
