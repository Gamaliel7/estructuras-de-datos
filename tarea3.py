class Nodo:
    def __init__(self, dato, siguiente):
        self.dato = dato
        self.siguiente = siguiente

def imprimir(nodo):
    while nodo != None:
        print(nodo.dato, end=" -> ")
        nodo = nodo.siguiente
    print('None')

nodo5 = Nodo(600, None)
nodo4 = Nodo(400, nodo5)
nodo3 = Nodo(300, nodo4)
nodo2 = Nodo(200, nodo3)
nodo1 = Nodo(100, nodo2)
imprimir(nodo1)

nodo_cambio_valor = nodo1.siguiente.siguiente
nodo_cambio_valor.dato = 333
imprimir(nodo1)

nuevo_nodo = Nodo(700, None)
nodo1.siguiente.siguiente.siguiente.siguiente.siguiente = nuevo_nodo
imprimir(nodo1)

nodo1 = Nodo(50, nodo1)
imprimir(nodo1)