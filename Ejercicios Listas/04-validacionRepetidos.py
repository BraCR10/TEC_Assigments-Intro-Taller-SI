# validacion de conjuntos
def conjunto(lista):
    largo=0
    pos=0 
    while largo<len(lista):
        while pos<len(lista):#Compara un numero con todos los otros
            if largo!=pos:#Se salta el mismo elemento
                if lista[pos]==lista[largo]:
                    return(False)   
                else:
                    pos+=1#
            else:#Se salta el mismo element
                pos+=1
        pos=0
        largo+=1
    return( True)
print(conjunto([1,2]))