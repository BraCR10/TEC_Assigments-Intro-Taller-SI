

#Construye un numero nuevo de solo pares y escribe una funcion que recibe un numero entero y positivo 
def Pares(num):
    if type(num)==int:
        num=abs(num)
        if num==0:
            return 0
        else:
            return ParesAux(abs(num),0,0,0)
    else:
        print('Parametro incorrecto')

def ParesAux(num,exp,resultado, bandera):
    if num==0 and bandera==1:
        return resultado
    elif num==0 and bandera==0:
        return 'No hay pares'
    elif (num%10)%2==0:
        return ParesAux(num//10,exp+1,resultado+((num%10)*10**exp),1)
    else:
        return ParesAux(num//10,exp,resultado,bandera)