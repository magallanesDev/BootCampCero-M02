# las funciones recursivas se llaman a sí mismas

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1  # hay que poner 0 porque sino devolvería None y no se puede sumar None con enteros, daría error.


print(factorial(5))

    
    
    
