#Escribir una funcion que recibe una lista y los suma destruyendo
lista=[2,3,4,5,6]
def sumador1(lista):
    if isinstance(lista,list):
        if lista==[]:
            return 0
        else:
            sum=0
            while lista!=[]:
                sum+=lista[0]
                lista=lista[1:]
            return sum
    else:
        return '\nEl parametro debe ser una lista, no se puede hacer la suma'
print('La suma de los elementos de la lista es: ',sumador1(lista))

#Escribir una funcion que recibe una lista y los suma sin destruir
def sumador2(lista):
    if isinstance(lista,list):
        if lista==[]:
            return 0
        else:
            sum=0
            i=0
            while i<len(lista):
                sum+=lista[i]
                i+=1
            return sum
    else:
        return '\nEl parametro debe ser una lista, no se puede hacer la suma'
print('La suma de los elementos de la lista es: ',sumador2(lista))


        