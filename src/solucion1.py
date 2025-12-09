from clases import Jugador, Equipo, Sede
from vector_dinamico import VectorDinamico

def comparador_jugador(a, b):
    # Ascendente por rendimiento
    if a.rendimiento != b.rendimiento:
        return a.rendimiento < b.rendimiento
    # En empate, mayor edad primero (descendente)
    return a.edad > b.edad

def comparador_equipo(a, b):
    # Ascendente por promedio
    prom_a = a.get_promedio_rendimiento()
    prom_b = b.get_promedio_rendimiento()
    if prom_a != prom_b:
        return prom_a < prom_b
    # En empate, mayor cantidad de jugadores primero
    return a.get_cantidad_jugadores() > b.get_cantidad_jugadores()

def comparador_sede(a, b):
    # Ascendente por promedio
    prom_a = a.get_promedio_rendimiento()
    prom_b = b.get_promedio_rendimiento()
    if prom_a != prom_b:
        return prom_a < prom_b
    # En empate, mayor total de jugadores primero
    return a.get_total_jugadores() > b.get_total_jugadores()

def construir_solucion_1(datos_sedes):
    """
    Construye la estructura usando Vectores Dinámicos y ordena manualmente.
    datos_sedes: Lista de diccionarios con estructura:
    [
        {
            "nombre": "Sede Cali",
            "equipos": [
                {
                    "nombre": "Futbol", "deporte": "Futbol", 
                    "jugadores": [obj_jugador, ...]
                },
                ...
            ]
        },
        ...
    ]
    """
    asociacion = VectorDinamico()

    for s_data in datos_sedes:
        vec_equipos = VectorDinamico()
        for e_data in s_data["equipos"]:
            vec_jugadores = VectorDinamico()
            for jug in e_data["jugadores"]:
                vec_jugadores.agregar(jug)
            
            equipo = Equipo(e_data["nombre"], e_data["deporte"], 0, 0, vec_jugadores)
            vec_equipos.agregar(equipo)
        
        sede = Sede(s_data["nombre"], vec_equipos)
        asociacion.agregar(sede)

    # --- ORDENAMIENTO MANUAL ---
    # 1. Ordenar Sedes
    asociacion.ordenar(comparador_sede)

    # 2. Ordenar Equipos y Jugadores
    for i in range(asociacion.size()):
        sede = asociacion.obtener(i)
        sede.equipos.ordenar(comparador_equipo)
        
        for k in range(sede.equipos.size()):
            equipo = sede.equipos.obtener(k)
            equipo.jugadores.ordenar(comparador_jugador)

    return asociacion
