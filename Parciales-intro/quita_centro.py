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
def quitaCentro(num):
    if num%2!=0 and type(num)==int:
        i=largoNum(num)//2
        numTem=0
        while i>0:
            numTem*=10
            numTem+=num%10
            num//=10
            i-=1
        num//=10
        while numTem!=0:
            num=num*10+(numTem%10)
            numTem//=10
        print(num)
quitaCentro(12345)