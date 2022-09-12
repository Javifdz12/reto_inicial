import numpy as np
movs=[[4,6],[6,8],[7,9],[4,8],[3,9,0],[],[1,7,0],[2,6],[1,3],[2,4]]

def casillas_caballo1():
    posibilidades=0
    for i in range(len(movs)):
        posibilidades+=len(movs[i])
    return posibilidades

def casillas_caballo2():
    posibilidades=0
    for i in range(len(movs)):
        for j in movs[i]:
            posibilidades+=len(movs[j])
    return posibilidades

def casillas_caballo3():
    posibilidades=0
    for i in range(len(movs)):
        for j in movs[i]:
            for n in movs[j]:
                posibilidades+=len(movs[n])
    return posibilidades

print(casillas_caballo3())

tablero=np.array([[0,0,0]
                ,[0,0,0]
                ,[1,0,0]
                ,[-1,0,-1]])

def mover_arriba(tablero):
    for x in range(tablero.shape[0]):
        for y in range(tablero.shape[1]):
            if tablero[x, y] == 1:
                if x > 0:
                    tablero[x, y] = 0
                    tablero[x-1, y] = 1
                else:
                    print("Movimiento invalido")

def mover_abajo(tablero):
    for x in range(tablero.shape[0]):
        for y in range(tablero.shape[1]):
            if tablero[x, y] == 1:
                if x < tablero.shape[0] - 1 and tablero[x + 1, y]>0:
                    tablero[x, y] = 0
                    tablero[x + 1, y] = 1
                else:
                    print("Movimiento invalido")


print(tablero)
#mover_arriba(tablero)
print(tablero)
mover_abajo(tablero)
print(tablero)

