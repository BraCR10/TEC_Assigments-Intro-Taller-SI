#II Parcial
# Brian Ramirez Arias
#Carnet 2024109557

def cambioExponente(num):#Para ir cambiando exponente en las matrices que con numeros no divicibles entere 3
    if num==2:
        return 3
    else:
        return 2
def quitarCentro(num):#Funacion que toma un numero de tamaño impar y le quita el centro conviertiendo a par
    if largoNum(num)%2!=0 and type(num)==int:
        i=largoNum(num)//2
        numTem=0
        while i>0:
            numTem*=10
            numTem+=num%10
            num//=10
            i-=1
        num//=10#Extrae el del centro
        corte=numTem#almacena la mitad de los numeros del nuevo num
        while numTem!=0:
            num=num*10+(numTem%10)
            numTem//=10
        return(num,corte)
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
    else:#Validacion
        return 'Deben ser enteros'
def centro(num):
    if isinstance(num,int) and num>0 and largoNum(num)%2!=0:#Validacion
        posicionCentro=largoNum(num)//2+1#Obtiene la pocicion del centro
        num1=num#Copia
        while largoNum(num1)!=posicionCentro:#Se detiene cuando llega al centro
            num1//=10            
        centro=num1%10#Obtiene el digito del centro
        return(centro)
