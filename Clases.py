import pygame as pg


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

    def movimiento(self, x_max= 0, y_max = 0):
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


class Raqueta:
    def __init__(self, pos_x, pos_y, color =(255,255,255), w=50, h=20):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.w =w
        self.h = h

    def dibujar(self, surface):
        def dibujar_rectangulo(self, pantalla):
            pg.draw.rect(surface,self.color,(self.pos_x,self.pos_y,self.w,self.h))    


class Pelota:
    def __init__(self, pos_x, pos_y, color =(255,255,255),radio =20):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio

    def dibujar(self,surface):
        pg.draw.circle(surface, self.color,(self.pos_x, self.pos_y), self.radio)

    