def normal(x):
    return x

def cuadrado(x):  # esta x no tiene nada que ver con la de arriba, solo pertenence al ámbito de esta función (líneas 4 y 5)
    return x * x


def sumaTodos(limitTo, f):   # las funciones de primer nivel admiten funciones como parámetros de entrada
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)
    
    return resultado




print(sumaTodos(100, normal))
print(sumaTodos(3, cuadrado))