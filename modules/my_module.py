"""
Módulo de funciones auxiliares
Materia: Programación
Alumno: Francheri Liriano Rosario
"""

import datetime


def validar_texto(texto):
    """
    Valida que el texto no esté vacío
    """
    if not texto or texto.strip() == "":
        return False
    return True


def validar_numero(numero):
    """
    Valida que el valor ingresado sea numérico
    """
    try:
        int(numero)
        return True
    except ValueError:
        return False


def obtener_fecha_actual():
    """
    Devuelve la fecha y hora actual
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def escribir_log(mensaje, archivo="logs.txt"):
    """
    Guarda un mensaje en un archivo de logs
    """
    fecha = obtener_fecha_actual()
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"[{fecha}] {mensaje}\n")

