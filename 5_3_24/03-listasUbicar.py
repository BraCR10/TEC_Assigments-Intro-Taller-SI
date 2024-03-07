
#Construye una lista nueva sumandole dig a cada impar del num
def transformador(num,dig):
    if isinstance(num,int) and dig<=9 and dig>=-9:#Validacion
        if num==0:#Validacion
            print([0])#Validacion
        else:
            lista=[]
            i=abs(num)#Para negativos
            while i>0:
                temp=i%10#Recolecta el ultimo numero
                lista=[temp]+lista
                i//=10#Quita el ultimo numero
            i=len(lista)-1#Se le resta 1 para que no haya error al iterar en la lista
            while i>=0:
                if lista[i]%2!=0:#Solo enteros
                    lista[i]+=dig
                i-=1
            print('\nLa nueva lista es: ', lista)
    else:#Validacion
        print( '\nEl parametro debe ser un entero y el digito no puede ser mayor a 9 o menor que -9')
transformador(-133,9)

#Ubica un elemento en la lista recibiendo un numero
def ubicador(num,dig):
    if isinstance(num,int) and dig<=9 and dig>=0:#Validacion
        if num==0:#Validacion
            print([0])#Validacion
        else:
            lista=[]#Almacena las ubicaciones
            check=0#Para verificar que esta en el numero
            i=abs(num)#Para negativos
            while i>0:
                temp=i%10#Recolecta el ultimo numero
                lista=[temp]+lista
                i//=10#Quita el ultimo numero
            i=len(lista)-1#Se le resta 1 para que no haya error al iterar en la lista
            nuevaLista=[]
            while i>=0:
                if lista[i]==dig:#Solo enteros
                    nuevaLista=[i]+nuevaLista
                    check=1
                i-=1
            
            if check==1:
                print('\nLas posiciones de ese digito en ese numero de derecha a izquierda es: ', nuevaLista)
            else:
                print('\nEl digito no esta en el numero')
    else:#Validacion
        print( '\nEl parametro debe ser un entero y el digito no puede ser mayor a 9 o menor que 0')
ubicador(4774,7)