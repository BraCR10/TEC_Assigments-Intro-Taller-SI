#Funcion que detecte si un numero entero tiene al menos un par
def detector(n):
    if isinstance(n,int):
        temp=abs(n)
        par=False
        if temp==0:
            par=True
        else:
            while temp!=0:
                if temp%10%2==0:
                    par=True
                temp//=10
                break
        return par
    else:#Validacion
        return 'Debe ser un numero entero'

print(detector(4))


