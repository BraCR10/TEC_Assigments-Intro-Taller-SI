#Cuenta solo pares y destruye  
def cuentaPares(lista):
    if type(lista)==list:
        if lista==[]:
            print(0)
        else:
            cont=0
            check=0
            for i in lista:
                if type(i)!=int:
                    print('La lista solo debe tener numeros enteros')
                    check=1
                elif i%2==0:
                    cont+=1
                    lista=lista[1:]
                else:
                    lista=lista[1:]
            if check==0:
                print(cont)
    else:
        print('El parametro debe ser una lista')
#Prueba
#cuentaPares([0,2])
