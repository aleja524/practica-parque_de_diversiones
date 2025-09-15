import random
class Queue():
    def __init__(self):
        self.__list = []

    def __str__(self):
        return '--'.join(map(str, self.__list))

    def enqueue(self, e):
        self.__list.append(e)
        return True

    def dequeue(self):
        if self.is_empty():
            return "Error no es posible desencolar, no hay elementos"
        return self.__list.pop(0)

    def first(self):
        if self.is_empty():
            return "Error no es posible leer el primer elemento, no hay elementos"
        return self.__list[0]

    def is_empty(self):
        return len(self.__list) == 0

    def len(self):
        return len(self.__list)

    def generate(self, num, min, max):
        for i in range(num):
            self.enqueue(random.randint(min, max))

class Stack():
    def __init__(self):
        self.__list = []

    def __str__(self):
        return '--'.join(map(str, reversed(self.__list)))

    def push(self, e):
        self.__list.append(e)
        return True

    def pop(self):
        if self.is_empty():
            return "Error no es posible desapilar, no hay elementos"
        return self.__list.pop()

    def top(self):
        if self.is_empty():
            return "Error no es posible leer el tope, no hay elementos"
        return self.__list[-1]

    def is_empty(self):
        return len(self.__list) == 0

    def len(self):
        return len(self.__list)

    def generate(self, num, min, max):
        for i in range(num):
            self.push(random.randint(min, max))

class Atraccion:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.visitantes = Stack()
    
    def __str__(self):
        return f"{self.nombre} ({self.capacidad}/turno): {self.visitantes}"


class ParqueDiversiones:
    def __init__(self):
        self.atracciones = Queue()
        self.contador_visitantes = 1
    
    def agregar_atraccion(self, nombre, capacidad):
        atr = Atraccion(nombre, capacidad)
        self.atracciones.enqueue(atr)
        print(f"Atraccion '{nombre}' agregada (capacidad: {capacidad}/turno) ")
    
    def agregar_visitante(self):
        if self.atracciones.is_empty():
            print("No hay atracciones para añadir visitantes")
            return
        visitante = f"V{self.contador_visitantes}"
        self.contador_visitantes += 1
        primera = self.atracciones.first()
        primera.visitantes.push(visitante)
        print(f"visitante {visitante} agregado a {primera.nombre}")
    
    def consultar_estado(self, n = None):
        if n is None:
            if self.atracciones.is_empty():
                print("No hay atracciones en el parque")
                return
            print("\n --- Estado del parque ---")
            n = self.atracciones.len()
        
        if n == 0:
            print(" --- Fin del estado --- \n")
            return
        
        atr = self.atracciones.dequeue()
        print(f"{atr.nombre} ({atr.capacidad}/turno): {atr.visitantes}")
        self.atracciones.enqueue(atr)

        self.consultar_estado(n - 1)

    
    def ejecutar_turno(self, n = None):
        if n is None:
            if self.atracciones.is_empty():
                print("No hay atracciones en el parque")
                return
            n = self.atracciones.len()
            print("\n === Ejecutando un turno ===")
        
        if n == 0:
            print("=== Fin del turno === \n")
            return
        
        atr = self.atracciones.dequeue()
        next_atr = None
        if n > 1:
            next_atr = self.atracciones.first()
        print(f"\n -- {atr.nombre} (capacidad {atr.capacidad}) --")

        def procesar_visitantes(capacidad):
            if capacidad == 0 or atr.visitantes.is_empty():
                return
            v = atr.visitantes.pop()
            if next_atr:
                next_atr.visitantes.push(v)
                print(f"Procesado {v} -> pasa a {next_atr.nombre}")
            else:
                print(f"Procesado {v} -> SALE del parque")
            procesar_visitantes(capacidad - 1)

        procesar_visitantes(atr.capacidad)
        print(f"En espera en {atr.nombre}: {atr.visitantes}")

        self.atracciones.enqueue(atr)
        self.ejecutar_turno(n - 1)


parque = ParqueDiversiones()
parque.agregar_atraccion("Montaña Rusa", 3)
parque.agregar_atraccion("Carros Chocones", 2)
parque.agregar_atraccion("Rueda de la Fortuna", 2)
parque.agregar_atraccion("Casa del Terror", 2)

for _ in range(5):
    parque.agregar_visitante()

parque.consultar_estado()

parque.ejecutar_turno()

parque.consultar_estado()