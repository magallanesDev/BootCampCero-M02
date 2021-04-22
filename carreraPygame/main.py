import pygame
import sys
import random


class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/turtle.png")
        self.position = [x, y]
        self.name = "Tortuga"
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
    
    

class Game():
    runners = []
    __startLine = 5
    __finishLine = 620
      
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))  # creamos la pantalla
        pygame.display.set_caption("Carrera de bichos")  # título de la pantalla
        self.__background = pygame.image.load("images/background.png")  # cargamos imagen de fondo
        
        firstRunner = Runner(self.__startLine, 240)
        firstRunner.name = 'Speedy'
        self.runners.append(firstRunner)
        
        
    def competir(self):
        gameOver = False 
        while not gameOver:   
            # comprobación de los eventos (siempre hay que hacerlo en PyGame)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            self.runners[0].avanzar()
            
            if self.runners[0].position[0] >= self.__finishLine:
                print("{} ha ganado".format(self.runners[0].name))
                gameOver = True
                                            
            # refrescar / renderizar la pantalla
            self.__screen.blit(self.__background, (0, 0))  # esquina superior izda. en PyGame
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            pygame.display.flip()
                
        pygame.quit()
        sys.exit()
        
        
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    