def sumatoria(n):
    if type(n)==int:
        #Condicion de finalizacion
        if n==0:
            return 0#Identificador
        else:
            #La llamada recursiva
            return n+ sumatoria(n-1)
    else:
        print('Parametro incorrecto')
#Prueba
#print(factorialSinAux(3))
print(sumatoria(8))


#Pila
def sumatoriaPila(n):
    if type(n)==int:
        #Condicion de finalizacion
        if n==0:
            return 0
        else:
            #La llamada recursiva
            return n+ SumatoriaPilaAux(n-1)
    else:
        print('Parametro incorrecto')


def SumatoriaPilaAux(n):
    if n==0:
        return 0
    else:
        #La llamada recursiva
        return n+ SumatoriaPilaAux(n-1)
#Pruebas
#print(sumatoriaPila(8))


#Cola
def SumatoriaCola(n):
    if isinstance(n,int):
        if n==0:
            return 0
        else:
            return SumatoriaPilaAux(n,0)
    else:
        print('Parametro incorrecto')

def SumatoriaPilaAux(n,resultado):
    if n==0:
        return resultado#Identificador
    else:
        return SumatoriaPilaAux(n-1,resultado+n)
#Pruebas
#print(SumatoriaCola(8))