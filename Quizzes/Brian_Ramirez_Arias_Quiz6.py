#Pruebas
#print(buscadorPar([2,6]))
#Funcion de cola que mide el len de ua lista destruyendo
#Cola
def largoListaColaD(lista):
    if isinstance(lista,list):
        if lista==[]:
            return 0
        else:
            return largoListaColaD_aux(lista,0)
    else:
        print('Parametro incorrecto')


def largoListaColaD_aux(lista,cont):
    if lista==[]:
        return cont#Identificador
    else:
        return largoListaColaD_aux(lista[1:],cont+1)
#print(largoListaColaD([1,2,4,3]))

#Funcion de cola que mide el len de ua lista sin destruyendo
#Cola
def largoListaColaSD(lista):
    if isinstance(lista,list):
        if lista==[]:
            return 0
        else:
            return largoListaColaSD_aux(lista,0)
    else:
        print('Parametro incorrecto')


def largoListaColaSD_aux(lista,cont):
    if len(lista)==cont:
        return cont#Identificador
    else:
        return  largoListaColaSD_aux(lista,cont+1)
#print(largoListaColaSD([0]))

#Funcion de pila que mide el len de ua lista destruyendo
#Pila
def largoListaPilaD(lista):
    if type(lista)==list:
        #Condicion de finalizacion
        if lista==[]:
            return 0
        else:
            #La llamada recursiva
            return 1 + largoListaPilaD(lista[1:])
    else:
        print('Parametro incorrecto')
#print(largoListaPilaD([5,2]))
#Funcion de pila que mide el len de ua lista sin destruir
#Pila
def largoListaPilaPilaSD(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        #La llamada recursiva
        return  1+largoListaPilaSD_aux(lista,0)
    else:
        print('Parametro incorrecto')
def largoListaPilaSD_aux(lista,cont):
    if len(lista)==cont:
        return cont-1
    else:
        #La llamada recursiva
        return  largoListaPilaSD_aux(lista,cont+1)

#Pruebas
#print(largoListaPilaPilaSD([2,5,5,5,6]))