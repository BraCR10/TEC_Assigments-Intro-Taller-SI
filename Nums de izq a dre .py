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
#Menejar numero de izq a der
num=3056#Este metodo no toma los 0s, ¡Cuidado!
print('Numero original:', num,' \n')
while num!=0:
    temp1=num//(10**(lenNum(num)-1))#Extrae el numero
    print('Primer numero de izq a der: ',temp1)
    num%=(10**(lenNum(num)-1))#Crea el nuevo numero
    print('El numero que va quedando',num,' \n')

