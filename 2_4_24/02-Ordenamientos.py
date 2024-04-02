def ordenamientoBurbuja(lista):
    for i in range(1,len(lista)):
        #print(f'Los limites del for externo son: de {i} a {len(lista)} | {len(lista)-i} pasadas')
        #print('estamos en el externo',i, 'vuelta')
        #print(f'Los limites del for interno son: de 0 a {len(lista)-i} | son {len(lista)-i} pasadas')
        for j in range(0,len(lista)-i):
            #print('Estamos en el interno',j+1, 'vuelta','|',lista[j],'>',lista[j+1])
            if lista[j]>lista[j+1]:
                #print('Se cumple',j)
                temporal=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=temporal
        #print(f'Como va quedando la lista despues de bucle interno {lista}\n')
    print(lista)
#ordenamientoBurbuja([9,1,4,2,3,7])

def interseccion(lista):
    for i in range(1,len(lista)):
        v=lista[i]
        j=i-1
        while j >=0 and lista[j]>v:
            lista[j+1]=lista[j]
            j-=1
        lista[j+1]=v
    print(lista)
#interseccion([1,8,2,3,4])

def selectionSort(lista):
    for i in range (0,len(lista)-1):
        minimo=i
        for j in range(i+1,len(lista)):
            if lista[minimo]>lista[j]:
                minimo=j
            aux=lista[minimo]
        lista[minimo]=lista[i]
        lista[i]=aux
    print(lista)
#selectionSort([9.1,9.8,1,2,8,9])        

def busquedaSecuencial(lista,num):
    posicion=0
    encontrado=False
    while posicion<len(lista) and  not encontrado:
        if lista[posicion]==num:
            encontrado=True
            break
        else:
            posicion=posicion+1
    return encontrado
#print(busquedaSecuencial([1,2,3,11,7],2))
    
def busquedaBinaria(lista,num):
    primero=0
    ultimo=len(lista)-1
    encontrado=False
    while primero<=ultimo and not encontrado:
        puntoMedio=(primero+ultimo)//2
        if lista[puntoMedio]==num:
            encontrado=True
        else:
            if num<lista[puntoMedio]:
                ultimo=puntoMedio-1
            else:
                primero=puntoMedio+1
    print(encontrado)
#busquedaBinaria([1,2,3,5],1)

def list_reverse(list):
    inicio=0
    fin=len(list)-1
    while inicio<fin:
        list[inicio],list[fin]=list[fin],list[inicio]
        inicio+=1
        fin-=1
    return list

        