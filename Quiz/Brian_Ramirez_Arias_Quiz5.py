def numeros(num1,num2):
    if isinstance(num1,int) and isinstance(num2,int):
        num1=abs(num1)
        num2=abs(num2)
        lista1=[]
        lista2=[]
        while num1!=0:
            print(num1)
            lista1+=[num1]
            num1//=2
        for i in range(len(lista1)):
            lista2+=[num2]
            num2*=2
        print(lista1,lista2)
        listaImpares=[]
        for i in range(len(lista1)):
            if lista1[i] %2!=0:
                listaImpares+=[i]
        print(listaImpares)
        suma=0
        for i in listaImpares:
            suma+=lista2[i]
        print(suma)
#Pruebas
numeros(90,5)