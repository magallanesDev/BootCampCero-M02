from functools import reduce  # map y filter están predefinidas, reduce hay que imnportarla

lista = [1, 3, -1, 15, 9]


listaDobles = map(lambda x: x*2, lista)

def doble(x):
    return x*2

listaDobles1 = map(doble, lista)  # Daría el mismo resultado que la lista anterior


listaPares = filter(lambda x: x % 2 == 0, lista)

def esPar(x):
    return x % 2 == 0

listaPares1 = filter(esPar, lista)  # Daría el mismo resultado que la lista anterior


sumatorio = reduce(lambda x, y: x + y, lista)  # reduce a un solo valor con la función aplicada (x+y)

suma100 = reduce(lambda x,y: x+y, range(101))  # suma los 100 primeros números


print(list(listaDobles))
print(list(listaDobles1))

print(list(listaPares))
print(list(listaPares1))

print(sumatorio)
print(suma100)