#Funcion con 2 numeros enteros positivos(abs) y mismo largo 
#num1=1023 -> 123
#num2=2305 -> 235
#sumar
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
    else:#Validacion
        return 'Deben ser enteros'
def sumasinceros(num1,num2):
    if type(num1)==int and isinstance(num2,int) and lenNum(num1)==lenNum(num2):
        num1=abs(num1)#Para siempre tener positivos
        num2=abs(num2)#Para siempre tener positivos
        expnum1=0
        expnum2=0
        numNuevo1=0
        numNuevo2=0
        while num1!=0:
            if num1%10==0:#Ve el ultimo digito del numero, para brincarse los 0s
                num1//=10#Quita el ultimo digito
            else:
                numNuevo1+=(num1%10)*(10**expnum1)#Concatena cada numero en el entero
                #Primero numNuevo1 = 3*1=3 Segundo numNuevo1 = 3*1=3 + 2*10=20 ........
                num1//=10#Quita el ultimo digito
                expnum1+=1
        while num2!=0:
            if num2%10==0:#Ve el ultimo digito del numero, para brincarse los 0s
                num2//=10#Quita el ultimo digito
            else:
                numNuevo2+=(num2%10)*(10**expnum2)
                num2//=10
                expnum2+=1
        return numNuevo1+numNuevo2
    else:
        return 'Deben ser enteros'
print('La suma es de: ',sumasinceros(1023,2305))

