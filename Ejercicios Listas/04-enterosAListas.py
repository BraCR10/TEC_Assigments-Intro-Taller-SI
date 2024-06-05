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

#Creador de listas apartir de enteros destruyendo de izq a der, hay problemas con el 0
def covertidor(numero):
    if type(numero)==int:#Validacion
        if numero==0:
            return [0]
        else: 
            lista=[]
            validarCeros=numero
            while numero>0:
                temp=numero//(10**(lenNum(numero)-1))#Extrae el primer numero
                lista=lista+[temp]
                numero%=(10**(lenNum(numero)-1))#Crea el nuevo numero
            return f'El numero queda como {numero} y la lista es {lista}'
    else:
        return '\nEl parametro debe ser una lista, no se puede hacer el promedio '
entero=1623
print(covertidor(entero))

#Creador de listas apartir de enteros sin detruir de izq a der, hay problemas con el 0
def covertidor2(numero):
    if type(numero)==int:#Validacion
        if numero==0:
            return [0]
        else: 
            lista=[]
            num=numero
            while num>0:
                temp=num//(10**(lenNum(num)-1))#Extrae el primer numero
                lista=lista+[temp]
                num%=(10**(lenNum(num)-1))#Crea el nuevo numero
            return f'El numero queda como {numero} y la lista es {lista}'
    else:
        return '\nEl parametro debe ser una lista, no se puede hacer el promedio '
entero=1623
print(covertidor2(entero))

