import pygame as pg

from PongPingApp.Clases import Pelota, Raqueta
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
        self.valor_tasa_refresco = 200

    def buclePartida(self):
        gameOn = True
        round = False
        while gameOn:
            self.tasa_refresco.tick(self.valor_tasa_refresco)
            
            for eventos in pg.event.get():
                #print(eventos)
                if eventos.type == pg.QUIT:
                    gameOn = False

            estadoTeclado = pg.key.get_pressed()

            self.mainScreen.fill((  28, 126, 28))
            for i in range(0,screenY +20,20):
                pg.draw.line(self.mainScreen,color_blanco,(screenX//2,0 + i),(screenX//2,i+10),10)
            pg.draw.circle(self.mainScreen,color_blanco,(screenX//2,screenY//2), 120)
            pg.draw.circle(self.mainScreen,( 25, 133, 32),(screenX//2,screenY//2), 110)
            self.pelota1.mostrar_marcador(self.mainScreen)

            self.pelota1.dibujar(self.mainScreen)
            self.raquetaI.dibujar(self.mainScreen)
            self.raquetaD.dibujar(self.mainScreen)

            
            self.raquetaI.movimiento(pg.K_w,pg.K_s)
            self.raquetaD.movimiento(pg.K_UP, pg.K_DOWN)
            self.pelota1.mover(screenX, screenY)
            

            self.pelota1.comprobar_choqueV3(self.raquetaD, self.raquetaI)
            

            
            
            
            
            
            pg.display.flip()

    pg.quit()
            
class Menu:
    def __init__(self):
        pg.init()
        self.menuScreen = pg.display.set_mode((screenX,screenY))
        pg.display.set_caption("PongPing")
        self.font_title = pg.font.SysFont("Pixellari", 175)
        self.font_context = pg.font.SysFont("Pixellari", 75)
        self.fontont = self.font_title.render("Pong Ping", True, color_blanco)
        self.tasa_refresco = pg.time.Clock()
        self.valor_tasa_refresco = 5
        self.context = self.font_context.render("Press Any Key", True, color_blanco)
        
    def bucleMenu(self):
        gameOn = True
        p_y= 10
        counter = 0
        while gameOn:
            self.tasa_refresco.tick(self.valor_tasa_refresco)
            for eventos in pg.event.get():
                if eventos.type == pg.KEYDOWN:
                    juego.buclePartida()
                if eventos.type == pg.QUIT:
                    gameOn = False
            
            self.menuScreen.fill(color_negro)
            p_y += 10
            for i in range(20-p_y, screenX+p_y,50):
                pg.draw.circle(self.menuScreen,color_blanco,(i,0), 5)
                for x in range(0, screenY+100, 50):
                    pg.draw.circle(self.menuScreen,color_blanco,(i,x), 5)
                
            
            self.menuScreen.blit(self.fontont,(150,150))
            if counter %5 != 0:
                self.menuScreen.blit(self.context, (250, 450))
                        
            counter += 1
            

            
            pg.display.flip()
            

    pg.quit()        

class MenuV2:
    def __init__(self):
        pg.init()
        self.menuScreen = pg.display.set_mode((screenX,screenY))
        pg.display.set_caption("PongPing")
        self.tasa_refresco = pg.time.Clock()
        self.pelota1 = Pelota(screenX//2, screenY//2, radio=15) 
        self.raquetaI = Raqueta(0,self.pelota1.pos_y-50,w=20,h=100)
        self.raquetaD = Raqueta(1030,self.pelota1.pos_y-50,h=100)
        self.valor_tasa_refresco = 300
        self.font_title = pg.font.SysFont("Pixellari", 175)
        self.font_context = pg.font.SysFont("Pixellari", 75)
        self.fontont = self.font_title.render("Pong Ping", True, color_blanco)
        self.context = self.font_context.render("Press Any Key", True, color_blanco)
        self.transparencia = pg.Surface((1050, 700) )
        self.transparencia.fill( ( 91, 98, 91 ) )
        self.transparencia.set_alpha(200)


    def bucleMenuV2(self):
        gameOn = True
        counter = 0
        while gameOn:
            self.tasa_refresco.tick(self.valor_tasa_refresco)
            
            for eventos in pg.event.get():
                
                if eventos.type == pg.KEYDOWN:
                    juego.buclePartida()
                
                if eventos.type == pg.QUIT:
                    gameOn = False

            estadoTeclado = pg.key.get_pressed()

            self.menuScreen.fill((  28, 126, 28))
            for i in range(0,screenY +20,20):
                pg.draw.line(self.menuScreen,color_blanco,(screenX//2,0 + i),(screenX//2,i+10),10)
            pg.draw.circle(self.menuScreen,color_blanco,(screenX//2,screenY//2), 120)
            pg.draw.circle(self.menuScreen,( 25, 133, 32),(screenX//2,screenY//2), 110)
            self.pelota1.dibujar(self.menuScreen)
            self.raquetaI.dibujar(self.menuScreen)
            self.raquetaD.dibujar(self.menuScreen)

            self.raquetaI.movimientoMenu(self.pelota1.pos_y)
            self.raquetaD.movimientoMenu(self.pelota1.pos_y)
            self.pelota1.moverMenu(screenX, screenY)
            

            self.pelota1.comprobar_choqueV2(self.raquetaD, self.raquetaI)
            self.menuScreen.blit(self.transparencia,(0,0))
            self.menuScreen.blit(self.fontont,(150,150))
            
            if counter < 300:
                    self.menuScreen.blit(self.context, (screenX//4, 450))
            if counter > 600:
                counter = 0        
            counter += 1
            
            posicionRaton = pg.mouse.get_pos()
            print(posicionRaton)
            if posicionRaton == (100,100):
                print("esto pasa")
            

            pg.display.flip()
            










juego = Partida()
menu = Menu()
menu2 = MenuV2()
menu2.bucleMenuV2()
