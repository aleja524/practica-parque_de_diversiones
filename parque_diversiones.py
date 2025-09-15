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
