import argparse
import math
import os
import statistics
import time

import matplotlib.pyplot as plt
import numpy as np

from clases import Jugador
from vector_dinamico import VectorDinamico
from arbol_rojinegro import ArbolRojinegro
from solucion1 import construir_solucion_1, comparador_jugador
from solucion2 import construir_solucion_2

# Importar todos los inputs
from inputs.input1 import obtener_datos as datos_input1
from inputs.input2 import obtener_datos as datos_input2
from inputs.input3 import obtener_datos as datos_input3
from inputs.input4 import obtener_datos as datos_input4

def contar_jugadores(datos):
    """Cuenta el total de jugadores en los datos"""
    total = 0
    for sede in datos:
        for equipo in sede["equipos"]:
            total += len(equipo["jugadores"])
    return total

def _resumen_tiempos_ms(tiempos_ms):
    """Devuelve (mediana, min, max) en ms a partir de una lista de tiempos."""
    if not tiempos_ms:
        return (0.0, 0.0, 0.0)
    return (
        float(statistics.median(tiempos_ms)),
        float(min(tiempos_ms)),
        float(max(tiempos_ms)),
    )

def _merge_sort_por_clave(lista, clave):
    """MergeSort manual para listas de dicts/objetos, ordenando ascendente por clave(item)."""
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izq = _merge_sort_por_clave(lista[:medio], clave)
    der = _merge_sort_por_clave(lista[medio:], clave)

    i = 0
    j = 0
    res = []
    while i < len(izq) and j < len(der):
        if izq[i][clave] <= der[j][clave]:
            res.append(izq[i])
            i += 1
        else:
            res.append(der[j])
            j += 1

    if i < len(izq):
        res.extend(izq[i:])
    if j < len(der):
        res.extend(der[j:])
    return res

def generar_datos_sinteticos(n_jugadores, k_sedes=2, m_equipos=3):
    """
    Genera una instancia sintética del problema con:
    - k_sedes sedes
    - m_equipos equipos por sede
    - n_jugadores jugadores en total distribuidos entre todos los equipos

    Esto permite medir escalabilidad del flujo COMPLETO (sedes/equipos/jugadores),
    igual que en los inputs reales.
    """
    deportes = ["Futbol", "Volleyball", "Basketball", "Tenis", "Natacion", "Atletismo"]
    deportes = deportes[:m_equipos]

    # Crear estructura vacía
    datos = []
    for s in range(k_sedes):
        equipos = []
        for e in range(m_equipos):
            equipos.append({"nombre": deportes[e], "deporte": deportes[e], "jugadores": []})
        datos.append({"nombre": f"Sede {s + 1}", "equipos": equipos})

    total_equipos = k_sedes * m_equipos
    for i in range(1, n_jugadores + 1):
        # Distribuir por equipos de manera uniforme
        idx_equipo_global = (i - 1) % total_equipos
        idx_sede = idx_equipo_global // m_equipos
        idx_equipo = idx_equipo_global % m_equipos

        edad = 18 + ((i * 7) % 23)          # 18..40
        rendimiento = 1 + ((i * 37) % 100)  # 1..100
        jug = Jugador(i, f"Jugador{i}", edad, rendimiento)

        datos[idx_sede]["equipos"][idx_equipo]["jugadores"].append(jug)

    return datos

def medir_tiempo_vector(n_elementos):
    """Mide tiempo total de Vector (inserción + ordenamiento)"""
    vec = VectorDinamico()
    inicio = time.perf_counter()
    for i in range(n_elementos):
        vec.agregar(Jugador(i, f"Jugador{i}", 20, 50 - i))
    vec.ordenar(comparador_jugador)
    return (time.perf_counter() - inicio) * 1000

def medir_tiempo_arbol(n_elementos):
    """Mide tiempo total de Árbol (inserción con ordenamiento implícito)"""
    arbol = ArbolRojinegro()
    inicio = time.perf_counter()
    for i in range(n_elementos):
        arbol.insertar(Jugador(i, f"Jugador{i}", 20, 50), comparador_jugador)
    return (time.perf_counter() - inicio) * 1000

