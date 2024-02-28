#Sumatoria 1
#(i+n)**2 * (3+n)**2 Incremento     
def sumatoria1(n):#Inicia siempre en 1 hasta n
    if type(n)!=int:#Validacion
        print("El numero debe ser entero")
    elif n<0:#Validacion
        print("Para esta sumatoria el numero debe ser mayor  a 0")
    else:
        i=0
        suma=0
        while i<=n:
            suma=suma+(i+n)**2 * (3+n)**2
            i+=1
        return suma
#Sumatoria 2
#((n*3)**2+4) Incremento     
def sumatoria2(n):#Inicia siempre en 1 hasta n
    if type(n)!=int:#Validacion
        print("El numero debe ser entero")
    elif n<=0:#Validacion
        print("Para esta sumatoria el numero debe ser mayor o igual a 1")
    else:
        i=1
        suma=0
        while i<=n:
            suma=suma+((n*3)**2+4)
            i+=1
        return suma
    
#concatenador
#sumatoria1 + sumatoria2 Incremento     
def concatenador(n1,n2):#Suma ambas sumatorias y las eleva a la 2
    if type(n1)!=int or type(n2)!=int:#Validacion
        print("El numero debe ser entero")
    elif n1<0 or n2<0:#Validacion
        print("Para esta sumatoria el numero debe ser mayor o igual a 0")
    else:
      print('El resultado es: ',(n1+n2)**2)
print(sumatoria1(1))
print(sumatoria2(1))
concatenador(sumatoria1(1),sumatoria2(1))