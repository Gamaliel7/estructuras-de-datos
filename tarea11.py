class Pila:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def length(self):
        return len(self.data)

    def pop(self):
        if not self.is_empty():
            return  self.data.pop()

    def peek(self):
        if not self.is_empty():
            return self.data[-1]

    def push(self, elemento):
        self.data.append(elemento)

    def __str__(self):
        return str(self.data)


pila = Pila()
pila.push(0)
pila.push(1)
pila.push(2)
pila.push(3)
pila.push(4)
pila.push(5)
pila.push(6)
pila.push(7)
pila.push(8)
print(pila)


def sacar_medio(pila, mitad = (pila.length() // 2), i = 0):
    if mitad == i:
        return f'Eliminado: {pila.pop()}'
    else:
        i += 1
        actual = pila.pop()
        eliminado = sacar_medio(pila, mitad, i)
        pila.push(actual)
    return eliminado


print(sacar_medio(pila))
print(pila)

#-----------------------------------------------------------------------------

def sumar_numeros(numeros):
    if not numeros:
        return 0
    else:
        return numeros[0] + sumar_numeros(numeros[1:])


lista_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'\nLa suma de los numeros {lista_num} es: {sumar_numeros(lista_num)}\n')


def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente <= -1:
        exponente = -exponente
        return 1/calcular_potencia(base, exponente)
    elif exponente >= 1:
        return base * calcular_potencia(base, exponente - 1)


print(f'\n3 elevado a -5 es: {calcular_potencia(3, -5)}\n')


def contador_regresivo(n):
    if n > 0:
        print(n)
        return contador_regresivo(n - 1)
    else:
        return 0


print(contador_regresivo(10))