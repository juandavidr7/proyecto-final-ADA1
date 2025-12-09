# Proyecto Final ADA I - Asociación Deportiva

## Requisitos

- Python 3.x
- matplotlib (para los benchmarks)

```bash
pip install matplotlib
```

## Estructura del proyecto

```
src/
├── clases.py           # Clases base (Jugador, Equipo, Sede)
├── vector_dinamico.py  # Implementación del vector dinámico
├── arbol_rojinegro.py  # Implementación del árbol rojinegro
├── solucion1.py        # Solución con vectores dinámicos
├── solucion2.py        # Solución con árboles rojinegros
├── main.py             # Script principal
├── benchmark.py        # Script de análisis de rendimiento
└── inputs/             # Casos de prueba
    ├── input1.py
    ├── input2.py
    ├── input3.py
    └── input4.py
```

## Ejecución

### Ejecutar el programa principal

```bash
cd src
python main.py
```

Para cambiar el caso de prueba, editar `main.py` y descomentar el input deseado:

```python
from inputs.input1 import obtener_datos
# from inputs.input2 import obtener_datos
# from inputs.input3 import obtener_datos
# from inputs.input4 import obtener_datos
```

### Ejecutar el benchmark

```bash
cd src
python benchmark.py
```

Esto genera:
- Tiempos de ejecución para cada input
- Comparación Vector vs Árbol
- Gráfico guardado como `benchmark_resultados.png`

## Autor

Juan David Rincón López
Libardo Alejandro Quintero
Juan Sebastián Sierra Cruz
Maria Juliana Saavedra 
