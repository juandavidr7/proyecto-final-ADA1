Proyecto Final ADA I - Asociación Deportiva

Requisitos
- Python 3.x
- matplotlib (para correr el benchmark y generar gráficos)

Instalación (solo si vas a ejecutar el benchmark):
  pip install matplotlib

Estructura (carpeta src/)
- clases.py: Clases base (Jugador, Equipo, Sede)
- vector_dinamico.py: Vector dinámico + MergeSort manual
- arbol_rojinegro.py: Árbol rojinegro (inserción ordenada)
- solucion1.py: Alternativa 1 (Vectores dinámicos + ordenamiento manual)
- solucion2.py: Alternativa 2 (Árboles rojinegros)
- main.py: Ejecución principal (muestra salidas y estadísticas)
- benchmark.py: Benchmark + generación de gráficos
- inputs/: 4 instancias del problema (input1..input4)

Ejecución
1) Programa principal:
  cd src
  python main.py

Para cambiar el caso de prueba, editar src/main.py y descomentar el input deseado:
  from inputs.input1 import obtener_datos
  # from inputs.input2 import obtener_datos
  # from inputs.input3 import obtener_datos
  # from inputs.input4 import obtener_datos

2) Benchmark (tiempos + gráfico):
  cd src
  python benchmark.py

Opcionales:
  python benchmark.py --reps-inputs 30 --reps-escala 50 --tamanios 10,20,30,40,50,60
  python benchmark.py --show

Salida del benchmark:
- Muestra tiempos (mediana, min y max) por input y por escalabilidad
- Genera el archivo src/benchmark_resultados.png

