'''Recibe un numero de cualquier tamaño que sea entero y positivo
- Los pares del numero  se le aplica (n+3)**2
-Los impares del numero se aplica (n+2)**3'''
def primeraFuncion(num):
    if type(num)!=int:#Validacion
        print("Para esta funcion se requiere un numero entero")
    elif num<=0:#Validacion
        print('Debe ser un numero positivo o diferente de 0')
    else:
        temp=num#Evita errores con numeros negativos
        suma=0
        mult=1
        check=0#Verifica si  hay numeros impares en la cifra
        while temp!=0:
            ultimoDigito=temp%10#Obtiene el ultimo digito del numero 
            if ultimoDigito%2==0:#Si es par
                suma=suma + (ultimoDigito+3)**2
            else:#Si es impar
                mult=mult*((ultimoDigito+2)**3)
                check=1
            temp//=10#Quita el ultimo digito del numero hasta dejarlo en 0
        if check ==0:#En caso de que no haya un numero impar
            print('El resultado de la suma es: ',suma)
            print('El resultado de la multiplicacion es: 0')
        else:#Si hay numeros impares
            print('El resultado de la suma es: ',suma)
            print('El resultado de la multiplicacion  es: ',mult)

primeraFuncion(456893)