##########################################################################################################################
def UNO(n1,n2):
    if type(n1)==int and type(n2)==int and largoNum(n1)%2!=0 and largoNum(n2)%2!=0 and largoNum(n1)%5==0 and largoNum(n2)%5==0:
        n1Copia=abs(n1)
        n2Copia=abs(n2)
        num1Nuevo=0
        num2Nuevo=0
        bandera=0#Permite saber con cual numero se debe trabajar
        #Primer nuevo numero de izq a der
        for i in range(largoNum(n1)-1,-1,-1):
            temp1=n1Copia//(10**i)#Extrae el primer numero
            temp2=n2Copia//(10**i)#Extrae el primer numero
            n1Copia%=(10**i)#Crea el nuevo numero
            n2Copia%=(10**i)#Crea el nuevo numero
            if bandera==0:
                num1Nuevo=(num1Nuevo*10)+temp1
                bandera=1
            else:
                num1Nuevo=(num1Nuevo*10)+temp2
                bandera=0
        #Segundo nuevo numero de der a izq
        n1Copia=abs(n1)
        n2Copia=abs(n2)
        bandera=0
        for i in range(largoNum(n1)-1,-1,-1):
            temp1=n1Copia%10#Extrae el ultimo numero
            temp2=n2Copia%10#Extrae el ultimo numero
            n1Copia//=10#Crea el nuevo numero
            n2Copia//=10#Crea el nuevo numero
            if bandera==1:
                num2Nuevo=(num2Nuevo*10)+temp1
                bandera=0
            else:
                num2Nuevo=(num2Nuevo*10)+temp2
                bandera=1
        if largoNum(num2Nuevo)==largoNum(num1Nuevo):#Validacion
            n1Copia=num1Nuevo#Copia 1
            n2Copia=num2Nuevo#Copia 2
            #Creacion matrices
            matriz1=[]
            matriz2=[]
            if largoNum(num1Nuevo)%3==0 and largoNum(num2Nuevo)%3==0:#Si es divisible entre 3
                #Primera matriz
                exp=largoNum(num1Nuevo)-1#Se utiliza para encontrar el primer numero
                expFormula=2#Cambia para elevarlo deacuerdo al ejercicio
                for i in range(largoNum(num1Nuevo)//3):#Cantidad de sublistas
                    temp1=[]
                    for j in range(3):#De tres en tres
                        temp1+=[(n1Copia//10**exp)**expFormula]
                        n1Copia%=10**exp
                        exp-=1
                        expFormula=cambioExponente(expFormula)
                    matriz1+=[temp1]
                #Segunda matriz
                exp=largoNum(num2Nuevo)-1#Se utiliza para encontrar el primer numero
                expFormula=2#Cambia para elevarlo deacuerdo al ejercicio
                for i in range(largoNum(num2Nuevo)//3):#Cantidad de sublistas
                    temp1=[]
                    for j in range(3):#De tres en tres
                        temp1+=[(n2Copia//10**exp)**expFormula]
                        n2Copia%=10**exp
                        exp-=1
                        expFormula=cambioExponente(expFormula)
                    matriz2+=[temp1]
            else:#Si no es divicible entre 3
                #Primera matriz
                centro1=centro(num1Nuevo)#Obtiene el centro del nuevo num
                n1Copia,corte=quitarCentro(n1Copia)#Le quita el numero del centro a n1Copia y crea una variable que almacena los primero digitos
                mitad=largoNum(corte)#La cantidad de digitos de la mitad de n1Copia
                exp=largoNum(n1Copia)-1#Se utiliza para encontrar el primer numero
                expFormula=3#Cambia para elevarlo deacuerdo al ejercicio
                cont=0#Se utiliza para saber el numero de iteracion y de esta manera darse cuenta cuando se sobre pasa el dig del centro
                bandera=0#Se utiliza para las elevaciones, Da 1 solo una vez, cuando se sobre pasa el dig del centro
                for i in range(mitad):
                    temp1=[]
                    #Cada dos elementos
                    for j in range(2):
                        expFormula=cambioExponente(expFormula)#Se cambia el exponente
                        temp1+=[(n1Copia//10**exp)**expFormula]
                        n1Copia%=10**exp
                        exp-=1
                        cont+=1
                    expFormula=cambioExponente(expFormula)
                    #Para agregar el elemento del centro
                    if cont<=largoNum(corte):#Si es antes del dig del centro
                        temp1+=[centro1**expFormula]
                        if cont==largoNum(corte):
                            expFormula=cambioExponente(expFormula)
                            bandera=1
                    else:#Si es despues del dig del centro 
                        if bandera==1:
                            bandera=0
                            expFormula=cambioExponente(expFormula)
                        temp1=[centro1**expFormula]+temp1
                    matriz1+=[temp1]#Agrega temp a la matriz
                #Segunda matriz
                centro1=centro(num2Nuevo)#Obtiene el centro del nuevo num
                n2Copia,corte=quitarCentro(n2Copia)#Le quita el numero del centro a n2Copia y crea una variable que almacena los primero digitos
                mitad=largoNum(corte)#La cantidad de digitos de la mitad de n1Copia
                exp=largoNum(n2Copia)-1#Se utiliza para encontrar el primer numero
                expFormula=3#Cambia para elevarlo deacuerdo al ejercicio
                cont=0#Se utiliza para saber el numero de iteracion y de esta manera darse cuenta cuando se sobre pasa el gid del centro
                bandera=0#Se utiliza para las elevaciones, Da 1 solo una vez, cuando se sobre pasa el dig del centro
                for i in range(mitad):
                    temp1=[]
                    #Cada dos elementos
                    for j in range(2):
                        expFormula=cambioExponente(expFormula)#Se cambia el exponente
                        temp1+=[(n2Copia//10**exp)**expFormula]
                        n2Copia%=10**exp
                        exp-=1
                        cont+=1
                    expFormula=cambioExponente(expFormula)
                    #Para agregar el elemento del centro
                    if cont<=largoNum(corte):#Si es antes del dig del centro
                        temp1+=[centro1**expFormula]
                        if cont==largoNum(corte):
                            expFormula=cambioExponente(expFormula)
                            bandera=1
                    else:#Si es despues del dig del centro 
                        if bandera==1:
                            bandera=0
                            expFormula=cambioExponente(expFormula)
                        temp1=[centro1**expFormula]+temp1
                    matriz2+=[temp1]#Agrega temp a la matriz   
            #Suma de matrices
            sumaMatrices=[] 
            for i in range(len(matriz1)):
                temp1=[]
                for j in range(3):
                    temp1+=[matriz1[i][j]+matriz2[i][j]]
                sumaMatrices+=[temp1]
            print(n1)#Original1
            print(n2)#Original2
            print(num1Nuevo)#Nuevo numero 1
            print(num2Nuevo)#Nuevo numero 2
            print(matriz1)
            print(matriz2)
            print(sumaMatrices)      
        else:
            print(n1)#Original1
            print(n2)#Original2
            print(num1Nuevo)#Nuevo numero 1
            print(num2Nuevo)#Nuevo numero 2
            print('No se puede continuar porque los numeros nuevos tienen diferente largo')
    else:
        print('Parametros incorrectos')
#Pruebas       
#UNO(612576789012345,891025432156789)
#UNO(-612576789012345,891025432156789)
#UNO(61257,89102)
#UNO(1234567890123456789012345,1234567890123456789012345)
#UNO(12345678901234567890123451234567894,12345678901234567890123451234567891)
#UNO(1111111111119111111111111,1111111111119111111111111)
#UNO(1234512345123451234512345123451234512345123451234512345, 1234512345123451234512345123451234512345123451234512345)
#UNO(123456789123456789123456789123456789123456789,123456789123456789123456789123456789123456789) 
#UNO(123456789112340,123456789112340)
#UNO(1111111111111111111111191111111111111111111111111111111,1111111111111111111111111111119111111111111111111111111)
#UNO(34211,23452)

################################################################################################  
#Validar conjuntos
def conjunto(lista):
    largo=0
    pos=0 
    while largo<len(lista):
        while pos<len(lista):#Compara un numero con todos los otros
            if largo!=pos:#Se salta el mismo elemento
                if lista[pos]==lista[largo]:
                    return(False)
                elif type(lista[pos])!=int:
                    return(False)
                else:
                    pos+=1#
            else:#Se salta el mismo element
                pos+=1
        pos=0
        largo+=1
    return(True)
def DOS(lista):
    if isinstance(lista,list) and  conjunto(lista)==True:#Validacion
        if lista==[]:#Validacion
            print(lista)
            print([])
        else:
            temp=[]
            listaNueva=[]
            bandera=0#Se utiliza para saber si la lista estaba ordenada
            i=0
            while i<len(lista):#Hasta el largo de la lista
                if i==0:#Para saber que es la primera vez
                    temp+=[[1,0,lista[i]+1,lista[i],-(lista[i]),lista[i]-1,0,1]]
                else:
                    if lista[i]>=lista[i-1]:#Si el valor anterior es mayor
                        temp+=[[1,0,lista[i]+1,lista[i],-(lista[i]),lista[i]-1,0,1]]#Agrega
                    else:
                        bandera=1#Se activa, quiere decir que ya no estaba acomodada
                        listaNueva+=[temp]#Se agrega todos los datos en temp
                        temp=[[1,0,lista[i]+1,lista[i],-(lista[i]),lista[i]-1,0,1]]#Se resetea temp
                if i==len(lista)-1:#Para agregar lo ultimo em temp
                    listaNueva+=[temp]  
                i+=1  
            if bandera==0:#Validacion
                listaNueva=[lista]    
            print(lista)
            print(listaNueva)       
    else:#Validacion
        print(lista,' no es un conjunto')
#Pruebas
#DOS([8,-1,3,9,16,105,-220,13,18,17,1000])
#DOS([-100,99,-8])
#DOS([-5555,-88,-9,56,321])
#DOS([-5555,-88,-9,77,56,321])
#DOS([3,4,3])
#DOS([])
##########################################################################################################################
def TRES(elem,lista):
    if isinstance(elem,int) and type(lista)==list:
        nuevaLista=lista[:]
        operacion=[1,0,elem,elem,-(elem),0,1]
        listaNiveles = [nuevaLista]  # La lista principal
        print(lista)
        for i in listaNiveles:
            for j in range(len(i)):#Descompone niveles
                temp = i[j]#Vale cada num en la lista
                if isinstance(temp, list):
                    listaNiveles+=[temp]  # Se agrega al final de la lista de niveles para volver a pasar
                elif temp == elem:#Si es entero
                    i[j] = operacion  # agrega la operacion 
        print(nuevaLista)#Imprime la nueva lista
    else:
        print('Parametros incorrectos')
#Pruebas
#TRES(2,[2,5,2,[2],[2,[2,[2,[2,[8,8,9,[2]]]]]],8])
#TRES(2,[2,5,[2,[2,[2]]],5,[2,[5,2]]])
#TRES(2,[1,[2,9],[[4,2,6],[8]],2,10])
#TRES(-10,[1,[2,9],[[4,2,6],[8]],2,-10])
#TRES(-10,[1,[2,9],[[[[-10]]],[4,2,6],[8]],2,-10)]
#TRES(-10,[-10,888])
#TRES(1, [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[5,[[[[[[[[[[[[[[[[[[[[[[1]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]])
##########################################################################################################################
def CUATRO(num,numIncluir,cant,numBuscar):
    if isinstance(num,int) and isinstance(numIncluir,int) and isinstance(cant,int) and isinstance(numBuscar,int) and largoNum(numIncluir)==1:#Validacion
        if num==0:
            if numBuscar==0:#En caso de que sea el numero buscado
                listatemp=[0-1,1,0,1]#Primera parte llega desde antecesor hasta el primer patron
                cont=0
                while cant!=cont:
                    listatemp+=[numIncluir]#Incluye el numero a incluir la cantidad de veces indicadas
                    cont+=1
                listatemp+=[0,0]#El numero y el opuesto
                cont=0
                while cant!=cont:
                    listatemp+=[numIncluir]#Incluye el numero a incluir la cantidad de veces indicadas
                    cont+=1
                listatemp+=[0,-1,0,0+1]#El patron final y el sucesor 
                nuevaLista=[listatemp]#Agrega a la lista
            else:#En caso de que cero no sea el numero buscado
                nuevaLista=[0]
        else:
            numCopia=abs(num)
            cant=abs(cant)
            numBuscar=abs(numBuscar)
            nuevaLista=[]
            while numCopia!=0:
                temp=numCopia%10#Exstrae un digito de der a izq
                if temp==numBuscar:
                    listatemp=[temp-1,1,0,1]#Primera parte llega desde antecesor hasta el primer patron
                    cont=0
                    while cant!=cont:
                        listatemp+=[numIncluir]#Incluye el numero a incluir la cantidad de veces indicadas
                        cont+=1
                    listatemp+=[temp,-(temp)]#El numero y el opuesto
                    cont=0
                    while cant!=cont:
                        listatemp+=[numIncluir]#Incluye el numero a incluir la cantidad de veces indicadas
                        cont+=1
                    listatemp+=[0,-1,0,temp+1]#El patron final y el sucesor 
                    nuevaLista=[listatemp]+nuevaLista#Agrega a la lista
                else:
                    nuevaLista=[temp]+nuevaLista#Agrega a la lista
                numCopia//=10#Exstrae un digito de der a izq
        
        print(num , nuevaLista)
    else:#Validacion
        print('Parametros incorrectoa')
#Pruebas
#CUATRO(73439,8,2,3)
#CUATRO(73439777,-8,5,1)
#CUATRO(-73439777,-8,5,1)
#CUATRO(855,-8,5,0)
#CUATRO(0,-8,5,0)
#CUATRO(-0,-8,5,0)
#CUATRO(81180,-3,-10,-8)
#CUATRO(1, -2, 1,1)
#CUATRO(1, -2, 0,1)
#CUATRO(0,-2,0,0)
#CUATRO(0,-2,1,0)
