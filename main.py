import pygame as pg
from Clases import Figura, Raqueta, Pelota
pg.init()
x_display = 1050; y_display = 700
surface= pg.display.set_mode((x_display,y_display))
pg.display.set_caption("Pong")

#Definir tasa de refresco en nuestro bucle.
tasaRefresco = pg.time.Clock()




raquetaI = Raqueta(10, 300,(255,255,255),w=20, h=100)
raquetaD = Raqueta(1020, 300,(255,255,255),w=20, h=100)

pelota1 = Pelota(525,350,(1,1,1),radio=10)

game= True
while game:
    valorTasa = tasaRefresco.tick(300)#variable para controlar la velocidad entre tasas
    
    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game = False
    estadoTeclado = pg.key.get_pressed()
    #print(estadoTeclado[pg.K_UP])
    """
    if estadoTeclado[pg.K_w] == True:
        raquetaI.pos_y -= 0.50
    if estadoTeclado[pg.K_s] == True:
        raquetaI.pos_y += 0.50   

    if estadoTeclado[pg.K_UP] == True:
        raquetaD.pos_y -= 0.50
    if estadoTeclado[pg.K_DOWN] == True:
        raquetaD.pos_y += 0.50
    """           
    surface.fill(( 25, 133, 32))
    pg.draw.line(surface,(255,255,255),(515,0),(515,700),10)
    pg.draw.circle(surface,(255,255,255),(520,350), 150)
    pg.draw.circle(surface,( 25, 133, 32),(520,350), 140)
    pelota1.dibujar(surface)
    raquetaI.dibujar(surface)
    raquetaD.dibujar(surface)

    raquetaI.movimiento(pg.K_w,pg.K_s)
    raquetaD.movimiento(pg.K_UP, pg.K_DOWN)
    pelota1.movimiento(x_display, y_display)

    pg.display.flip()


pg.quit()                

