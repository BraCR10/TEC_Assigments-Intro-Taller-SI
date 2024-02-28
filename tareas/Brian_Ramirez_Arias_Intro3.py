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
    
'''Crea una lista con una operacion entre los digitos de los numero, 
cada digito se toma por su posicion por ejemplo:
Si se usa 12 y 34, el programa toma 1 y 3 (1+3)**3 y luego 2 y 4 (2+4)**2 
- Todo negativo se convierte a positivo'''

def funcionConListas(num1,num2):
    if type(num1)==int and isinstance(num2,int) and lenNum(num1)==lenNum(num2):#Validacion
        if num1==0 and num2==0:#Validacion
            return 'La nueva lista es: [0] '
        else: 
            lista1=[]
            if num1==0:#Validacion
                lista1=[0]
            lista2=[]
            if num2==0:#Validacion
                lista2=[0]
            resultado=[]
            num1Copia=abs(num1)#Copias para no destruir y trabajar solo con numero positivos
            num2Copia=abs(num2)#Copias para no destruir y trabajar solo con numero positivos
            while num1Copia>0:#Crea la lista del primer numero
                temp=num1Copia%10#Recolecta el ultimo numero
                lista1=[temp]+lista1
                num1Copia//=10#Quita el ultimo numero
            while num2Copia>0:#Crea la lista del segundo numero
                temp=num2Copia%10#Recolecta el ultimo numero
                lista2=[temp]+lista2
                num2Copia//=10#Quita el ultimo numero
            while lista1!=[]:#Crea la lista resultado
                resultado=resultado+[((lista1[0]+lista2[0])**3)]#Coloca cada resultado al final de la lista
                lista1=lista1[1:]#Elimina elemento 0
                lista2=lista2[1:]#Elimina elemento 0
            return f'La nueva lista es: {resultado}'
    else:#Validacion
        return 'Los numeros deben ser enteros y tener la misma logitud'
#Pruebas
num1=61278
num2=78987
print(funcionConListas(num1,num2))

