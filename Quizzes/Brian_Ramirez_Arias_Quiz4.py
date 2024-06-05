def funcion(num1,lista):
    num1=abs(num1)
    if type(num1)==int and type(lista)==list:
        listaNueva=[]
        for i in range(len(lista)):
            if type(lista[i])==int:
                if lista[i]%2==0:
                    listaNueva+=[lista[i]+num1]
                else:
                    listaNueva+=[lista[i]*num1]
            else:
                print('Los valores de la lista deben ser enteros')
        print(listaNueva)
    else:
        print('Los parametros son de tipos incorrectos')
#Prueba
#funcion(2,[1,2,3,4])
def funcion2(num1,lista):
    num1=abs(num1)
    if type(num1)==int and type(lista)==list:
        for i in range(len(lista)):
            if type(lista[i])==int:
                if lista[i]%2==0:
                    lista[i]=lista[i]+num1
                else:
                    lista[i]=lista[i]*num1
            else:
                print('Los valores de la lista deben ser enteros')
        print(lista)
    else:
        print('Los parametros son de tipos incorrectos')
#Prueba
#funcion2(2,[1,2,3,4])
def funcion3(num1,lista):
    num1=abs(num1)
    if type(num1)==int and type(lista)==list:
        i=0
        while i<len(lista):
            if type(lista[i])==int:
                if lista[i]%2==0:
                    lista[i]=lista[i]+num1
                else:
                    lista[i]=lista[i]*num1
            else:
                print('Los valores de la lista deben ser enteros')
            i+=1
        print(lista)
    else:
        print('Los parametros son de tipos incorrectos')
#Prueba
#funcion3(8,[1,2,3,4])
def funcion4(num1,lista):
    num1=abs(num1)
    if type(num1)==int and type(lista)==list:
        listaNueva=[]
        for i in lista:
            if type(i)==int:
                if i%2==0:
                    listaNueva+=[i+num1]
                else:
                    listaNueva+=[i*num1]
            else:
                print('Los valores de la lista deben ser enteros')
        print(listaNueva)
    else:
        print('Los parametros son de tipos incorrectos')
#Prueba
#funcion4(2,[1,2,3,4])
        
def funcion5(num1,lista):
    if type(num1)==int and type(lista)==list:
        cont=0
        while lista!=[]:
            if lista[0]==num1:
                cont+=1
                lista=lista[1:]
            else:
                lista=lista[1:]
        print(cont)
    else:
        print('Los parametros son de tipos incorrectos')
#Prueba
#funcion5(3,[2,1,2,'uu',3,2,3,4])

def funcion6(num1,lista):
    if type(num1)==int and type(lista)==list:
        cont=0
        i=0
        while i<len(lista):
            if lista[i]==num1:
                cont+=1
            i+=1
        print(cont)
    else:
        print('Los parametros son de tipos incorrectos')
#Prueba
#funcion6(-1,[2,2,-1,2,'n',2,2,3,4])
        
def funcion7(num1,lista):
    if type(num1)==int and type(lista)==list:
        cont=0
        i=0
        for i in range (len(lista)):
            if lista[i]==num1:
                cont+=1
        print(cont)
    else:
        print('Los parametros son de tipos incorrectos')
#Prueba
#funcion7(-1,[-1,2,2,-1,-1,2,'n',2,2,3,4])
        
def funcion8(num1,lista):
    if type(num1)==int and type(lista)==list:
        cont=0
        i=0
        for i in lista:
            if i==num1:
                cont+=1
        print(cont)
    else:
        print('Los parametros son de tipos incorrectos')
#Prueba
#funcion8(-1,[-1,2,2,-1,-1,2,'n',2,2,3,4,-1])