class Jugador:
    def __init__(self, id, nombre, edad, rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

    def __repr__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}, Rendimiento: {self.rendimiento}"

class Equipo:
    def __init__(self, nombre, deporte, n_min, n_max, coleccion_jugadores):
        self.nombre = nombre
        self.deporte = deporte
        self.n_min = n_min
        self.n_max = n_max
        self.jugadores = coleccion_jugadores 
    def agregar_jugador(self, jugador, comparador=None):
        try:
            self.jugadores.agregar(jugador, comparador)
        except TypeError:
            self.jugadores.agregar(jugador)

    def get_promedio_rendimiento(self):
        # Asumimos que la colección tiene un método para iterar o devolver lista
        lista = self.jugadores.obtener_elementos()
        if not lista or len(lista) == 0:
            return 0.0
        
        suma = sum(j.rendimiento for j in lista)
        return suma / len(lista)

    def get_cantidad_jugadores(self):
        return self.jugadores.size()

    def __repr__(self):
        return f"Equipo: {self.nombre} ({self.deporte}) - Promedio: {self.get_promedio_rendimiento():.2f}"

class Sede:
    def __init__(self, nombre, coleccion_equipos):
        self.nombre = nombre
        self.equipos = coleccion_equipos # Puede ser VectorDinamico o ArbolRojinegro

    def agregar_equipo(self, equipo, comparador=None):
        try:
            self.equipos.agregar(equipo, comparador)
        except TypeError:
            self.equipos.agregar(equipo)

    def get_promedio_rendimiento(self):
        lista = self.equipos.obtener_elementos()
        if not lista or len(lista) == 0:
            return 0.0
        
        suma = sum(e.get_promedio_rendimiento() for e in lista)
        return suma / len(lista)

    def get_total_jugadores(self):
        lista = self.equipos.obtener_elementos()
        return sum(e.get_cantidad_jugadores() for e in lista)

    def __repr__(self):
        return f"Sede: {self.nombre} - Promedio: {self.get_promedio_rendimiento():.2f}"
