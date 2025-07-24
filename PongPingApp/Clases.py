import pygame as pg
import random as ra
from PongPingApp.utils import *


class Raqueta:
    def __init__(self, pos_x, pos_y, color = color_blanco, w=20, h=100):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w =w
        self.h = h
        self.pos_reb_x_I = self.pos_x + self.w
        self.pos_reb_x_D = self.pos_x 
        self.p_rebote_Y =[self.pos_y,self.pos_y+self.h]
        
    def dibujar(self, surface):
        pg.draw.rect(surface,self.color,(self.pos_x,self.pos_y,self.w,self.h))    
        pg.draw.rect(surface,color_negro,(self.pos_x+5,self.pos_y+5,self.w-10,self.h-10))
    
    def movimiento(self, keyy_U, keyy_D):
        self.p_rebote_Y =[self.pos_y,self.pos_y+self.h]
        estadoTeclado = pg.key.get_pressed()
        if estadoTeclado[keyy_U] == True and self.pos_y > 0:
            self.pos_y -= 1
        if estadoTeclado[keyy_D] == True and self.pos_y < screenY - self.h:
            self.pos_y += 1 
    def movimientoMenu(self, pos_pelota):
        self.pos_y = pos_pelota - 50
    @property


    def derecha(self):

        return self.pos_x + (self.w//2)

    @property

    def izquierda(self):

        return self.pos_x - (self.w//2)

    @property

    def arriba(self):

        return self.pos_y - (self.h//2)

    @property

    def abajo(self):

        return self.pos_y + (self.h//2)     

class Pelota:
    def __init__(self, pos_x, pos_y, color = color_negro,radio =20, vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.p_rebote_Y_U = self.pos_y - radio
        self.p_rebote_Y_D = self.pos_y + radio
        self.round = False
        
    def dibujar(self,surface):
        pg.draw.circle(surface,self.color,(self.pos_x, self.pos_y), self.radio)
        pg.draw.circle(surface,color_blanco,(self.pos_x, self.pos_y), self.radio-5)
        
           
    def mover(self,x_max=screenX,y_max=screenY):
        estadoTeclado = pg.key.get_pressed()
        
        if estadoTeclado[pg.K_SPACE]:
            self.round = True     
        
        if self.round == True:
            self.pos_x += self.vx

            self.pos_y += self.vy



            if self.pos_x >= x_max+(5*self.radio) or self.pos_x <=0-(5*self.radio):

                if self.pos_x >= x_max+(5*self.radio):

                    self.puntuacion1 +=1
                    self.round = False

                elif self.pos_x <=0-(5*self.radio):

                    self.puntuacion2 +=1
                    self.round = False

                self.pos_x = screenX//2
                self.pos_y = screenY//2
                self.vx *= -1

            if self.pos_y >= y_max-(self.radio) or self.pos_y <=0+(self.radio):
                self.vy *= -1
    def moverMenu(self,x_max=screenX,y_max=screenY):
            self.pos_x += self.vx

            self.pos_y += self.vy

            if self.pos_x >= x_max+(5*self.radio) or self.pos_x <=0-(5*self.radio):

                if self.pos_x >= x_max+(5*self.radio):

                    self.puntuacion1 +=1
                    

                elif self.pos_x <=0-(5*self.radio):

                    self.puntuacion2 +=1
                    

                self.pos_x = screenX//2
                self.pos_y = screenY//2
                self.vx *= -1

            if self.pos_y >= y_max-(self.radio) or self.pos_y <=0+(self.radio):
                self.vy *= -1


        
        
        
        
    def comprobar_choqueV2(self,*raquetas):

        for r in raquetas:

            if self.derecha >= r.izquierda and\
                self.izquierda <= r.derecha and\
                self.abajo >= r.arriba and\
                self.arriba <= r.abajo:       
                self.vx *= -1

    def comprobar_choqueV3(self,*raquetas):

        for r in raquetas:

            if self.derecha == r.pos_reb_x_D and (self.arriba >= r.p_rebote_Y[0] and  self.abajo <= r.p_rebote_Y[1]):
                self.vx *= -1
               
             
            if self.izquierda == r.pos_reb_x_I and (self.arriba >= r.p_rebote_Y[0] and  self.abajo <= r.p_rebote_Y[1]):
                self.vx *= -1
    
    

    @property
    def derecha(self):
        return self.pos_x + self.radio

    @property
    def izquierda(self):
        return self.pos_x - self.radio

    @property
    def arriba(self):
        return self.pos_y - self.radio

    @property
    def abajo(self):
        return self.pos_y + self.radio

    def mostrar_marcador(self,pantalla):
        fuente1 = pg.font.SysFont("Pixellari",40)
        fuente2 = pg.font.SysFont(("Pixellari"),400)
        jugador1= fuente1.render("Jugador 1:",True,color_blanco)
        jugador2 = fuente1.render("Jugador 2:",True,color_blanco)
        marcador1 = fuente2.render(str(self.puntuacion1),True,color_blanco)
        marcador2 = fuente2.render(str(self.puntuacion2),True,color_blanco)
        context = fuente1.render("Press Space to Start", True, color_blanco)
        marcador1.set_alpha(75)
        marcador2.set_alpha(75)
        if self.round == False:
            pantalla.blit(context,(screenX//4, screenY-150))
        pantalla.blit(marcador1,(100, 225))
        pantalla.blit(marcador2,(screenX-325,225))  
        pantalla.blit(jugador1,(screenX-screenX+100, 50)) 
        pantalla.blit(jugador2,((screenX-screenX//3, screenY-screenY+50)))
        
        







































