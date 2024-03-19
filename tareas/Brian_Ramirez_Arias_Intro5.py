#Tarea 5 intro- Brian Ramirez Arias
#Factorial
def factorial(num):#Funcion para factorial
    if num<0 or not type(num)==int:#Validacion
        return 'Parametros incorrectos'
    elif num==0:#Factorial de 0 es 1
        return 1
    else:
        result = num#Result vale num
        for i in range(1, num):#Multiplica de 1 a num-1
            result*=i
        return result
#Largo con for
def largoNum(num):#Funcion que permite obtener el largo
    if isinstance(num,int):#Validacion
        if num==0:#Validacion
            return 1
        else:#Validacion
            num=abs(num)
            contador=0
            for i in range(0,num):
                if num==0:
                    break
                num=num//10#Elimina el ultimo numero
                contador+=1#Contador
            return contador
    else:#Validacion
        return 'Deben ser enteros'

 #Suamtoria   
def sumatoria(n):#Inicia siempre en 1 hasta n
    if type(n)!=int or n<1:#Validacion
        print( "El numero debe ser entero y debe ser mayor o igual a 1")
    else:
        suma=0
        for i in range(1,n+1):#De 1 a n
            suma=suma+( (((factorial(n))**2)**2)+(i**n))/(n+i)#Operacion
        print( suma**2)
#Prueba
#sumatoria(0)

#Recibe dos números de igual tamaño. Enteros positivos de tamaño impar y opera con ellos
def transformador(num1,num2):
    if   largoNum(num1)%2!=0  and largoNum(num1)%2!=0  and largoNum(num1)==largoNum(num2) and isinstance(num1,int) and isinstance(num2,int):#Validacion
        num1Copia=abs(num1)
        num2Copia=abs(num2)
        operacion=0
        bandera=0#Valida si se recorre el numero de der a iqz o alreves
        primera=0#Valida si es la primera vez
        tamanoNums = largoNum(num1)#Cantidad de digitos, se usa para imprimir 0 cuando se esta recorriendo de izq a der
        for  i in range(0,largoNum(num1)):
            if bandera==0:
                primerDig1=num1Copia//(10**(tamanoNums-1))#Extrae el primer numero
                ultimoDig2=num2Copia%10#Consigue el ultimo numero
                if primera==0:
                    operacion=primerDig1+ultimoDig2#Hace la suma
                    primera=1
                else:
                    operacion-=primerDig1+ultimoDig2#Hace la suma
                num1Copia%=(10**(tamanoNums-1))#Crea el nuevo numero
                num2Copia//=10
                bandera=1
            elif bandera==1:
                ultimoDig1=num1Copia%10#Extrae el ultimo numero
                primerDig2=num2Copia//(10**(tamanoNums-1))#Consigue el primer numero
                operacion-=ultimoDig1+primerDig2#Hace la suma
                num1Copia//=10#Crea el nuevo numero
                num2Copia%=(10**(tamanoNums-1))
                bandera=0
            tamanoNums=tamanoNums-1
        print( operacion)
    else:
        print( 'Los 3 numeros deben ser impares y tener el mismo tamaño, ademas deben ser enteros ')
#Prueba
transformador(41741,57465)

