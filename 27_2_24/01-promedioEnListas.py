#Promedio de una lista sin destruir 
def promedioLista(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            sum=0
            i=0
            while i<len(lista):
                sum+=lista[i]
                i+=1
            promedio=sum/len(lista)
            return f'{promedio} y la lista queda como {lista}'
    else:
        return '\nEl parametro debe ser una lista, no se puede hacer el promedio '
lista=[6,4,5,2,3]
print('El promedio de los elementos  de la lista es: ',promedioLista(lista))

#Promedio de una lista destruyendo
def promedioLista2(lista):
    if type(lista)==list:
        if lista==[]:
            return 0
        else:
            lenLista=len(lista)
            sum=0
            while lista!=[]:
                sum+=lista[0]
                lista=lista[1:]
            promedio=sum/lenLista
            return f'{promedio} y la lista queda como {lista}'
    else:
        return '\nEl parametro debe ser una lista, no se puede hacer el promedio '
lista=[6,4,5,2,3]
print('El promedio de los elementos  de la lista es: ',promedioLista2(lista))