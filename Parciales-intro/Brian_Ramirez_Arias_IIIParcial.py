#III Parcial
# Brian Ramirez Arias
#Carnet 2024109557

#Num es el numero para trabajar
#NumIncluir es el numero a incluir en el patron
#Cant es la cantidad de veces que se incluira numIncluir
#BumBuscar es el num a buscar en Num
def UNO(num,numIncluir,cant,numBuscar):#Funcion de cola con varias funciones axiliares
    if type(num)==int and type(numIncluir)==int and type(cant)==int and type(numBuscar)==int:#Validaciones
        if cant==0:# Si  cantidad es 0
            #Salida
            return noHay_aux(num,[],False)#Funcion exclusiva de que no existe el numero buscado o cant=0
        elif verificadorNumBuscado_aux(abs(num),abs(num),abs(numBuscar))==False:#Si no esta el dig buscado
            #Salida
            return noHay_aux(num,[],False)#Funcion exclusiva de que no existe el numero buscado o cant=0
        else:
            #Salida
            return UNONormal_aux(abs(num),False,numIncluir,abs(cant),abs(numBuscar),[])#Funcion para cualquier otro caso
    else:
        print('Parametro incorrecto')

#Num es el numero para trabajar, se corta conforme pasa la funcion
#Bandera se utiliza para saber si el num no es 0 desde un principio
#NumIncluir es el numero a incluir en el patron
#Cant es la cantidad de veces que se incluira numIncluir
#numBuscar es el num a buscar en Num
#lista se retorna, es donde se almacena digito por digito
def UNONormal_aux(num,bandera,numIncluir,cant,numBuscar,lista):#Verifica numero por numero y agrega a la lista, si hay un numero que coincide con el numBuscado llama a la funcion patron_aux que genera el patron
    if num==0 and bandera==True:#Finalizacion
        return []
    elif num%10==numBuscar:#Si el dig coincide con el numBuscado
      return UNONormal_aux(num//10,True,numIncluir,cant,numBuscar,lista)+patron_aux(cant*2,cant*4,numIncluir,numBuscar,[],0,False,False)+lista#Se llama a el generador de patron,la lista retornada se agrega a la lista y se vuelve a llamar a la funcion sin el dig ya verificado
    elif num%10!=numBuscar:#Si el dig no coincide
      return UNONormal_aux(num//10,True,numIncluir,cant,numBuscar,lista)+[num%10]+lista

#num es el numero para trabajar, se corta conforme pasa la funcion
#verificador se utiliza para saber si el num no es 0 desde un principio
#numBuscar es el num a buscar en Num
def verificadorNumBuscado_aux(num,verificador,numBuscado):#Verifica si esta el numBuscado
    if num==0 and verificador!=0:#Condicion de finalizacion
        return False
    elif num%10==numBuscado:#Si  esta
        return True
    else:
        return verificadorNumBuscado_aux(num//10,verificador,numBuscado)

#CantOriginal contine la cantidad dada el usuario multplicada por 2 ya que se duplica entre el num a agregar y el opuesto
#cant contine la cantidad dada el usuario multplicada por 4, debido a que se ocupa la misma cantidad antes y despues del dig que coincide
#NumIncluir es el numero a incluir en el patron
#numBuscar es el num a buscar en Num
#lista se retorna con el patron completo
#bandera se usa para verificar si se debe insertar el num a incluir o el opuesto
#centro se utliza para saber en que momento se incerto el centro
#inicio se utiliza para agregar el [0] al inicio solo una vez
def patron_aux(cantOriginal,cant,numIncluir,numBuscar,lista,bandera,centro,inicio):#Esta funcion genera el patron solo si es llamada por UNONormal_aux
    if cant==0:#Condicion de finalizacion
        return [-1]
    elif cantOriginal*2==cant and inicio==False:#Verifica si es el inicio
        return lista+[0]+patron_aux(cantOriginal,cant,numIncluir,numBuscar,lista,bandera,centro,True)
    elif cant>cantOriginal  and bandera==0:#Si bandera = 0 y antes de centro
        return lista+[numIncluir]+patron_aux(cantOriginal,cant-1,numIncluir,numBuscar,lista,1,centro,inicio)
    elif cant>cantOriginal  and bandera==1:#Si bandera =1 y antes de centro
        if numBuscar==0:
            return lista+[1]+patron_aux(cantOriginal,cant-1,numIncluir,numBuscar,lista,0,centro,inicio)
        else:
            return lista+[-(numBuscar)]+patron_aux(cantOriginal,cant-1,numIncluir,numBuscar,lista,0,centro,inicio)
    elif cant==cantOriginal and centro==False:#Si esta el centro
        return lista+[numBuscar]+patron_aux(cantOriginal,cant,numIncluir,numBuscar,lista,0,True,inicio)
    elif  cant>0  and bandera==0:#Si bandera = 0 y despues del centro
        return lista+[numIncluir]+patron_aux(cantOriginal,cant-1,numIncluir,numBuscar,lista,1,centro,inicio)
    elif  cant>0 and bandera==1:#Si bandera =1 y despues del centro
        if numBuscar==0:
            return lista+[1]+patron_aux(cantOriginal,cant-1,numIncluir,numBuscar,lista,0,centro,inicio)
        else:
            return lista+[-(numBuscar)]+patron_aux(cantOriginal,cant-1,numIncluir,numBuscar,lista,0,centro,inicio)
#num es el numero para trabajar, se corta conforme pasa la funcion
#lista se retorna con el patron completo
#bandera verifica que si num es 0, de igual forma se agregue el patron
def noHay_aux(num,lista,bandera):#Se utiliza en caso de que cant sea 0 o que no haya un dig que coincida con numBuscado
    if num==0 and bandera==True:#Si ya se ejecuto mas de una vez y num=0
        return []
    else:#Si num!=0
        return noHay_aux(num//10,lista,True)+ [0]+[num%10]+[-1]+lista
#Pruebas
#print(UNO(8779,-2,-1,7))
#print(UNO(0,-2,-1,0))
#print(UNO(789,-2,-1,8))
#print(UNO_aux(789,1,1,8,[]))
#print(patron_aux(5*2,5*4,8,3,[],0,False,False))
#print(UNO(73439,8,5,3))
#print(UNO(0,0,0,0))
#print(UNO(175653, 22, 0, 23))
#print(UNO(5731210, 4, -2, -1))
#print(UNO(705430, -1, 2, 0))
#print(UNO(0, 1, 2, 0))
#print(UNO(1020, -5, 2, 0))
#print(UNO(2523, -2, 0, 2))
#print(UNO(333,4,2,4))
#print(UNO(1020,-5,2,0))
#print(UNO(123,1,0,1))
#print(UNO(0,1,9,0))
#print(UNO(0,-1,9,0))
#print(UNO(90548950,-8,2,0))

##########################################################################################################################################
# largoLista Almacena el largo de la lista
#nuevaLista almacena las sublistas con los patrones
#lista la lista que se da el usuario
def DOS(lista):
    if isinstance(lista,list):#Validacion
        largoLista=len(lista)
        if largoLista%2!=0 and largoLista>=3:#Validacion
            nuevaLista=[]#Almacena las sublistas con los patrones
            if largoLista==3:#En caso de que la lista sea de 3
                for i in range(3):
                    if i==0:
                            nuevaLista+=[[1,0,1,(lista[i]+lista[2]-lista[1])**2,-1,0,-1]]
                    elif i==1:
                        nuevaLista+=[[-2,0,-2,(lista[i]+lista[0]-lista[2])**3,2,0,2]]
                    elif i==2:
                        nuevaLista+=[[1,0,1,(lista[i]+lista[1]-lista[0])**2,-1,0,-1]]
            else:#En caso de que el largo de la lista sea mayor a 5
                for i in range(largoLista):
                    if i%2==0:#si es pocision par
                        if  i+2==largoLista:#En caso de que se necesite sumar el elemento [0] de la lista y evitar el error index out range
                            nuevaLista+=[[1,0,1,(lista[i]+lista[0]-lista[2])**2,-1,0,-1]]
                        elif  i+1==largoLista:#En caso de que se necesite sumar el elemento [1] de la lista y evitar el error index out range
                            nuevaLista+=[[1,0,1,(lista[i]+lista[1]-lista[3])**2,-1,0,-1]]
                        else:#En cualquier otro caso sin problema de index
                            if i+4==largoLista:#Si el elemento que se resta esta en la posicion 0
                                nuevaLista+=[[1,0,1,(lista[i]+lista[i+2]-lista[0])**2,-1,0,-1]]
                            elif i+3==largoLista:#Si el elemento que se resta esta en la posicion 1
                                nuevaLista+=[[1,0,1,(lista[i]+lista[i+2]-lista[1])**2,-1,0,-1]]
                            else:#En cualquier otro caso
                                nuevaLista+=[[1,0,1,(lista[i]+lista[i+2]-lista[i+4])**2,-1,0,-1]]
                    else:#si es pocision impar
                        if  i+2==largoLista:#En caso de que se necesite sumar el elemento [0] de la lista y evitar el error index out range
                            nuevaLista+=[[-2,0,-2,(lista[i]+lista[0]-lista[2])**3,2,0,2]]
                        elif i+1==largoLista:#En caso de que se necesite sumar el elemento [1] de la lista y evitar el error index out range
                            nuevaLista+=[[-2,0,-2,(lista[i]+lista[1]-lista[3])**3,2,0,2]]
                        else:#En cualquier otro caso sin problema de index
                            if i+4==largoLista:#Si el elemento que se resta esta en la posicion 0
                                nuevaLista+=[[-2,0,-2,(lista[i]+lista[i+2]-lista[0])**3,2,0,2]]
                            elif i+3==largoLista:#Si el elemento que se resta esta en la posicion 1
                                nuevaLista+=[[-2,0,-2,(lista[i]+lista[i+2]-lista[1])**3,2,0,2]]
                            else:#En cualquier otro caso
                                nuevaLista+=[[-2,0,-2,(lista[i]+lista[i+2]-lista[i+4])**3,2,0,2]]

            print(nuevaLista)#Salida
        else:
            print('La lista debe ser de tamaño impar y mayor a 3')
    else:
        print('Parametro incorrecto')
#Pruebas
#DOS([6,1,2,3,4])
#DOS([1,2,3,4,5,6,7])
#DOS([6,1,2,3,4,4,7,8,9])
#DOS([6,1,223,3,4])
#DOS([3,5,6])
#DOS([8,5,1])
#DOS([1,2,3,7,8,11,223,1000,10,3,1])
#DOS([7,2,5,4,3,6,7])
#DOS([3,2,1])
#DOS([6,1,2,3,4])
##################################################################################################################################
#i Contador del while
#lista la lista que se da el usuario
#pocision contiene un elemento de lista en cada iteracion del while
#j Contador del while anidado
#temp contiene un elemento de lista en cada iteracion del while, si usa para verificar si es sublista o int
def TRES(lista,elemento):
    if type(lista)==list and type(elemento)==int:#Validacion
        i=0#Contador del while
        lista=[lista]#Se trabaja sobre la misma lista
        while i<len(lista):
            pocision=lista[i]
            j=0
            while j<len(pocision):#Descompone niveles
                temp = pocision[j]#Vale cada num en la lista
                if isinstance(temp, list):
                    lista+=[temp]  # Se agrega al final de la lista para volver a pasar
                elif temp == elemento:#Si es entero
                    pocision[j] = [1,0,elemento,elemento,0,1] # agrega el patron
                j+=1
            i+=1
        lista=lista[0] #Se elimina los niveles inferiores ya actualizados que se añadieron a la lista para buscar valores

        print(lista)#Salida
#Pruebas
#TRES([[[[[[[[[[[[[2]]]],3]]]]]]]]],2)
#TRES([2,[2,3,[-2],5,9],7],-2)
#TRES( [1,[2,9,],[[4,2,6],[8]],2,10],2)
#TRES([1,2,3],3)
#TRES([],2)
#TRES([1,2,3],-3)
#############################################################################################################################################
#Num es el numero al que se le va a evaluar el largo
#Cont incremeta conforme se corta el num
def largoNum(num):#Funcion del largo
    if isinstance(num,int):
        if num==0:#Validacion
            return 1
        else:
            n=abs(num)#Negativos
            cont=0
            for i in range(n+1):
                if n ==0:#Corta el bucle cuando n vale 0
                    return cont
                cont+=1
                n//=10
    else:
        return 0#Retorna 0 para evitar errores, el usuario no interactua con esta funcion directamente

#num es el num donde se buscar el centro
def buscarCentro(num):#Funacion que encuentra el centro de un impar
    for i in range(largoNum(num)//2):
        num//=10
    return num%10

#num1 es el primer numero para trabajar
#num2 es el segunda numero para trabajar
#num3 es el tercer numero para trabajar
#centroNum1 contiene el centro del numero
#centroNum2 contiene el centro del numero
#centroNum3 contiene el centro del numero
#lista donde se insertan los numeros
#bandera Tiene 4 modos mas adelante se detalla
#contNum1Num3 Se utiliza para elevar el 10 a la hora de buscar los extremos izq tanto de num 1 como num3
#contNum2 Se utiliza para elevar el 10 a la hora de buscar extremos der y izq en num 2
#ceros Se utiliza para buscar extremos izq en num1 y num3
#confirmador Se utiliza para saber si ya interactuo centro de num1 con extremos de num3 y centro de num3 con extremos de num1, se incrementa ceros y contNum1Num3
# temp2 Almacena lo que se agrega a cada sublista en posicion [2] en el bucle
# temp1 Almacena lo que se agrega a cada sublista en posicion [1] en el bucle
# centro #Almacena el centro que se agrega a cada lista al principio, ya sea de num1 o num3
def CUATRO(num1,num2,num3):
    if type(num1)==int and type(num2)==int and type(num3)==int:#Validacion
        if  largoNum(num1)%2!=0 and largoNum(num2)>=3 and largoNum(num2)%2!=0 and largoNum(num3)>=3 and (largoNum(num1)==largoNum(num2)==largoNum(num3)):#Validacion
            num1=abs(num1)
            num2=abs(num2)
            num3=abs(num3)
            centroNum1=buscarCentro(num1)
            centroNum2=buscarCentro(num2)
            centroNum3=buscarCentro(num3)
            lista=[]#Donde se insertan los numeros
            bandera=0#Tiene 4 modos
            #0 cuando interactua con el centro de num 1 y los extremos de num3
            #1 cuando interactua con el centro de num 3 y los extremos de num1
            #2 cuando interactua con el centro de num 1, extremos izq de num2 y centro num2
            #3 cuando interactua con el centro de num 5, extremos der de num2 y centro num2
            contNum1Num3=1#Se utiliza para elevar el 10 a la hora de buscar los extremos izq tanto de num 1 como num3
            contNum2=1#Se utiliza para elevar el 10 a la hora de buscar extremos der y izq en num 2
            ceros=1#Se utiliza para buscar extremos izq en num1 y num3
            confirmador=False#Se utiliza para saber si ya interactuo centro de num1 con extremos de num3 y centro de num3 con extremos de num1, se incrementa ceros y contNum1Num3
            for i in range(largoNum(num1)*2-2):#La lista final esta formada por sublistas, la cant de sublistas estan dadas por (largo de num *2 )-2
                temp2=0#Almacena lo que se agrega a cada sublista en posicion [2]
                temp1=0#Almacena lo que se agrega a cada sublista en posicion [1]
                centro=0#Almacena el centro que se agrega a cada lista al principio, ya sea de num1 o num3
                if bandera==0:#interactua con el centro de num 1 y los extremos de num3
                    centro=centroNum1
                    temp1=(num3//(10**(largoNum(num1)-contNum1Num3)))%10
                    temp2=num3%10**(ceros)
                    if largoNum(temp2)!=ceros:#Verificacion para evitar perder un cero
                        temp2=0
                    else:
                        temp2//=(10**(largoNum(temp2)-1))
                    bandera=1
                elif bandera==1:#interactua con el centro de num 3 y los extremos de num1
                    centro=centroNum3
                    temp1=(num1//(10**(largoNum(num1)-contNum1Num3)))%10
                    temp2=num1%10**(ceros)
                    if largoNum(temp2)!=ceros:#Verificacion para evitar perder un cero
                        temp2=0
                    else:
                        temp2//=(10**(largoNum(temp2)-1))
                    bandera=2
                    confirmador=True#Confirma que ya hubo interaccion de ambos tanto extremos de num1 con centro num3 y alrevez
                elif bandera==2:#interactua con el centro de num 1, extremos izq de num2 y centro num2
                    centro=centroNum1
                    temp1=(num2//(10**(largoNum(num1)-contNum2)))%10
                    temp2=centroNum2
                    bandera=3
                elif bandera==3:#interactua con el centro de num 5, extremos der de num2 y centro num2
                    centro=centroNum3
                    temp1=num2%10**(contNum2)
                    if largoNum(temp1)!=contNum2:#Verificacion para evitar perder un cero
                        temp1=0
                    else:
                        temp1//=(10**(largoNum(temp1)-1))
                    temp2=centroNum2
                    bandera=0
                    contNum2+=1#Confirma que ya interactuo extremo num2 izq con centro num1 y extremo der num2 con centro num3
                if confirmador==True:#Solo sucede cuando  ya interactuo centro de num1 con extremos de num3 y centro de num3 con extremos de num1, se incrementa ceros y contNum1Num3
                    ceros+=1
                    contNum1Num3+=1
                    confirmador=False#Otra vez falso para que no incremente hasta que se confirme nuevamente
                lista+=[[centro,temp1,temp2]]#Agrega a la lista el centro y los temporales correspondientes

            print(lista,num1,num2,num3)#Salida
        else:
          print('Parametros incorrectos')
    else:
        print('Parametros incorrectos')

#CUATRO(122,-421,155)
#CUATRO(312359061,890121635,435762340)
#CUATRO(3123590,8901216,4357623)
#CUATRO(31235,89012,43576)
#CUATRO(312,890,465)
#CUATRO(354,100,500)
#CUATRO(340123795,100237206,311053450)
#CUATRO(257,132,583)
#CUATRO(000,000,000)
#CUATRO(10130,20507,43805)
#CUATRO(-7030215,-5019702,-3031550)
#print(176%1000//(10**(3-1)))
#CUATRO(123,456,789)
#CUATRO(12307,45076,78679)
#CUATRO(122310003,450007826,782000782)