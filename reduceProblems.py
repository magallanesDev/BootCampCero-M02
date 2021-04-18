from functools import reduce

##### ejemplos de funciones clásicas #######
def sumatorioClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor
    
    return resultado


def sumatorioDobleClasico(l):
    resultado = 0
    for valor in l:
        resultado += valor * 2
    
    return resultado


def productoTotal(l):
    resultado = 1
    for valor in l:
        resultado *= valor
        
    return resultado
#############################################

lista = [1, 3, -1, 15, 9]

sumatorio = reduce(lambda x,y: x+y, lista)

# creo una copia de la lista, clonamos la lista
l = lista[:]
# añado el neutro para la suma (0) en la posición cero de la lista
l.insert(0,0)
sumatorioDobles = reduce(lambda x,y: x + y*2, l)

print(sumatorio)
print(sumatorioDobles)

