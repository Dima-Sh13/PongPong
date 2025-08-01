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
        self.font_font_main = pg.font.SysFont("Pixellari", 60)
        self.font_menu = 60
        self.posicion_bloque = screenY//2+15
        self.counter = 0
        self.color_bloque = color_blanco
       
        
        
    def menu_main(self):
            self.font_main = self.font_font_main.render("Play", True, color_blanco)
            self.font_main2 = self.font_font_main.render("Settings", True, color_blanco)
            self.font_main3 = self.font_font_main.render("Records", True, color_blanco)
            self.font_main4 = self.font_font_main.render("Quit", True, color_blanco)



            self.menuScreen.blit(self.font_main, (screenX//3,screenY//2))
            self.menuScreen.blit(self.font_main2,(screenX//3,screenY//2 +self.font_menu) )
            self.menuScreen.blit(self.font_main3,(screenX//3,screenY//2 +self.font_menu*2) )
            self.menuScreen.blit(self.font_main4,(screenX//3,screenY//2 +self.font_menu*3) )
            pg.draw.rect(self.menuScreen,self.color_bloque,(screenX//3 - 30,self.posicion_bloque,15,15))
            if self.counter < 300:
                    self.color_bloque = color_blanco
            if self.counter > 600:
                self.color_bloque = color_campo
                self.counter = 0        
            self.counter += 1        
    def menu_setting(self):
        self.font_setting1 = self.font_font_main.render("Ball Speed", True, color_blanco)
        self.font_setting2 = self.font_font_main.render("Paddle Size",True, color_blanco)
        self.font_setting3 = self.font_font_main.render("Music", True,color_blanco)
        self.font_setting4 = self.font_font_main.render("Back", True, color_blanco)
        self.menuScreen.blit(self.font_setting1, (screenX//3,screenY//2))
        self.menuScreen.blit(self.font_setting2,(screenX//3,screenY//2 +self.font_menu) )
        self.menuScreen.blit(self.font_setting3,(screenX//3,screenY//2 +self.font_menu*2) )
        self.menuScreen.blit(self.font_setting4,(screenX//3,screenY//2 +self.font_menu*3) )
        pg.draw.rect(self.menuScreen,self.color_bloque,(screenX//3 - 30,self.posicion_bloque,15,15))
        
        if self.counter < 300:
                    self.color_bloque = color_blanco
        if self.counter > 600:
                self.color_bloque = color_campo
                self.counter = 0        
        self.counter += 1        
    def menu_ball_speed(self):
        self.font_setting_ball = self.font_font_main.render("Slow", True, color_blanco)
        self.font_setting_ball2 = self.font_font_main.render("Normal", True, color_blanco)
        self.font_setting_ball3 = self.font_font_main.render("Fast", True, color_blanco)
        self.font_setting_ball4 = self.font_font_main.render("Back", True, color_blanco)
        self.menuScreen.blit(self.font_setting_ball, (screenX//3,screenY//2))
        self.menuScreen.blit(self.font_setting_ball2,(screenX//3,screenY//2 +self.font_menu) )
        self.menuScreen.blit(self.font_setting_ball3,(screenX//3,screenY//2 +self.font_menu*2) )
        self.menuScreen.blit(self.font_setting_ball4,(screenX//3,screenY//2 +self.font_menu*3) )
        pg.draw.rect(self.menuScreen,self.color_bloque,(screenX//3 - 30,self.posicion_bloque,15,15))



        if self.counter < 300:
                    self.color_bloque = color_blanco
        if self.counter > 600:
                self.color_bloque = color_campo
                self.counter = 0        
        self.counter += 1        

    def bucleMenuV2(self):
        gameOn = True
        menuMain = True
        menuSettings = False
        menuBallSpeed = False
        while gameOn:
            estadoTeclado = pg.key.get_pressed()
            self.tasa_refresco.tick(self.valor_tasa_refresco)
           
            for eventos in pg.event.get():
                if eventos.type == pg.KEYDOWN:
                    if eventos.key == pg.K_RETURN and self.posicion_bloque == screenY//2 +15 :
                        if menuMain == True:
                            juego.buclePartida()
                        elif menuSettings == True:
                             menuSettings = False
                             menuBallSpeed = True
                        elif menuBallSpeed == True:
                             juego.valor_tasa_refresco = 150
                             menuBallSpeed = False
                             menuSettings = True         
                    
                    elif eventos.key == pg.K_RETURN and self.posicion_bloque == screenY//2 + (self.font_menu + 15):
                        menuMain = False
                        menuSettings = True
                        if menuBallSpeed == True:
                            juego.valor_tasa_refresco = 200
                            menuBallSpeed = False
                            menuSettings = True 

                        
                    
                    elif eventos.key == pg.K_RETURN and self.posicion_bloque == screenY//2 + (self.font_menu*2 + 15):
                        if menuBallSpeed == True:
                            juego.valor_tasa_refresco = 250
                            menuBallSpeed = False
                            menuSettings = True 
                    
                    elif eventos.key == pg.K_RETURN and self.posicion_bloque == screenY//2 + (self.font_menu*3 + 15):
                        if menuMain == True:
                            gameOn = False
                        elif menuSettings == True:
                             menuMain = True
                             menuSettings = False 
                        elif menuBallSpeed == True:
                             menuSettings = True
                             menuBallSpeed = False
                if eventos.type == pg.QUIT:
                    gameOn = False
                if eventos.type == pg.KEYDOWN:
                    if eventos.key == pg.K_DOWN:
                       if self.posicion_bloque < screenY//2 +self.font_menu*3:
                            self.posicion_bloque += 60
                    if eventos.key == pg.K_UP:
                        if self.posicion_bloque > screenY//2 +self.font_menu:
                            self.posicion_bloque -= 60

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
            if menuMain == True:
                self.menu_main()  
            if menuSettings == True:
                self.menu_setting()
            if menuBallSpeed == True:
                 self.menu_ball_speed()       
            
                        
                  
            pg.display.flip()

class PartidaSolo(Partida):
    def __init__(self):
        pg.init()
        self.mainScreen = pg.display.set_mode((screenX,screenY))
        pg.display.set_caption("PongPing")
        self.tasa_refresco = pg.time.Clock()

        self.pelota1 = Pelota(screenX//2, screenY//2, radio=15) 
        self.raquetaI = Raqueta(0,330,w=20,h=100)
        self.raquetaD = Raqueta(1030,0,w=20,h=700)
        self.valor_tasa_refresco = 200
        self.counter = 0

    def buclePartida(self):
        gameOn = True
        round = False
        while gameOn:
            self.tasa_refresco.tick(self.valor_tasa_refresco)
            
            for eventos in pg.event.get():
                
                if eventos.type == pg.QUIT:
                    gameOn = False

            estadoTeclado = pg.key.get_pressed()

            self.mainScreen.fill((  28, 126, 28))
            for i in range(0,screenY +20,20):
                pg.draw.line(self.mainScreen,color_blanco,(screenX//2,0 + i),(screenX//2,i+10),10)
            pg.draw.circle(self.mainScreen,color_blanco,(screenX//2,screenY//2), 120)
            pg.draw.circle(self.mainScreen,( 25, 133, 32),(screenX//2,screenY//2), 110)
            self.pelota1.mostrar_marcador_solo(self.mainScreen, self.counter)

            self.pelota1.dibujar(self.mainScreen)
            self.raquetaI.dibujar(self.mainScreen)
            self.raquetaD.dibujar(self.mainScreen)

            
            self.raquetaI.movimiento(pg.K_w,pg.K_s)
            self.raquetaD.movimiento(pg.K_UP, pg.K_DOWN)
            self.pelota1.mover(screenX, screenY)
            

            self.pelota1.comprobar_choqueV3(self.raquetaD, self.raquetaI)
            

            self.counter += 1
            if self.counter > 201:
                self.counter = 0
            
            
            print(self.pelota1.puntuacion_solo)
            
            pg.display.flip()

    pg.quit()











juegoSolo = PartidaSolo()
juego= Partida()
#juego.buclePartida()
menu = MenuV2()
menu2 = MenuV2()
menu2.bucleMenuV2()

            