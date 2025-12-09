import time
from vector_dinamico import VectorDinamico

class NodoRB:
    def __init__(self, data, color="ROJO"):
        self.data = data
        self.color = color # "ROJO" o "NEGRO"
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolRojinegro:
    DELAY_MS = 0.001  # 1ms delay para benchmarking
    
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def _rotar_izquierda(self, ptr):
        derecha_hijo = ptr.derecha
        ptr.derecha = derecha_hijo.izquierda

        if ptr.derecha is not None:
            ptr.derecha.padre = ptr

        derecha_hijo.padre = ptr.padre

        if ptr.padre is None:
            self.raiz = derecha_hijo
        elif ptr == ptr.padre.izquierda:
            ptr.padre.izquierda = derecha_hijo
        else:
            ptr.padre.derecha = derecha_hijo

        derecha_hijo.izquierda = ptr
        ptr.padre = derecha_hijo

    def _rotar_derecha(self, ptr):
        izquierda_hijo = ptr.izquierda
        ptr.izquierda = izquierda_hijo.derecha

        if ptr.izquierda is not None:
            ptr.izquierda.padre = ptr

        izquierda_hijo.padre = ptr.padre

        if ptr.padre is None:
            self.raiz = izquierda_hijo
        elif ptr == ptr.padre.izquierda:
            ptr.padre.izquierda = izquierda_hijo
        else:
            ptr.padre.derecha = izquierda_hijo

        izquierda_hijo.derecha = ptr
        ptr.padre = izquierda_hijo

    def _arreglar_insercion(self, ptr):
        while ptr != self.raiz and ptr.color == "ROJO" and ptr.padre.color == "ROJO":
            padre = ptr.padre
            abuelo = ptr.padre.padre

            if padre == abuelo.izquierda:
                tio = abuelo.derecha
                if tio is not None and tio.color == "ROJO":
                    abuelo.color = "ROJO"
                    padre.color = "NEGRO"
                    tio.color = "NEGRO"
                    ptr = abuelo
                else:
                    if ptr == padre.derecha:
                        self._rotar_izquierda(padre)
                        ptr = padre
                        padre = ptr.padre
                    
                    self._rotar_derecha(abuelo)
                    padre.color, abuelo.color = abuelo.color, padre.color
                    ptr = padre
            else:
                tio = abuelo.izquierda
                if tio is not None and tio.color == "ROJO":
                    abuelo.color = "ROJO"
                    padre.color = "NEGRO"
                    tio.color = "NEGRO"
                    ptr = abuelo
                else:
                    if ptr == padre.izquierda:
                        self._rotar_derecha(padre)
                        ptr = padre
                        padre = ptr.padre
                    
                    self._rotar_izquierda(abuelo)
                    padre.color, abuelo.color = abuelo.color, padre.color
                    ptr = padre
        
        self.raiz.color = "NEGRO"

    def insertar(self, data, comparador):
        time.sleep(ArbolRojinegro.DELAY_MS)  # Delay para simular procesamiento
        ptr = NodoRB(data)
        self.raiz = self._insertar_bst(self.raiz, ptr, comparador)
        self._arreglar_insercion(ptr)
        self.cantidad += 1

    def _insertar_bst(self, root, ptr, comparador):
        if root is None:
            return ptr
        
        # Usamos el comparador para decidir izquierda o derecha
        # Si comparador(ptr.data, root.data) es True -> Izquierda
        if comparador(ptr.data, root.data):
            root.izquierda = self._insertar_bst(root.izquierda, ptr, comparador)
            root.izquierda.padre = root
        else:
            root.derecha = self._insertar_bst(root.derecha, ptr, comparador)
            root.derecha.padre = root
        
        return root

    def obtener_elementos(self):
        # Devuelve una lista de Python estándar ordenada (in-order)
        resultado = []
        self._in_order_helper(self.raiz, resultado)
        return resultado

    def _in_order_helper(self, root, resultado):
        if root is None:
            return
        self._in_order_helper(root.izquierda, resultado)
        resultado.append(root.data)
        self._in_order_helper(root.derecha, resultado)

    def size(self):
        return self.cantidad

    # Método para cumplir interfaz común con VectorDinamico
    def agregar(self, elemento, comparador):
        self.insertar(elemento, comparador)
