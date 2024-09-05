from tarea4 import *

smartphones = Smartphone() # Se crea la lista de objetos
smartphones.agregar_al_final('Samsung')
smartphones.agregar_al_final('Xiaomi')
smartphones.agregar_al_final('Iphone')
smartphones.agregar_al_final('Huawei')
smartphones.agregar_al_final('Motorola')
smartphones.transversal()
smartphones.eliminar_en_posicion(2)
smartphones.transversal()
smartphones.actualizar('Motorola', 'LG')
smartphones.agregar_al_inicio('Pixel')
smartphones.agregar_al_final('Lenovo')
smartphones.transversal()
smartphones.eliminar_el_primero()
smartphones.transversal()