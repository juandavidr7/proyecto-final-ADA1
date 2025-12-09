import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from clases import Jugador

def obtener_datos():
    # Jugadores
    j1 = Jugador(1, "Sofia Garcia", 21, 66)
    j2 = Jugador(2, "Alejandro Torres", 27, 24)
    j3 = Jugador(3, "Valentina Rodriguez", 19, 15)
    j4 = Jugador(4, "Juan Lopez", 22, 78)
    j5 = Jugador(5, "Martina Martinez", 30, 55)
    j6 = Jugador(6, "Sebastian Perez", 25, 42)
    j7 = Jugador(7, "Camila Fernandez", 24, 36)
    j8 = Jugador(8, "Mateo Gonzalez", 29, 89)
    j9 = Jugador(9, "Isabella Diaz", 40, 92)
    j10 = Jugador(10, "Daniel Ruiz", 17, 57)
    j11 = Jugador(11, "Luciana Sanchez", 18, 89)
    j12 = Jugador(12, "Lucas Vasquez", 26, 82)
    j13 = Jugador(13, "william hernandez", 30, 44)
    j14 = Jugador(14, "Laura Perez", 20, 78)
    j15 = Jugador(15, "Santiago Rodriguez", 23, 32)
    j16 = Jugador(16, "Maria Gonzalez", 28, 65)
    j17 = Jugador(17, "Carlos Lopez", 19, 72)
    j18 = Jugador(18, "Valeria Martinez", 21, 45)
    j19 = Jugador(19, "Andres Perez", 30, 78)
    j20 = Jugador(20, "Sara Hernandez", 22, 56)

    datos = [
        {
            "nombre": "Sede Cali",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j10, j2]},
                {"nombre": "Volleyball", "deporte": "Volleyball", "jugadores": [j1, j9, j12, j6]},
                {"nombre": "Basketball", "deporte": "Basketball", "jugadores": [j13, j14, j15, j16]}
            ]
        },
        {
            "nombre": "Sede Medellin",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j11, j8, j7]},
                {"nombre": "Volleyball", "deporte": "Volleyball", "jugadores": [j3, j4, j5]},
                {"nombre": "Basketball", "deporte": "Basketball", "jugadores": [j17, j18, j19, j20]}
            ]
        }
    ]
    return datos
