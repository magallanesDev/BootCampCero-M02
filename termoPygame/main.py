import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("images/termo1.png")
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
        
        return "{:10.2f}".format(resultado)  # máxima longitud 10 con 2 decimales


class Selector():
    __tipoUnidad = None
    
    def __init__(self, unidad = "C"):
        self.__customes = []
        self.__customes.append(pygame.image.load("images/posiF.png"))
        self.__customes.append(pygame.image.load("images/posiC.png"))
        self.__tipoUnidad = unidad
        
    def custome(self):
        if self.__tipoUnidad == "F":
            return self.__customes[0]
        else:
            return self.__customes[1]
    
    def unidad(self):
        return self.__tipoUnidad
      
    def change(self):
        if self.__tipoUnidad == 'F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
        
class NumberInput():
    __value = 0
    __strValue = ""
    __position = [0, 0]
    __size = [0, 0]
    __pointsCount = 0
    
    def __init__(self, value=""):
        self.__font = pygame.font.SysFont("Arial", 24)
        self.value(value)  # invocamos el método de más abajo para comprobar que sea un entero y transformar en cadena
                           # los métodos de una misma clase se leen todos a la vez, da igual el orden en el que los pongamos
    
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strValue) < 10 or (event.unicode == "." and self.__pointsCount == 0):  # comprobamos que sea un dígito y que quepa en el recuadro. Admitimos decimales con punto
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == ".":
                    self.__pointsCount += 1
            elif event.key == K_BACKSPACE:
                if self.__strValue[-1] == ".":  # penúltima posición
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[:-1]  # borramos el último dígito de la cadena
                self.value(self.__strValue)
                
    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74))
        rect = textBlock.get_rect()
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size
        
        return (rect, textBlock)   
    #   return {"fondo" : rect, "texto" : textBlock} se podría hacer así tb con un diccionario en vez de una lista
    
   
    def value(self, val=None):
        if val == None:  # GETTER
            return self.__value
        else:  # SETTER
            val = str(val)  # SETTER, lo transformamos en cadena (si fuera cadena no pasa nada)
            try:
                self.__value = float(val)  # lo transformamos en flotante
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount = 0
            except:
                pass
            
    def width(self, val=None):
        if val == None:  # GETTER
            return self.__size[0]
        else:  # SETTER
            try:
                self.__size[0] = int(val)
            except:
                pass        
    
    def height(self, val=None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass
    
    def size(self, val=None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
    
    def posX(self, val=None):
        if val == None:  
            return self.__position[0]
        else:  
            try:
                self.__position[0] = int(val)
            except:
                pass
 
    def posY(self, val=None):
        if val == None:  
            return self.__position[1]
        else:  
            try:
                self.__position[1] = int(val)
            except:
                pass
            
    def pos(self, val=None):
        if val == None:
            return self.__position
        else: 
            try:
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass


class MainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
       
        self.termometro = Termometro()
        self.entrada = NumberInput()
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28))
        
        self.selector = Selector()
        
   
    def __on_close(self):
        pygame.quit()
        sys.exit()
            
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                
                self.entrada.on_event(event)
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                
            # pintamos el fondo de pantalla
            self.__screen.fill((244, 236, 203))
            
            # pintamos el termómetro en su posición
            self.__screen.blit(self.termometro.custome, (50, 34))
            
            # pintamos el cuadro de texto
            text = self.entrada.render()  # obtenemos rectángulo blanco y foto de texto y lo asignamos a variable text
            pygame.draw.rect(self.__screen, (255, 255, 255), text[0])  # creamos el rectángulo blanco con sus datos (posición y tamaño) text[0] 
            self.__screen.blit(text[1], self.entrada.pos())  # pintamos la foto del texto
            
            # pintamos el selector
            self.__screen.blit(self.selector.custome(), (112, 153))
            
            pygame.display.flip()
            
        
        
if __name__ == '__main__':
    pygame.init()
    app = MainApp()
    app.start()
    