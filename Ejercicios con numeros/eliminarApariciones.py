#Funcion de pila que eliminar un elmento
#Pila
def delPrimeraAparicion(lista,num):
    if type(lista)==list and type(num)==int:
        if lista==[]:
            return []
        else:
            #La llamada recursiva
            return delPrimeraAparicion_aux(lista,num)
    else:
        print('Parametro incorrecto')
def delPrimeraAparicion_aux(lista,num):
    if lista==[]:
        return []
    elif lista[0]==num:
        return lista[1:]
    else:
        #La llamada recursiva
        return  [lista[0]]+delPrimeraAparicion_aux(lista[1:],num)

#Pruebas
#print(delPrimeraAparicion([2,5,6,5,5,6],6))
print(delPrimeraAparicion([2,5,6,7,5,5,6],8))

#Funcion de pila que elimina todos los elementos
#Pila
def delPrimeraAparicionTodo(lista,num):
    if type(lista)==list and type(num)==int:
        if lista==[]:
            return []
        else:
            #La llamada recursiva
            return delPrimeraAparicion_auxTodo(lista,num)
    else:
        print('Parametro incorrecto')
def delPrimeraAparicion_auxTodo(lista,num):
    if lista==[]:
        return []
    elif lista[0]==num:
        return delPrimeraAparicion_auxTodo(lista[1:],num)
    else:
        #La llamada recursiva
        return  [lista[0]]+delPrimeraAparicion_auxTodo(lista[1:],num)

#Pruebas
#print(delPrimeraAparicionTodo([2,5,6,5,5,6,6,6,6,6,1],6))