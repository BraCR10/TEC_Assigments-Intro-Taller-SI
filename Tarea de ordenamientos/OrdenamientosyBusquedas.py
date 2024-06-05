#ordemnamiento burbuja
def ordenamientoBurbuja(lista):
     for i in range(1,len(lista)):
          print(len(lista))
          for j in range(0,len(lista)-i):
               if(lista[j] > lista[j+1]):
                    k = lista[j+1]
                    lista[j+1] = lista[j]
                    lista[j] = k
                    #print(lista,len(lista)-i)
ordenamientoBurbuja([100,22,95,1,23,45,450,18,35])
#ordenamiento seleccion
def  selectionsort(lista):
     for  i in range(0,len(lista)-1):
          minimo=i
          for j in range(i+1,len(lista)):
               if lista[minimo] > lista[j]:
                    minimo=j
               aux=lista[minimo]
          lista[minimo]=lista[i]
          lista[i]=aux
     print(lista)

#ordemiento insercion
def  insercionDirecta(lista):
     for i in range(1,len(lista)):
          v=lista[i]
          j=i-1
          while j >= 0 and lista[j] > v:
               lista[j+1] = lista[j]
               j=j-1 
          lista[j+1]=v
          0
     print(lista)

#ordenamiento shell
def  ordenShell(lista):
     inc=int(len(lista)/2 )
     while  inc>0:
          for  i in range(inc,len(lista)):
               j=i
               temp=lista[i]
               while j>=inc and lista[j-inc]>temp:
                    lista[j]=lista[j-inc]
                    j=j-inc 
               lista[j]=temp
          if (inc==2) :
               inc=1
          else :
               inc=int(inc/2.5)
     print(lista)

#Busqueda binaria
def busquedaBinaria(lista,item):
    primero=0
    ultimo=len(lista)-1
    encontrado=False
    while primero <=ultimo and not encontrado:
        puntoMedio=(primero+ultimo)//2
        if lista[puntoMedio]==item:
            encontrado=True
        else:
            if item<lista[puntoMedio]:
                ultimo=puntoMedio-1
            else:
                primero=puntoMedio+1
    print (encontrado)

#Busqueda secuencial
def busquedaSecuencial(lista,nume):
    posicion=0
    encontrado=False
    while posicion < len(lista) and not encontrado:
        if lista[posicion]== nume:
            encontrado = True
        else:
            posicion = posicion+1
    print (encontrado)

#ordenamiento quicksort
def quicksort(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        pivot = lista[0]
        print(pivot)
        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < pivot:
                lista[j+1],lista[i+1] = lista[i+1], lista[j+1]
                i += 1
        lista[0],lista[i] = lista[i],lista[0]
        primera = quicksort(lista[:i])
        segunda = quicksort(lista[i+1:])
        primera.append(lista[i])   
        print(primera + segunda)
    return (primera + segunda)

#ordenamiento radix
#ordenamiento radix
def largo(n):
 if not isinstance(n, int):
     return 'Error'
 elif n == 0:
     return 1
 cont = 0
 for i in range(n):
     cont += 1
     n //= 10
     if n == 0:
         return cont

def radix(lista):
 if not isinstance(lista, list):
     return 'Dato inválido'
 elif lista == []:
     return []
 else:
     for i in range(len(lista)):
         if lista[i] < 0:
             return 'Hay elementos negativos en la lista'
         
     mayor = 0
     for i in range(len(lista)):
         if i == 0:
             mayor = lista[i]
         else:
             if lista[i] > mayor:
                 mayor = lista[i]
                 
     cont = 0
     for i in range(largo(mayor)):
         l0 = []
         l1 = []
         l2 = []
         l3 = []
         l4 = []
         l5 = []
         l6 = []
         l7 = []
         l8 = []
         l9 = []            
         while lista != []:
             if (lista[0] // (10 ** cont)) % 10 == 0:
                 l0 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 1:
                 l1 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 2:
                 l2 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 3:
                 l3 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 4:
                 l4 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 5:
                 l5 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 6:
                 l6 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 7:
                 l7 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 8:
                 l8 += [lista[0]]
             elif (lista[0] // (10 ** cont)) % 10 == 9:
                 l9 += [lista[0]]
             lista = lista[1:]
         print(l0, l1, l2, l3, l4, l5, l6, l7, l8, l9)
         lista = lista + l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9                 
         print(lista)
         cont += 1
     return lista

        
    
