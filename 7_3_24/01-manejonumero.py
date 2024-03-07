def largo(num): #234=>3 
    if num==0: #validacion 
        return 1
    else:
        cont=0 #contador
        while num!=0:# 9 0 Ejecuta las instrucciones las 2 instrucciones dentro del while
            cont=cont+1 #0+1 =1 mientras la condicion es verdadera
            #print("valor del contador:",cont)
            num=num//10 #9//10=0
            #print("cambio del parametro num:",num)
        return cont
    

#****************************************************************
def suma(num):#230789
    resultado = 0#0 0 11 110 1111 11110
    mayorExp = largo(num)-1#6-1=5 4 3 2
    menorExp = 1#1 2 3 4
    resultadoExp = 0#0 1 2 3
    #**********************************************************
    while menorExp <= largo(num)/2:
        #
        if resultado != 0:#
            resultado *= 10
        #Calcular numeros en los extremos
        n1 = (num//(10**mayorExp))%10
            
        n2 = (num%(10**menorExp))//(10**resultadoExp)
        #
        print("Primer numero: ",n1)#2 3 0
        print("Segundo numero: ",n2)#9 8 7
        suma = n1 + n2#11 11 7
        if suma >= 10:#11si 11si
            resultado *= 10# 110*10=1100
        resultado += suma#1100+11=1111 11110+7=11117
        print("Suma: ",resultado)#11 1111 11117
        print("\n")#cambio de linea
        mayorExp -= 1
        menorExp += 1
        resultadoExp += 1
        
    # fuera del while      2306789
    if largo(num)%2 == 1:#6%2x 
        #Si es impar se saca el del centro
        n = (num//(10**mayorExp))%10
        print("Numero del centro: ", n)
        resultado *= 10
        resultado += n
    return resultado

print(suma(1789))