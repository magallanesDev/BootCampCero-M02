from functools import reduce  # map y filter están predefinidas, reduce hay que imnportarla

lista = [1, 3, -1, 15, 9]

listaDobles = map(lambda x: x*2, lista)

listaPares = filter(lambda x: x % 2 == 0, lista)


sumatorio = reduce(lambda x, y: x + y, lista)  # reduce a un solo valor con la función aplicada (x+y)

suma100 = reduce(lambda x,y: x+y, range(101))  # suma los 100 primeros números