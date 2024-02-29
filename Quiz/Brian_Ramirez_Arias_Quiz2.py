
def lenNum(num):#Funcion del largo
    if isinstance(num,int):
        if num==0:#Validacion
            return 1
        else:
            num=abs(num)
            cont=0
            while num!=0:
                temp=num%10#Recolecta el ultimo numero 
                num=num//10#Elimina el ultimo numero
                cont+=1#Contador
            return cont
    else:
        return 'Deben ser enteros'

#Escribir una funcion que:
#A los pares**2 y los multiplica
#A los impares**3 y los suma
def operacionesPares(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int) and lenNum(num1)==lenNum(num2):#Validacion
        temp1=abs(num1)#Evita errores con numeros negativos

        temp2=abs(num2)#Evita errores con numeros negativos
        mult=0#Contiene una suma
        suma=1#Contiene una multiplicacion
        check=0#Verifica si  hay numeros impares en la cifra
        if temp1!=0:
            while temp1!=0 :
                ultimoDigito1=temp1%10#Obtiene el ultimo digito del numero 
                ultimoDigito2=temp2%10#Obtiene el ultimo digito del numero 
                if ultimoDigito1%2!=0 and ultimoDigito2%2!=0:#Si ambos son impares
                    mult+= (ultimoDigito1**3)+(ultimoDigito2**3)
                elif ultimoDigito1%2==0 and ultimoDigito2%2!=0 :#Si num1 es par y num2 impar
                    mult=mult + (ultimoDigito2**3)
                    suma=suma*(ultimoDigito1**2)
                    check=1
                elif ultimoDigito1%2!=0 and ultimoDigito2%2==0 :#Si num1 es impar y num2 par
                    mult=mult + (ultimoDigito1**3)
                    suma=suma*(ultimoDigito2**2)
                    check=1
                else:#Si ambos son pares
                    suma=suma*(ultimoDigito2**2)*(ultimoDigito1**2)
                    check=1
                temp1//=10#Quita el ultimos digito
                temp2//=10#Quita el ultimos digito
        else:#En caso de que temp1 sea igual a 0
            while temp2!=0 :
                ultimoDigito1=temp1%10#Obtiene el ultimo digito del numero 
                ultimoDigito2=temp2%10#Obtiene el ultimo digito del numero 
                if ultimoDigito1%2!=0 and ultimoDigito2%2!=0:#Si ambos son impares
                    mult+= (ultimoDigito1**3)+(ultimoDigito2**3)
                elif ultimoDigito1%2==0 and ultimoDigito2%2!=0 :#Si num1 es par y num2 impar
                    mult=mult + (ultimoDigito2**3)
                    suma=suma*(ultimoDigito1**2)
                    check=1
                elif ultimoDigito1%2!=0 and ultimoDigito2%2==0 :#Si num1 es impar y num2 par
                    mult=mult + (ultimoDigito1**3)
                    suma=suma*(ultimoDigito2**2)
                    check=1
                else:#Si ambos son pares
                    suma=suma*(ultimoDigito2**2)*(ultimoDigito1**2)
                    check=1
                temp1//=10#Quita el ultimos digito
                temp2//=10#Quita el ultimos digito
        if check ==0:#En caso de que no haya un numero impar
            print('\nEl resultado de la mult es: ',mult)
            print('El resultado de la suma es: 0')
        else:#Si hay numeros impares
            print('\nEl resultado de la mult(suma) es: ',mult)
            print('El resultado de la suma(multiplicacion)  es: ',suma)
    else:
        return print('\nLos parametros deben ser numeros enteros del mismo largo')
#Pruebas
operacionesPares(1234,2356)
operacionesPares(0,9)
operacionesPares(-9,-7)
operacionesPares(-22,20)
operacionesPares(0,0)