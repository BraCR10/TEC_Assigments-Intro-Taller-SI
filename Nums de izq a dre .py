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
def izqAder(num):#Menejar numero de izq a der
    numOriginal = num#Copia del numero
    numDigitos = lenNum(numOriginal)#Cantidad de digitos
    while numDigitos > 0:
        temp1=num//(10**(numDigitos-1))#Extrae el primer numero
        #print('Primer numero de izq a der: ',temp1)
        num%=(10**(numDigitos-1))#Crea el nuevo numero
        numDigitos=numDigitos-1
        print (temp1 )


izqAder(1203)