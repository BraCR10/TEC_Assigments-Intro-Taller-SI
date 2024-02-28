def condicionales(x):
    if x%4==0:
        print('El resultado de la operacion es: ',x*x)
    elif x%4==1:
        print('El resultado de la operacion es: ',x/6)
    elif x%4==2:
        print('El resultado de la operacion es: ',(x**2*x**3)**2)
    elif x%4==3:
        print('El resultado de la operacion es: ',x*x*x+5)
    else:
        print('Nada que hacer')

condicionales(27.5)
