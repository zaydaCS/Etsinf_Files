#### Zayda Ferrer ####

fichas_oponenteGL = [(1,0),(3,0),(5,0),(7,0),(0,1),(2,1),(4,1),(6,1),(1,2),(3,2),(5,2),(7,2)]
#fichas_robotGL = [(0,5),(2,5),(4,5),(6,5),(1,6),(3,6),(5,6),(7,6),(0,7),(2,7),(4,7),(6,7)]
fichas_robotGL = [(0,5),(2,3),(4,5),(6,5),(1,6),(3,6),(5,6),(7,6),(0,7),(2,7),(4,7),(6,7)]
cont_fop = [12]
cont_robot = [12]
#estadoPartida[ganar,perder,empatar]
estadoPartida = [0,0,0]


####DIBUJAR el tablero
def begin():
    print("0 1 2 3 4 5 6 7   ")
    print("------------------|")
    print("                  |")
    for a in range(0,8):
        for b in range(0,8):
            contParcial = 0
            for c in range(0,12):
                elem = fichas_oponenteGL[c]
                x1 = elem[0]
                y1 = elem[1]
                if ((b==x1)&(a==y1)):
                    print("O ", end="")
                    contParcial = 1
            if(contParcial == 0):
                for c in range(0,12):
                    elem = fichas_robotGL[c]
                    x1 = elem[0]
                    y1 = elem[1]
                    if((b==x1)&(a==y1)):
                        print("X ", end="")
                        contParcial = 1
            if(contParcial == 0):
                print("_ ", end="")
        print("  |",a)
        #print()



####INTERACCION CON LA PANTALLA:
def movExterior():
    print()
    x1=input("(X,Y) desde:")
    x2=input("(X,Y) hasta:")
    print()
    z1=x1[1]
    z2=x1[3]
    z3=x2[1]
    z4=x2[3]
    aMover = [z1,z2,z3,z4]
    return aMover

def moviendo(paraMover):
    for a in range(0,12):
        elemento = fichas_oponenteGL[a]
        elemX = elemento[0]
        elemY = elemento[1]
        if ((elemX == int(paraMover[0]))& (elemY == int(paraMover[1]))):
            comiendo = siNo(int(paraMover[2]),int(paraMover[3]))
            if (comiendo == 1):
                difX = int(paraMover[2]) - elemX
                difY = int(paraMover[3]) - elemY
                newX = int(paraMover[2]) + difX
                newY = int(paraMover[3]) + difY
                fichas_oponenteGL[a] = (newX,newY)
                eliminando = posEliminar(int(paraMover[2]),int(paraMover[3]))
                fichas_robotGL[eliminando] = (-1,-1)
                cont_robot[0]=cont_robot[0] - 1
            else:
                fichas_oponenteGL[a] = (int(paraMover[2]),int(paraMover[3]))

def siNo (xd,yd):
    for v in range(0,12):
        fichita = fichas_robotGL[v]
        xv = fichita[0]
        yv = fichita[1]
        if ((xv == xd)&(yv == yd)):
            devolviendo = 1
            return devolviendo
    devolviendo = 0
    return devolviendo

def posEliminar(xd,yd):
    for v in range(0,12):
        ficha = fichas_robotGL[v]
        x = ficha[0]
        y = ficha[1]
        if ((x == xd)& (y == yd)):
            return v
        
####ROBOT GANA SI:
        #Oponente no tiene fichas en el tablero --> cont_fop[0] = 0
        #O
        #Todas las fichas que tiene en el tablero estan bloqueadas  --> bloqeadas = cont_fop[0]
def ganar():
    lasBloqueadasDeOP = bloqueadasOpo()
    enTableroDeOP = cont_fop[0]
    if ((enTableroDeOP == 0) | (lasBloqueadasDeOP == enTableroDeOP)):
        win = 1
        estadoPartida[0] = 1
        print("HE GANADO!!!")
        print("lasBloqueadasDeOP, enTableroDeOP")
        print(lasBloqueadasDeOP, enTableroDeOP)
        return -1
    else:
        return 10
        
def bloqueadasOpo():
    totalBloqueadas = 0
    for p in range(0,12):
        laFichaO = fichas_oponenteGL[p]
        laX = laFichaO[0]
        laY = laFichaO[1]
        laFR = fichas_robotGL[0:12]
        laFO = fichas_oponenteGL[0:12]
        
        dr = bloqueoOpo(laX,laY,laFR,laFO)
        #print(dr)
        if (dr > 0):
            totalBloqueadas = totalBloqueadas + 1
    #print(totalBloqueadas)
    return totalBloqueadas

####ROBOT PIERDE SI:
        #Robot no tiene fichas en el tablero --> cont_robot[0] = 0
        #O
        #Todas las fichas que tiene en el tablero estan bloqueadas  --> bloqeadas = cont_robot[0]
def perder():
    lasBloqueadasDeRo = bloqueadasRobot()
    enTableroDeRO = cont_robot[0]
    if ((enTableroDeRO == 0) | (lasBloqueadasDeRo == enTableroDeRO)):
        lose = 1
        estadoPartida[1] = 1
        print("HE PERDIDO!!")
        print("lasBloqueadasDeRo, enTableroDeRO")
        print(lasBloqueadasDeRo, enTableroDeRO)
        return -1
    else:
        return 10

