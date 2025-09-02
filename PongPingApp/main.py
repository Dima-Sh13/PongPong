
from utils import *
#from pantallas import Partida, PartidaSolo, MenuV2

class Marcador():
    def __init__(self, n_jugador1, n_jugador2):
        self.j_izq = n_jugador1
        self.j_drch = n_jugador2

    def dibujar(self, mainScreen):
        pg.draw.polygon(mainScreen, color_negro, [(ANCHO//4,0),(ANCHO//4 +50,0),(ANCHO//4 +50,50)] )
        pg.draw.polygon(mainScreen, color_negro, [(ANCHO//4*3,0),(ANCHO//4*3-50,0),(ANCHO//4*3-50,50)] )  
        pg.draw.rect(mainScreen, color_negro, (ANCHO//4 +50,0,300, 51))    





import pygame  # Importamos la librería pygame

# Inicializamos pygame
pygame.init()

# Definimos el tamaño de la ventana
ANCHO = 800
ALTO = 600

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
    ventana.fill(BLANCO)
    objeto = Marcador("Dima","carolina")
    objeto.dibujar(ventana)
    # Actualizamos la pantalla
    pygame.display.flip()

# Cerramos pygame correctamente
pygame.quit()
