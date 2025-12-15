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
from my_module import validar_texto, escribir_log

nombre = input("Ingrese su nombre: ")

if validar_texto(nombre):
    escribir_log(f"Nombre ingresado: {nombre}")
    print("Dato válido")
else:
    print("Dato inválido")
