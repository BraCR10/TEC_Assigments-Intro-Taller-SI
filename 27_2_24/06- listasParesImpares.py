#Elementos pares de una lista se elevan a la 3 y los impares a la 2 
def Listas(lista):
    if isinstance(lista,list):#Validacion
        if lista==[]:#Validacion
            return f'La nueva lista es: {[0]}'
        else:
            i=0
            nuevaLista=[]
            while i<len(lista):
                if type(lista[i])!=int:
                    return '\nLa lista solo puede tener numeros, no se puede hacer la operacion'
                if lista[i]%2==0:
                    nuevaLista=nuevaLista+[lista[i]**3]
                else:
                    nuevaLista=nuevaLista+[lista[i]**2]
                i+=1
            return f'La nueva lista es: {nuevaLista}'
    else:#Validacion
        return '\nEl parametro debe ser una lista, no se puede hacer la operacion'
lista=[6,1,2,3,7,'']
print(Listas(lista))