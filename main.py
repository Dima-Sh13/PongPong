import pygame as pg
from Clases import Raqueta, Pelota
from functions import rebote

pg.init()
x_display = 1050; y_display = 700
surface= pg.display.set_mode((x_display,y_display))
pg.display.set_caption("PongPing")

#Definir tasa de refresco en nuestro bucle.
tasaRefresco = pg.time.Clock()




raquetaI = Raqueta(10, 300,(255,255,255),w=20, h=100)
raquetaD = Raqueta(1020, 300,(255,255,255),w=20, h=100)

pelota1 = Pelota(525,350,(1,1,1),radio=10,vy=0)

game= True
while game:
    valorTasa = tasaRefresco.tick(300)#variable para controlar la velocidad entre tasas
    #Agregamos Marcadores.
    #Asignacion de tamanño y fuente
    
    marcador1_font = pg.font.SysFont("arial",30)
    marcador2_font = pg.font.SysFont("arial",30)

    marcador1 = marcador1_font.render("10", True, (255,255,255))
    
    surface.blit(marcador1,(200,100))
    
    

    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game = False

    estadoTeclado = pg.key.get_pressed()

    surface.fill(( 25, 133, 32))
    pg.draw.line(surface,(255,255,255),(515,0),(515,700),10)
    pg.draw.circle(surface,(255,255,255),(520,350), 120)
    pg.draw.circle(surface,( 25, 133, 32),(520,350), 110)
    pelota1.dibujar(surface)
    raquetaI.dibujar(surface)
    raquetaD.dibujar(surface)

    raquetaI.movimiento(pg.K_w,pg.K_s)
    raquetaD.movimiento(pg.K_UP, pg.K_DOWN)
    #pelota1.movimiento(x_display, y_display,raquetaI.pos_reb_x,raquetaI.p_rebote_Y,raquetaD.pos_reb_x - raquetaD.w,raquetaD.p_rebote_Y)
    pg.display.flip()


pg.quit()                

