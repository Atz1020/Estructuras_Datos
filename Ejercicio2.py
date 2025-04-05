class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def _init_(self):
        self.tope = None

        
    def push(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def mostrar(self):
        actual = self.tope
        while actual:
            print(actual.valor)
            actual = actual.siguiente


pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
pila.mostrar()