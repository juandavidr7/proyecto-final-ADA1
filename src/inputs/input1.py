import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from clases import Jugador

def obtener_datos():
    # Jugadores
    j1 = Jugador(1, "Juan", 20, 94)
    j2 = Jugador(2, "Maria", 21, 94)
    j3 = Jugador(3, "Pedro", 22, 21)
    j4 = Jugador(4, "Ana", 23, 25)
    j5 = Jugador(5, "Carlos", 24, 66)
    j6 = Jugador(6, "Laura", 25, 52)
    j7 = Jugador(7, "Jose", 26, 48)
    j8 = Jugador(8, "Luis", 27, 73)
    j9 = Jugador(9, "Sara", 28, 92)
    j10 = Jugador(10, "Jorge", 29, 51)
    j11 = Jugador(11, "Lorena", 30, 90)
    j12 = Jugador(12, "Raul", 31, 100)

    datos = [
        {
            "nombre": "Sede Cali",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j1, j2, j3]},
                {"nombre": "Volleyball", "deporte": "Volleyball", "jugadores": [j4, j5, j6]}
            ]
        },
        {
            "nombre": "Sede Medellin",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j7, j8, j9]},
                {"nombre": "Volleyball", "deporte": "Volleyball", "jugadores": [j10, j11, j12]}
            ]
        }
    ]
    return datos
