from solucion1 import construir_solucion_1
from solucion2 import construir_solucion_2
from solucion1 import comparador_jugador, comparador_equipo

# Cambiar el input aquí para usar diferentes datos de prueba
# from inputs.input1 import obtener_datos
# from inputs.input2 import obtener_datos
# from inputs.input3 import obtener_datos
from inputs.input4 import obtener_datos

def imprimir_resultados(asociacion, titulo):
    print(f"\n{'='*60}")
    print(f" {titulo}")
    print(f"{'='*60}")
    
    sedes = asociacion.obtener_elementos()
    
    for sede in sedes:
        print(f"\n>> {sede.nombre}")
        print(f"   Rendimiento promedio: {sede.get_promedio_rendimiento():.2f}")
        print(f"   Total jugadores: {sede.get_total_jugadores()}")
        print()
        
        equipos = sede.equipos.obtener_elementos()
        for equipo in equipos:
            print(f"   [{equipo.nombre}]")
            print(f"   Rendimiento promedio: {equipo.get_promedio_rendimiento():.2f}")
            print(f"   Jugadores: ", end="")
            
            jugadores = equipo.jugadores.obtener_elementos()
            ids = [str(j.id) for j in jugadores]
            print("{" + ", ".join(ids) + "}")
            print()

def calcular_estadisticas(asociacion):
    print(f"\n{'='*60}")
    print(f" ESTADISTICAS GENERALES")
    print(f"{'='*60}")
    
    # Recolectar jugadores (sin usar sorted()/.sort() de Python)
    todos_jugadores = []
    sedes = asociacion.obtener_elementos()
    for sede in sedes:
        equipos = sede.equipos.obtener_elementos()
        for equipo in equipos:
            jugadores = equipo.jugadores.obtener_elementos()
            todos_jugadores.extend(jugadores)
    
    # Ranking de jugadores: usar MergeSort manual (VectorDinamico.ordenar)
    from vector_dinamico import VectorDinamico
    ranking = VectorDinamico()
    for j in todos_jugadores:
        ranking.agregar(j)
    ranking.ordenar(comparador_jugador)
    jugadores_rank = ranking.obtener_elementos()
    ids_ranking = [str(j.id) for j in jugadores_rank]
    
    print(f"\nRanking de jugadores (por rendimiento):")
    print("{" + ", ".join(ids_ranking) + "}")
    
    if not todos_jugadores:
        return

    todos_equipos = []
    for sede in sedes:
        equipos = sede.equipos.obtener_elementos()
        for eq in equipos:
            todos_equipos.append((eq, sede.nombre))
    
    # Equipo con mayor/menor rendimiento: recorrido lineal (no requiere ordenar toda la lista)
    equipo_min = todos_equipos[0]
    equipo_max = todos_equipos[0]
    for item in todos_equipos[1:]:
        eq, _sede = item
        # item va antes que equipo_min => es "menor" según el criterio del proyecto
        if comparador_equipo(eq, equipo_min[0]):
            equipo_min = item
        # equipo_max va antes que item => item es "mayor"
        if comparador_equipo(equipo_max[0], eq):
            equipo_max = item
    
    print(f"\nEquipo con MAYOR rendimiento: {equipo_max[0].nombre} ({equipo_max[1]}) - {equipo_max[0].get_promedio_rendimiento():.2f}")
    print(f"Equipo con MENOR rendimiento: {equipo_min[0].nombre} ({equipo_min[1]}) - {equipo_min[0].get_promedio_rendimiento():.2f}")

    # Jugador con mayor/menor rendimiento: recorrido lineal con el comparador del proyecto
    jug_min = jugadores_rank[0]
    jug_max = jugadores_rank[0]
    for j in jugadores_rank[1:]:
        if comparador_jugador(j, jug_min):
            jug_min = j
        if comparador_jugador(jug_max, j):
            jug_max = j
    
    print(f"\nJugador con MAYOR rendimiento: {{ {jug_max.id}, {jug_max.nombre}, {jug_max.rendimiento} }}")
    print(f"Jugador con MENOR rendimiento: {{ {jug_min.id}, {jug_min.nombre}, {jug_min.rendimiento} }}")

    # Jugador más joven / más veterano: recorrido lineal (evita sorted())
    jug_joven = todos_jugadores[0]
    jug_veterano = todos_jugadores[0]
    for j in todos_jugadores[1:]:
        if j.edad < jug_joven.edad:
            jug_joven = j
        if j.edad > jug_veterano.edad:
            jug_veterano = j

    print(f"\nJugador MAS JOVEN: {{ {jug_joven.id}, {jug_joven.nombre}, {jug_joven.edad} años }}")
    print(f"Jugador MAS VETERANO: {{ {jug_veterano.id}, {jug_veterano.nombre}, {jug_veterano.edad} años }}")

    prom_edad = sum(j.edad for j in todos_jugadores) / len(todos_jugadores)
    prom_rend = sum(j.rendimiento for j in todos_jugadores) / len(todos_jugadores)

    print(f"\nPromedio de edad: {prom_edad:.2f} años")
    print(f"Promedio de rendimiento: {prom_rend:.2f}")

def main():
    datos = obtener_datos()
    
    print(f"Datos cargados: {len(datos)} sedes")
    for sede in datos:
        print(f"  - {sede['nombre']}: {len(sede['equipos'])} equipos")
    
    # Solucion 1
    asoc1 = construir_solucion_1(datos)
    imprimir_resultados(asoc1, "SOLUCION 1: VECTORES DINAMICOS")
    
    # Solucion 2
    asoc2 = construir_solucion_2(datos)
    imprimir_resultados(asoc2, "SOLUCION 2: ARBOLES ROJINEGROS")
    
    # Estadisticas
    calcular_estadisticas(asoc1)

if __name__ == "__main__":
    main()
