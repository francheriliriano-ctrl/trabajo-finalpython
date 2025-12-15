"""
Trabajo Final
Aplica PEP8, PEP257 y Zen of Python.
"""

import typer
from rich.console import Console
from rich.table import Table

from storage import load_data, save_data

app = typer.Typer()
console = Console()


@app.command()
def agregar(tarea: str) -> None:
    """Agrega una nueva tarea."""
    tareas = load_data()
    tareas.append({"tarea": tarea, "hecha": False})
    save_data(tareas)
    console.print("Tarea agregada correctamente")


@app.command()
def listar() -> None:
    """Lista todas las tareas."""
    tareas = load_data()
    tabla = Table(title="Lista de Tareas")

    tabla.add_column("ID")
    tabla.add_column("Tarea")
    tabla.add_column("Estado")

    for i, t in enumerate(tareas):
        estado = "✔" if t["hecha"] else "Pendiente"
        tabla.add_row(str(i), t["tarea"], estado)

    console.print(tabla)


@app.command()
def completar(id: int) -> None:
    """Marca una tarea como completada."""
    tareas = load_data()
    try:
        tareas[id]["hecha"] = True
        save_data(tareas)
        console.print("Tarea completada")
    except IndexError:
        console.print("ID inexistente")


if __name__ == "__main__":
    app()
