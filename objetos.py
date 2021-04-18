import turtle

tortuguita = turtle.Turtle()  # los objetos son funciones de primer nivel capaces de invocarse a si mismas y
                              # generar copias de si mismas

otraTortuguita = turtle.Turtle()

lentorra = turtle.Turtle()

tortuguita.shape('turtle')
tortuguita.color('blue')
tortuguita.speed(5)
tortuguita.fd(50)


otraTortuguita.color('green')
otraTortuguita.speed(5)
otraTortuguita.left(90)
otraTortuguita.fd(50)

lentorra.speed(1)