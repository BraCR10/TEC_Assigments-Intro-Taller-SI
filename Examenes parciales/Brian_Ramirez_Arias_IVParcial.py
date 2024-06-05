#IV Parcial
# Brian Ramirez Arias
#Carnet 2024109557
#Pila
#n es el numero a calcula el largo
def largoNum(n):
    if type(n)==int:
        #Condicion de finalizacion
        if n==0:
            return 1
        else:
            #La llamada recursiva
            return  1+largoNumAux(abs(n)//10)
    else:
        print('Parametro incorrecto')
#n es el numero a calcula el largo
def largoNumAux(n):
    if n==0:
        return 0
    else:
        #La llamada recursiva
        return 1+largoNumAux(n//10)

#Num es el numero para trabajar
#NumIncluir es el numero a incluir en el patron
#Cant es la cantidad de veces que se incluira numIncluir
#BumBuscar es el num a buscar en Num
def UNO(num,numIncluir,cant,numBuscar):
    if type(num)==int and type(cant)==int and type(numIncluir)==int and type(numBuscar)==int:
        if abs(cant)==0:
            return cant0_aux(num,[],False),abs(num),numIncluir,abs(cant),abs(numBuscar)
        else:
            if abs(num)==0 and abs(numBuscar)==0:
                return [patron_aux(abs(cant)*2,abs(cant)*4,numIncluir,abs(numBuscar),[],0,False,False)],abs(num),numIncluir,abs(cant),abs(numBuscar)
            elif abs(num)%10==abs(numBuscar):
                return UNO_aux(abs(num)//10,numIncluir,abs(cant),abs(numBuscar))+[patron_aux(abs(cant)*2,abs(cant)*4,numIncluir,abs(numBuscar),[],0,False,False)],abs(num),numIncluir,abs(cant),abs(numBuscar)
            else:
                return UNO_aux(abs(num)//10,numIncluir,abs(cant),abs(numBuscar))+[[0,abs(num%10),-1]],abs(num),numIncluir,abs(cant),abs(numBuscar)
    else:
        print('Parametro incorrecto')

#NumCopia es una copia para no destruir
#NumIncluir es el numero a incluir en el patron
#Cant es la cantidad de veces que se incluira numIncluir
#BumBuscar es el num a buscar en Num
def UNO_aux(numCopia,numIncluir,cant,numBuscar):#Auxiliar UNO
    if largoNum(numCopia)==1 and numCopia==numBuscar:#Condicion de finalizacion
        return [patron_aux(cant*2,cant*4,numIncluir,numBuscar,[],0,False,False)]
    elif largoNum(numCopia)==1 and numCopia!=numBuscar:#Condicion de finalizacion
        return [[0,numCopia,-1]]
    elif numCopia%10==numBuscar:
        return  UNO_aux(numCopia//10,numIncluir,cant,numBuscar)+[patron_aux(cant*2,cant*4,numIncluir,numBuscar,[],0,False,False)]
    elif numCopia%10!=numBuscar:
        return  UNO_aux(numCopia//10,numIncluir,cant,numBuscar)+[[0,numCopia%10,-1]]
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
        return [numBuscar+1,-1]
    elif cantOriginal*2==cant and inicio==False:#Verifica si es el inicio
        return lista+[0,numBuscar-1]+patron_aux(cantOriginal,cant,numIncluir,numBuscar,lista,bandera,centro,True)
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
def cant0_aux(num,lista,bandera):#Se utiliza en caso de que cant sea 0
    if num==0 and bandera==True:#Si ya se ejecuto mas de una vez y num=0
        return []
    else:#Si num!=0
        return cant0_aux(num//10,lista,True)+ [[0]+[num%10]+[-1]]+lista
#Pruebas
#print(UNO(73439,8,1,3))
#print(UNO(0,8,1,0))
#print(UNO(123,0,5,0))
#print(UNO(123,0,0,2))
#print(UNO(5132222235617,-2,-1,7))
#print(UNO(51322272235617,-2,-1,7))
#print(UNO(0,-2,-1,0))
#print(UNO(789,-2,-1,8))
#print(UNO(73439,8,5,3))
#print(UNO(0,0,0,0))
#print(UNO(17562353, 22, 0, 3))
#print(UNO(17562353, 22, 1, 3))
#print(UNO(17562353, 22, 10, 3))
#print(UNO(5731210, 4, -2, -1))
#print(UNO(705430, -1, 2, 0))
#print(UNO(0, 1, 2, 0))
#print(UNO(1, 1, 2, 1))
#print(UNO(1020, -5, 2, 0))
#print(UNO(2523, -2, 0, 2))
#print(UNO(333,4,2,4))
#print(UNO(1020,-5,2,0))
#print(UNO(123,1,0,1))
#print(UNO(0,1,9,0))
#print(UNO(0,-1,9,0))
#print(UNO(90548950,-8,2,0))
#print(UNO(90548950,0,-2,8))
####################################################################################################################################
#Cola
#n es el numero para calcular factorial
def factorial(n):
    if isinstance(n,int):
        if n==0:
            return 1
        else:
            return factorial_aux(n,1)
    else:
        print('Parametro incorrecto')

#resultado alamacena el resultado final
#n es el numero para calcular factorial
def factorial_aux(n,resultado):
    if n==0:
        return resultado#Identificador
    else:
        return factorial_aux(n-1,resultado*n)
#COLA
#la sumatoria empeza en n y termina en 1
def DOS1(n):#Decremento
    if isinstance(n,int):
        if n<=0:
            return'El numero debe ser mayor o igual a 1'
        else:
            return (DOS1_aux(n,0,n))**(n+1)
    else:
        print('Parametro incorrecto')

#i decrementa en la  sumatoria termina en 1
#resultado alamacena el resultado final
#n es el n origina para la formula
def DOS1_aux(n,resultado,i):
    if i<1:
        return resultado#Identificador
    else:

        return DOS1_aux(n,resultado+((((factorial(i)*(n-2))**n)*((n-1)**(n+i)))/(((2*((n*4)**i)+n)*i)**(n*i))), i-1)
#Pruebas
#print(DOS1(1))
#print(DOS1(26))
#print(DOS1(2))
#print(DOS1(3))
#print(DOS1(4))
#print(DOS1(1))
#print(DOS1(-55))

#PILA
#n es hasta donde la sumatoria debe llegar
def DOS2(n):#Incremento
    if type(n)==int:
        #Condicion de finalizacion
        if n<=0:
            return 'El numero debe ser mayor o igual a 1'
        else:
            #La llamada recursiva
            return (((((n**2)*(n+1)*n)**(n-1))*n/((2*(n*3)**(n+1))+(n+n))**n)+DOS2_aux(1,n-1,n))**2
    else:
        print('Parametro incorrecto')

#i incrementa en la  sumatoria empieza en 1
#finalizacion le dice a la aux cuando parar siempre es n-1
#n es el n origina para la formula
def DOS2_aux(i,finalizacion,n):
    if i>finalizacion:
        return 0
    else:
        #La llamada recursiva
        return  ((((i**2)*(n+1)*n)**(n-1))*n/((2*(n*3)**(i+1))+(n+i))**n)+DOS2_aux(i+1,finalizacion,n)
#Pruebas
#print(DOS2(4))
#print(DOS2(2))
#print(DOS2(3))
#print(DOS2(1))
#print(DOS2(44))

##############################################################################################################################################
#Cola
#n es el numero al que se le va a evaluar el largo
def largoNumCola(n):#Determina el largo de un numero
    if isinstance(n,int):
        if n==0:
            return 1
        else:
            return largoNumCola_aux(abs(n),0)
    else:
        print('Parametro incorrecto')

#cont incremeta conforme se corta el num
def largoNumCola_aux(n,cont):
    if n==0:
        return cont#Identificador
    else:
        return largoNumCola_aux(n//10,cont+1)
#Cola
#num es el num donde se buscar el centro
def buscarCentro(num):#Funcion que encuentra el centro de un impar
    if isinstance(num,int):
        if largoNumCola(num)%2==0:#Si es de largo par
            return None
        else:
            return buscarCentro_aux(num,largoNumCola(num)//2)
    else:
        print('Parametro incorrecto')
    for i in range(largoNum(num)//2):
        num//=10
    return num%10

#num es el num donde se buscar el centro
#numerosAQuitar la cantidad de numeros a quitar por la der para encontrar el centro
def buscarCentro_aux(num,numerosAQuitar):
    if numerosAQuitar==0:
        return num%10#Identificador
    else:
        return buscarCentro_aux(num//10,numerosAQuitar-1)
#Cola
#num1 es el primer numero para trabajar
#num2 es el segunda numero para trabajar
#num3 es el tercer numero para trabajar
def TRES(num1,num2,num3):
    if type(num1)==int and type(num2)==int and type(num3)==int:#Validacion
        if  largoNum(abs(num1))%2!=0 and largoNum(abs(num2))>=3 and largoNum(abs(num2))%2!=0 and largoNum(abs(num3))>=3 and (largoNum(abs(num1))==largoNum(abs(num2))==largoNum(abs(num3))):#Validacion
            #Bandera tiene 4 modos
            #0 cuando interactua con el centro de num 1 y los extremos de num3
            #1 cuando interactua con el centro de num 3 y los extremos de num1
            #2 cuando interactua con el centro de num 1, extremos izq de num2 y centro num2
            #3 cuando interactua con el centro de num 5, extremos der de num2 y centro num2
            return TRES_aux(abs(num1),abs(num2),abs(num3),buscarCentro(abs(num1)),buscarCentro(abs(num2)),buscarCentro(abs(num3)),[],largoNum(abs(num1))*2-2,1,0,1,1,1),abs(num1),abs(num2),abs(num3)
        else:
          return('Parametros incorrectos')
    else:
        return('Parametros incorrectos')

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
# temp2 Almacena lo que se agrega a cada sublista en posicion [2] en el bucle
# temp1 Almacena lo que se agrega a cada sublista en posicion [1] en el bucle
def TRES_aux(num1,num2,num3,centroNum1,centroNum2,centroNum3,lista,finalizacion,inicio,bandera,contNum1Num3,ceros,contNum2):#Auxiliar de cola
    if inicio>finalizacion:
        return lista
    elif bandera==0:#interactua con el centro de num 1 y los extremos de num3
        temp1=(num3//(10**(largoNum(num1)-contNum1Num3)))%10
        temp2=num3%10**(ceros)
        if largoNum(temp2)!=ceros:#Verificacion para evitar perder un cero
            temp2=0
        else:
            temp2//=(10**(largoNum(temp2)-1))
        # Verifica el mayor y menor para el cuarto elemento en la lista
        mayor = temp1
        menor = temp1
        if temp2 > mayor:
            mayor = temp2
        if temp2 < menor:
            menor = temp2
        if centroNum1 > mayor:
            mayor = centroNum1
        if centroNum1 < menor:
            menor = centroNum1
        temp3=mayor-menor
        return TRES_aux(num1,num2,num3,centroNum1,centroNum2,centroNum3,lista+[[centroNum1**2,temp1**3,temp2**2,temp3**3]],finalizacion,inicio+1,1,contNum1Num3,ceros,contNum2)
    elif bandera==1:#interactua con el centro de num 3 y los extremos de num1
        temp1=(num1//(10**(largoNum(num1)-contNum1Num3)))%10
        temp2=num1%10**(ceros)
        if largoNum(temp2)!=ceros:#Verificacion para evitar perder un cero
            temp2=0
        else:
            temp2//=(10**(largoNum(temp2)-1))
        # Verifica el mayor y menor para el cuarto elemento en la lista
        mayor = temp1
        menor = temp1
        if temp2 > mayor:
            mayor = temp2
        if temp2 < menor:
            menor = temp2
        if centroNum3 > mayor:
            mayor = centroNum3
        if centroNum3 < menor:
            menor = centroNum3
        temp3=mayor-menor
        return TRES_aux(num1,num2,num3,centroNum1,centroNum2,centroNum3,lista+[[centroNum3**2,temp1**3,temp2**2,temp3**3]],finalizacion,inicio+1,2,contNum1Num3+1,ceros+1,contNum2)
    elif bandera==2:#interactua con el centro de num 1, extremos izq de num2 y centro num2
        temp1=(num2//(10**(largoNum(num1)-contNum2)))%10
        temp2=centroNum2
        # Verifica el mayor y menor para el cuarto elemento en la lista
        mayor = temp1
        menor = temp1
        if temp2 > mayor:
            mayor = temp2
        if temp2 < menor:
            menor = temp2
        if centroNum1 > mayor:
            mayor = centroNum1
        if centroNum1 < menor:
            menor = centroNum1
        temp3=mayor-menor
        return TRES_aux(num1,num2,num3,centroNum1,centroNum2,centroNum3,lista+[[centroNum1**2,temp1**3,temp2**2,temp3**3]],finalizacion,inicio+1,3,contNum1Num3,ceros,contNum2)

    elif bandera==3:#interactua con el centro de num 5, extremos der de num2 y centro num2
        temp1=num2%10**(contNum2)
        if largoNum(temp1)!=contNum2:#Verificacion para evitar perder un cero
            temp1=0
        else:
            temp1//=(10**(largoNum(temp1)-1))
        temp2=centroNum2
        # Verifica el mayor y menor para el cuarto elemento en la lista
        mayor = temp1
        menor = temp1
        if temp2 > mayor:
            mayor = temp2
        if temp2 < menor:
            menor = temp2
        if centroNum3 > mayor:
            mayor = centroNum3
        if centroNum3 < menor:
            menor = centroNum3
        temp3=mayor-menor
        return TRES_aux(num1,num2,num3,centroNum1,centroNum2,centroNum3,lista+[[centroNum3**2,temp1**3,temp2**2,temp3**3]],finalizacion,inicio+1,0,contNum1Num3,ceros,contNum2+1)

#print(TRES(312359061,890121635,435762340))
#print(TRES(122,-421,155))
#print(TRES(3123590,8901216,4357623))
#print(TRES(31235,89012,43576))
#print(TRES(312,890,465))
#print(TRES(354,100,500))
#print(TRES(340123795,100237206,311053450))
#print(TRES(257,132,583))
#print(TRES(000,000,000))
#print(TRES(10130,20507,43805)))
#print(TRES(110,210,443))
#print(TRES(-7030215,-5019702,-3031550))
#print(176%1000//(10**(3-1))))
#print(TRES(123,456,789))
#print(TRES(12307,45076,78679))
#print(TRES(122310003,450007826,782000782))
##############################################################################################################################################
#Cola
#lista la lista que se da el usuario
#elemento el elemento a buscar
def CUATRO(lista,elemento):
    if type(lista)==list and type(elemento)==int:#Validacion
        return CUATRO_aux(lista, elemento)
    else:
        return('Parametro incorrecto')

#lista la lista que se da el usuario
#elemento el elemento a buscar
def CUATRO_aux(lista, elemento):#Auxiliar de cola
    if isinstance(lista, int):
        if lista == elemento:#Se el elemento de las lista es el elemento buscado
            return [1,0,elemento+1,elemento,elemento,elemento-1,0,1]
        else:#Si no es el elemento
            return lista
    elif isinstance(lista, list):
        # Si hay mas listas dentro de la lista principal
        return sublistasCUATRO_aux(lista, elemento, 0)
    else:
        return lista
#lista la lista que  da el usuario
#elemento el elemento a buscar
#i itera dentro de las sublistas
def sublistasCUATRO_aux(lista, elemento, i):#Verifica si hay mas listas adentro y las inspecciona
    if i == len(lista):
        return lista
    lista[i] = CUATRO_aux(lista[i], elemento)
    return sublistasCUATRO_aux(lista, elemento, i + 1)

#Pruebas
#print(CUATRO([[[[2,[[[[[[[[[2]]]],3]]]]]],2]]],2))
#print(CUATRO([-2,[-2,3,[-2],5,9],-2],-2))
#print(CUATRO( [1,[2,9,],[[4,2,6],[8]],2,10],2))
#print(CUATRO([1,2,3],3))
#print(CUATRO([3],2))
#print(CUATRO([1,-2,3],-2))
#print(CUATRO( [1,[2,9,],[[4,2,6],[8]],2,10],2))