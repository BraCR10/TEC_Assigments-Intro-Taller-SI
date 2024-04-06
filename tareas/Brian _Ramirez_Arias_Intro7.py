def numeros(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):#Validacion
        if num1==0 or num2==0:#Si uno es 0
            print(0)
        else:
            bandera=0
            if   (num2<0 or num1<0) and  not(num2<0 and  num1<0):#Si alguno es negativo
                bandera=1#Bandera
            num1=abs(num1)
            num2=abs(num2)
            lista1=[]
            lista2=[]
            while num1!=0:#Crea la primera lista, divicion entera hasta 0 de num1
                lista1+=[num1]
                num1//=2
            for i in range(len(lista1)):#Crea una segunda lista, multiplicando num2 por 2 hasta el tamaño de la lista1
                lista2+=[num2]
                num2*=2
            print(lista1,lista2)
            listaImpares=[]
            for i in range(len(lista1)):#Obtiene las ubicaciones de los numeros impares en la lista 1
                if lista1[i] %2!=0:
                    listaImpares+=[i]
            print(listaImpares) 
            suma=0
            for i in listaImpares:#Suma los numeros de la lista 2 con respecto a la ubicacion en listaimpares
                suma+=lista2[i]
            if bandera==1:#Validacion
                print(suma*-1)
            else:#Validacion
                print(suma)
#Pruebas
#numeros(8,1)