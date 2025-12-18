## Proyecto Final ADA I — Asociación Deportiva

Implementación en **Python** de dos estrategias para organizar sedes/equipos/jugadores y cumplir los criterios de ordenamiento del enunciado:

- **Estrategia 1**: `VectorDinamico` + **MergeSort manual**
- **Estrategia 2**: `ArbolRojinegro` (orden implícito por inserción + recorrido in-order)

### Requisitos

- **Python 3.x**
- **matplotlib** (solo si vas a ejecutar el benchmark y generar gráficas)

```bash
pip install matplotlib
```

### Estructura del proyecto

```
src/
├── clases.py           # Clases base (Jugador, Equipo, Sede)
├── vector_dinamico.py  # Vector dinámico + MergeSort manual
├── arbol_rojinegro.py  # Árbol rojinegro (inserción ordenada + balanceo)
├── solucion1.py        # Solución 1 (vectores + ordenamiento manual)
├── solucion2.py        # Solución 2 (árboles RN)
├── main.py             # Programa principal (muestra estructura y estadísticas)
├── benchmark.py        # Benchmark y generación de gráficas
└── inputs/             # Casos de prueba (4 instancias)
    ├── input1.py
    ├── input2.py
    ├── input3.py
    └── input4.py
```

### Ejecución

#### Programa principal

```bash
cd src
python main.py
```

Para cambiar el caso de prueba, edita `src/main.py` y descomenta el input deseado:

```python
from inputs.input1 import obtener_datos
# from inputs.input2 import obtener_datos
# from inputs.input3 import obtener_datos
# from inputs.input4 import obtener_datos
```

#### Benchmark (tiempos + gráficas)

```bash
cd src
python benchmark.py
```

Salida del benchmark:
- Imprime tiempos por input y por escalabilidad (se reporta **mediana** de varias repeticiones).
- Genera **4 imágenes** en la **raíz del proyecto**:
  - `1.png` (barras por input)
  - `2.png` (tamaño vs tiempo — inputs reales)
  - `3.png` (escalabilidad — flujo completo)
  - `4.png` (real vs teórico \(b + a\cdot n\log n\))

Parámetros opcionales:

```bash
# Ajustar repeticiones y tamaños de escalabilidad
python benchmark.py --reps-inputs 30 --reps-escala 50 --tamanios 10,20,30,40,50,60

# Mostrar ventanas de matplotlib
python benchmark.py --show
```

### Autores

- Juan David Rincón López
- María Juliana Saavedra
- Libardo Alejandro Quintero
- Juan Sebastián Sierra Cruz
