import pygame as pg
import random as ra
"""
class Figura:
    def __init__(self, pos_x, pos_y, color =(255,255,255),vx=1, vy=1, w=40, h=40, radio =20):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.vx = vx
        self.vy = vy
        self.w =w
        self.h = h
        self.radio = radio

    def movimiento(self, x_max= 0, y_max = 0, ):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_x == x_max or self.pos_x == 0:
            self.vx = self.vx * -1
        if self.pos_y == y_max or self.pos_y == 0:
            self.vy = self.vy * -1


    def dibujar_rectangulo(self, pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x,self.pos_y,self.w,self.h))

    def dibujar_circulo(self, pantalla):
        pg.draw.circle(pantalla, self.color,(self.pos_x, self.pos_y), self.radio)
"""

class Raqueta:
    def __init__(self, pos_x, pos_y, color =(255,255,255), w=50, h=20):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w =w
        self.h = h
        self.pos_reb_x = self.pos_x +w
        self.p_rebote_Y =[self.pos_y+ self.pos_y+self.h]
        
    def dibujar(self, surface):
        pg.draw.rect(surface,self.color,(self.pos_x,self.pos_y,self.w,self.h))    

    def movimiento(self, keyy_U, keyy_D):
        estadoTeclado = pg.key.get_pressed()
        self.p_rebote_Y=[self.pos_y+self.w, self.pos_y+self.h]
        if estadoTeclado[keyy_U] == True and self.pos_y >= 0  :
            self.pos_y -= 1
        if estadoTeclado[keyy_D] == True and self.pos_y <= 700 - self.h:
            self.pos_y += 1 

class Pelota:
    def __init__(self, pos_x, pos_y, color =(255,255,255),radio =20, vx=1, vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.puntuacion1 = 0
        self.puntuacion2 = 0
        self.p_rebote =[self.pos_x-self.radio, self.pos_y-self.radio]
        
    def dibujar(self,surface):
        pg.draw.circle(surface, self.color,(self.pos_x, self.pos_y), self.radio)

    def movimiento(self, x_max, y_max, p_rauqetax, praquetay):
        """
        self.direccion_x = ra.randint(-10,10)
        self.direccion_y = ra.randint(-10,10)
        """
       
        self.pos_x += self.vx
        self.pos_y += self.vy
        self.p_rebote =[self.pos_x-self.radio, self.pos_y-self.radio]
        
        if self.pos_x <= 0 +self.radio or self.pos_x >= x_max - self.radio:
            if self.pos_x <=0:
                self.puntuacion2 += 1
            elif self.pos_x >= x_max:
                self.puntuacion1 +=1    
            
            self.pos_x = x_max//2
            self.pos_y = y_max//2
            self.vx *= -1
        if  self.pos_y >= y_max or self.pos_y <= 0:
            self.vy *= -1    
        if self.p_rebote[0] ==p_rauqetax and self.p_rebote[1]>= praquetay[0] and self.p_rebote[1] <= praquetay[1]:
            self.vx *= -1
        """
        if posicion_balon[0] ==poscionX_raquetaD and posicion_balon[1]>= posicionY_raquetaD[0] and posicion_balon[1] <= posicionY_raquetaD[1]:
        vx_balon*= -1
        """