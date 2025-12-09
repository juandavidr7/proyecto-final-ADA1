from solucion1 import construir_solucion_1
from solucion2 import construir_solucion_2

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
    
    todos_jugadores = []
    sedes = asociacion.obtener_elementos()
    for sede in sedes:
        equipos = sede.equipos.obtener_elementos()
        for equipo in equipos:
            jugadores = equipo.jugadores.obtener_elementos()
            todos_jugadores.extend(jugadores)
    
    todos_jugadores.sort(key=lambda x: (x.rendimiento, -x.edad))
    ids_ranking = [str(j.id) for j in todos_jugadores]
    
    print(f"\nRanking de jugadores (por rendimiento):")
    print("{" + ", ".join(ids_ranking) + "}")
    
    if not todos_jugadores:
        return

    todos_equipos = []
    for sede in sedes:
        equipos = sede.equipos.obtener_elementos()
        for eq in equipos:
            todos_equipos.append((eq, sede.nombre))
    
    todos_equipos.sort(key=lambda x: (x[0].get_promedio_rendimiento(), -x[0].get_cantidad_jugadores()))
    
    equipo_min = todos_equipos[0]
    equipo_max = todos_equipos[-1]
    
    print(f"\nEquipo con MAYOR rendimiento: {equipo_max[0].nombre} ({equipo_max[1]}) - {equipo_max[0].get_promedio_rendimiento():.2f}")
    print(f"Equipo con MENOR rendimiento: {equipo_min[0].nombre} ({equipo_min[1]}) - {equipo_min[0].get_promedio_rendimiento():.2f}")

    jug_max = todos_jugadores[-1]
    jug_min = todos_jugadores[0]
    
    print(f"\nJugador con MAYOR rendimiento: {{ {jug_max.id}, {jug_max.nombre}, {jug_max.rendimiento} }}")
    print(f"Jugador con MENOR rendimiento: {{ {jug_min.id}, {jug_min.nombre}, {jug_min.rendimiento} }}")

    todos_jugadores_edad = sorted(todos_jugadores, key=lambda x: x.edad)
    jug_joven = todos_jugadores_edad[0]
    jug_veterano = todos_jugadores_edad[-1]

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
