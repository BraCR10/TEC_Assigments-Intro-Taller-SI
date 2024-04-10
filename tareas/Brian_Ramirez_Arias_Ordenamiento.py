def ordenamientoBurbuja(lista):
     for i in range(1,len(lista)):
          for j in range(0,len(lista)-i):
               if(lista[j] > lista[j+1]):
                    k = lista[j+1]
                    lista[j+1] = lista[j]
                    lista[j] = k
     print(lista)
########################################################################################################
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
###################################################################################################################
def  insercionDirecta(lista):
     for i in range(1,len(lista)):
          v=lista[i]
          j=i-1
          while j >= 0 and lista[j] > v:
               lista[j+1] = lista[j]
               j=j-1 
          lista[j+1]=v     
     print(lista)
##############################################################################################################################
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
######################################################################################################################################
def quicksort(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        pivot = lista[0]

        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < pivot:
                lista[j+1],lista[i+1] = lista[i+1], lista[j+1]
                i += 1
        lista[0],lista[i] = lista[i],lista[0]
        primera = quicksort(lista[:i])
        segunda = quicksort(lista[i+1:])
        primera.append(lista[i])   
        
    return (primera + segunda)#Se retorna debido a que se usa en busqueda binaria
###############################################################################################################
#Largo se necesita para radix
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

         lista = lista + l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9                 
         cont += 1
     print(lista)
#######################################################################################
def shakeSort(lista) :# Codigo de https://the-algorithms.com/es/playground?id=0152
    inicio, final = 0, len(lista) - 1
    while inicio < final:
        intercambiado = False
        # Pasa de izq a der
        for i in range(inicio, final):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambiado = True
        if not intercambiado:
            break
        final -= 1  # Decrementa el punto de finalizacion despues de cada pasada 
        # Pasa de der a izq
        for i in range(final, inicio, -1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                intercambiado = True

        if not intercambiado:
            break
        inicio += 1  # Incrementa el punto de inicio despues de cada pasada 
    print( lista)
##########################################################################################################################
def mergeSort(lista):#Codigo de https://platzi.com/tutoriales/1775-algoritmos-python/9403-merge-sort-con-un-ejemplo/
    if len(lista) > 1:
        medio = len(lista) // 2 
        izquierda = lista[:medio]
        derecha = lista[medio:]

        # Llamada recursiva en cada mitad.
        mergeSort(izquierda)
        mergeSort(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0; j = 0
        # Iterador de la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista
###########################################################################################################
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
    return (encontrado)
##################################################################################################
#Busqueda secuencial
def busquedaSecuencial(lista,nume):
    posicion=0
    encontrado=False
    while posicion < len(lista) and not encontrado:
        if lista[posicion]== nume:
            encontrado = True
        else:
            posicion = posicion+1
    return (encontrado)
##################################################################################################################
def menu():
    while True:#Menu
        #Opciones de menu
        print('\n--- Programa de ordenamientos ---\n')
        print('Lista de opciones:\n')
        print('1-Ordenamientos')
        print('2-Busquedas ')
        print('3-Salir ')
        opcion=int(input('\nEscoja un numero: '))
        if opcion==1:#Ordenamientos
            print('Lista de opciones:\n')
            print('1.1-Burbuja')
            print('1.2-Seleccion ')
            print('1.3-Insercion')
            print('1.4-Shell')
            print('1.5-Quicksort')
            print('1.6-Radix')
            print('1.7-Shake')
            print('1.8-Merge')
            opcion=float(input('\nEscoja un numero: '))
            lista=str(input('\nIngrese los numero separado por comas(,) con el formato elemento1,elemento2..: '))
            print('\n')
            lista=lista.split(',')
            for i in range(len(lista)):#Para hacer todos los datos numeros
                lista[i]=int(lista[i])
            if opcion==1.1:#Burbuja
                ordenamientoBurbuja(lista)
            elif opcion==1.2:#Seleccion
               selectionsort(lista) 
            elif opcion==1.3:#Insercion
               insercionDirecta(lista) 
            elif opcion==1.4:#Shell
                ordenShell(lista)
            elif opcion==1.5:#QuickSort
                print(quicksort(lista))#El unico con retorno para usarlo en busqueda binaria
            elif opcion==1.6:#Radix
                radix(lista)
            elif opcion==1.7:#Shake
                shakeSort(lista)
            elif opcion==1.8:#Merge
                if len(mergeSort(lista))==len(lista):#Debido a que merge es recursiva
                    print(mergeSort(lista))
            temp=str(input('\n Presione enter para continuar: '))
        elif opcion==2:
            print('\nLista de opciones:\n')
            print('2.1-Secuencial')
            print('2.2-Binaria ')
            opcion=float(input('\nEscoja un numero: '))
            lista=str(input('\nIngrese los numero separado por comas(,) con el formato elemento1,elemento2..: '))
            num=int(input('\nIngrese el entero a buscar: '))
            print('\n')
            lista=lista.split(',')
            for i in range(len(lista)):#Para hacer todos los datos numeros
                lista[i]=int(lista[i])
            if opcion==2.1:#Secuencial
                if busquedaSecuencial(lista,num) == True:
                    print('--> El numero ',num,' SI esta presente en la lista')
                else:
                    print('--> El numero ',num,' NO esta presente en la lista')
            elif opcion==2.2:#Binaria
                if busquedaBinaria(quicksort(lista),num)==True:#Para este metodo se necesita la lista ordenada, se usa el metodo mas rapido 
                    print('--> El numero ',num,' SI esta presente en la lista')
                else:
                    print('--> El numero ',num,' NO esta presente en la lista')
            temp=str(input('\n Presione enter para continuar: '))
        elif opcion==3:
            break
        else:
            print('\n ---> Esta opcion no exite, vuelva a intentarlo ')
        
menu()
