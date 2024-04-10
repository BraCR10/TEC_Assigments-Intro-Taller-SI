
#Pila
def largoNum(n):
    if type(n)==int:
        #Condicion de finalizacion
        if n==0:
            return 1
        else:
            #La llamada recursiva
            return  largoNumAux(abs(n))
    else:
        print('Parametro incorrecto')


def largoNumAux(n):
    if n==0:
        return 0
    else:
        #La llamada recursiva
        
        return 1+largoNumAux(n//10)
#Pruebas
#print(largoNum(111))


#Cola
def largoNumCola(n):
    if isinstance(n,int):
        if n==0:
            return 1
        else:
            return largoNumCola_aux(abs(n),0)
    else:
        print('Parametro incorrecto')


def largoNumCola_aux(n,cont):
    if n==0:
        return cont#Identificador
    else:
        return largoNumCola_aux(n//10,cont+1)
#Pruebas
print(largoNumCola(-44444))