def bloqueadasRobot():
    totalBloqueadas = 0
    for p in range(0,12):
        laFichaR = fichas_robotGL[p]
        laX = laFichaR[0]
        laY = laFichaR[1]
        laFR = fichas_robotGL[0:12]
        laFO = fichas_oponenteGL[0:12]
        dr = bloqueoRobot(laX,laY,laFR,laFO)
        #print(dr)
        if (dr > 0):
            totalBloqueadas = totalBloqueadas + 1
    #print(totalBloqueadas)
    return totalBloqueadas

####PARTIDA EN EMPATE SI:
        #Todas las fichas del tablero (tanto del robot como del oponente) estan bloqueadas
def empatar():
    lasBloqueadasDeRo = bloqueadasRobot()
    lasBloqueadasDeOP = bloqueadasOpo()
    enTableroDeOP = cont_fop[0]
    enTableroDeRO = cont_robot[0]
    print("Bloqeadas OP, contOP, bloqeadasRo, contRo")
    print(lasBloqueadasDeOP,enTableroDeOP,lasBloqueadasDeRo,enTableroDeRO)

    if ((lasBloqueadasDeOP == enTableroDeOP) & (lasBloqueadasDeRo == enTableroDeRO)):
        draw = 1
        estadoPartida[2] = 1
        print("HEMOS EMPATADO!!")
        #print("Bloqeadas OP, contOP, bloqeadasRo, contRo")
        #print(lasBloqueadasDeOP,enTableroDeOP,lasBloqueadasDeRo,enTableroDeRO)
        return -1
    else:
        return 10

####Para saber si la partida continua (si no ha empate o victoria)
def comoVamos():
    heGanado = ganar()
    hePerdido = perder()
    hemosEmpatado = empatar()
    #print("ganar", heGanado)
    #print("perder", hePerdido)
    #print("empatar", hemosEmpatado)
    if ((heGanado < 0) | (hePerdido < 0) | (hemosEmpatado < 0)):
        return 1
    else:
        return 0

####MOVER FICHA
def moverA(dire,index):
    print("Direccion e indice pasado a moverA: ", end="")
    print(dire, index)
    if (dire == 1):
        #direPrint = "IZQUIERDA"
        #movFinDerUp(index)
        movFinIzqUp(index)
    else:
        #direPrint = "DERECHA"
        #movFinIzqUp(index)
        movFinDerUp(index)

    #elementoH = fichas_robotGL[index]
    #posX = elementoH[0]
    #posY = elementoH[1]
    #print("Moveremos la ficha ", end="")
    #print(posX,posY, end="")
    #print(" que se encuentra en la posicion ", end="")
    #print(index, end="")
    #print(" del array de fichas del robot, hacia la ", end="")
    #print(direPrint)

def movFinDerUp(ii):
    print("Derecha")
    elementoH = fichas_robotGL[ii]
    posX = elementoH[0]
    posY = elementoH[1]
    posX2 = posX + 1
    posY2 = posY - 1
    contadorMuerta = 0
    for g in range(0,12):
        elementoHH = fichas_oponenteGL[g]
        posXX = elementoHH[0]
        posYY = elementoHH[1]
        if ((posXX == posX2) & (posYY == posY2)):
            posX3 = posX2 + 1
            posY3 = posY2 - 1
            fichas_robotGL[ii] = (posX3,posY3)
            fichas_oponenteGL[g] = (-1,-1)
            cont_fop[0] = cont_fop[0] - 1
            contadorMuerta = 1
    if (contadorMuerta == 0):
        fichas_robotGL[ii] = (posX2,posY2)
        

def movFinIzqUp(ii):
    print("Izquierda")
    elementoH = fichas_robotGL[ii]
    posX = elementoH[0]
    posY = elementoH[1]
    posX2 = posX - 1
    posY2 = posY - 1
    contadorMuerta = 0
    for g in range(0,12):
        elementoHH = fichas_oponenteGL[g]
        posXX = elementoHH[0]
        posYY = elementoHH[1]
        if ((posXX == posX2) & (posYY == posY2)):
            posX3 = posX2 - 1
            posY3 = posY2 - 1
            fichas_robotGL[ii] = (posX3,posY3)
            fichas_oponenteGL[g] = (-1,-1)
            cont_fop[0] = cont_fop[0] - 1
            contadorMuerta = 1
            print("nueva posicion = ", end="")
            print(posX3,posY3)
    if (contadorMuerta == 0):
        fichas_robotGL[ii] = (posX2,posY2)
        print("nueva posicion = ", end="")
        print(posX2,posY2)





