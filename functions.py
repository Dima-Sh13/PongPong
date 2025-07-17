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
    



   
