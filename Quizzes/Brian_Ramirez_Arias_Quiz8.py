#Pila
def sumatoriaPila(n):
    if type(n)==int and n>=0:
        #Condicion de finalizacion
        if n==0:
            return 0
        else:
            #La llamada recursiva
            return ( ( 0+1)**2)+(n*((n**2)**3))+ SumatoriaPilaAux(n,1)
    else:
        print('Parametro incorrecto')
def SumatoriaPilaAux(n,i):
    if n<i:
        return 0
    else:
        #La llamada recursiva
        return ( ( i+1)**2)+(n*((n**2)**3))+ SumatoriaPilaAux(n,i+1)
#Pruebas
print(sumatoriaPila(2))

#Cola
def SumatoriaCola(n):
    if isinstance(n,int) and n>=0:
        if n==0:
            return 1
        else:
            return SumatoriaColaAux(n,0,0)
    else:
        print('Parametro incorrecto')

def SumatoriaColaAux(n,resultado,i):
    if i>n:
        return resultado#Identificador
    else:
        return SumatoriaColaAux(n,resultado+( ( i+1)**2)+(n*((n**2)**3)),i+1)
#Pruebas
#print(SumatoriaCola(2))