####CALCULO FUNCION DE UTILIDAD
def calcular(fichasRO,fichasOP,contRO,contOP):
    total = 0
    parcialRO = 0
    parcialOPO = 0
    for p in range(0,12):
        elemRobot = fichasRO[p]
        xRobot = elemRobot[0]
        yRobot = elemRobot[1]
        elemOpo = fichasOP[p]
        xOpo = elemOpo[0]
        yOpo = elemOpo[1]
        #Esta muerta la ficha del robot??
        if ((xRobot >= 0) & (yRobot >= 0)):
            #Sino esta muerta, esta bloqueada la fichas del robot??
            bloqueadaPRO = bloqueoRobot(xRobot,yRobot,fichasRO,fichasOP)
            #Si esta bloqueada, anyadir al contador de bloqueadas del robot
            if (bloqueadaPRO > 0):
                parcialRO = parcialRO + 1
        #Esta muerta la ficha del oponente??
        if ((xOpo >= 0) & (yOpo >= 0)):
        #Sino esta muerta, esta bloqueada la ficha del Oponente??
            bloqueadaPOP = bloqueoOpo(xOpo,yOpo,fichasRO,fichasOP)
            #Si esta bloqueada, anyadir al contador de bloqueadas del oponente
            if (bloqueadaPOP > 0):
                parcialOPO = parcialOPO + 1


    sinBloquearRO = (contRO - parcialRO)
    sinBloquearRO = sinBloquearRO * 2
    parcialRO = parcialRO * (-5)
    #print(parcialRO, sinBloquearRO, contRO)
    parcial1 = (parcialRO + sinBloquearRO + (contRO * 100))
    #print(parcial1)
    sinBloquearOP = (contOP - parcialOPO)
    sinBloquearOP = sinBloquearOP * (-2)
    parcialOPO = parcialOPO * 5
    #print(parcialOPO, sinBloquearOP, contOP)
    parcial2 = (parcialOPO + sinBloquearOP + (contOP * (-100)))
    #print(parcial2)

    #print(parcialOPO, parcialRO)
    total = total + parcial1 + parcial2
    #print("Funcion de utilidad = ", total)
    return total

def bloqueoRobot(x1,y1,fichasR,fichasO):
    contadorD = 0
    contadorI = 0
    contadorT = 0
    for d in range(0,12):
        elementoOPO = fichasO[d]
        elementoROBOT = fichasR[d]
        xo = elementoOPO[0]
        yo = elementoOPO[1]
        xr = elementoROBOT[0]
        yr = elementoROBOT[1]

        ####COMPROBAR SI ESTA BLOQUEADA HACIA LA DERECHA####
        #si hay otra ficha del robor a la derecha no se puede mover = bloqueada
        if ((xr == (x1 + 1)) & (yr == (y1 - 1))):
            contadorD = contadorD + 1
        #si al mover hacia la derecha la X sale del tablero, no se puede mover = bloqueada
        elif ((x1 + 1) > 7):
            contadorD = contadorD + 1
        #si al mover hacia la derecha la Y sale del tablero, no se puede mover = bloqueada
        elif ((y1 - 1) < 0):
            contadorD = contadorD + 1
        #Si al mover hacia la derecha hay una ficha del oponente
        elif ((xo == (x1 + 1)) & (yo == (y1 - 1))):
            contadorParcial = 0
            #Si despues la X se sale del tablero, no se puede mover = bloqueada
            if ((x1 + 2) > 7):
                contadorParcial = contadorParcial + 1
            #Si despues la Y se sale del tablero, no se puede mover = bloqueada
            elif ((y1 - 2) < 0):
                contadorParcial = contadorParcial + 1
            else:
            #Si no, comprobar si la siguiente posicion esta vacia, o hay alguna ficha del robot o del oponente
                for f in range(0,12):
                    elemento2OPO = fichasO[f]
                    x2o = elemento2OPO[0]
                    y2o = elemento2OPO[1]
                    elemento2ROBOT = fichasR[f]
                    x2r = elemento2ROBOT[0]
                    y2r = elemento2ROBOT[1]
                    #Si despues hay otra ficha del oponente, no se puede mover = bloqueada
                    if ((x2o == (x1 + 2)) & (y2o == (y1 - 2))):
                        contadorParcial = contadorParcial + 1
                    #Si despues hay otra dicha del robot, no se puede mover = bloqueada
                    elif ((x2r == (x1 + 2)) & (y2r == (y1 - 2))):
                        contadorParcial = contadorParcial + 1
            if (contadorParcial > 0):
                contadorD = contadorD + 1
                
        ####SI ESTA BLOQUEADA HACIA LA DERECHA COMPROBAR QUE HACIA LA IZQUIERDA TAMBIEN
            #Si tb esta bloqueada hacia la derecha, entonces la fichas esta bloqueada en ambas direcciones == FICHA BLOQUEADA                
        if (contadorD > 0):
            for d in range(0,12):
                elementoOPO2 = fichasO[d]
                elementoROBOT2 = fichasR[d]
                xo2 = elementoOPO2[0]
                yo2 = elementoOPO2[1]
                xr2 = elementoROBOT2[0]
                yr2 = elementoROBOT2[1]
                #Si hay otra ficha del robot a la izquierda no se puede mover = bloqueada
                if ((xr2 == (x1 - 1)) & (yr2 == (y1 - 1))):
                    contadorI = contadorI + 1
                #Si al mover hacia la izquierda la X sale del tablero, no se puede mover = bloqueada
                elif ((x1 - 1) < 0):
                    contadorI = contadorI + 1
                #Sia al mover hacia la izquierda la Y sale del tablero, no se puede mover = bloqueada
                elif ((y1 - 1) < 0):
                    contadorI = contadorI + 1
                #Si al mover hacia la izquierda hay una ficha del oponente
                elif ((xo2 == (x1 - 1)) & (yo2 == (y1 - 1))):
                    contadorParcial2 = 0
                    #Si despues la X se sale del tablero, no se puede mover = bloqueada
                    if ((x1 - 2) < 0):
                        contadorParcial2 = contadorParcial2 + 1
                    #Si despues la Y se sale del tablero, no se puede mover = bloqueada
                    elif ((y1 - 2) < 0):
                        contadorParcial2 = contadorParcial2 + 1
                    else:
                    #Si no, comprobar si la siguiente posicion esta vacia, o hay alguna ficha del robot o del oponente
                        for f in range(0,12):
                            elemento2OPO2 = fichasO[f]
                            x2o2 = elemento2OPO2[0]
                            y2o2 = elemento2OPO2[1]
                            elemento2ROBOT2 = fichasR[f]
                            x2r2 = elemento2ROBOT2[0]
                            y2r2 = elemento2ROBOT2[1]
                            #Si despues hay otra ficha del oponente, no se puede mover = bloqueada
                            if ((x2o2 == (x1 - 2)) & (y2o2 == (y1 - 2))):
                                contadorParcial2 = contadorParcial2 + 1
                            #Si despues hay otra dicha del robot, no se puede mover = bloqueada
                            elif ((x2r2 == (x1 + 2)) & (y2r2 == (y1 - 2))):
                                contaforParcial2 = contadorParcial2 + 1
                    if (contadorParcial2 > 0):
                        contadorI = contadorI + 1

        if ((contadorD > 0) & (contadorI > 0)):
            contadorT = contadorT + 1
    if (contadorT > 0):
        return 1
    else:
        return 0
    
