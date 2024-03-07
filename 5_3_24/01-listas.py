#Construye una lista nueva de  los pares de la lista trabajando de atrás hacia adelante SIN DESTRUIR
def transformador(lista):
    if isinstance(lista,list):#Validacion
        if lista==[]:#Validacion
             print( [],[])#Validacion
        else:
            check=0#Valida si todos los elemnetos son enteros
            i=len(lista)-1#Se le resta 1 para que no haya error al iterar en la lista
            nuevaListaPar=[]
            nuevaListaImpar=[]
            while i>=0:
                if type(lista[i])!=int:#Si hay un elemento que no es numero
                    print( '\nLa lista solo puede tener numeros enteros, no se puede hacer la operacion')
                    check=1
                    break
                if lista[i]%2==0:#Solo enteros
                    nuevaListaPar=nuevaListaPar+[lista[i]]
                else:
                    nuevaListaImpar=nuevaListaImpar+[lista[i]]
                i-=1
            if check==0:
                print('\nLa nueva lista es: ', nuevaListaPar,' y la lista de impares es: ',nuevaListaImpar)
    else:#Validacion
        print( ['\nEl parametro debe ser una lista, no se puede hacer la operacion'])

#Pruebas
transformador([1,2,3,4,5,6,7,8,9,10])
#Construye una lista nueva de  los pares de la lista trabajando de adelante hacia atras  DESTRUIR
def transformador(lista):
    if isinstance(lista,list):#Validacion
        if lista==[]:#Validacion
             print( [],[])#Validacion
        else:
            check=0#Valida si todos los elemnetos son enteros
            i=len(lista)-1#Se le resta 1 para que no haya error al iterar en la lista
            nuevaListaPar=[]
            nuevaListaImpar=[]
            while i>=0:
                if type(lista[0])!=int:#Si hay un elemento que no es numero
                    print( '\nLa lista solo puede tener numeros enteros, no se puede hacer la operacion')
                    check=1
                    break
                if lista[0]%2==0:#Solo enteros
                    nuevaListaPar=nuevaListaPar+[lista[0]]
                    lista=lista[1:]
                else:
                    nuevaListaImpar=nuevaListaImpar+[lista[0]]
                    lista=lista[1:]
                i-=1
            if check==0:
                print('\nLa nueva lista es: ', nuevaListaPar,' y la lista de impares es: ',nuevaListaImpar)
    else:#Validacion
        print( '\nEl parametro debe ser una lista, no se puede hacer la operacion')

#Pruebas
transformador([1,2,3,4,5,6,7,8,9,10])