# validacion de conjuntos
def conjunto(lista):#[2,3,4]si  [2,3,4,2]x
    largo=0 #0 1 2 3
    pos=0 #0 0 0 0
    while largo<len(lista):# Afuera o Externo
        #largo<3si 
        while pos<len(lista):#Adentro o Interno
            if largo!=pos:#
                if lista[pos]==lista[largo]:#
                    return(False)   
                else:
                    pos=pos+1#
            else:
                pos=pos+1#0
        #Antes del externo
        pos=0
        largo=largo+1
    return( True)
print(conjunto([1,2]))