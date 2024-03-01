def lenNum(num):#Funcion del largo
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
#recibe un numero entero, positivo de tamaño impar y encuentra el elemento del centro del número. 
def inspector(num):
    if type(num)==int and lenNum(num)%2!=0 and num>=0:#Validacion
        numCopia=num
        while lenNum(numCopia)-1!=lenNum(num)//2:#Se detiene cuando el la copia del numero es igual a la diferencia entera del numero original
            numCopia//=10
        resultado=numCopia%10
        print( '\nEl numero del medio es: ',resultado)
    else:#Validacion
        print ('\nEl parametro debe se un numero entero, impar y positivo')
#Prueba       
inspector(187)

#Recibe un entero positivo de tamaño impar, lo pasa a lista y encuentra el numero del centro
def inspector2(numero):
    if type(numero)==int and lenNum(numero)%2!=0 and numero>=0:#Validacion
        if numero==0:
            print( '\nEl numero del medio en la lista es: 0')
        else: 
            lista=[]
            num=numero#Copia para destruir
            while num>0:
                temp=num%10#Recolecta el ultimo numero
                lista=[temp]+lista
                num//=10#Quita el ultimo numero
            print ('\nEl numero del medio en la lista es :', lista[len(lista)//2],' y  la lista', lista)#Se hace divicion de 2 entera a len(lista) y se elecciona ese num en la lista 
    else:
        print( '\nEl parametro debe se un numero entero, impar y positivo ')
#Prueba
inspector2(878)

#Construye una lista nueva de  los pares de la lista trabajando de atrás hacia adelante
def transformador(lista):
    if isinstance(lista,list):#Validacion
        if lista==[]:#Validacion
            print( 'La lista esta vacia')#Validacion
        else:
            check=0#Valida si todos los elemnetos son enteros
            i=len(lista)-1#Se le resta 1 para que no haya error al iterar en la lista
            nuevaLista=[]
            while i>=0:
                if type(lista[i])!=int:#Si hay un elemento que no es numero
                    print( '\nLa lista solo puede tener numeros enteros, no se puede hacer la operacion')
                    check=1
                    break
                if lista[i]%2==0:#Solo enteros
                    nuevaLista=nuevaLista+[lista[i]]
                i-=1
            if check==0:
                print('\nLa nueva lista es: ', nuevaLista)
    else:#Validacion
        print( '\nEl parametro debe ser una lista, no se puede hacer la operacion')

#Pruebas
transformador([1,2,3,4,5,6,7,8,9,10])

