
class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def _init_(self):
        self.cabeza = None


    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")


lista = ListaEnlazada()
lista.insertar_al_final(10)
lista.insertar_al_final(20)
lista.insertar_al_final(30)
lista.mostrar()