def bloqueoOpo(x1,y1,fichasR,fichasO):
    contadorD = 0
    contadorI = 0
    contadorT = 0
    for d in range(0,12):
        elementoOPO = fichasO[d]
        elementoROBOT = fichasR[d]
        xo = elementoOPO[0]
        yo = elementoOPO[1]
        xr = elementoROBOT[0]
        yr = elementoROBOT[1]

        ####COMPROBAR SI ESTA BLOQUEADA HACIA LA DERECHA####
        if ((xo == (x1 + 1)) & (yo == (y1 + 1))):
            contadorD = contadorD + 1
        elif ((x1 + 1) > 7):
            contadorD = contadorD + 1
        elif ((y1 - 1) > 7):
            contadorD = contadorD + 1
        elif ((xr == (x1 + 1)) & (yr == (y1 + 1))):
            contadorParcial = 0
            if ((x1 + 2) > 7):
                contadorParcial = contadorParcial + 1
            elif ((y1 - 2) > 7):
                contadorParcial = contadorParcial + 1
            else:
                for f in range(0,12):
                    elemento2OPO = fichasO[f]
                    x2o = elemento2OPO[0]
                    y2o = elemento2OPO[1]
                    elemento2ROBOT = fichasR[f]
                    x2r = elemento2ROBOT[0]
                    y2r = elemento2ROBOT[1]
                    if ((x2r == (x1 + 2)) & (y2r == (y1 + 2))):
                        contadorParcial = contadorParcial + 1
                    elif ((x2o == (x1 + 2)) & (y2o == (y1 + 2))):
                        contadorParcial = contadorParcial + 1
            if (contadorParcial > 0):
                contadorD = contadorD + 1
                
        ####SI ESTA BLOQUEADA HACIA LA DERECHA COMPROBAR QUE HACIA LA IZQUIERDA TAMBIEN
        if (contadorD > 0):
            for d in range(0,12):
                elementoOPO2 = fichasO[d]
                elementoROBOT2 = fichasR[d]
                xo2 = elementoOPO2[0]
                yo2 = elementoOPO2[1]
                xr2 = elementoROBOT2[0]
                yr2 = elementoROBOT2[1]
                if ((xo2 == (x1 - 1)) & (yo2 == (y1 + 1))):
                    contadorI = contadorI + 1
                elif ((x1 - 1) < 0):
                    contadorI = contadorI + 1
                elif ((y1 - 1) > 7):
                    contadorI = contadorI + 1
                elif ((xr2 == (x1 - 1)) & (yr2 == (y1 + 1))):
                    contadorParcial2 = 0
                    if ((x1 - 2) < 0):
                        contadorParcial2 = contadorParcial2 + 1
                    elif ((y1 + 2) > 7):
                        contadorParcial2 = contadorParcial2 + 1
                    else:
                        for f in range(0,12):
                            elemento2OPO2 = fichasO[f]
                            x2o2 = elemento2OPO2[0]
                            y2o2 = elemento2OPO2[1]
                            elemento2ROBOT2 = fichasR[f]
                            x2r2 = elemento2ROBOT2[0]
                            y2r2 = elemento2ROBOT2[1]
                            if ((x2r2 == (x1 - 2)) & (y2r2 == (y1 + 2))):
                                contadorParcial2 = contadorParcial2 + 1
                            elif ((x2o2 == (x1 + 2)) & (y2o2 == (y1 + 2))):
                                contaforParcial2 = contadorParcial2 + 1
                    if (contadorParcial2 > 0):
                        contadorI = contadorI + 1
        if ((contadorD > 0) & (contadorI > 0)):
            contadorT = contadorT + 1
    if (contadorT > 0):
        return 1
    else:
        return 0            
        
    