def ejecutar_benchmark(repeticiones=30):
    """Ejecuta benchmark con los 4 inputs (repite para reducir ruido)"""
    inputs = [
        ("Input 1", datos_input1()),
        ("Input 2", datos_input2()),
        ("Input 3", datos_input3()),
        ("Input 4", datos_input4()),
    ]
    
    resultados = []
    
    print("="*60)
    print(" BENCHMARK: Vectores Dinámicos vs Árboles Rojinegros")
    print("="*60)
    print(f" Repeticiones por medición: {repeticiones}")
    
    for nombre, datos in inputs:
        n_jugadores = contar_jugadores(datos)
        
        tiempos_vector = []
        tiempos_arbol = []

        for _ in range(repeticiones):
            # Benchmark Solución 1 (Vectores)
            inicio = time.perf_counter()
            construir_solucion_1(datos)
            tiempos_vector.append((time.perf_counter() - inicio) * 1000)

            # Benchmark Solución 2 (Árboles)
            inicio = time.perf_counter()
            construir_solucion_2(datos)
            tiempos_arbol.append((time.perf_counter() - inicio) * 1000)

        tiempo_vector_med, tiempo_vector_min, tiempo_vector_max = _resumen_tiempos_ms(tiempos_vector)
        tiempo_arbol_med, tiempo_arbol_min, tiempo_arbol_max = _resumen_tiempos_ms(tiempos_arbol)
        
        print(f"\n{nombre}: {n_jugadores} jugadores")
        print(f"  Vector Dinámico: mediana={tiempo_vector_med:.3f} ms (min={tiempo_vector_min:.3f}, max={tiempo_vector_max:.3f})")
        print(f"  Árbol Rojinegro: mediana={tiempo_arbol_med:.3f} ms (min={tiempo_arbol_min:.3f}, max={tiempo_arbol_max:.3f})")
        
        resultados.append({
            "nombre": nombre,
            "n": n_jugadores,
            "tiempo_vector": tiempo_vector_med,
            "tiempo_arbol": tiempo_arbol_med,
            "tiempo_vector_min": tiempo_vector_min,
            "tiempo_vector_max": tiempo_vector_max,
            "tiempo_arbol_min": tiempo_arbol_min,
            "tiempo_arbol_max": tiempo_arbol_max,
        })
    
    return resultados

def ejecutar_benchmark_escalabilidad(tamanios=None, repeticiones=50):
    """Benchmark con diferentes tamaños para ver escalabilidad del flujo completo (mediana de N repeticiones)"""
    if tamanios is None:
        # Mantenerlo alineado con los tamaños de los inputs reales (n <= ~60)
        tamanios = [10, 20, 30, 40, 50, 60]
    resultados = []
    
    print("\n" + "="*60)
    print(" BENCHMARK DE ESCALABILIDAD")
    print("="*60)
    print(f" Repeticiones por tamaño: {repeticiones}")
    print(" Nota: se mide construir_solucion_1/2 sobre datos sintéticos con sedes y equipos (mismo flujo que inputs reales).")
    
    for n in tamanios:
        tiempos_vec = []
        tiempos_arbol = []

        for _ in range(repeticiones):
            datos = generar_datos_sinteticos(n_jugadores=n, k_sedes=2, m_equipos=3)

            inicio = time.perf_counter()
            construir_solucion_1(datos)
            tiempos_vec.append((time.perf_counter() - inicio) * 1000)

            inicio = time.perf_counter()
            construir_solucion_2(datos)
            tiempos_arbol.append((time.perf_counter() - inicio) * 1000)

        t_vec, vec_min, vec_max = _resumen_tiempos_ms(tiempos_vec)
        t_arbol, arbol_min, arbol_max = _resumen_tiempos_ms(tiempos_arbol)
        
        print(f"n = {n}: Solución 1 (Vector) mediana={t_vec:.3f} ms (min={vec_min:.3f}, max={vec_max:.3f}), "
              f"Solución 2 (Árbol) mediana={t_arbol:.3f} ms (min={arbol_min:.3f}, max={arbol_max:.3f})")
        
        resultados.append({
            "n": n,
            "tiempo_vector": t_vec,
            "tiempo_arbol": t_arbol,
            "tiempo_vector_min": vec_min,
            "tiempo_vector_max": vec_max,
            "tiempo_arbol_min": arbol_min,
            "tiempo_arbol_max": arbol_max,
            "n_log_n": n * math.log2(n) if n > 0 else 0
        })
    
    return resultados

