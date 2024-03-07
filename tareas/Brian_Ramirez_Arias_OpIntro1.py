#TareaOp#1
#Introducción a la Programación
#Solicitud 05 marzo
#Entrega 07 marzo
#Hora máxima de entrega 7:50am

def Pasalista(num): #234  [2,3,4] 0 [0]  
    num=abs(num)#234
    if isinstance (num,int):
        if num==0:
            return [0]
        else:
            listaNueva=[]#definiendo un lista vacia,almacenar los elementos
            while num!=0:#234 23 2 0
                #             #4 [4]+[]=[4] 3 [3]+[4]=[3,4] 2 [2]+[3,4]=[2,3,4]
                listaNueva= [num%10]+listaNueva
                num=num//10#234 23 2 0
            return(listaNueva)#[2,3,4]
    else:
         print(" No es entero")

#Escribir una funcion que recibe un numero entero y positivo
#Un digito entero y positivo
#Sumar el digito a los elementos impares del numero
#Pasando el numero a lista

def sumadigito(num,dig):
    dig=abs(dig)
    if type(num)==int and type(dig)==int and dig>=0 and dig<=9:
            num=abs(num)
            check=0
            lista=Pasalista(num)
            i=len(lista)-1#Se le resta 1 para que no haya error al iterar en la lista
            i//=10#Quita el ultimo numero
            i=len(lista)-1#Se le resta 1 para que no haya error al iterar en la lista
            while i>=0:
                if lista[i]%2!=0:#Solo enteros
                    lista[i]+=dig
                i-=1
            print('\nLa lista original es:', Pasalista(num))
            print('\nLa nueva lista es: ', lista)
            
    else:
         print("Parametro incorrecto")
#Pruebas
sumadigito(-123456789,-3)
        
    
