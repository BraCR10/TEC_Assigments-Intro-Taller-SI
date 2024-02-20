#Parte I
#Sumatoria 1
#(((i**3+n**4+i**5)**5)*((n**n-i)+i**3)**2)**2 Incremento     
def sumatoria1(n):#Inicia siempre en 1 hasta n
    if type(n)!=int:#Validacion
        print("El numero debe ser entero")
    elif n<=0:#Validacion
        print("Para esta sumatoria el numero debe ser mayor o igual a 1")
    else:
        i=1
        suma=0
        while i<=n:
            suma=suma+(((i**3+n**4+i**5)**5)*((n**n-i)+i**3)**2)**2
            i=i+1
        print("El valor total de la sumatoria es :", suma)
        
sumatoria1(1)
print('**************************************************************************')
#Parte II
#Sumatoria 2
#((i**3+i**4+i**5)**5)*(n**4+i**3)**2 Incremento
def sumatoria2(n):#Inicia siempre en 1 hasta n
    if type(n)!=int:#Validacion
        print("El numero debe ser entero")
    elif n<=0:#Validacion
        print("Para esta sumatoria el numero debe ser mayor o igual a 1")
    else:
        i=1
        suma=0
        while i<=n:
            suma=suma+((i**3+i**4+i**5)**5)*(n**4+i**3)**2
            i=i+1
        print("El valor total de la sumatoria es :", suma)
sumatoria2(1)
