#Creador de listas apartir de enteros destruyendo 
def covertidor(numero):
    if type(numero)==int:#Validacion
        if numero==0:
            return [0]
        else: 
            lista=[]
            while numero>0:
                temp=numero%10#Recolecta el ultimo numero
                lista=[temp]+lista
                numero//=10#Quita el ultimo numero
            return f'El numero queda como {numero} y la lista es {lista}'
    else:
        return '\nEl parametro debe ser una lista, no se puede hacer el promedio '
entero=1623
print(covertidor(entero))

#Creador de listas apartir de enteros sin detruir
def covertidor2(numero):
    if type(numero)==int:#Validacion
        if numero==0:
            return [0]
        else: 
            lista=[]
            num=numero
            while num>0:
                temp=num%10#Recolecta el ultimo numero
                lista=[temp]+lista
                num//=10#Quita el ultimo numero
            return f'El numero queda como {numero} y la lista es {lista}'
    else:
        return '\nEl parametro debe ser una lista, no se puede hacer el promedio '
entero=1623
print(covertidor2(entero))

