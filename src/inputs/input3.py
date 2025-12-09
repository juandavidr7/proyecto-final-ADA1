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
    j21 = Jugador(21, "Diego Castro", 23, 67)
    j22 = Jugador(22, "Gabriela Ramos", 24, 43)
    j23 = Jugador(23, "Adrian Torres", 22, 15)
    j24 = Jugador(24, "Natalia Gomez", 21, 39)
    j25 = Jugador(25, "Ivan Vargas", 29, 84)
    j26 = Jugador(26, "Fernanda Ortiz", 26, 33)
    j27 = Jugador(27, "Pablo Ramirez", 27, 65)
    j28 = Jugador(28, "Julia Sanchez", 28, 79)
    j29 = Jugador(29, "Ricardo Ruiz", 30, 52)
    j30 = Jugador(30, "Victoria Leon", 25, 59)
    j31 = Jugador(31, "Emilio Molina", 19, 46)
    j32 = Jugador(32, "Andrea Herrera", 20, 75)
    j33 = Jugador(33, "Leonardo Delgado", 22, 54)
    j34 = Jugador(34, "Rosa Moreno", 23, 68)
    j35 = Jugador(35, "Oscar Gutierrez", 26, 60)
    j36 = Jugador(36, "Daniela Romero", 24, 58)
    j37 = Jugador(37, "Miguel Diaz", 21, 77)
    j38 = Jugador(38, "Lucia Alvarez", 19, 49)
    j39 = Jugador(39, "Rodrigo Martinez", 28, 63)
    j40 = Jugador(40, "Elena Cruz", 27, 41)
    j41 = Jugador(41, "Manuel Silva", 23, 61)
    j42 = Jugador(42, "Paula Garcia", 28, 88)
    j43 = Jugador(43, "Jorge Torres", 27, 47)
    j44 = Jugador(44, "Carolina Ramirez", 25, 69)
    j45 = Jugador(45, "Martin Fernandez", 21, 83)
    j46 = Jugador(46, "Sofia Ruiz", 39, 34)
    j47 = Jugador(47, "Antonio Vasquez", 28, 73)
    j48 = Jugador(48, "Alicia Ortega", 26, 66)
    j49 = Jugador(49, "Alberto Mendoza", 30, 66)
    j50 = Jugador(50, "Patricia Guzman", 42, 37)
    j51 = Jugador(51, "Eduardo Alvarez", 22, 78)
    j52 = Jugador(52, "Teresa Morales", 29, 14)
    j53 = Jugador(53, "Luis Gutierrez", 36, 57)
    j54 = Jugador(54, "Veronica Castillo", 25, 45)
    j55 = Jugador(55, "Raul Romero", 27, 88)
    j56 = Jugador(56, "Carmen Martinez", 30, 84)
    j57 = Jugador(57, "Marcos Soto", 32, 62)
    j58 = Jugador(58, "Ana Campos", 29, 12)
    j59 = Jugador(59, "Hector Pena", 28, 76)
    j60 = Jugador(60, "Diana Herrera", 26, 11)

    datos = [
        {
            "nombre": "Sede Cali",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j16, j2, j40, j49]},
                {"nombre": "Volleyball", "deporte": "Volleyball", "jugadores": [j17, j9, j18, j26, j38, j50, j51]},
                {"nombre": "Basketball", "deporte": "Basketball", "jugadores": [j1, j27, j39, j54]},
                {"nombre": "Tenis", "deporte": "Tenis", "jugadores": [j10, j19, j33, j48]},
                {"nombre": "Natacion", "deporte": "Natacion", "jugadores": [j15, j20, j37, j59]}
            ]
        },
        {
            "nombre": "Sede Medellin",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j7, j30, j42, j45]},
                {"nombre": "Volleyball", "deporte": "Volleyball", "jugadores": [j13, j31, j41]},
                {"nombre": "Basketball", "deporte": "Basketball", "jugadores": [j60, j6, j22, j29]},
                {"nombre": "Tenis", "deporte": "Tenis", "jugadores": [j14, j35, j43, j55]},
                {"nombre": "Natacion", "deporte": "Natacion", "jugadores": [j23, j5, j34, j44, j56]}
            ]
        },
        {
            "nombre": "Sede Bogota",
            "equipos": [
                {"nombre": "Futbol", "deporte": "Futbol", "jugadores": [j25, j8, j32, j58]},
                {"nombre": "Volleyball", "deporte": "Volleyball", "jugadores": [j4, j21, j52]},
                {"nombre": "Basketball", "deporte": "Basketball", "jugadores": [j11, j46, j53]},
                {"nombre": "Tenis", "deporte": "Tenis", "jugadores": [j24, j12, j28, j57]},
                {"nombre": "Natacion", "deporte": "Natacion", "jugadores": [j3, j36, j47]}
            ]
        }
    ]
    return datos
