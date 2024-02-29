#Creador de listas
def covertidor(numero):
    if type(numero)==int:#Validacion
            lista=[]
            num=numero#Copia
            temp=0
            if num>=0:#Si num es positivo
                while num>=0:
                    lista+=[[temp,num]]
                    num-=1
                    temp+=1
            else:#Si num es negativo
                 while num<=0:
                    lista+=[[temp,num]]
                    num+=1
                    temp-=1
            return f'\nEl numero {numero} en la lista genera: {lista}'
    else:#Validacion
        return '\nEl parametro debe ser un entero'
#Pruebas
print(covertidor(5))
print(covertidor(-5))
print(covertidor(0))
print(covertidor(2.5))
