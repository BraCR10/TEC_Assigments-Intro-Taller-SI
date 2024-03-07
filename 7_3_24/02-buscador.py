#Ubica un elemento en la lista recibiendo un numero
def ubicador(dig,lista):
    if isinstance(lista,list) and dig<=9 and dig>=0:#Validacion
        if lista==[]:#Validacion
            print([])#Validacion
        else:
            check=0#Para verificar que esta en el numero
            i=len(lista)-1#Se le resta 1 para que no haya error al iterar en la lista
            nuevaLista=[]
            '''if dig in lista:
                print('\n', True)
            else:
                print('',False)'''
            while i>=0:
                if lista[i]==dig:#Solo enteros
                    print('\n', True)
                    check=1
                    break
                i-=1
            if check==0:
                print('\n',False)
    else:#Validacion
        print( '\nEl parametro debe ser una lista y el digito no puede ser mayor a 9 o menor que 0')
ubicador(7,[7,2,3,8])