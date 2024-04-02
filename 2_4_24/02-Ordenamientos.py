def ordenamientoBurbuja(lista):
    for i in range(1,len(lista)):
        #print(f'Los limites del for externo son: de {i} a {len(lista)} | {len(lista)-i} pasadas')
        #print('estamos en el externo',i, 'vuelta')
        #print(f'Los limites del for interno son: de 0 a {len(lista)-i} | son {len(lista)-i} pasadas')
        for j in range(0,len(lista)-i):
            print('Estamos en el interno',j+1, 'vuelta','|',lista[j],'>',lista[j+1])
            if lista[j]>lista[j+1]:
                #print('Se cumple',j)
                temporal=lista[j+1]
                lista[j+1]=lista[j]
                lista[j]=temporal
        #print(f'Como va quedando la lista despues de bucle interno {lista}\n')
    print(lista)
ordenamientoBurbuja([9,1,4,2,3,7])