####MOVIMIENTO IZQUIERDA-ARRIBA DEL ROBOT
        
def moverIzquiedaR(fichasRobot,fichasOpo,fichaX,fichaY):
    #mover izquierda: x--,y--
    x1 = fichaX - 1
    y1 = fichaY - 1
    if((x1 >= 0) & (y1 >= 0)):
        for b in range(0,12):
            fRobot = fichasRobot[b]
            fOpo = fichasOpo[b]
            fRx = fRobot[0]
            fRy = fRobot[1]
            fOx = fOpo[0]
            fOy = fOpo[1]
            if((fRx == x1) & (fRy == y1)): #hay otra ficha del robot --> por tanto NO se puede mover
                return -2
            elif((fOx == x1) & (fOy == y1)): #Hay ficha del oponente --> por tanto puede comer si la siguiente esta libre
                x2 = x1 - 1
                y2 = y1 - 1
                if((x2 >= 0) & (y2 >= 0)):
                    for c in range(0,12):
                        elR = fichasRobot[c]
                        erx = elR[0]
                        ery = elR[1]
                        elO = fichasOpo[c]
                        eox = elO[0]
                        eoy = elO[1]
                        if((erx == x2) & (ery == y2)):
                            return -2   #La siguiente posicion ocupada por ficha de robot --> por tanto no se puede mover
                        elif((eox == x2) & (eoy == y2)):
                            return -2   #La siguiente posicion ocupada por ficha Oponente --> por tanto no se puede mover
                    return b    #La siguientes posicion esta libre (y dentro del tablero) --> por tanto puede comer y mover
                return -2   #La posicion esta fuera del tablero --> Por tanto no se puede mover
        return -1   #La posicion esta libre
    return -2   #Posicion fuera del tablero y por tanto no se puede mover
        
def izqRobotA(fichasRobot,fichasOpo,conRobot,conOpo):
    utilidadT = -1000000
    direccionT = 2
    xT = -1
    yT = -1
    indiceT = -1
    utilidad1 = -1100000
    direccionP = -2
    xP = -2
    yP = -2
    indiceP = -2
    for a in range(0,12):
        fichaRobot = fichasRobot[a]
        fichaX = fichaRobot[0]
        fichaY = fichaRobot[1]
        puedeMover = moverIzquiedaR(fichasRobot,fichasOpo,fichaX,fichaY)
        #puedeMover = -2 sino puedo mover
        if(puedeMover > -2):
            #Anyadido para no modificar los arrays
            fichasRobotQ = fichasRobot[0:12]
            fichasOpoQ = fichasOpo[0:12]
            conRobotQ=conRobot
            conOpoQ=conOpo
        #puedeMover = -1 si puedo mover
            if(puedeMover == -1):
                #Anyadido para no modificar los arrays
                #fichasRobotQ = fichasRobot[0:12]
                #fichasOpoQ = fichasOpo[0:12]
                #conRobotQ=conRobot
                #conOpoQ=conOpo

                
                x3 = fichaX - 1
                y3 = fichaY - 1
                #fichasRobot[a] = (x3,y3)
                fichasRobotQ[a] = (x3,y3)

                #subD = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #print(fichaX, fichaY)
                #print("Al mover a la izquierda, utilidad = ", subD)


                utilidadDerecha1 = dereOpoA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                utilidadIzquierda1 = izqOponenteA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                if (utilidadDerecha1 >= utilidadIzquierda1):
                    utilidad1 = utilidadDerecha1
                    direccionP = 1
                    direccionP = 1
                    xP = fichaX
                    yP = fichaY
                    indiceP = a
                else:
                    utilidad1 = utilidadIzquierda1
                    direccionP = 2
                    xP = fichaX
                    yP = fichaY
                    indiceP = a
        #puedeMover = b(indice) porque puedo comer ficha almacena en el indice b, b>=0
            else:
                x3 = fichaX - 2
                y3 = fichaY - 2
                #fichasRobot[a] = (x3,y3)
                #fichasOpo[puedeMover] = (-1,-1)     #Ficha eliminada
                fichasRobotQ[a] = (x3,y3)
                fichasOpoQ[puedeMover] = (-1,-1)
                conOpoQ = conOpoQ - 1

                #subD = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #print(fichaX, fichaY)
                #print("Al mover a la derecha, utilidad = ", subD)

                utilidadDerecha1 = dereOpoA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                utilidadIzquierda1 = izqOponenteA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                if (utilidadDerecha1 >= utilidadIzquierda1):
                    utilidad1 = utilidadDerecha1
                    direccionP = 1
                    xP = fichaX
                    yP = fichaY
                    indiceP = a
                else:
                    utilidad1 = utilidadIzquierda1
                    direccionP = 2
                    xP = fichaX
                    yP = fichaY
                    indiceP = a
        if (utilidad1 > utilidadT):
            utilidadT = utilidad1
            direccionT = direccionP
            xT = xP
            yT = yP
            indiceT = indiceP

        arrayParaDevolver = [utilidadT,direccionT,xT,yT,indiceT]

    print(utilidadT,direccionT,xT,yT,indiceT)
    return arrayParaDevolver


