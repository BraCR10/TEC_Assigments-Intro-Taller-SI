def lenNum(num):#Funcion del largo
    if type(num)!=int:
         print("Para esta funcion se requiere numeros enteros")
    elif num==0:#Validacion
        return 1
    else:
        cont=0
        while num!=0:
            temp=num%10#Recolecta el ultimo numero 
            num=num//10#Elimina el ultimo numero
            cont+=1#Contador
        return cont

def primeraFuncion(num1,num2):
    largo1=lenNum(num1)
    largo2=lenNum(num2)
    if not type(num1)==int or not type(num2)==int:#Validacion
        print("Para esta funcion se requiere dos numeros enteros")
    elif type(num1)==int and type(num2)==int and num1<=0 or num2==0:#Validacion
        print('Deben ser un numeros  diferentes de 0')
    elif largo1 != largo2:
        print('Los numero deben tener la misma longitud')
    else:
        temp1=abs(num1)#Evita errores con numeros negativos
        temp2=abs(num2)#Evita errores con numeros negativos
        suma=0
        mult=1
        check=0#Verifica si  hay numeros impares en la cifra
        while temp1!=0:
            ultimoDigito=temp1%10#Obtiene el ultimo digito del numero 
            if ultimoDigito%2==0:#Si es par
                suma=suma + ultimoDigito
            else:#Si es impar
                mult=mult*ultimoDigito
                check=1
            temp1//=10#Quita el ultimo digito del numero hasta dejarlo en 0
        while temp2!=0:
            ultimoDigito=temp2%10#Obtiene el ultimo digito del numero 
            if ultimoDigito%2==0:#Si es par
                suma=suma + ultimoDigito
            else:#Si es impar
                mult=mult*ultimoDigito
                check=1
            temp2//=10#Quita el ultimo digito del numero hasta dejarlo en 0
        if check ==0:#En caso de que no haya un numero impar
            print('El resultado de la suma es: ',suma)
            print('El resultado de la multiplicacion es: 0')
        else:#Si hay numeros impares
            print('El resultado de la suma es: ',suma)
            print('El resultado de la multiplicacion  es: ',mult)

primeraFuncion("6183",1429)
