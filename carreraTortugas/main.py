import turtle
import random

class Circuito():
    # los atributos tb pueden ir fuera de la función constructora como aquí. No se pone self pero es como si lo llevaran implícito
    corredores = []  # lista vacia
    __posStartY = (-30, -10, 10, 30)  # daría igual que fuera público porque es una tupla inmutable
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__createRunners()  # invocamos desde el constructor esta función que se define más abajo
        
    
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()  # levantamos lápiz para que no salga una raya en el posicionamiento de las tortugas en línea salida
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
    
    
    def competir(self):
        hayGanador = False
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1, 6)  # simulamos el lanzamiento de un dado
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
                    break  # forzamos la salida del bucle si ya hay ganador


if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()