####MOVIMIENTO DERECHA-ARRIBA DEL ROBOT

def moverDerechaR(fichasRobot1,fichasOpo1,fichaX1,fichaY1):
    #mover derecha: x++,y--
    x1 = fichaX1 + 1
    y1 = fichaY1 - 1
    if((x1 < 8) & (y1 >= 0)):
        for b in range(0,12):
            fRobot = fichasRobot1[b]
            fOpo = fichasOpo1[b]
            fRx = fRobot[0]
            fRy = fRobot[1]
            fOx = fOpo[0]
            fOy = fOpo[1]
            if((fRx == x1) & (fRy == y1)): #hay otra ficha del robot --> por tanto NO se puede mover
                return -2
            elif((fOx == x1) & (fOy == y1)): #Hay ficha del oponente --> por tanto puede comer si la siguiente esta libre
                x2 = x1 + 1
                y2 = y1 - 1
                if((x2 < 8) & (y2 >= 0)):
                    for c in range(0,12):
                        elR = fichasRobot1[c]
                        erx = elR[0]
                        ery = elR[1]
                        elO = fichasOpo1[c]
                        eox = elO[0]
                        eoy = elO[1]
                        if((erx == x2) & (ery == y2)):
                            return -2   #La siguiente posicion ocupada por ficha de robot --> por tanto no se puede mover
                        elif((eox == x2) & (eoy == y2)):
                            return -2   #La siguiente posicion ocupada por ficha Oponente --> por tanto no se puede mover
                    return b    #La siguientes posicion esta libre (y dentro del tablero) --> por tanto puede comer y mover
                return -2   #La posicion esta fuera del tablero --> Por tanto no se puede mover
        return -1   #La posicion esta libre
    return -2   #Posicion fuera del tablero y por tanto no se puede mover
 
def dereRobotA(fichasRobot,fichasOpo,conRobot,conOpo):
    utilidadT = -1000000
    direccionT = 2
    xT = -1
    yT = -1
    indiceT = -1
    utilidad1 = -1100000
    direccionP = -2
    xP = -2
    yP = -2
    indiceP = -2
    for a in range(0,12):
        fichaRobot = fichasRobot[a]
        fichaX = fichaRobot[0]
        fichaY = fichaRobot[1]
        puedeMover = moverDerechaR(fichasRobot,fichasOpo,fichaX,fichaY)
        #puedeMover = -2 sino puedo mover
        if(puedeMover > -2):
            #Anyadido para no modificar los arrays
            fichasRobotQ=fichasRobot[0:12]
            fichasOpoQ=fichasOpo[0:12]
            conRobotQ=conRobot
            conOpoQ=conOpo
        #puedeMover = -1 si puedo mover
            if(puedeMover == -1):
                #Anyadido para no modificar los arrays
                #fichasRobotQ=fichasRobot[0:12]
                #fichasOpoQ=fichasOpo[0:12]
                #conRobotQ=conRobot
                #conOpoQ=conOpo
                
                x3 = fichaX + 1
                y3 = fichaY - 1
                #fichasRobot[a] = (x3,y3)
                fichasRobotQ[a] = (x3,y3)

                
                #subD = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #print(fichaX, fichaY)
                #print("Al mover a la derecha, utilidad = ", subD)

                
                utilidadDerecha1 = dereOpoA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                utilidadIzquierda1 = izqOponenteA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                if (utilidadDerecha1 >= utilidadIzquierda1):
                    utilidad1 = utilidadDerecha1
                    direccionP = 1
                    xP = fichaX
                    yP = fichaY
                    indiceP = a
                else:
                    utilidad1 = utilidadIzquierda1
                    direccionP = 2
                    xP = fichaX
                    yP = fichaY
                    indiceP = a
        #puedeMover = b(indice) porque puedo comer ficha almacena en el indice b, b>=0
            else:
                x3 = fichaX + 2
                y3 = fichaY - 2
                fichasRobotQ[a] = (x3,y3)
                fichasOpoQ[puedeMover] = (-1,-1)     #Ficha eliminada
                conOpoQ = conOpoQ - 1

                #subD = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #print(fichaX, fichaY)
                #print("Al mover a la derecha, utilidad = ", subD)

                utilidadDerecha1 = dereOpoA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                utilidadIzquierda1 = izqOponenteA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                if (utilidadDerecha1 >= utilidadIzquierda1):
                    utilidad1 = utilidadDerecha1
                    direccionP = 1
                    xP = fichaX
                    yP = fichaY
                    indiceP = a
                else:
                    utilidad1 = utilidadIzquierda1
                    direccionP = 2
                    xP = fichaX
                    yP = fichaY
                    indiceP = a
        if (utilidad1 > utilidadT):
            utilidadT = utilidad1
            direccionT = direccionP
            xT = xP
            yT = yP
            indiceT = indiceP

        arrayParaDevolver = [utilidadT,direccionT,xT,yT,indiceT]

    print(utilidadT,direccionT,xT,yT,indiceT)
    return arrayParaDevolver
            




