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

#Cuenta solo pres   
def cuentaPare(lista):
    if type(lista)==list:
        cont=0
        check=0
        for i in lista:
            if type(i)!=int:
                print('La lista solo debe tener numeros enteros')
                check=1
            elif i%2==0:
                cont+=1
        if check==0:
            print('La cantidad de pares es: ',cont)
    else:
        print('El parametro debe ser una lista')
#Prueba
#cuentaPare([1,2,6,8,5,7])

#Suma solo pres   
def suma(lista):
    if type(lista)==list:
        suma=0
        check=0
        for i in lista:
            if type(i)!=int:
                print('La lista solo debe tener numeros enteros')
                check=1
            else:
                suma+=i
        if check==0:
            print('Lacsuma de toda la lista es: ',suma)
    else:
        print('El parametro debe ser una lista')
#Prueba
#suma([1,2])

#Suma solo pres   
def sumaPares(lista):
    if type(lista)==list:
        suma=0
        check=0
        for i in lista:
            if type(i)!=int:
                print('La lista solo debe tener numeros enteros')
                check=1
            elif i%2==0:
                suma+=i
        if check==0:
            print('La cantidad de pares es: ',suma)
    else:
        print('El parametro debe ser una lista')
#Prueba
#sumaPares([7,2,8,9])
        
#Suma solo pres y multiplica los impares   
def sumParYMultImp(lista):
    if type(lista)==list:
        suma=0
        mult=1
        check=0
        bandera=0
        for i in lista:
            if type(i)!=int:
                print('La lista solo debe tener numeros enteros')
                check=1
            elif i%2==0:
                suma+=i
            elif i%2!=0:
                mult*=i
                bandera=1
        if check==0 and bandera==1:
            print('La cantidad de pares es: ',suma, ' y la multiplicaion de impares es: ',mult)
        elif check==0 and bandera==0:
            print('La cantidad de pares es: ',suma, ' y la multiplicaion de impares es: 0')
    else:
        print('El parametro debe ser una lista')
#Prueba
sumParYMultImp([])