# las funciones recursivas se llaman a sí mismas

def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0  # hay que poner 0 porque sino devolvería None y no se puede sumar None con enteros, daría error.


print(sumatorio(5))

    
    
    