####MOVIMIENTO DERECHA-ARRIBA DEL OPONENTE

def moverDerechaO(fichasRobot1,fichasOpo1,fichaX1,fichaY1):
    #mover derecha: x++,y++
    x1 = fichaX1 + 1
    y1 = fichaY1 + 1
    if((x1 < 8) & (y1 < 8)):
        for b in range(0,12):
            fRobot = fichasRobot1[b]
            fOpo = fichasOpo1[b]
            fRx = fRobot[0]
            fRy = fRobot[1]
            fOx = fOpo[0]
            fOy = fOpo[1]
            if((fOx == x1) & (fOy == y1)): #hay otra ficha del robot --> por tanto NO se puede mover
                return -2
            elif((fRx == x1) & (fRy == y1)): #Hay ficha del oponente --> por tanto puede comer si la siguiente esta libre
                x2 = x1 + 1
                y2 = y1 + 1
                if((x2 < 8) & (y2 < 8)):
                    for c in range(0,12):
                        elR = fichasRobot1[c]
                        erx = elR[0]
                        ery = elR[1]
                        elO = fichasOpo1[c]
                        eox = elO[0]
                        eoy = elO[1]
                        if((eox == x2) & (eoy == y2)):
                            return -2   #La siguiente posicion ocupada por ficha de robot --> por tanto no se puede mover
                        elif((erx == x2) & (ery == y2)):
                            return -2   #La siguiente posicion ocupada por ficha Oponente --> por tanto no se puede mover
                    return b    #La siguientes posicion esta libre (y dentro del tablero) --> por tanto puede comer y mover
                return -2   #La posicion esta fuera del tablero --> Por tanto no se puede mover
        return -1   #La posicion esta libre
    return -2   #Posicion fuera del tablero y por tanto no se puede mover
 
def dereOpoA(fichasRobot,fichasOpo,conRobot,conOpo):
    utiDereOpo = 1000000
    for a in range(0,12):
        fichaOpo = fichasOpo[a]
        fichaX = fichaOpo[0]
        fichaY = fichaOpo[1]
        puedeMover = moverDerechaO(fichasRobot,fichasOpo,fichaX,fichaY)
        #puedeMover = -2 sino puedo mover
        if(puedeMover > -2):
            #Anyadido para no modificar los arrays
            fichasRobotQ=fichasRobot[0:12]
            fichasOpoQ=fichasOpo[0:12]
            conRobotQ=conRobot
            conOpoQ=conOpo
        #puedeMover = -1 si puedo mover
            if(puedeMover == -1):
                #Anyadido para no modificar los arrays
                #fichasRobotQ=fichasRobot[0:12]
                #fichasOpoQ=fichasOpo[0:12]
                #conRobotQ=conRobot
                #conOpoQ=conOpo
                
                x3 = fichaX + 1
                y3 = fichaY - 1
                #fichasRobot[a] = (x3,y3)
                fichasRobotQ[a] = (x3,y3)

                
                #subD = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #print(fichaX, fichaY)
                #print("Al mover a la derecha, utilidad = ", subD)

                utiDereOpoPar = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                if(utiDereOpoPar <= utiDereOpo):
                    utiDereOpo = utiDereOpoPar

                #utilidadDerecha1 = dereOpoA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #utilidadIzquierda1 = izqOponenteA(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #if (utilidadDerecha1 >= utilidadIzquierda1):
                #    utilidad1 = utilidadDerecha1
                #else:
                #    utilidad1 = utilidadIzquierda1
                    
        #puedeMover = b(indice) porque puedo comer ficha almacena en el indice b, b>=0
            else:                
                x3 = fichaX + 2
                y3 = fichaY + 2
                fichasOpoQ[a] = (x3,y3)
                fichasRobotQ[puedeMover] = (-1,-1)     #Ficha eliminada
                conRobotQ = conRobotQ - 1

                #subD = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #print(fichaX, fichaY)
                #print("Al mover a la derecha, utilidad = ", subD)

                utiDereOpoPar = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                if(utiDereOpoPar <= utiDereOpo):
                    utiDereOpo = utiDereOpoPar
    return utiDereOpo


####MOVIMIENTO IZQUIERDA-ARRIBA DEL ROBOT
        
