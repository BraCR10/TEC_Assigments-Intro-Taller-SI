#Validar conjuntos
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
def unionConjunto(lista1,lista2):
    if isinstance(lista1,list) and isinstance(lista2,list):#Validacion
        if conjunto(lista1)==True and conjunto(lista2)==True:#Validacion
            union=lista1#Listas para unir conjuntos
            for i in lista2:
                if i in lista1:
                    continue
                else:
                    union+=[i]
            print( union)
        else:
            print('Debe ingresar conjuntos!')
    else:
        print('Deben ingresar listas!')
#Pruebas
#unionConjunto([1,5,75,68,9,6,'**'],[1,2,3,6,7,'*2*','**'])