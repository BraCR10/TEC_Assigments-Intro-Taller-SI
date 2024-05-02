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
      
def quizWhileD(num):
    if type(num)==int and largoNum(num)>=3:
        numCopia=abs(num)
        lista=pasaLista(num)
        primero=lista[0]
        ultimo=lista[len(lista)-1]
        nuevaLista=[]
        i=0#Se usa para saber posicion original del dig
        while lista!=[]:
            if i%2==0:
                if i==0:#Si es el primer numero
                    nuevaLista+=[(lista[0]+lista[1]-ultimo)**3]
                elif i==largoNum(numCopia)-1:#Si es el ultimo numero
                    nuevaLista+=[(lista[0]+primero-anterior)**3]
                else:
                    nuevaLista+=[(lista[0]+lista[1]-anterior)**3]
            elif i%2!=0:#Si es impar
                if i==0:#Si es el primer numero
                    nuevaLista+=[(lista[0]+lista[1]-ultimo)**2]
                elif i==largoNum(numCopia)-1:#Si es el ultimo numero
                    nuevaLista+=[(lista[0]+primero-anterior)**2]
                else:
                    nuevaLista+=[(lista[0]+lista[1]-anterior)**2]
            i+=1
            anterior=lista[0]
            lista=lista[1:]
        print(nuevaLista,lista)
    else:
        print('Parametros incorrectos o numero con menos de 3 digitos')
#Pruebas
#quizWhileD(234)
def quizForR(num):#Recibe in entero lo pasa a lista y le suma al num el sig y le resta el anterior, ademas si es pocision par lo eleva a 3 o si es impar a 2
    if type(num)==int and largoNum(num)>=3:
        numCopia=abs(num)
        lista=pasaLista(num)
        nuevaLista=[]
        for i in range(len(lista)):
            if i%2==0:
                if i==0:#Si es el primer numero
                    nuevaLista+=[(lista[i]+lista[i+1]-lista[len(lista)-1])**3]
                elif i==largoNum(numCopia)-1:#Si es el ultimo numero
                    nuevaLista+=[(lista[i]+lista[0]-lista[i-1])**3]
                else:
                    nuevaLista+=[(lista[i]+lista[i+1]-lista[i-1])**3]
            elif i%2!=0:#Si es impar
                if i==0:#Si es el primer numero
                    nuevaLista+=[(lista[i]+lista[i+1]-lista[len(lista)-1])**2]
                elif i==largoNum(numCopia)-1:#Si es el ultimo numero
                    nuevaLista+=[(lista[i]+lista[0]-lista[i-1])**2]
                else:
                    nuevaLista+=[(lista[i]+lista[i+1]-lista[i-1])**2]
            i+=1
        print(nuevaLista,lista)
    else:
        print('Parametros incorrectos o numero con menos de 3 digitos')
#Pruebas
#quizForR(234)
