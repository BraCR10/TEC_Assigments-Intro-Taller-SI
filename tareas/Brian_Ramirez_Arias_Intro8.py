
#Funcion de cola promedio destruyendo
#Cola
def promedioCD(lista):
    if isinstance(lista,list):
        if lista==[]:
            return 0
        else:
            return promedioCD_aux(0,0,lista)
    else:
        return('Parametro incorrecto')


def promedioCD_aux(sum,cont,lista):
    if lista==[]:
        return sum/cont
    else:
        return promedioCD_aux(sum+lista[0],cont+1,lista[1:])
#print(promedioCD([5,2,7]))
#print(promedioCD(5))
#print(promedioCD([2,3,5,2,3]))

#Funcion de cola promedio  sin destruyendo
#Cola
def promedioCSD(lista):
    if isinstance(lista,list):
        if lista==[]:
            return 0
        else:
            return promedioCSD_aux(0,0,lista)
    else:
        return('Parametro incorrecto')


def promedioCSD_aux(sum,i,lista):
    if len(lista)==i:
        return sum/len(lista)
    else:
        return promedioCSD_aux(sum+lista[i],i+1,lista)
#print(promedioCSD([5,2,7]))
#print(promedioCSD(5))

#Funcion de pila promedio destruyendo
#Pila

def promedioPD(lista):
    if type(lista)==list:
        if  lista==[]:
            return 0  
        suma = promedioPD_aux(lista)
        print(lista)
        return suma / len(lista)
    else:
        return 'Parametros incorrectos'
def promedioPD_aux(lista):#Suma
    if  lista==[]:
        return 0
    return lista[0] + promedioPD_aux(lista[1:])
#Pruebas
#print(promedioPD([5,2,7]))
#print(promedioPD(5))
#Funcion de pila promedio SIN destruyendo
#Pila

def promedioPSD(lista):
    if type(lista)==list:
        if  lista==[]:
            return 0  
        suma = promedioPSD_aux(lista,0)
        return suma / len(lista)
    else:
        return 'Parametros incorrectos'
def promedioPSD_aux(lista,i):#Suma
    if  len(lista)==i:
        return 0
    return lista[i] + promedioPSD_aux(lista,i+1)
#Pruebas
#print(promedioPSD([5,2,7]))
#print(promedioPSD(4))