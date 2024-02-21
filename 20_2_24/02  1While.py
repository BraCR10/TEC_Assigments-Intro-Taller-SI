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
    if (type(num1)==int and type(num2)==int) and (largo1 == largo2) and (num1!=0 and num2!=0):#Validacion
        print("Para esta funcion se requiere dos numeros enteros")
        temp1=abs(num1)#Evita errores con numeros negativos
        temp2=abs(num2)#Evita errores con numeros negativos
        suma=0
        mult=1
        check=0#Verifica si  hay numeros impares en la cifra
        while temp1!=0:
            ultimoDigito1=temp1%10#Obtiene el ultimo digito del numero 
            ultimoDigito2=temp2%10#Obtiene el ultimo digito del numero 
            if ultimoDigito1%2==0 and ultimoDigito2%2==0:
                suma=suma + ultimoDigito1+ultimoDigito2
            elif ultimoDigito1%2==0 and ultimoDigito2%2!=0 :
                suma=suma + ultimoDigito1
                mult=mult*ultimoDigito2
                check=1
            elif ultimoDigito1%2!=0 and ultimoDigito2%2==0 :
                suma=suma + ultimoDigito2
                mult=mult*ultimoDigito1
                check=1
            else:
                mult=mult*ultimoDigito1*ultimoDigito2
                check=1 
            temp1//=10
            temp2//=10
        if check ==0:#En caso de que no haya un numero impar
            print('El resultado de la suma es: ',suma)
            print('El resultado de la multiplicacion es: 0')
        else:#Si hay numeros impares
            print('El resultado de la suma es: ',suma)
            print('El resultado de la multiplicacion  es: ',mult)

primeraFuncion("",1429)
