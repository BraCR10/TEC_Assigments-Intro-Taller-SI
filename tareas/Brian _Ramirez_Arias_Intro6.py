def largoNum(num):#Funcion del largo
    if isinstance(num,int):
        if num==0:#Validacion
            return 1
        else:
            num=abs(num)
            cont=0
            while num!=0:
                num=num//10#Elimina el ultimo numero
                cont+=1#Contador
            return cont
def max(lista):#Funcion para determinar el mayor
    mayor=0
    for i in lista:
        if isinstance(i,int):#Validacion
            i=abs(i)
            if i >mayor:
                mayor=i
    return mayor
def Filtrador(lista):
    if isinstance(lista,list):#Validacion
        mayor=max(lista)
        cont=0
        temp=1#Se utiliza para elevar el localizador
        while largoNum(mayor)>cont:#Termina hasta que se tome en cuenta todos los digitos del numero mas grande
            #Listas en blanco
            L0=[]
            L1=[]
            L2=[]
            L3=[]
            L4=[]
            L5=[]
            L6=[]
            L7=[]
            L8=[]
            L9=[]
            for i in lista:  
                if isinstance(i,int):#Validacion
                    i=abs(i)
                    localizador=10**temp#Esta variable se utiliza para obtener el numero que se necesita en la pocision especifica, ya sea en unidades,decenas,etc
                    eliminador=10**cont#Esta variable elimina los numero antes de el numero que determina la lista en la que debe ir el numero 
                    #Ejemplo: numero=1806
                    #numero=numero%localizador=806 *En este caso se esta determinando el numero de las centenas
                    #numero=numero//eliminador=8 *En este caso se esta determinando el numero de las centenas
                    if i%localizador//eliminador==0:
                        L0+=[i]
                    elif i%localizador//eliminador==1:
                        L1+=[i]
                    elif i%localizador//eliminador==2:
                        L2+=[i]
                    elif i%localizador//eliminador==3:
                        L3+=[i]
                    elif i%localizador//eliminador==4:
                        L4+=[i]
                    elif i%localizador//eliminador==5:
                        L5+=[i]
                    elif i%localizador//eliminador==6:
                        L6+=[i]
                    elif i%localizador//eliminador==7:
                        L7+=[i]
                    elif i%localizador//eliminador==8:
                        L8+=[i]
                    elif i%localizador//eliminador==9:
                        L9+=[i]
                else:#Validacion
                    print('El elemento ',i,' no es un entero, por lo que se omite!' )
            lista=L0+L1+L2+L3+L4+L5+L6+L7+L8+L9   
            cont+=1
            temp+=1
        print(lista)
    else:
        print('Debe ingresar una lista ')
#Prueba
Filtrador([6000,12,1500,3,40,10,11,1,2,16,200,5])          
   
#Validar conjuntos
def conjunto(lista):
    largo=0
    pos=0 
    while largo<len(lista):
        while pos<len(lista):#Compara un numero con todos los otros
            if largo!=pos:#Se salta el mismo elemento
                if lista[pos]==lista[largo]:
                    return(False)   
                else:
                    pos+=1#
            else:#Se salta el mismo element
                pos+=1
        pos=0
        largo+=1
    return( True)
def unionConjunto(lista1,lista2):
    if isinstance(lista1,list) and isinstance(lista2,list):#Validacion
        if conjunto(lista1)==True and conjunto(lista2)==True:#Validacion
            union=lista1#Listas para unir conjuntos
            for i in lista2:
                if i in lista1:
                    continue
                else:
                    union+=[i]
            print( union)
        else:
            print('Debe ingresar conjuntos!')
    else:
        print('Deben ingresar listas!')
#Pruebas
#unionConjunto([1,5,75,68,9,6,'**'],[1,2,3,6,7,'*2*','**'])
            
        
        
    
    
