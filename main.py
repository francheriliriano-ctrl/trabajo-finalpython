"""Programa principal de gestión de tareas.
Cumple PEP8, PEP257 y usa módulos propios.
"""

from modules.my_module import cargar_tareas, mostrar_tareas

def main():
    """Función principal del programa."""
    tareas = cargar_tareas("data/tasks.json")
    mostrar_tareas(tareas)

if __name__ == "__main__":
    main()
