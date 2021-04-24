import pygame
import sys
import random


class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')  # lista de disfraces
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)  # asignamos disfraces de manera aleatoria
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
    
    
class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ('Speedy', 'Lucera', 'Alonso', 'Torcuata')
    __startLine = 5
    __finishLine = 620
      
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))  # creamos la pantalla
        self.__background = pygame.image.load("images/background.png")  # cargamos imagen de fondo
        pygame.display.set_caption("Carrera de bichos")  # título de la pantalla
        
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
        
    def close(self):
        pygame.quit()
        sys.exit()
        
    
    def competir(self):
        gameOver = False 
        while not gameOver:   
            # comprobación de los eventos (siempre hay que hacerlo en PyGame)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
                                            
            # refrescar / renderizar la pantalla
            self.__screen.blit(self.__background, (0, 0))  # esquina superior izda. en PyGame
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
                
            pygame.display.flip()
                
        
        while True:  # esto sería un bucle infinito, siempre es True, pero saldríamos con el método close
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
        
        
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    