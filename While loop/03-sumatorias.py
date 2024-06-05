def factorial(num):#Funcion para factorial
    if num<0 or not type(num)==int:#Validacion
        print('Parametros incorrectos')
        return 0
    elif num==0:#Factorial de 0 es 1
        return 1
    else:
        result = num
        i=1
        while i<num:
            result*=i
            i+=1
        return result
#Sumatoria 1
#(i*n)+((factorial(i)**2)*(factorial(i)**3)) Incremento     
def sumatoria1(n):#Inicia siempre en 1 hasta n
    if type(n)!=int:#Validacion
        print("El numero debe ser entero")
    elif n<0:#Validacion
        print("Para esta sumatoria el numero debe ser mayor o igual a 1")
    else:
        i=0
        suma=0
        while i<=n:
            suma=suma+(i*n)+((factorial(i)**2)*(factorial(i)**3))
            i+=1
        print("El valor total de la sumatoria es :", suma)
        
sumatoria1(0)