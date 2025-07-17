import pygame as pg

from Clases import Raqueta, Pelota
screenX = 1050
screenY = 700

class Partida:  
    def __init__(self):
        pg.init()
        self.mainScreen = pg.display.set_mode((screenX,screenY))
        pg.display.set_caption("PongPing")
        self.tasa_refresco = pg.time.Clock()

        self.pelota1 = Pelota(screenX//2, screenY//2,(1,1,1), 10)
        self.raquetaI = Raqueta(0,330,w=20,h=100)
        self.raquetaD = Raqueta(1030,330,w=20,h=100)

    def buclePartida(self):
        gameOn = True
        while gameOn:
            marcador1_font = pg.font.SysFont("arial",30)
            marcador2_font = pg.font.SysFont("arial",30)

            marcador1 = marcador1_font.render("10", True, (255,255,255))
            
            #self.mainScreen(marcador1,(200,100))
            
            

            for eventos in pg.event.get():
                #print(eventos)
                if eventos.type == pg.QUIT:
                    gameOn = False

            estadoTeclado = pg.key.get_pressed()

            self.mainScreen.fill(( 25, 133, 32))
            pg.draw.line(self.mainScreen,(255,255,255),(515,0),(515,700),10)
            pg.draw.circle(self.mainScreen,(255,255,255),(520,350), 120)
            pg.draw.circle(self.mainScreen,( 25, 133, 32),(520,350), 110)
            self.pelota1.dibujar(self.mainScreen)
            self.raquetaI.dibujar(self.mainScreen)
            self.raquetaD.dibujar(self.mainScreen)

            self.raquetaI.movimiento(pg.K_w,pg.K_s)
            self.raquetaD.movimiento(pg.K_UP, pg.K_DOWN)
            #pelota1.movimiento(x_display, y_display,raquetaI.pos_reb_x,raquetaI.p_rebote_Y,raquetaD.pos_reb_x - raquetaD.w,raquetaD.p_rebote_Y)
            pg.display.flip()

    pg.quit()



juego = Partida()
juego.buclePartida()