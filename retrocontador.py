# las funciones recursivas se llaman a sí mismas

def retrocontador(e):
    print("{},".format(e), end="")
    if e > 0:  # para que pare en cero
        retrocontador(e-1)
            
retrocontador(10)


    
    
    
