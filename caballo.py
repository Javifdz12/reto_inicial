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

def casillas_caballo(cantidad):
    list=[]
    if cantidad>1:
        for i in range(len(movs)):
            





