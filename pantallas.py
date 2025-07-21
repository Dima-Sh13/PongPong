import pygame as pg

from PongPingApp.Clases import Raqueta, Pelota
from PongPingApp.utils import *

class Partida:  
    def __init__(self):
        pg.init()
        self.mainScreen = pg.display.set_mode((screenX,screenY))
        pg.display.set_caption("PongPing")
        self.tasa_refresco = pg.time.Clock()

        self.pelota1 = Pelota(screenX//2, screenY//2, radio=15)
        self.raquetaI = Raqueta(0,330,w=20,h=100)
        self.raquetaD = Raqueta(1030,330,w=20,h=100)
        self.valor_tasa_refresco = 100

    def buclePartida(self):
        gameOn = True
        while gameOn:
            self.tasa_refresco.tick(self.valor_tasa_refresco)
            
            for eventos in pg.event.get():
                #print(eventos)
                if eventos.type == pg.QUIT:
                    gameOn = False

            estadoTeclado = pg.key.get_pressed()

            self.mainScreen.fill(( 25, 133, 32))
            for i in range(0,screenY +20,20):
                pg.draw.line(self.mainScreen,color_blanco,(screenX//2,0 + i),(screenX//2,i+10),10)
            pg.draw.circle(self.mainScreen,color_blanco,(screenX//2,screenY//2), 120)
            pg.draw.circle(self.mainScreen,( 25, 133, 32),(screenX//2,screenY//2), 110)
            self.pelota1.dibujar(self.mainScreen)
            self.raquetaI.dibujar(self.mainScreen)
            self.raquetaD.dibujar(self.mainScreen)

            self.raquetaI.movimiento(pg.K_w,pg.K_s)
            self.raquetaD.movimiento(pg.K_UP, pg.K_DOWN)
            self.pelota1.mover(screenX, screenY)

            self.pelota1.comprobar_choqueV2(self.raquetaD, self.raquetaI)
            self.pelota1.mostrar_marcador(self.mainScreen)
            
            
            
            
            pg.display.flip()

    pg.quit()
            

            




juego = Partida()
juego.buclePartida()