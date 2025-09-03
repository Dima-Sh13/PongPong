from Clases import Boton
from utils import *
#from pantallas import Partida, PartidaSolo, MenuV2
"""
class Marcador():
    def __init__(self, n_jugador1, n_jugador2):
        self.j_izq = n_jugador1
        self.j_drch = n_jugador2
        self.font1 = pg.font.SysFont("Pixellari", 45)
        self.score_p1 = 0
        self.score_p2 = 0

    def dibujar(self, mainScreen):
        pg.draw.polygon(mainScreen, color_negro, [(ANCHO//4,0),(ANCHO//4 +50,0),(ANCHO//4 +50,50)] )
        pg.draw.polygon(mainScreen, color_negro, [(ANCHO//4*3,0),(ANCHO//4*3-50,0),(ANCHO//4*3-50,50)] )  
        pg.draw.rect(mainScreen, color_negro, (ANCHO//4 +50,0,ANCHO//4*2-100, 51))
        for i in range(0, 50,5 ):
            pg.draw.line(mainScreen, color_blanco, (ANCHO//2+10,i),(ANCHO//2+10,i),2)    
        self.font_main = self.font1.render(str(self.score_p1), True, color_blanco)
        self.font2 = self.font1.render(str(self.score_p2), True, color_blanco )
        mainScreen.blit(self.font_main, (ANCHO//2 -25, 10))
        mainScreen.blit(self.font2, (ANCHO//2 +25, 10))
        self.font_n1 = self.font1.render((self.j_izq), True, color_blanco)
        self.font_n2 = self.font1.render((self.j_drch), True, color_blanco)
        mainScreen.blit(self.font_n1, (screenX//4 +75, 10))
        mainScreen.blit(self.font_n2, (screenX//2 +100, 10))
"""


import pygame  # Importamos la librería pygame

# Inicializamos pygame
pygame.init()

# Definimos el tamaño de la ventana
ANCHO = screenX
ALTO = screenY

# Creamos la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Ponemos un título en la ventana
pygame.display.set_caption("Ventana con fondo blanco")

# Definimos el color blanco en formato RGB
BLANCO = (255, 255, 255)

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # Revisamos los eventos (como cerrar la ventana)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Si se cierra la ventana
            ejecutando = False          # Terminamos el bucle

    # Rellenamos la ventana con color blanco
    ventana.fill(color_campo)
    #objeto = Marcador("Dima","Mina")
    #objeto.dibujar(ventana)
    boton1 = Boton("settings",100,50,pos_1[0], pos_1[1] )
    boton2 = Boton("Records", 100, 50, pos_2[0],pos_2[1])
    boton1.show(ventana)
    boton2.show(ventana)
    print("i")
    # Actualizamos la pantalla
    pygame.display.flip()

# Cerramos pygame correctamente
pygame.quit()
