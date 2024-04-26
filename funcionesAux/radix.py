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