def moverIzquiedaO(fichasRobot,fichasOpo,fichaX,fichaY):
    #mover izquierda: x--,y++
    x1 = fichaX - 1
    y1 = fichaY + 1
    if((x1 >= 0) & (y1 < 8)):
        for b in range(0,12):
            fRobot = fichasRobot[b]
            fOpo = fichasOpo[b]
            fRx = fRobot[0]
            fRy = fRobot[1]
            fOx = fOpo[0]
            fOy = fOpo[1]
            if((fOx == x1) & (fOy == y1)): #hay otra ficha del robot --> por tanto NO se puede mover
                return -2
            elif((fRx == x1) & (fRy == y1)): #Hay ficha del oponente --> por tanto puede comer si la siguiente esta libre
                x2 = x1 - 1
                y2 = y1 + 1
                if((x2 >= 0) & (y2 < 8)):
                    for c in range(0,12):
                        elR = fichasRobot[c]
                        erx = elR[0]
                        ery = elR[1]
                        elO = fichasOpo[c]
                        eox = elO[0]
                        eoy = elO[1]
                        if((eox == x2) & (eoy == y2)):
                            return -2   #La siguiente posicion ocupada por ficha de robot --> por tanto no se puede mover
                        elif((erx == x2) & (ery == y2)):
                            return -2   #La siguiente posicion ocupada por ficha Oponente --> por tanto no se puede mover
                    return b    #La siguientes posicion esta libre (y dentro del tablero) --> por tanto puede comer y mover
                return -2   #La posicion esta fuera del tablero --> Por tanto no se puede mover
        return -1   #La posicion esta libre
    return -2   #Posicion fuera del tablero y por tanto no se puede mover
        
def izqOponenteA(fichasRobot,fichasOpo,conRobot,conOpo):
    utiIzqOpo = 1000000
    for a in range(0,12):
        fichaOpo = fichasOpo[a]
        fichaX = fichaOpo[0]
        fichaY = fichaOpo[1]
        puedeMover = moverIzquiedaO(fichasRobot,fichasOpo,fichaX,fichaY)
        #puedeMover = -2 sino puedo mover
        if(puedeMover > -2):
        #puedeMover = -1 si puedo mover
            #Anyadido para no modificar los arrays
            fichasRobotQ = fichasRobot[0:12]
            fichasOpoQ = fichasOpo[0:12]
            conRobotQ=conRobot
            conOpoQ=conOpo
            if(puedeMover == -1):
                #Anyadido para no modificar los arrays
                #fichasRobotQ = fichasRobot[0:12]
                #fichasOpoQ = fichasOpo[0:12]
                #conRobotQ=conRobot
                #conOpoQ=conOpo

                
                x3 = fichaX - 1
                y3 = fichaY + 1
                #fichasRobot[a] = (x3,y3)
                fichasOpoQ[a] = (x3,y3)

                #subD = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #print(fichaX, fichaY)
                #print("Al mover a la izquierda, utilidad = ", subD)

                utiIzqOpoPar = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                if(utiIzqOpoPar <= utiIzqOpo):
                    utiIzqOpo = utiIzqOpoPar
                    
        #puedeMover = b(indice) porque puedo comer ficha almacena en el indice b, b>=0
            else:
                x3 = fichaX - 2
                y3 = fichaY + 2
                #fichasRobot[a] = (x3,y3)
                #fichasOpo[puedeMover] = (-1,-1)     #Ficha eliminada
                fichasOpoQ[a] = (x3,y3)
                fichasRobotQ[puedeMover] = (-1,-1)
                conRobotQ = conRobotQ - 1

                #subD = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                #print(fichaX, fichaY)
                #print("Al mover a la izquierda, utilidad = ", subD)

                utiIzqOpoPar = calcular(fichasRobotQ,fichasOpoQ,conRobotQ,conOpoQ)
                if(utiIzqOpoPar <= utiIzqOpo):
                    utiIzqOpo = utiIzqOpoPar
    return utiIzqOpo

                


###FUNCION MAIN####
def main():
    #Instrucciones para interaccionar con el tablero:
    begin()
    #paraMover = movExterior()
    #moviendo(paraMover)
    #begin()
    
    #print("\nRobot pensando....\n")

    """
    frobot = fichas_robotGL[0:12]
    fopo = fichas_oponenteGL[0:12]
    crobot = cont_robot[0]
    copos = cont_fop[0]
    """


    contando = 1
    while True:
        print("Jugando")

        frobot = fichas_robotGL[0:12]
        fopo = fichas_oponenteGL[0:12]
        crobot = cont_robot[0]
        copos = cont_fop[0]
        
        if ((contando % 2) != 0):
            #JUGADA ROBOT
            arrayDerecha = dereRobotA(frobot,fopo,crobot,copos)
            arrayIzquierda = izqRobotA(frobot,fopo,crobot,copos)
            testeando1 = arrayDerecha[0]
            #print(arrayDerecha[1],arrayIzquierda[1])
            testeando2 = arrayIzquierda[0]
            #print(testeando1, testeando2)
    
            if (testeando1 >= testeando2):
                #moverA = derecha/izquierda,indiceAMover
                print("Debe mover a DERECHA")
                #moverA(arrayDerecha[1],arrayDerecha[4])
                moverA(2,arrayDerecha[4])
            else:
                print("Debe mover a IZQUIERDA")
                #moverA(arrayIzquierda[1],arrayIzquierda[4])
                moverA(1,arrayIzquierda[4])
                
        else:
            #JUGADA OPONENTE
            paraMover = movExterior()
            moviendo(paraMover)

        begin()
        seguimos = comoVamos()
        if (seguimos == 1):
            break
        contando = contando + 1
        
    

    
main()

