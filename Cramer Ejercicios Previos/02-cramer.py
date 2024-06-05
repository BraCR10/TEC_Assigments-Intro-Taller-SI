import matplotlib.pyplot as plt
def cramer():
    ecuacion = open('19_3_24\ecuaciones.txt', 'r')
    listaEcuacion=ecuacion.readlines()
    ecuacion.close
    listaTemp=[]
    principal=[]
    cont=1
    limite=0
    for i in listaEcuacion:#Itera en lista sin cambios
        i=int(i)
        listaTemp+=[i]
        if cont==3:
            principal+=[listaTemp]
            listaTemp=[]
            cont=0
        cont+=1
        limite+=1
        if limite==6:
            break
    print('La lista es:',principal)
    deterG=(principal[0][0]*principal[1][1])-(principal[1][0]*principal[0][1])
    deterX=(principal[0][2]*principal[1][1])-(principal[1][2]*principal[0][1])
    deterY=(principal[0][0]*principal[1][2])-(principal[1][0]*principal[0][2])
    print('El determinante General es:',deterG)
    print('El determinante X es:',deterX)
    print('El determinante Y es:',deterY)
    #Ecuaciones
    print('La ecuacion de la recta A es: ',principal[0][0],'x +',principal[0][1],'y =',principal[0][2])
    print('La ecuacion de la recta B es: ',principal[1][0],'x +',principal[1][1],'y =',principal[1][2])
    #Creacion de la figura
    fig, ax= plt.subplots()
    #Punto de ineterseccion
    if deterG!=0:
        x=deterX/deterG
        y=deterY/deterG
        print('X es igual a',x,' y Y es igual a',y)
        print('El punto de interseccion es: (',x,',',y,')')
        ax.scatter(x ,y,color='yellow')
    else:
        x=0
        y=0
        print("No hay interseccion entre las rectas, son paralelas!")
    
    #Mensaje de que debe ser paralelos
    #Interseccion con ejes de recta uno
    X1=principal[0][2]/principal[0][0]#Eje X
    Y1=principal[0][2]/principal[0][1]#Eje y
    #Interseccion con ejes de recta dos
    X2=principal[1][2]/principal[1][0]
    Y2=principal[1][2]/principal[1][1]
    #Listas para la cracion de las lineas
    LX1=[]
    LX2=[]
    LY1=[]
    LY2=[]
    mayorX=x
    menorX=x
    for i in [X1,X2]:
        if mayorX<i:
            mayorX=i
        if menorX>i:
            menorX=i
    mayorY=y
    menorY=y
    for i in [Y1,Y2]:
        if mayorY<i:
            mayorY=i
        if menorY>i:
            menorY=i
    #Se determina el punto mas largo de la coordenada (0,0) y se generan las listas para crar las lineas
    for i in range(int(menorX-8),int(mayorX+8)):
        LX1+=[i]
    for i in range(int(menorX-8),int(mayorX+8)):
        LX2+=[0]
    for i in range(int(menorY-8),int(mayorY+8)):
        LY1+=[0]
    for i in range(int(menorY-8),int(mayorY+8)):
        LY2+=[i]
    ax.axhline(y=0, color="black", linestyle="--")
    ax.axvline(color="red",linestyle="--")
    #Linea 1
    ax.axline((X1, 0), (0, Y1), linewidth=4, color='r')
    L1Y=[]
    for i in LX1:
        saltoY=(principal[0][2]-(principal[0][0]*i))/principal[0][1]
        L1Y+=[saltoY]
    #Linea 2
    ax.axline((X2, 0), (0, Y2), linewidth=4, color='r')
    L2Y=[]
    for i in LX1:
        saltoY=(principal[1][2]-(principal[1][0]*i))/principal[1][1]
        L2Y+=[saltoY]
    ax.plot(LX1,L1Y,color='#65FB30')
    ax.plot(LX1,L2Y, color='black')
    
    #Interseccion con ejes de recta uno
    ax.scatter(X1,0,color='green',)#Eje X
    ax.scatter(0,Y1,color='green')#Eje y
    ax.scatter(X2,0,color='green')#Eje X
    ax.scatter(0,Y2,color='green')#Eje y
    #Cuadro de signos
    if x==0 and y==0:
        plt.legend(["Eje X", "Eje Y","Recta A","Recta B","Intersecciones con ejes ordenados"])
    else:
        plt.legend([f"Punto de interseccion:  ({x} , {y})","Eje X", "Eje Y","Recta A","Recta B","Intersecciones con ejes ordenados"])
    plt.title("Interseccion entre rectas")
    #Limites de las rectas
    plt.scatter(LX1[0],L1Y[0],marker = '^',color="#65FB30")
    plt.scatter(LX1[0],L2Y[0],marker = '^',color="black")
    plt.scatter(LX1[len(LX1)-1],L1Y[len(L1Y)-1],marker = '^',color="#65FB30")
    plt.scatter(LX1[len(LX1)-1],L2Y[len(L2Y)-1],marker = '^',color="black")
    plt.scatter(LX1[len(LX1)-1],L2Y[len(L2Y)-1],marker = '^',color="black")


    plt.grid(True)
    plt.show()
    
cramer()
