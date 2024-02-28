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
def operacionesConElementos(num1,num2):#Crea una lista con una operacion entre los digitos de los numero cada numero tiene una cordenada por ejemplo
    # 12 y 34, el programa toma 1 y 3 (1+3)**3 y luego 2 y 4 (2+4)**2
    if type(num1)==int and isinstance(num2,int) and lenNum(num1)==lenNum(num2):#Validacion
        if num1<=0 and num2<=0:#Validacion
            return f'La nueva lista es: {[0]}'
        else: 
            lista1=[]
            if num1==0:#Validacion
                lista1=[0]
            lista2=[]
            if num2==0:#Validacion
                lista2=[0]
            result=[]
            num1Copy=num1#Copias para no destruir 
            num2Copy=num2#Copias para no destruir 
            while num1Copy>0:#Crea la lista del primer numero
                temp=num1Copy%10#Recolecta el ultimo numero
                lista1=[temp]+lista1
                num1Copy//=10#Quita el ultimo numero
            while num2Copy>0:#Crea la lista del primer numero
                temp=num2Copy%10#Recolecta el ultimo numero
                lista2=[temp]+lista2
                num2Copy//=10#Quita el ultimo numero
            while lista1!=[]:#Crea la liesta resultado
                result=result+[((lista1[0]+lista2[0])**3)]#Coloca cada resultado al final de la lista
                lista1=lista1[1:]#Elimina elemento 0
                lista2=lista2[1:]#Elimina elemento 0
            return f'La nueva lista es: {result}'
    else:#Validacion
        return f'Los numeros deben ser enteros y tener la misma logitud'
num1=88
num2=12
print(operacionesConElementos(num1,num2))

            
