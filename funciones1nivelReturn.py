
def maxi(*l):   # l es un array (lista)
    if len(l) == 0: # si lista vacia
        return 0    # devolvemos 0
    
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    return m


def mini(*l):   # l es un array (lista)
    if len(l) == 0: # si lista vacia
        return 0    # devolvemos 0
    
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
    return m


def media(*l):
    if len(l) == 0:
        return 0
    
    suma = 0
    for valor in l:
        suma += valor
    
    return suma / len(l)



funciones = {
    'max': maxi,
    'min': mini,
    'med': media
    }

def returnF(nombre):
    nombre = nombre.lower()  # lower es para pasar a minúsculas
    if nombre in funciones.keys():  # keys nos saca un listado de claves
        return funciones[nombre]
    
    return None  # si esto se cumple va a dar un error pero bueno es solo un ejemplo

# las funciones de primer nivel admiten funciones como parámetros de entrada o su resultado es una función o ambas a la vez