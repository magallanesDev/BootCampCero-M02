import pygame, sys, random
from pygame.locals import *  # importamos todo de locals de PyGame


class Runner():
    __customes = ('turtle', 'fish', 'prawn', 'moray', 'octopus')  # lista de disfraces
    
    def __init__(self, x=0, y=0):
        ixCustome = random.randint(0, 4)  # asignamos disfraces de manera aleatoria
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        
        
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))  # creamos la pantalla
        self.__background = pygame.image.load("images/background.png")  # cargamos imagen de fondo
        pygame.display.set_caption("Carrera de bichos")  # título de la pantalla 
        self.runner = Runner(320, 240)    
    
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:  # flecha arriba - mover hacia arriba el runner
                        self.runner.position[1] -= 5
                    elif event.key == K_DOWN:  # flecha abajo - mover hacia abajo el runner
                        self.runner.position[1] += 5
                    elif event.key == K_LEFT:  # flecha izquierda - mover hacia izquierda el runner
                        self.runner.position[0] -= 5
                    elif event.key == K_RIGHT:  # flecha derecha - mover hacia derecha el runner
                        self.runner.position[0] += 5
                    else:
                        pass
                    
            self.__screen.blit(self.__background, (0, 0))  
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
                    
           
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.start()
            
