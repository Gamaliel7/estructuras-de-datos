class NodoDoble:
    def __init__(self, dato, anterior = None, siguiente = None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente

    def get_dato(self):
        return self.dato

    def get_siguiente(self):
        return self.siguiente

    def get_anterior(self):
        return self.anterior

    def set_anterior(self, anterior):
        self.anterior = anterior

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def set_dato(self, dato):
        self.dato = dato

class DoubleLinkedList:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        if self.cabeza is None:
            vacia = True
        else:
            vacia = False
        return vacia

    def get_tamanio(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def agregar_al_inicio(self, dato):

        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def agregar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def agregar_despues_de(self, referencia, dato):
        nuevo_nodo = NodoDoble(dato)
        actual = self.cabeza
        while actual.dato != referencia:
            actual = actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente = nuevo_nodo

    def obtener_pocicion(self, posicion):
        contador = 2
        actual = self.cabeza
        if posicion > 1:
            while contador < posicion + 1:
                actual = actual.siguiente
                contador += 1
        print(f'En la posicion {posicion} se encuentra {actual.get_dato()}')

    def eleminar_el_primero(self):
        actual = self.cabeza
        self.cabeza = actual.get_siguiente()

    def eliminar_el_final(self):
        self.cola = self.cola.anterior
        self.cola.siguiente = None

    def eliminar_posicion(self, posicion):
        actual = self.cabeza
        contador = 1
        if posicion == 1:
            self.cabeza = actual.get_siguiente()
        else:
            while contador < posicion - 1:
                actual = actual.get_siguiente()
                contador += 1
            actual.set_siguiente(actual.get_siguiente().get_siguiente())

    def buscar_valor(self, dato):
        actual = self.cabeza
        contador = 1
        while actual.dato != dato:
            actual = actual.get_siguiente()
            contador += 1
        print(f'{dato} se encuentra en la posicion {contador}')

    def actualizar(self,a_buscar,dato):
        contador = 1
        actual = self.cabeza
        if a_buscar > 1:
            while contador < a_buscar:
                actual = actual.get_siguiente()
                contador += 1
        actual.set_dato(dato)

    def transversal(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato, end=' --> ')
            actual = actual.get_siguiente()
        print('None')