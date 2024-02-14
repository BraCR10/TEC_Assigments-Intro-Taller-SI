print('¡Contador de digitos pares en una cifra entera!')
print('-------------------------------------------------')
num=int(input('Digite un numero entero en la consola: '))
def verificadorPares(num):
    cont=0
    if num==0:
        print('Has digitado 0, se considera un numero par.')
    else:
        while num!=0:
            ultimoDigito=num%10
            if ultimoDigito%2==0:
                cont+=1
            num//=10
        print(f'La cantidad de digitos pares en el numero es: {cont}')

verificadorPares(num)

