class Perro():  # por convenio las clase empiezan por mayúsculas, igual que Turtle()
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("ay, ay")
        
    def __str__(self):   # esta función devuelve una cadena cuando le pedimos un Print
        return "Perro {}, edad: {}, peso: {}".format(self.nombre, self.edad, self.peso)
    


class PerroAsistencia(Perro):  # sería una subclase de Perro, hereda sus propiedades
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        self.__trabajando = False  # por defecto False. Escondemos el atributo poniendo los dos guiones delante. Lo definimos más adelante
        
    def __str__(self):  # sobreescribimos el método de jerarquía superior (clase Perro)
        return "Perro de asistencia de {}".format(self.amo)
    
    def pasear(self):
        print("{} ayudo a mi dueño {} a pasear".format(self.nombre, self.amo))
        
    def ladrar(self):  # aquí tb sobreescribimos el método de la clase superior Perro
        if self.trabajando:
            print("shhhh, no puedo ladrar")
        else:
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):  # creamos método getter / setter
        if valor == None:
            return self.__trabajando
        else:
            self.__trabajando = valor
    

    
    
    
