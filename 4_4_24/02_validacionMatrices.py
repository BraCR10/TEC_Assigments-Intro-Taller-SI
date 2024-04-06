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