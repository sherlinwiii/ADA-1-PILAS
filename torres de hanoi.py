class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    
    def __str__(self):
        return f"{self.nombre}: {self.items}"

def hanoi(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        movimientos.append(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")
        return
    hanoi(n - 1, origen, auxiliar, destino, movimientos)
    hanoi(1, origen, destino, auxiliar, movimientos)
    hanoi(n - 1, auxiliar, destino, origen, movimientos)

def imprimir_torres(origen, auxiliar, destino):
    print(origen)
    print(auxiliar)
    print(destino)
    print("-")

origen = Pila("Origen")
auxiliar = Pila("Auxiliar")
destino = Pila("Destino")


for disco in range(3, 0, -1):
    origen.apilar(disco)


movimientos = []
hanoi(3, origen, destino, auxiliar, movimientos)


for movimiento in movimientos:
    print(movimiento)
    imprimir_torres(origen, auxiliar, destino)