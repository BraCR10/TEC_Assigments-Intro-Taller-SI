
#Eleva los impares a las 3 y los multiplica en una variable 
def Impares(num):
    if type(num)==int:
        num=abs(num)
        if num==0:
            return 0
        else:
            return ImparesAux(abs(num),1,0)
    else:
        print('Parametro incorrecto')

def ImparesAux(num,temp,bandera):
    if num==0 and bandera==1:
        return temp
    elif num==0 and bandera==0:
        return 'No hay impares'
    elif (num%10)%2!=0:
        mult=temp*((num%10))**3
        return ImparesAux(num//10,mult,1)
    else:
        return ImparesAux(num//10,temp,bandera)
#Pruebas
#print(Impares(48613))
#print(Impares(59874563214587))
