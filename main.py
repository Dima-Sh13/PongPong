import pygame as pg
from Clases import Figura, Raqueta, Pelota
pg.init()
x_display = 1050; y_display = 700
surface= pg.display.set_mode((x_display,y_display))
pg.display.set_caption("Pong")
raquetaI = Raqueta(10, 300,(255,255,255),w=20, h=100)
raquetaD = Raqueta(1020, 300,(255,255,255),w=20, h=100)

pelota1 = Pelota(525,350,(1,1,1),radio=10)

game= True
while game:
    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game = False

    surface.fill(( 25, 133, 32))
    pg.draw.line(surface,(255,255,255),(515,0),(515,700),10)
    pg.draw.circle(surface,(255,255,255),(520,350), 150)
    pg.draw.circle(surface,( 25, 133, 32),(520,350), 140)
    pelota1.dibujar(surface)
    raquetaI.dibujar(surface)
    raquetaD.dibujar(surface)

    pg.display.flip()


pg.quit()                

