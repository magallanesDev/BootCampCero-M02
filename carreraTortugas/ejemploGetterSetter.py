class ClaseConGetterSetter():
    def __init__(self):
        self.__propiedad_privada = None
        
    def setPropiedadPrivada(self, valor):  # Actúa como SETTER asignando un valor
        self.__propiedad_privada = valor
        
    def getPropiedadPrivada(self):  # Actúa como GETTER informándonos del valor
        return self.__propiedad_privada
    
    def propiedadPrivada(self, valor = None):  # Esta función actúa como GETTER o SETTER
        if valor == None:
            return self.__propiedad_privada  # GETTER
        else:
            self.__propiedad_privada = valor  # SETTER
        
        
    def __str__(self):
        return "ClaseConGetterSetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
    
    
    
if __name__ == 'main':
    c = ClaseConGetterSetter()