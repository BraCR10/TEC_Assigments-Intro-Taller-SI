
def heap(lista):
    print(lista)#Impresion de la lista que ingresa
    lista=[0]+lista#Se inserta un elemento cualquiera en la posicion 0 para trabajar como esta echo el codigo originalmente
    for siguiente in range(1,len(lista)):
        siguiente=siguiente#Siempre tiene el valor de siguiente
        nuevaLlave=lista[siguiente]
        padre=(siguiente)//2
        lista[siguiente]=nuevaLlave
        while siguiente!=1 and lista[padre]<=lista[siguiente]:
            aux=lista[padre]
            lista[padre]=lista[siguiente]
            lista[siguiente]=aux
            siguiente=padre
            padre=(siguiente)//2
            print(lista[1:])#Impresion de la lista en cada iteracion, se elimina el elemento insertado
    print('Final del heap:',lista[1:],'\n')#Impresion final de la lista
    return lista[1:]#Retorna la lista eliminando el elemento ficticio
        

def heapsort(lista):
    print(lista)#Impresion de la lista que ingresa
    lista=[0]+lista#Se inserta un elemento cualquiera en la posicion 0 para trabajar como esta echo el codigo originalmente
    for ultima in range(len(lista)-1,1,-1):#De el largo de la lista original a 2, decrementando en 1
        #Mueve la llave raíz al ultimo lugar
        llaveAnterior=lista[ultima]
        lista[ultima]=lista[1]
        #Ajusta el árbol al tamaño menos 1
        padre=1
        #Busca al mayor de los hijos de la raíz
        if (ultima-1>=3) and (lista[3]>lista[2]):
            hijo=3
        else:
            hijo=2
        #Mueve las llaves hacia arriba hasta encontrar el lugar para la llaveanterior 
        while (hijo<=ultima-1) and (lista[hijo]>llaveAnterior):
            lista[padre]=lista[hijo]
            padre=hijo
            hijo = padre*2
            #Encuentra al mayor de los hijos del padre
            if (hijo+1<=ultima-1) and (lista[hijo+1]>lista[hijo]):
                hijo=hijo+1
        lista[padre]=llaveAnterior
        print(lista[1:])
    print('Final del heapsort:',lista[1:])      
    return lista[1:]
#Pruebas
#heapsort(heap([45,12,400,89,1000,2,5,1,700,5000]))
#listaHeap=heap([45,12,400,89,1000,2,5,1,700,5000])
#heapsort(listaHeap)
