from utils import *

def rebote(posicionX_raquetaI, poscionX_raquetaD,posicionY_raquetaI, posicionY_raquetaD,posicion_balon,vx_balon):
    dir_balon=posicion_balon[0]+vx_balon
    valores_rebote_raqI=[]
    valores_rebote_raqD =[]
    """
    for i in range(posicionY_raquetaI[0],posicionY_raquetaI[1]+1):
        valores_rebote_raqI.append(i)
        print(valores_rebote_raqI)
        if posicionX_raquetaI == posicion_balon[0] and (posicion_balon[1] in valores_rebote_raqI):
            dir_balon *= -1

    for i in range(posicionY_raquetaD[0],posicionY_raquetaD[1]+1):
        valores_rebote_raqD.append(i)
        if posicionX_raquetaI == posicion_balon[0] and (posicion_balon[1] in valores_rebote_raqD):
            dir_balon *= -1
    """
    if posicion_balon[0] ==posicionX_raquetaI and posicion_balon[1]>= (posicionY_raquetaI[0] and posicion_balon[1] <= posicionY_raquetaI[1]):
        vx_balon *= -1

    if posicion_balon[0] ==poscionX_raquetaD and posicion_balon[1]>= posicionY_raquetaD[0] and posicion_balon[1] <= posicionY_raquetaD[1]:
        vx_balon*= -1
    
def draw_field_tennis(mainScreen):
        mainScreen.fill((245, 73, 39))       
        pg.draw.line(mainScreen,color_blanco,(0,55),(screenX,55),7)        
        pg.draw.line(mainScreen,color_blanco,(3,0),(3,screenY),7)
        pg.draw.line(mainScreen,color_blanco,(3,screenY-55),(screenX,screenY-55),7)
        pg.draw.line(mainScreen,color_blanco,(screenX-4,0),(screenX-4,screenY),7)
        pg.draw.line(mainScreen,color_blanco,(0,3),(screenX,3),7)
        pg.draw.line(mainScreen,color_blanco,(0,screenY-3),(screenX,screenY-3),7)
        pg.draw.line(mainScreen,color_blanco,(screenX//4-50,55),(screenX//4-50,screenY-55),7)
        pg.draw.line(mainScreen,color_blanco,(screenX//4*3+50,55),(screenX//4*3+50,screenY-55),7)
        pg.draw.line(mainScreen,color_blanco,(screenX//4*2,0),(screenX//4*2,screenY),7)
        pg.draw.line(mainScreen,color_blanco,(screenX//4-50,screenY//2),(screenX//4*3+50,screenY//2),7)

def draw_field_BB(mainScreen):
        background = pg.image.load("BB.jpg")
        background = pg.transform.scale(background,(screenX,screenY))
        mainScreen.blit(background,(0,0))
        pg.draw.line(mainScreen,color_negro,(screenX//2, 0),(screenX//2,screenY),7)
        pg.draw.circle(mainScreen,color_negro,(screenX//2,screenY//2),100,7)
        pg.draw.line(mainScreen,color_negro,(20,20),(screenX-20,20),7)
        pg.draw.line(mainScreen,color_negro,(20,screenY-20),(screenX-20,screenY-20),7)
        pg.draw.line(mainScreen,color_negro,(20,17),(20,screenY-17),7)
        pg.draw.line(mainScreen,color_negro,(screenX-20,17),(screenX-20,screenY-17),7) 
        pg.draw.circle(mainScreen,color_negro,(20, screenY//2),screenY//3, 7)
        pg.draw.circle(mainScreen,color_negro,(screenX-20, screenY//2),screenY//3, 7)
        pg.draw.circle(mainScreen,color_negro,(screenX//7,screenY//2),75,7)
        pg.draw.line(mainScreen,color_negro,(0, screenY//2-100),(screenX//7,screenY//2-73),7)
        pg.draw.line(mainScreen,color_negro,(0, screenY//2+100),(screenX//7,screenY//2+73),7)
        pg.draw.circle(mainScreen,color_negro,(screenX-screenX//7,screenY//2),75,7)
        pg.draw.line(mainScreen,color_negro,(screenX, screenY//2-100),(screenX-screenX//7,screenY//2-73),7)
        pg.draw.line(mainScreen,color_negro,(screenX, screenY//2+100),(screenX-screenX//7,screenY//2+73),7)


def draw_pong_field(mainScreen):
        mainScreen.fill((  28, 126, 28))
        for i in range(0,screenY +20,20):
                pg.draw.line(mainScreen,color_blanco,(screenX//2,0 + i),(screenX//2,i+10),10)
        pg.draw.circle(mainScreen,color_blanco,(screenX//2,screenY//2), 120)
        pg.draw.circle(mainScreen,( 25, 133, 32),(screenX//2,screenY//2), 110)


def menu_controller(index):
       
       pos = pos_cursor_y[index]
       for eventos in pg.event.get():
             if eventos.type == pg.KEYDOWN:
                    if eventos.key == pg.K_DOWN:
                       if pos < pos_cursor_y[3]:
                            index += 1
                    if eventos.key == pg.K_UP:
                        if pos > pos_cursor_y[0]: 
                            index -=1
       return index

                    