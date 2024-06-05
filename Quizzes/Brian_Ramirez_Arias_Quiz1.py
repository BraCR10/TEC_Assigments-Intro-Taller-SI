print('¡Este programa suma los pares en un numero y multiplica los impares!')
print('-------------------------------------------------')
#num=int(input('Digite un numero entero en la consola: '))
num=0

def pares_e_impares(num):
    sum=0
    multi=1
    contMul=0
    if num==0:
        print(f'La suma de los numeros pares en la cifra es 0 y la multiplicacion de los impares es 0')
    else:
        while num!=0:
            ultimoDigito=num%10#Obtiene el ultimo digito del numero 
            if ultimoDigito%2==0:
                sum+=ultimoDigito
            else:
                multi*=ultimoDigito
                contMul+=1
            num//=10#Quita el ultimo digito del numero hasta dejarlo en 0
        if contMul==0:
            print(f'La suma de los numeros pares en la cifra es {sum} y la multiplicacion de los impares es 0')
        else:
            print(f'La suma de los numeros pares en la cifra es {sum} y la multiplicacion de los impares es {multi}')


pares_e_impares(num)

