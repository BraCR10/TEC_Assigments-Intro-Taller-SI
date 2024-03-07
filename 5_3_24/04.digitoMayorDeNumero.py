
#recibe un numero entero, y obtiene el digito mayor dentro del entero
def inspector(num):
    if type(num)==int and num>=0:#Validacion
        numCopia=num
        max=0
        while numCopia!=0:
            numActual=numCopia%10#Obtiene cada ultimo digito de numActual
            if numActual>max:#Actualiza el max
                max=numActual
            numCopia//=10
        print( '\nEl digito mayor en el numero es: ',max)
    else:#Validacion
        print ('\nEl parametro debe se un numero entero y positivo')
#Prueba       
inspector(51)

#recibe un numero entero, y obtiene el mayor en una lista
def inspector(num):
    if type(num)==int and num>=0:#Validacion
        numCopia=num
        max=0
        i=abs(num)#Para negativos
        lista=[]
        while i>0:
            temp=i%10#Recolecta el ultimo numero
            lista=[temp]+lista
            i//=10#Quita el ultimo numero
        i=len(lista)
        while numCopia!=0:
            numActual=numCopia%10#Obtiene cada ultimo digito de numActual
            if numActual>max:#Actualiza el max
                max=numActual
            numCopia//=10
        print( '\nEl digito mayor en el numero es: ',max)
    else:#Validacion
        print ('\nEl parametro debe se un numero entero y positivo')
#Prueba       
inspector(51)