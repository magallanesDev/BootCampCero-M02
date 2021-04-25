class Objeto():
    __atributoPrivado = None
    atributoPublico = None
    
    def __init__(self):
        self.__atributoPrivado = 0
        self.atributoPublico = "me lo ha pedido Jorge"
        
    def atributoPrivado(self, valor = None):
        if valor == None:
            return self.__atributoPrivado
        else:
            self.__atributoPrivado = valor
        