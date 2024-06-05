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
            return union
        else:
            print('Debe ingresar conjuntos!')
    else:
        print('Deben ingresar listas!')
#Pruebas
#print(unionConjunto([1,5,75,68,9,6,'**'],[1,2,3,6,7,'*2*','**']))

def interConjuntos(lista1,lista2):
    if isinstance(lista1,list) and isinstance(lista2,list):#Validacion
        if conjunto(lista1)==True and conjunto(lista2)==True:#Validacion
            inter=[]#Listas para unir conjuntos
            for i in lista1:
                if i in lista2:
                    inter+=[i]   
            return inter
        else:
            print('Debe ingresar conjuntos!')
    else:
        print('Deben ingresar listas!')
#Pruebas
print(interConjuntos([1,2,4],[1,2,3,7,89]) )

def difSimConjuntos(lista1,lista2):
    if isinstance(lista1,list) and isinstance(lista2,list):#Validacion
        if conjunto(lista1)==True and conjunto(lista2)==True:#Validacion
            inter=interConjuntos(lista1,lista2)#Hay un error si ejecuta primero union
            union=unionConjunto(lista1,lista2)
            difSim=[]#Listas para difSimetrica conjuntos
            for i in union:
                if i not in inter:
                    difSim+=[i]
            print(difSim)
        else:
            print('Debe ingresar conjuntos!')
    else:
        print('Deben ingresar listas!')
#Pruebas
#difSimConjuntos([1,2,4,78979],[1,2,3,7,89]) 