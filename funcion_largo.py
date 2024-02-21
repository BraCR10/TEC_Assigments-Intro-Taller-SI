def lenNum(num):#Funcion del largo
    if num==0:#Validacion
        return 1
    else:
        cont=0
        while num!=0:
            temp=num%10#Recolecta el ultimo numero 
            num=num//10#Elimina el ultimo numero
            cont+=1#Contador
    return cont

print(lenNum(12))