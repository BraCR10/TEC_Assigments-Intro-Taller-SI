#Suma un numero a elementos de la lista  o eleva en lista nueva
def operacionesListaNueva(lista,num):
    if type(lista)==list and type(num)==int:
        if lista==[]:
            print([])
        else:
            nueva=[]
            check=0
            num=abs(num)
            for i in range(len(lista)):
                if type(lista[i])!=int:#Valida que todos los numero sean enteros
                    print('La lista solo debe tener numeros enteros')
                    check=1
                elif lista[i]%2==0:
                    nueva+=[lista[i]+num]
                else:
                    nueva+=[lista[i]**num]
            if check==0:
                print(nueva)
    else:
        print('El parametro debe ser una lista y un entero')
#Prueba
#operacionesListaNueva([0,8,5],-3)
        
#Suma un numero a elementos de la lista o eleva  en la misma lista
def operacionesLista(lista,num):
    if type(lista)==list and type(num)==int:
        if lista==[]:
            print([])
        else:
            check=0
            num=abs(num)
            for i in range(0,len(lista)):
                if lista[i]%2==0:
                    lista[i]=lista[i]+num
                else:
                    lista[i]=lista[i]**num
            if check==0:
                print(lista)
    else:
        print('El parametro debe ser una lista y un entero')
#Prueba
#operacionesLista([6,1,2,5],2)
        
#Suma un numero a elementos de la lista  o eleva y destruye
def operacionesListaNuevaDestruye(lista,num):
    if type(lista)==list and type(num)==int:
        if lista==[]:
            print([])
        else:
            nueva=[]
            check=0
            num=abs(num)
            copia=lista
            for i in range(0,len(lista)):
                if type(copia[i])!=int:#Valida que todos los numero sean enteros
                    print('La lista solo debe tener numeros enteros')
                    check=1
                elif copia[i]%2==0:
                    nueva+=[copia[i]+num]
                    lista=lista[1:]
                else:
                    nueva+=[copia[i]**num]
                    lista=lista[1:]
            if check==0:
                print(nueva)
    else:
        print('El parametro debe ser una lista y un entero')
#Prueba
#operacionesListaNuevaDestruye([6,1,2,7,5],2)

#Pasa lista while 
def Pasalista(num): #234  [2,3,4] 0 [0]  
    num=abs(num)#234
    if isinstance (num,int):
        if num==0:
            return [0]
        else:
            listaNueva=[]#definiendo un lista vacia,almacenar los elementos
            while num!=0:#234 2 3 2 0
                listaNueva= [num%10]+listaNueva
                num=num//10#234 23 2 0
            return(listaNueva)#[2,3,4]
    else:
         print(" No es entero")
         
#Largo num con for
def largoNum(num):#Funcion del largo
    if isinstance(num,int):
        if num==0:#Validacion
            return 1
        else:
            n=abs(num)#Negativos
            cont=0
            for i in range(n):
                if n ==0:#Corta el bucle cuando n vale 0
                    return cont
                cont+=1
                n//=10
    else:
        return 'Deben ser enteros'
#Pasa lista for 
def PasalistaFor(num): #234  [2,3,4] 0 [0]  
    num=abs(num)#234
    if isinstance (num,int):
        if num==0:
            return [0]
        else:
            listaNueva=[]#definiendo un lista vacia,almacenar los elementos
            for i in range(0,largoNum(num)):#234 2 3 2 0
                listaNueva= [num%10]+listaNueva
                num=num//10#234 23 2 0
            return(listaNueva)#[2,3,4]
    else:
         print(" No es entero")

#Funcion 1
def whileDestruye(num,dig):
    if isinstance(num,int) and type(dig)==int:
           num=abs(num)
           dig=abs(dig)
           lista=Pasalista(num)
           cont=0
           while lista!=[]:
               if lista[0]==dig:
                   cont+=1
               lista=lista[1:]
           print(cont)
    else:
        print('Parametros incorrectos')
#Prueba
#whileDestruye(1424,4)     
                    
#Funcion 2
def whileNoDestruye(num,dig):
    if isinstance(num,int) and type(dig)==int:
           num=abs(num)
           dig=abs(dig)
           lista=Pasalista(num)
           cont=0
           i=0
           while i<len(lista):
               if lista[i]==dig:
                   cont+=1
               i+=1
           print(cont)
    else:
        print('Parametros incorrectos')
#Prueba
#whileNoDestruye(14244,4)  
                       
#Funcion 3
def forRange(num,dig):
    if isinstance(num,int) and type(dig)==int:
           num=abs(num)
           dig=abs(dig)
           lista=PasalistaFor(num)
           cont=0
           for i in range(len(lista)):
               if lista[i]==dig:
                   cont+=1
           print(cont)
    else:
        print('Parametros incorrectos')
#Prueba
#forRange(142744,4)  
                       
#Funcion 4
def forItem(num,dig):
    if isinstance(num,int) and type(dig)==int:
           num=abs(num)
           dig=abs(dig)
           lista=PasalistaFor(num)
           cont=0
           for i in lista:
               if i==dig:
                   cont+=1
           print(cont)
    else:
        print('Parametros incorrectos')
#Prueba
#forItem(14424,4)                 
