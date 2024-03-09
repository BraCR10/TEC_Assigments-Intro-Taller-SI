#Primer Parcial
#Brian Ramirez Arias Carnet:2024109557

def factorial(num):#Funcion que permite calcular el factorial
    if (num>0 or num<0) and type(num)==int:#Validacion
        resultado = num
        validador=abs(num)#Se utiliza para sacar factorial a negativos
        i=1
        while i<validador:#Validador permite calcular tanto factorial de negativos y positivos
            resultado*=i
            i=i+1
        return resultado
    elif num==0:#Factorial de 0 es 1
        return 1
    else:#Se ejecuta solo en caso de que el parametro no sea entero
        return 0

def largoNum(num):#Funcion que permite obtener el largo
    if isinstance(num,int):#Validacion
        if num==0:#Validacion
            return 1
        else:#Validacion
            num=abs(num)
            contador=0
            while num!=0:
                num=num//10#Elimina el ultimo numero
                contador+=1#Contador
            return contador
    else:#Validacion
        return 'Deben ser enteros'

def UNO(n):#Esta funcion realiza una sumatoria, empienza en 1 y el parametro n representa el final
    if n > 0 and isinstance(n,int):#Validacion
        i=1
        suma=0
        while i<=n:#Desde 1 hasta n
            suma=suma+( ( ( (factorial(i**2))**3 ) * ( (  (n**2)+1 )**n ) ) * ( (n-1)**2 ) )/ (( 3*( (n*(i)**2)**i ) ) + (n**3)) # Se realiza las operaciones y se almacena en suma
            i=i+1  
        print(suma**3)#Resultado
    else:#Validacion
        print('El parametro debe ser mayor a 0 y entero')

def DOS(num):#Recibe un número de cualquier tamaño entero positivo, cada vez que se encuentra un digito cero lo cambia por un 101
    if isinstance(num,int):#Validacion
        num=abs(num)#Siempre la funcion va a trabajar con positivos
        nuevoNum=0
        ceros=1#Se utiliza para agragarle ceros al numero nuevo
        while num!=0:
            ultimoDigito=num%10#Obtiene el ultimo digito del numero
            if ultimoDigito==0:
                operacion=1*10000+(0+1)*1000+ultimoDigito*100+(0+2)*10+1#Operacion para cada cero
                nuevoNum=nuevoNum+operacion*ceros#Le suma a nuevoNum la opercion y lo multiplica la cantidad de ceros necesaria para agregar mas numeros
                ceros=ceros*100000#Agrega 5 ceros para sumar los 5 digitos de operacion
            else:
                nuevoNum=nuevoNum+ ultimoDigito*ceros#Agrega los numeros diferentes de 0 a nuevoNum
                ceros=ceros*10#Agrega 1 cero mas para sumar los demas digitos
            num=num//10#Quita el ultimo digito de num
            
        print(nuevoNum)#Resultado
                
        
