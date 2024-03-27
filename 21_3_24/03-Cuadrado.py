def Cuadrado(n):
    return n**2
def aplicaFuncion(funcion,lista):
    listaNueva=[]
    i=0
    while i<len(lista):
        listaNueva+=[(funcion(lista(i)))]
        i+=1
    return listaNueva

for i in range(0,3):
    for j in range(0,4):
        print(i,j)
