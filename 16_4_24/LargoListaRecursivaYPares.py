#Funcion de cola si la lista tiene algun par destruyendo
#Cola
def buscadorPar(lista):
    if isinstance(lista,list):
        if lista==[]:
            return False
        else:
            return buscadorPar_aux(lista)
    else:
        print('Parametro incorrecto')


def buscadorPar_aux(lista):
    if lista==[]:
        return False
    elif lista[0]%2==0:
        return True#Identificador
    else:
        return buscadorPar_aux(lista[1:])
#Pruebas
#print(buscadorPar([1,3,5,]))
#Funcion de cola si la lista tiene todos pares destruyendo
#Cola
def buscadorPar(lista):
    if isinstance(lista,list):
        if lista==[]:
            return False
        else:
            return buscadorPar_aux(lista)
    else:
        print('Parametro incorrecto')


def buscadorPar_aux(lista):
    if lista==[]:#Ya reviso todos
        return True
    elif lista[0]%2!=0:#Existe uno que no cumple
        return False#Identificador
    else:#LLamada recursiva
        return buscadorPar_aux(lista[1:])
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
            return largoListaColaD_aux(lista,0)
    else:
        print('Parametro incorrecto')


def largoListaColaD_aux(lista,cont):
    if len(lista)==cont:
        return cont#Identificador
    else:
        return largoListaColaD_aux(lista,cont+1)
#print(largoListaColaD([1,2,4]))

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


#Pruebas
#print(largoListaPilaD([2,5,2,3,6,5]))
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