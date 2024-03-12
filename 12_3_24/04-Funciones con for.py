def largoNum(num):#Funcion del largo
    if isinstance(num,int):
        if num==0:#Validacion
            return 1
        else:
            n=abs(num)#Negativos
            cont=0
            for i in range(n):
                if n ==0:#Corta el bucle cuando n vale 0
                    return cont
                cont+=1
                n//=10
    else:
        return 'Deben ser enteros'
#Prueba
#print(largoNum(555))

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
#Prueba
#print(factorial(5))

def sumatoriaInc(n):#Inicia siempre en 1 hasta n
    if type(n)!=int or n<0:#Validacion
        return "El numero debe ser entero y debe ser mayor o igual a 0"
    elif n==0:#Validacion
        return 1
    else:
        suma=0
        for i in range(0,n+1):#De 0 a n
            suma=suma+(factorial(factorial(i)+(n+i)**2))#Operacion
        return suma
#Prueba
#print(sumatoriaInc(3))

def sumatoriaDec(n):#Inicia siempre en 1 hasta n
    if type(n)!=int or n<0:#Validacion
        return "El numero debe ser entero y debe ser mayor o igual a 0"
    elif n==0 :#Validacion
        return 1
    else:
        suma=0
        for i in range(n,-1,-1):#De n a 0
            suma=suma+(factorial(factorial(i)+(n+i)**2))#Operacion
        return suma
#Prueba    
#sumatoriaDec(3)
    
def largoLista(lista):
    if type(lista)!=list:#Validacion
        return "Debe ser una lista"
    else:
        cont=0
        for i in range(len(lista)):#De 0 a n
            cont+=1
        return cont
#Prueba
#print(largoLista([1,2]))