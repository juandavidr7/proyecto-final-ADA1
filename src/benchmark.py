import time
import math
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

def ejecutar_benchmark():
    """Ejecuta benchmark con los 4 inputs"""
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
    
    for nombre, datos in inputs:
        n_jugadores = contar_jugadores(datos)
        
        # Benchmark Solución 1 (Vectores)
        inicio = time.perf_counter()
        asoc1 = construir_solucion_1(datos)
        tiempo_vector = (time.perf_counter() - inicio) * 1000
        
        # Benchmark Solución 2 (Árboles)
        inicio = time.perf_counter()
        asoc2 = construir_solucion_2(datos)
        tiempo_arbol = (time.perf_counter() - inicio) * 1000
        
        print(f"\n{nombre}: {n_jugadores} jugadores")
        print(f"  Vector Dinámico: {tiempo_vector:.2f} ms")
        print(f"  Árbol Rojinegro: {tiempo_arbol:.2f} ms")
        
        resultados.append({
            "nombre": nombre,
            "n": n_jugadores,
            "tiempo_vector": tiempo_vector,
            "tiempo_arbol": tiempo_arbol
        })
    
    return resultados

def ejecutar_benchmark_escalabilidad():
    """Benchmark con diferentes tamaños para ver escalabilidad"""
    tamanios = [10, 20, 50, 100, 200]
    resultados = []
    
    print("\n" + "="*60)
    print(" BENCHMARK DE ESCALABILIDAD")
    print("="*60)
    
    for n in tamanios:
        t_vec = medir_tiempo_vector(n)
        t_arbol = medir_tiempo_arbol(n)
        
        print(f"n = {n}: Vector = {t_vec:.2f} ms, Árbol = {t_arbol:.2f} ms")
        
        resultados.append({
            "n": n,
            "tiempo_vector": t_vec,
            "tiempo_arbol": t_arbol,
            "n_log_n": n * math.log2(n) if n > 0 else 0
        })
    
    return resultados

def generar_graficos(resultados_basico, resultados_escala):
    """Genera gráficos en una sola figura"""
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # ========================================
    # Gráfico 1: Barras comparativas por input
    # ========================================
    ax1 = axes[0, 0]
    nombres = [r["nombre"] for r in resultados_basico]
    tiempos_vector = [r["tiempo_vector"] for r in resultados_basico]
    tiempos_arbol = [r["tiempo_arbol"] for r in resultados_basico]
    
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
    
    # ========================================
    # Gráfico 2: Tamaño vs Tiempo (inputs reales)
    # ========================================
    ax2 = axes[0, 1]
    n_vals = [r["n"] for r in resultados_basico]
    
    ax2.plot(n_vals, tiempos_vector, 'o-', label='Vector Dinámico', color='steelblue', linewidth=2, markersize=8)
    ax2.plot(n_vals, tiempos_arbol, 's-', label='Árbol Rojinegro', color='coral', linewidth=2, markersize=8)
    ax2.set_xlabel('Número de jugadores (n)')
    ax2.set_ylabel('Tiempo (ms)')
    ax2.set_title('Tamaño de entrada vs Tiempo (inputs reales)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # ========================================
    # Gráfico 3: Escalabilidad
    # ========================================
    ax3 = axes[1, 0]
    n_escala = [r["n"] for r in resultados_escala]
    t_vec_escala = [r["tiempo_vector"] for r in resultados_escala]
    t_arbol_escala = [r["tiempo_arbol"] for r in resultados_escala]
    
    ax3.plot(n_escala, t_vec_escala, 'o-', label='Vector Dinámico', color='steelblue', linewidth=2, markersize=8)
    ax3.plot(n_escala, t_arbol_escala, 's-', label='Árbol Rojinegro', color='coral', linewidth=2, markersize=8)
    ax3.set_xlabel('Número de elementos (n)')
    ax3.set_ylabel('Tiempo (ms)')
    ax3.set_title('Escalabilidad: Tamaño vs Tiempo')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # ========================================
    # Gráfico 4: Comparación con O(n log n) teórico
    # ========================================
    ax4 = axes[1, 1]
    n_log_n = [r["n_log_n"] for r in resultados_escala]
    
    # Normalizar O(n log n) para que sea comparable visualmente
    factor = t_vec_escala[-1] / n_log_n[-1] if n_log_n[-1] > 0 else 1
    n_log_n_normalizado = [x * factor for x in n_log_n]
    
    ax4.plot(n_escala, t_vec_escala, 'o-', label='Vector (real)', color='steelblue', linewidth=2, markersize=8)
    ax4.plot(n_escala, t_arbol_escala, 's-', label='Árbol (real)', color='coral', linewidth=2, markersize=8)
    ax4.plot(n_escala, n_log_n_normalizado, '--', label='O(n log n) teórico', color='green', linewidth=2)
    
    ax4.set_xlabel('Número de elementos (n)')
    ax4.set_ylabel('Tiempo (ms)')
    ax4.set_title('Complejidad real vs O(n log n) teórico')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('benchmark_resultados.png', dpi=150)
    print("\n[Gráfico guardado como 'benchmark_resultados.png']")
    plt.show()

def main():
    print("Ejecutando benchmarks...\n")
    
    resultados_basico = ejecutar_benchmark()
    
    resultados_escala = ejecutar_benchmark_escalabilidad()
    
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
        generar_graficos(resultados_basico, resultados_escala)
    except Exception as e:
        print(f"\nError generando gráficos: {e}")
        print("Instala matplotlib: pip install matplotlib")

if __name__ == "__main__":
    main()