def TRES(num1,num2):#Crea 2 listas combinando 2 numero enteros
    if largoNum(num1)==largoNum(num2) and isinstance(num1,int) and isinstance(num2,int):#Validacion
        num1Copia=abs(num1)#Copias para destuir y hacer lista 1
        num2Copia=abs(num2)#Copias para destuir y hacer lista 1
        listaNum1=[]
        listaNum2=[]
        bandera=0#Se utiliza para saber si se esta agregando un digito de num1 o num2
        numDigitos1 = largoNum(num1Copia)#Cantidad de digitos, se usa para imprimir 0 cuando se esta recorriendo de izq a der
        numDigitos2 = largoNum(num2Copia)#Cantidad de digitos, se usa para imprimir 0 cuando se esta recorriendo de izq a der
        i=largoNum(num1Copia)#Para limitar while
        while i>0:#Genera la lista 1, recorre numero de izq a der
            if bandera==0:#Num1
                temp1=num1Copia//(10**(numDigitos1-1))#Extrae el primer numero
                listaNum1=listaNum1+[[1,0,1,temp1-1,temp1,temp1+1,-1,0,-1]]#Agrega a la lista
                num1Copia%=(10**(numDigitos1-1))#Crea el nuevo numero
                num2Copia%=(10**(numDigitos2-1))#Crea el nuevo numero
                bandera=1     
            else:#Num2
                temp1=num2Copia//(10**(numDigitos2-1))#Extrae el primer numero
                listaNum1=listaNum1+[[-2,0,-2,temp1-1,temp1,temp1+1,2,0,2]]#Agrega a la lista
                num2Copia%=(10**(numDigitos2-1))#Crea el nuevo numero
                num1Copia%=(10**(numDigitos1-1))#Crea el nuevo numero
                bandera=0
            numDigitos1-=1
            numDigitos2-=1
            i-=1
        bandera=0
        num1Copia=abs(num1)#Copias para destuir y hacer lista 2
        num2Copia=abs(num2)#Copias para destuir y hacer lista 2
        i=largoNum(num1Copia)#Para limitar while
        while i>0:#Genera la lista 2, recorre numero de der a izq
            if bandera==0:#Num1
                if largoNum(num1)%2==0:#Verifica si es par
                    temp1=num1Copia%10#Extrae el ultimo numero
                    listaNum2=listaNum2+[[1,0,1,temp1-1,temp1,temp1+1,-1,0,-1]]#Agrega a la lista
                else:#Verifica si es impar
                    temp1=num2Copia%10#Extrae el ultimo numero
                    listaNum2=listaNum2+[[-2,0,-2,temp1-1,temp1,temp1+1,2,0,2]]#Agrega a la lista
                num1Copia//=10#Crea el nuevo numero
                num2Copia//=10#Crea el nuevo numero
                bandera=1
            else:#Num2
                if largoNum(num1)%2==0:#Verifica si es par
                    temp1=num2Copia%10#Extrae el ultimo numero
                    listaNum2=listaNum2+[[-2,0,-2,temp1-1,temp1,temp1+1,2,0,2]]#Agrega a la lista
                else:#Verifica si es impar
                    temp1=num1Copia%10#Extrae el ultimo numero
                    listaNum2=listaNum2+[[1,0,1,temp1-1,temp1,temp1+1,-1,0,-1]]#Agrega a la lista
                num2Copia//=10#Crea el nuevo numero
                num1Copia//=10#Crea el nuevo numero
                bandera=0
            i-=1
        print(listaNum1)#Resultado 
        print(listaNum2)#Resultado
        print(num1,num2)#Resultado
    else:
        print('Los numeros deben ser del mismo largo y enteros')
        
def CUATRO(num1,num2,num3):
    if largoNum(num1)>=3 and largoNum(num2)>=3 and largoNum(num3)>=3 and largoNum(num1)%2!=0  and largoNum(num2)%2!=0 and largoNum(num3)%2!=0 and largoNum(num1)==largoNum(num2)==largoNum(num3) and isinstance(num1,int) and isinstance(num3,int) and isinstance(num2,int):#Validacion
        num3Copia=abs(num3)
        num1Copia=abs(num1)
        num2Copia=abs(num2)
        listaNums=[]
        tamanoNums = largoNum(num1)#Cantidad de digitos, se usa para imprimir 0 cuando se esta recorriendo de izq a der
        i = largoNum(num1)
        while i>0:
            primerDig1=num1Copia//(10**(tamanoNums-1))#Extrae el primer numero
            ultimoDig2=num2Copia%10#Consigue el ultimo numero
            primerDig3=num3Copia//(10**(tamanoNums-1))#Extrae el primer numero
            listaNums=listaNums+[(primerDig1+ultimoDig2-primerDig3)**2]+[(primerDig3+ultimoDig2-primerDig1)**3]#Inserta en la lista los numero y las operaciones
            num1Copia%=(10**(tamanoNums-1))#Crea el nuevo numero
            num2Copia//=10
            num3Copia%=(10**(tamanoNums-1))#Crea el nuevo numero
            tamanoNums=tamanoNums-1
            i-=1
        print(listaNums)
    else:
        print('Los 3 numeros deben ser impares y tener el mismo tamaño, el cual debe ser mayor o igual a 3, ademas deben ser enteros ')
