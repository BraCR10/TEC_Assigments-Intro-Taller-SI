def lenNum(num):#Funcion del largo
    if isinstance(num,int):
        if num==0:#Validacion
            return 1
        else:
            num=abs(num)
            cont=0
            while num!=0:
                num=num//10#Elimina el ultimo numero
                cont+=1#Contador
            return cont
    else:
        return 'Deben ser enteros'
    
#recibe dos numero entero, si es negativo le aplica abs y hace suma y multiplicacion deacuerdo a las posicion de cada digito en los numeros, si estan en posicion par los suma y si estan en pocision impar los multiplica . 
def imparesYPares(num1,num2):
    if type(num2)==int and type(num1)==int and lenNum(num1)==lenNum(num2):#Validacion
        numCopia1=abs(num1)
        numCopia2=abs(num2)
        suma=0
        bandera=0
        mult=1
        while numCopia1!=0 or numCopia2!=0  :
            ultimodig=numCopia1%10
            ultimodig2=numCopia2%10
            if ultimodig%2==0 and ultimodig2%2==0:
                suma+=ultimodig+ultimodig2
            elif ultimodig%2!=0 and ultimodig2%2==0:
                suma+=ultimodig2
                mult*=ultimodig
                bandera=1
            elif ultimodig%2==0 and ultimodig2%2!=0:
                suma+=ultimodig
                mult*=ultimodig2
                bandera=1
            else:
                mult*=ultimodig*ultimodig2
                bandera=1
            numCopia1//=10
            numCopia2//=10
        if bandera==1:
            print('La suma es ',suma,' y la multiplicacion es:', mult)
        else:
            print('La suma es ',suma,' y la multiplicacion es: 0')
    else:#Validacion
        print ('\nEl parametro debe ser 2 numeros enteros e de igual tamaño')
imparesYPares(123,123)


#recibe dos numero entero, si es negativo le aplica abs y encuentra el elemento del centro del número. 
def sumaPorUbicacion(num1,num2):
    if type(num2)==int and type(num1)==int and lenNum(num1)==lenNum(num2):#Validacion
        numCopia1=abs(num1)
        numCopia2=abs(num2)
        suma=0
        bandera=0
        mult=1
        while numCopia1!=0 or numCopia2!=0  :
            ultimodig=numCopia1%10
            ultimodig2=numCopia2%10
            if lenNum(numCopia1)%2==0 and lenNum(numCopia2)%2==0:
                suma+=ultimodig+ultimodig2
            elif lenNum(numCopia1)%2!=0 and lenNum(numCopia1)%2==0:
                suma+=ultimodig2
                mult*=ultimodig
                bandera=1
            elif lenNum(numCopia1)%2==0 and lenNum(numCopia2)%2!=0:
                suma+=ultimodig
                mult*=ultimodig2
                bandera=1
            else:
                mult*=ultimodig*ultimodig2
                bandera=1
            numCopia1//=10
            numCopia2//=10
        if bandera==1:
            print('\nLa suma es ',suma,' y la multiplicacion es:', mult)
        else:
            print('\nLa suma es ',suma,' y la multiplicacion es: 0')
    else:#Validacion
        print ('\nEl parametro debe ser 2 numeros enteros y de igual tamaño')
sumaPorUbicacion(777,444)
