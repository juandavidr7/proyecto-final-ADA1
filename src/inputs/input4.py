import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clases import Jugador

def obtener_datos():
    # Input 4: Caso grande con 4 sedes
    j1 = Jugador(1, "Carlos Mendez", 22, 75)
    j2 = Jugador(2, "Ana Rodriguez", 25, 88)
    j3 = Jugador(3, "Luis Garcia", 19, 42)
    j4 = Jugador(4, "Maria Lopez", 28, 91)
    j5 = Jugador(5, "Pedro Sanchez", 23, 63)
    j6 = Jugador(6, "Laura Martinez", 21, 55)
    j7 = Jugador(7, "Jorge Hernandez", 26, 79)
    j8 = Jugador(8, "Sofia Diaz", 24, 67)
    j9 = Jugador(9, "Diego Torres", 20, 48)
    j10 = Jugador(10, "Valentina Ruiz", 27, 85)
    j11 = Jugador(11, "Andres Vargas", 22, 72)
    j12 = Jugador(12, "Camila Ortiz", 25, 94)
    j13 = Jugador(13, "Felipe Castro", 29, 38)
    j14 = Jugador(14, "Isabella Gomez", 21, 81)
    j15 = Jugador(15, "Sebastian Perez", 24, 59)
    j16 = Jugador(16, "Daniela Morales", 23, 77)

    datos = [
        {
            "nombre": "Sede Bogota",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j1, j2, j3, j4]},
                {"nombre": "Basketball", "deporte": "Basketball", "jugadores": [j5, j6]}
            ]
        },
        {
            "nombre": "Sede Medellin",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j7, j8]},
                {"nombre": "Basketball", "deporte": "Basketball", "jugadores": [j9, j10, j11]}
            ]
        },
        {
            "nombre": "Sede Cali",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j12, j13, j14]},
                {"nombre": "Basketball", "deporte": "Basketball", "jugadores": [j15, j16]}
            ]
        },
        {
            "nombre": "Sede Barranquilla",
            "equipos": [
                {"nombre": "Natacion", "deporte": "Natacion", "jugadores": [j1, j5, j9, j13]},
                {"nombre": "Tenis", "deporte": "Tenis", "jugadores": [j2, j6, j10, j14]}
            ]
        }
    ]
    return datos
