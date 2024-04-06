def validacion(matriz):#[[3,4],[6,8]] [[6,8],[3,4]********[[3,4],[6,8],[5]]
    a=0 #                                              [[6,8],[5],[3,4]]
    b=0 #
    if matriz==[]:
        return False
    elif matriz[0] == [] and matriz[1] == []:
        return "La matriz no es valida"
    else:
        for i in range (len(matriz)):#
            #i=0si 1si   i=0 1 2
          #***********************
          #2do ejemplo
             #i=0si 1si 2
            print(i)#0 1    #0 1
            if matriz==[]:
                a=1
            elif matriz[0]==[]:
                a=1
            elif len(matriz[0])!=len(matriz[1]):
                 #
                matriz=matriz+[matriz[0]]#
                print(matriz)#
                matriz=matriz[1:]#
                print(matriz)#
                a=1                    #C0C1  C0C1
                #return False
            matriz=matriz+[matriz[0]]#
            matriz=matriz[1:]           #

            #Ejemplo NO Funciona
            #
    if a==b:#0==0 1==0x
        return True
    else:
        return False
def sumaM( ma1,ma2):#[[2,3],[4,6]]], [[5,6],[7,8]]=[[7,9],[11,14]]
    if validacion(ma1)!=validacion(ma2) :
        print ("matrices no validas")
    else:
        filas=len(ma1)#2 sublistas
        columnas=len(ma1[0])#2 elementos de la primera sublista
        filas1=len(ma2)#2
        columna1=len(ma2[0])#2
        for i in range (filas):#i=               
          for j in range (columnas):#    11
                ma1[i][j] =ma1[i][j]+ ma2[i][j] #   6+8
                #
        print( ma1) #                 
