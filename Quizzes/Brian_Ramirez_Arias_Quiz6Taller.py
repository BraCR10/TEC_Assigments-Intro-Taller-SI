def largoNum(num):#Funcion del largo
    if isinstance(num,int):
        if num==0:#Validacion
            return 1
        else:
            num=abs(num)
            cont=0
            while num!=0:
                num=num//10#Elimina el ultimo numero
                cont+=1#Contador
            return cont
    else:
        return 'Deben ser enteros'
def pasaLista(num):
    if type(num)==int:
        lista=[]
        while largoNum(num)!=0 and num!=0:
            dig=num%10
            lista=[dig]+lista
            num//=10
        return(lista) 
      

def quizWhileSD(num):
    if type(num)==int and largoNum(num)>=3:
        num=abs(num)
        lista=pasaLista(num)
        nuevaLista=[]
        i=len(lista)-1#Se usa para saber posicion original del dig
        bandera=0
        while i>=0:
            if bandera==0:
                if i==0:#Si es el ultimo numero
                    nuevaLista+=[(lista[i]+lista[i+1]-lista[len(lista)-1])**2]
                elif i==largoNum(num)-1:#Si es el primero numero
                    nuevaLista+=[(lista[i]+lista[0]-lista[i-1])**2]
                else:
                    nuevaLista+=[(lista[i]+lista[i+1]-lista[i-1])**2]
                bandera=1
            elif bandera==1:#Si es impar la pocision 
                if i==0:#Si es el primer numero
                    
                    nuevaLista+=[(lista[i]+lista[i+1]-lista[len(lista)-1])**3]
                else:
                    nuevaLista+=[(lista[i]+lista[i+1]-lista[i-1])**3]
                bandera=0
            i-=1
        print(nuevaLista,lista)
    else:
        print('Parametros incorrectos o numero con menos de 3 digitos')
#Pruebas
#quizWhileSD(11878)
def quizForItem(num):
    if type(num)==int and largoNum(num)>=3:
        num=abs(num)
        lista=pasaLista(num)
        nuevaLista=[]
        posicion=0#Constador de posicion
        posicionFinal=len(lista)-1#Para saber si la lista terminaba en par o impar
        bandera=0#Para elevar a la 3 o a la 2
        for i in lista:
            if posicionFinal%2==0:#Si el ultimo num termina en  posicion par
               if bandera==0:
                    if posicion==0:#Si es el ultimo numero
                        nuevaLista=[(i+lista[posicion+1]-lista[len(lista)-1])**2]+nuevaLista
                    elif posicion==largoNum(num)-1:#Si es el primero numero
                        nuevaLista=[(i+lista[0]-lista[posicion-1])**2]+nuevaLista
                    else:
                        nuevaLista=[(i+lista[posicion+1]-lista[posicion-1])**2]+nuevaLista
                    bandera=1
               elif bandera==1:
                    nuevaLista=[(i+lista[posicion+1]-lista[posicion-1])**3]+nuevaLista
                    bandera=0
               posicion+=1
            elif posicionFinal%2!=0:#Si el ultimo num termina en  posicion impar
                if posicion==0:#Si es el ultimo numero
                    nuevaLista=[(i+lista[posicion+1]-lista[len(lista)-1])**3]+nuevaLista
                elif posicion==largoNum(num)-1:#Si es el primero numero
                    nuevaLista=[(i+lista[0]-lista[posicion-1])**2]+nuevaLista
                else:
                    if bandera==0:
                        nuevaLista=[(i+lista[posicion+1]-lista[posicion-1])**2]+nuevaLista
                        bandera=1
                    else:
                        bandera=0
                        nuevaLista=[(i+lista[posicion+1]-lista[posicion-1])**3]+nuevaLista
                posicion+=1
        print(nuevaLista,lista)
    else:
        print('Parametros incorrectos o numero con menos de 3 digitos')
#Pruebas
#quizForItem(11878)