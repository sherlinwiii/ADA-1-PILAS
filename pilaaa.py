class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

def evaluar_posfija(expresion):
    pila = Pila()
    operadores = {'+', '-', '*', '/'}
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        elif token in operadores:
            b = pila.desapilar()
            a = pila.desapilar()
            resultado = eval(f"{a} {token} {b}")
            pila.apilar(resultado)
    return pila.desapilar()

def evaluar_prefija(expresion):
    pila = Pila()
    operadores = {'+', '-', '*', '/'}
    for token in reversed(expresion.split()):
        if token.isdigit():
            pila.apilar(int(token))
        elif token in operadores:
            a = pila.desapilar()
            b = pila.desapilar()
            resultado = eval(f"{a} {token} {b}")
            pila.apilar(resultado)
    return pila.desapilar()

modo = input("Ingrese 'posfija' o 'prefija': ").strip().lower()
expresion = input("Ingrese la expresión: ").strip()

if modo == "posfija":
    print("Resultado:", evaluar_posfija(expresion))
elif modo == "prefija":
    print("Resultado:", evaluar_prefija(expresion))
else:
    print("Modo no válido")