def generar_graficos(resultados_basico, resultados_escala, output_dir, show=False):
    """Genera 4 gráficos en 4 imágenes separadas: 1.png, 2.png, 3.png, 4.png"""

    os.makedirs(output_dir, exist_ok=True)
    out1 = os.path.join(output_dir, "1.png")
    out2 = os.path.join(output_dir, "2.png")
    out3 = os.path.join(output_dir, "3.png")
    out4 = os.path.join(output_dir, "4.png")

    # Datos comunes
    nombres = [r["nombre"] for r in resultados_basico]
    tiempos_vector = [r["tiempo_vector"] for r in resultados_basico]
    tiempos_arbol = [r["tiempo_arbol"] for r in resultados_basico]

    resultados_basico_ordenados = _merge_sort_por_clave(list(resultados_basico), "n")
    n_vals = [r["n"] for r in resultados_basico_ordenados]
    tiempos_vector_ordenados = [r["tiempo_vector"] for r in resultados_basico_ordenados]
    tiempos_arbol_ordenados = [r["tiempo_arbol"] for r in resultados_basico_ordenados]

    n_escala = [r["n"] for r in resultados_escala]
    t_vec_escala = [r["tiempo_vector"] for r in resultados_escala]
    t_arbol_escala = [r["tiempo_arbol"] for r in resultados_escala]
    n_log_n = [r["n_log_n"] for r in resultados_escala]

    # Escalado teórico a·n log n (ajuste por mínimos cuadrados sobre Vector)
    # En la práctica hay un overhead casi constante (Python/objetos/IO), por eso ajustamos:
    #   t(n) ≈ b + a * (n log n)
    # Esto sigue siendo O(n log n), pero evita que la curva "salga desde 0" y se vea rara en n pequeños.
    x_vals = n_log_n
    y_vals = t_vec_escala
    x_mean = sum(x_vals) / len(x_vals) if x_vals else 0.0
    y_mean = sum(y_vals) / len(y_vals) if y_vals else 0.0
    var_x = sum((x - x_mean) ** 2 for x in x_vals) or 1.0
    cov_xy = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_vals, y_vals))
    a = cov_xy / var_x
    b = y_mean - a * x_mean
    n_log_n_escalado = [b + (x * a) for x in n_log_n]

    # 1) Barras por input
    fig1, ax1 = plt.subplots(figsize=(9, 5))
    x = np.arange(len(nombres))
    width = 0.35
    ax1.bar(x - width/2, tiempos_vector, width, label='Vector Dinámico', color='steelblue')
    ax1.bar(x + width/2, tiempos_arbol, width, label='Árbol Rojinegro', color='coral')
    ax1.set_xlabel('Caso de prueba')
    ax1.set_ylabel('Tiempo (ms)')
    ax1.set_title('Comparación de tiempos por caso de prueba')
    ax1.set_xticks(x)
    ax1.set_xticklabels(nombres)
    ax1.legend()
    ax1.grid(axis='y', alpha=0.3)
    fig1.tight_layout()
    fig1.savefig(out1, dpi=150)

    # 2) Tamaño vs tiempo (inputs reales)
    fig2, ax2 = plt.subplots(figsize=(9, 5))
    ax2.plot(n_vals, tiempos_vector_ordenados, 'o-', label='Vector Dinámico', color='steelblue', linewidth=2, markersize=8)
    ax2.plot(n_vals, tiempos_arbol_ordenados, 's-', label='Árbol Rojinegro', color='coral', linewidth=2, markersize=8)
    ax2.set_xlabel('Número de jugadores (n)')
    ax2.set_ylabel('Tiempo (ms)')
    ax2.set_title('Tamaño de entrada vs Tiempo (inputs reales)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    fig2.tight_layout()
    fig2.savefig(out2, dpi=150)

    # 3) Escalabilidad (flujo completo)
    fig3, ax3 = plt.subplots(figsize=(9, 5))
    ax3.plot(n_escala, t_vec_escala, 'o-', label='Vector Dinámico', color='steelblue', linewidth=2, markersize=8)
    ax3.plot(n_escala, t_arbol_escala, 's-', label='Árbol Rojinegro', color='coral', linewidth=2, markersize=8)
    ax3.set_xlabel('Número de jugadores (n)')
    ax3.set_ylabel('Tiempo (ms)')
    ax3.set_title('Escalabilidad (flujo completo): Tamaño vs Tiempo')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    fig3.tight_layout()
    fig3.savefig(out3, dpi=150)

    # 4) Complejidad real vs a·n log n
    fig4, ax4 = plt.subplots(figsize=(9, 5))
    ax4.plot(n_escala, t_vec_escala, 'o-', label='Vector (real)', color='steelblue', linewidth=2, markersize=8)
    ax4.plot(n_escala, t_arbol_escala, 's-', label='Árbol (real)', color='coral', linewidth=2, markersize=8)
    ax4.plot(n_escala, n_log_n_escalado, '--', label='b + a·n log n (teórico)', color='green', linewidth=2)
    ax4.set_xlabel('Número de jugadores (n)')
    ax4.set_ylabel('Tiempo (ms)')
    ax4.set_title('Complejidad real vs O(n log n) teórico')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    fig4.tight_layout()
    fig4.savefig(out4, dpi=150)

    print(f"\n[Gráficos guardados como: '{out1}', '{out2}', '{out3}', '{out4}']")
    if show:
        plt.show()
    else:
        plt.close(fig1)
        plt.close(fig2)
        plt.close(fig3)
        plt.close(fig4)

def main():
    parser = argparse.ArgumentParser(description="Benchmark: Vector Dinámico vs Árbol Rojinegro")
    parser.add_argument("--reps-inputs", type=int, default=30, help="Repeticiones por input (medir solución 1 vs 2)")
    parser.add_argument("--reps-escala", type=int, default=50, help="Repeticiones por tamaño en benchmark de escalabilidad")
    parser.add_argument(
        "--tamanios",
        type=str,
        default="10,20,30,40,50,60",
        help="Lista separada por comas para escalabilidad (ej: 100,200,500,1000)",
    )
    parser.add_argument("--show", action="store_true", help="Mostrar la ventana del gráfico (plt.show)")
    args = parser.parse_args()

    print("Ejecutando benchmarks...\n")

    try:
        tamanios = [int(x.strip()) for x in args.tamanios.split(",") if x.strip()]
    except ValueError:
        print("Error: --tamanios debe ser una lista de enteros separados por comas.")
        return

    resultados_basico = ejecutar_benchmark(repeticiones=args.reps_inputs)

    resultados_escala = ejecutar_benchmark_escalabilidad(tamanios=tamanios, repeticiones=args.reps_escala)
    
    print("\n" + "="*60)
    print(" ANÁLISIS DE COMPLEJIDAD")
    print("="*60)
    print("\nComplejidad Teórica:")
    print("  VECTOR DINÁMICO:")
    print("    - Inserción: O(n)")
    print("    - Ordenamiento (MergeSort): O(n log n)")
    print("    - Total: O(n log n)")
    print("\n  ÁRBOL ROJINEGRO:")
    print("    - Inserción con balance: O(n log n)")
    print("    - Ordenamiento: Implícito")
    print("    - Total: O(n log n)")

    try:
        # Guardar en la raíz del proyecto para que el informe (informe.tex) encuentre 1.png..4.png
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        generar_graficos(resultados_basico, resultados_escala, output_dir=project_root, show=args.show)
    except Exception as e:
        print(f"\nError generando gráficos: {e}")
        print("Instala matplotlib: pip install matplotlib")

if __name__ == "__main__":
    main()
