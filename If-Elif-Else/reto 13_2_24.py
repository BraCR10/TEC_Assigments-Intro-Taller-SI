#Sumatoria desde 0 hasta n
def sumatoria(n):
    limit=n
    sum=0
    while limit >=0:
        sum=sum+limit
        limit-=1
    return sum

#Sumatoria con operacion
def sumatoriaOperacion(n):
    limit=n
    cont=n#Se define para limitar el while
    i=0
    
    while cont >=0:
        i=i+(((i**2)*(limit**3))+((i**limit)+(limit**i)))**2
        cont-=1
    return i

num=int(input('Digite un numero para la sumatoria: '))

print(f'El resultado de la sumatorio del numero {num} es {sumatoria(num)}')

if num==0:
    print(f'El resultado de la sumatoria especial del numero {num} es 0')
else:
    print(f'El resultado de la sumatoria especial del numero {num} es {sumatoriaOperacion(num)}')

    