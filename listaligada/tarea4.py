class Nodo:
    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

    def get_siguiente(self):
        return self.siguiente

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def set_dato(self, dato):
        self.dato = dato

class Smartphone:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        if self.cabeza is None:
            print('Está vacia')
        else:
            print('No está vacia')

    def get_tamanio(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.get_siguiente()
        return contador

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.get_siguiente() is not None:
                actual = actual.siguiente
            actual.set_siguiente(nuevo_nodo)

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def transversal(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=' --> ')
            actual = actual.get_siguiente()
        print('None')

    def agregar_despues_de(self, dato, referencia):
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        while actual.dato != referencia:
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_en_posicion(self, posicion):
        contador = 1
        actual = self.cabeza
        if posicion == 1:
            self.cabeza = actual.get_siguiente()
        else:
            while contador < posicion - 1:
                actual = actual.get_siguiente()
                contador += 1
            actual.set_siguiente(actual.get_siguiente().get_siguiente())

    def eliminar_el_primero(self):
        actual = self.cabeza
        self.cabeza = actual.get_siguiente()

    def eliminar_el_final(self):
        tamanio = self.get_tamanio()
        actual = self.cabeza
        contador = 2
        while contador < tamanio:
            actual = actual.get_siguiente()
            contador += 1
        actual.set_siguiente(None)

    def buscar_valor(self, dato):
        actual = self.cabeza
        contador = 1
        while actual.dato != dato:
            actual = actual.get_siguiente()
            contador += 1
        print(f'{dato} se encuentra en la posicion {contador}')

    def actualizar(self,a_buscar,dato):
        actual = self.cabeza
        while actual.dato != a_buscar:
            actual = actual.siguiente
        actual.set_dato(dato)