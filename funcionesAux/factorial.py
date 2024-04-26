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
    
print(factorial(5))