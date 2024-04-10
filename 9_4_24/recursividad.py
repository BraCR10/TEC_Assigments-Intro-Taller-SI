def factorialSinAux(n):
    if type(n)==int:
        #Condicion de finalizacion
        if n==0:
            return 1#Identificador
        else:
            #La llamada recursiva
            return n* factorialSinAux(n-1)
    else:
        print('Parametro incorrecto')
#Prueba
#print(factorialSinAux(3))


#Pila
def factorial(n):
    if type(n)==int:
        #Condicion de finalizacion
        if n==0:
            return 1
        else:
            #La llamada recursiva
            return n* factorial_aux(n-1)
    else:
        print('Parametro incorrecto')


def factorial_aux(n):
    if n==0:
        return 1
    else:
        #La llamada recursiva
        return n* factorial_aux(n-1)
#Pruebas
#print(factorial(3))

#Cola
def factorial2(n):
    if isinstance(n,int):
        if n==0:
            return 1
        else:
            return factorial2_aux(n,1)
    else:
        print('Parametro incorrecto')


def factorial2_aux(n,resultado):
    if n==0:
        return resultado#Identificador
    else:
        return factorial2_aux(n-1,resultado*n)
#Pruebas
#print(factorial2(3))

