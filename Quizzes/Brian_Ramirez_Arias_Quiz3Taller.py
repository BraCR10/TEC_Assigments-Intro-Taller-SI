def cramer():
    ecuacion = open('19_3_24\ecuaciones.txt', 'r')
    listaEcuacion=ecuacion.readlines()
    ecuacion.close
    listaTemp=[]
    principal=[]
    cont=1
    for i in listaEcuacion:#Itera en lista sin cambios
        i=int(i)
        listaTemp+=[i]
        if cont==3:
            principal+=[listaTemp]
            listaTemp=[]
            cont=0
        cont+=1
    print('La lista es:',principal)
    deterG=(principal[0][0]*principal[1][1])-(principal[1][0]*principal[0][1])
    deterX=(principal[0][2]*principal[1][1])-(principal[1][2]*principal[0][1])
    deterY=(principal[0][0]*principal[1][2])-(principal[1][0]*principal[0][2])
    print('El determinante General es:',deterG)
    print('El determinante X es:',deterX)
    print('El determinante Y es:',deterY)
    #Punto de ineterseccion
    if deterG!=0:
        x=deterX/deterG
        y=deterY/deterG
        print('X es igual a',x,' y Y es igual a',y)
        print('El punto de interseccion es: (',x,',',y,')')
    #Mensaje de que debe ser paralelos
    else:
        print('No se puede, ya que las graficas son paralelas')
    
cramer()
