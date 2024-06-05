def validacion(matriz):#[[3,4],[6,8]] [[3,4],[6,8],[5]]
    a=0 #1
    b=0
    if matriz==[]:
        return False
    elif matriz[0] == [] and matriz[1] == []:
        return "La matriz no es valida"
    else:
        for i in range (len(matriz)):#0,1,2(no llega a 2) 0,1,2,3(NO)
            #i=0 1   i=0 1 2
            print(i)
            if matriz==[]:
                a=1
            elif matriz[0]==[]:
                a=1
            elif len(matriz[0])!=len(matriz[1]):
                matriz=matriz+[matriz[0]]
                print(matriz)
                matriz=matriz[1:]
                print(matriz)
                a=1                    #C0C1  C0C1
                return False
            matriz=matriz+[matriz[0]]#[[6,8],[3,4]] [[3,4],[6,8]]
            matriz=matriz[1:]           #f0=2  f1=2  len(matriz)=2

            #Ejemplo NO Funciona
            #[[6,8],[5],[3,4]] [[5],[3,4],[6,8]] [[3,4],[6,8],[5]]
    if a==b:
        return True
    else:
        return False
    
def MatrizTraspuesta(pMatriz):#[[1,2,3,4],[5,6,7,8],[9,1,2,3]]
    largoFilas = len(pMatriz)#3
    print(largoFilas)#3
    largoColumnas = len(pMatriz[0])#4
    print(largoColumnas)#4
    matrizTraspuesta = [0]*largoColumnas#
    print(matrizTraspuesta)#
    for x in range(largoColumnas):# 
        matrizTraspuesta[x] = [0]*largoFilas#
        #[[1,5,9],[2,6,1],[0,0,0],0] #
        print(matrizTraspuesta)#
        for y in range(largoFilas):
            
            matrizTraspuesta[x][y] = pMatriz[y][x]
            
    return matrizTraspuesta
