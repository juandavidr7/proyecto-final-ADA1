from clases import Jugador, Equipo, Sede
from arbol_rojinegro import ArbolRojinegro
from solucion1 import comparador_jugador, comparador_equipo, comparador_sede

def construir_solucion_2(datos_sedes):
    """
    Construye la estructura usando Árboles Rojinegros (ordenamiento automático).
    """
    asociacion = ArbolRojinegro()

    for s_data in datos_sedes:
        arbol_equipos = ArbolRojinegro()
        for e_data in s_data["equipos"]:
            arbol_jugadores = ArbolRojinegro()
            for jug in e_data["jugadores"]:
                arbol_jugadores.insertar(jug, comparador_jugador)
            
            equipo = Equipo(e_data["nombre"], e_data["deporte"], 0, 0, arbol_jugadores)
            # Insertar equipo en arbol de equipos (usa comparador_equipo)
            # Nota: comparador_equipo usa promedios, que dependen de los jugadores ya insertados.
            arbol_equipos.insertar(equipo, comparador_equipo)
        
        sede = Sede(s_data["nombre"], arbol_equipos)
        asociacion.insertar(sede, comparador_sede)

    return asociacion
