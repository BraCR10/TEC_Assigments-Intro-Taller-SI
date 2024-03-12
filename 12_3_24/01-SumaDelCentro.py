def lenNum(num):#Funcion del largo
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
    else:
        return 'Deben ser enteros'
#Esta funcion obtiene el medio de un entero y suma todos los otros digitos con el centro
def sumaConCentro(num):
    if isinstance(num,int) and num>0 and lenNum(num)%2!=0:#Validacion
        posicionCentro=lenNum(num)//2+1#Obtiene la pocicion del centro
        num1=num#Copia
        while lenNum(num1)!=posicionCentro:#Se detiene cuando llega al centro
            num1//=10            
        centro=num1%10#Obtiene el digito del centro
        largo=lenNum(num)
        posicionCentro=lenNum(num)//2+1#Obtiene la pocicion del centro
        num1=num#Copia
        suma=0
        while largo>0:#
            if largo==posicionCentro:#Se salta el numero del centro
                num1//=10  
            else:
                suma+=centro+num1%10#Le suma a cada numero el centro
                num1//=10 
            largo-=1  
        print(suma)    


sumaConCentro(62891)
