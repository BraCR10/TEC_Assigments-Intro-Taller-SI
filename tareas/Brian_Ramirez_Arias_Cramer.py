import matplotlib.pyplot as plt
def cramer():
    ecuacion = open('tareas\ecuaciones.txt', 'r',encoding="utf8")
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
    if len(principal)!=2 :
        print('Datos insuficientes!')
        return None
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
        print('El X de la interseccion es igual a',x,' y el Y de la interseccion es igual a',y)
        print('El punto de interseccion es: (',x,',',y,')')
        ax.scatter(x ,y,color='orange',linewidth=5)
    else:
        x=0
        y=0
        print("No hay interseccion entre las rectas, son paralelas!")

    #Interseccion con ejes de recta uno
    vertical1=0
    horizontal1=0
    vertical2=0
    horizontal2=0
    if principal[0][0]==0:
        horizontal1=1
        X1=0
    else:
        X1=principal[0][2]/principal[0][0]#Eje X
    if principal[0][1]==0:
        vertical1=1
        Y1=0
    else:
        Y1=principal[0][2]/principal[0][1]#Eje y
    #Interseccion con ejes de recta dos
    if principal[1][0]==0:
        horizontal2=1
        X2=0
    else:
        X2=principal[1][2]/principal[1][0]
    if principal[1][1]==0:
        vertical2=1
        Y2=0
    else:
        Y2=principal[1][2]/principal[1][1]
    #Creacion de ejes ordenados X y Y
    ax.axhline(y=0, color="black", linestyle="--",linewidth=2,marker="^")
    ax.axvline(x=0,color="red",linestyle="--",linewidth=2,marker="^")
    #Recta 1 
    if vertical1==1:
        ax.axvline(x=X1, linewidth=1, color='b',marker="^")
    elif horizontal1==1:
        ax.axhline(y=Y1, linewidth=1, color='b',marker="^")
    else:
        ax.axline((X1, 0), (0, Y1), linewidth=1, color='b',marker="^")#Pasa por los dos punto de interseccion
    #Recta 2
    if vertical2==1:
        ax.axvline(x=X2, linewidth=1, color='#65FB30',marker="^")
    elif horizontal2==1:
        ax.axhline(y=Y2, linewidth=1, color='#65FB30',marker="^")
    else:
        ax.axline((X2, 0), (0, Y2), linewidth=1, color='#65FB30',marker="^")
    #Interseccion con ejes de recta uno
    if horizontal1!=1:
        ax.scatter(X1,0,color='green',)#Eje X
    if vertical1!=1:
        ax.scatter(0,Y1,color='green')#Eje y
    #Interseccion con ejes de recta dos
    if horizontal2!=1:
        ax.scatter(X2,0,color='green')#Eje X
    if vertical2!=1:
        ax.scatter(0,Y2,color='green')#Eje y
    #Cuadro de signos
    if x==0 and y==0:
        plt.legend(["Eje X", "Eje Y","Recta A","Recta B","Intersecciones con ejes ordenados"])
    else:
        plt.legend([f"Punto de interseccion:  ({x} , {y})","Eje X", "Eje Y","Recta A","Recta B","Intersecciones con ejes ordenados"])
    plt.title("Interseccion entre rectas")
    plt.grid(True)
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.show()
    
cramer()
