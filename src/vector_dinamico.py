class VectorDinamico:
    def __init__(self):
        self.capacidad = 2
        self.cantidad = 0
        self.datos = [None] * self.capacidad

    def _redimensionar(self, nueva_capacidad):
        nuevos_datos = [None] * nueva_capacidad
        for i in range(self.cantidad):
            nuevos_datos[i] = self.datos[i]
        self.datos = nuevos_datos
        self.capacidad = nueva_capacidad

    def agregar(self, elemento):
        if self.cantidad == self.capacidad:
            self._redimensionar(self.capacidad * 2)
        self.datos[self.cantidad] = elemento
        self.cantidad += 1

    def obtener(self, indice):
        if indice < 0 or indice >= self.cantidad:
            raise IndexError("Indice fuera de rango")
        return self.datos[indice]

    def size(self):
        return self.cantidad

    def esta_vacio(self):
        return self.cantidad == 0

    def obtener_elementos(self):
        resultado = []
        for i in range(self.cantidad):
            resultado.append(self.datos[i])
        return resultado

    # --- Algoritmo Merge Sort Manual ---
    def ordenar(self, comparador):
        self._merge_sort(0, self.cantidad - 1, comparador)

    def _merge(self, izquierda, medio, derecha, comparador):
        n1 = medio - izquierda + 1
        n2 = derecha - medio

        # Arrays temporales
        L = [None] * n1
        R = [None] * n2

        for i in range(n1):
            L[i] = self.datos[izquierda + i]
        for j in range(n2):
            R[j] = self.datos[medio + 1 + j]

        i = 0
        j = 0
        k = izquierda

        while i < n1 and j < n2:
            # Si comparador(L[i], R[j]) es True, entonces L[i] va antes
            if comparador(L[i], R[j]):
                self.datos[k] = L[i]
                i += 1
            else:
                self.datos[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            self.datos[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            self.datos[k] = R[j]
            j += 1
            k += 1

    def _merge_sort(self, izquierda, derecha, comparador):
        if izquierda < derecha:
            medio = (izquierda + derecha) // 2
            self._merge_sort(izquierda, medio, comparador)
            self._merge_sort(medio + 1, derecha, comparador)
            self._merge(izquierda, medio, derecha, comparador)
