#Parte A
#Esta funcion eleva cada impar en una cifra entera al cubo y los suma
def primeraFuncion(num):
    if type(num)!=int:#Validacion
        print("Para esta funcion se requiere un numero entero")
    elif num==0:#Validacion
        print('No hay numeros impares en el numero entero')
    else:
        temp=abs(num)#Evita errores con numeros negativos
        suma=0
        check=0#Verifica si  hay numeros impares en la cifra
        while temp!=0:
            ultimoDigito=temp%10#Obtiene el ultimo digito del numero 
            if ultimoDigito%2!=0:
                suma=suma + (ultimoDigito**3)
                check=1
            temp//=10#Quita el ultimo digito del numero hasta dejarlo en 0
        if check ==0:#En caso de que no haya un numero impar
            print('No hay numeros impares en el numero entero')
        else:#Si hay numeros impares
            print('El resultado de la suma  es : ', suma)

num=23456789123334567
primeraFuncion(num)
print('**************************************************************************')
#Parte B
#Esta funcion eleva cada numero par al cubo y los suma, ademas multiplica los (impares**2)+1
def segundaFuncion(num):
    if type(num)!=int:#Validacion
        print("Para esta funcion se requiere un numero entero")
    elif num==0:#Validacion
        print('El resultado de la suma es: 0')
        print('El resultado de la multiplicacion es: 0')
    else:
        temp=abs(num)#Evita errores con numeros negativos
        suma=0
        mult=1
        check=0#Verifica si hay numeros impares en la cifra
        while temp!=0:
            ultimoDigito=temp%10#Obtiene el ultimo digito del numero 
            if ultimoDigito%2==0:#Si es par
                suma=suma + (ultimoDigito**3)
            else:#Si es impar
                mult=mult*((ultimoDigito**2)+1)
                check=1
            temp//=10#Quita el ultimo digito del numero hasta dejarlo en 0
        if check ==0:#En caso de que no haya un numero impar
            print('El resultado de la suma es: ',suma)
            print('El resultado de la multiplicacion es: 0')
        else:#Si hay numeros impares
            print('El resultado de la suma es: ',suma)
            print('El resultado de la multiplicacion  es: ',mult)

num2=2548610891255548610
segundaFuncion(num2)
