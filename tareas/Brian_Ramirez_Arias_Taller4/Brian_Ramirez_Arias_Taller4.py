#Esta funcion lee un fichero llamado prueba.txt, los datos deben ser numeros separados por ;
#Ejemplo: 3;5 -----> El programa imprime 3 y 5 por separado
def leerPrueba(): 
    numeros = open('Prueba.txt', 'r')
    num=numeros.readlines()#Se crea una lista, cada linea en el fichero es un elemento
    numeros.close()
    lista=[]#Lista para almacenar cambios en los datos del fichero
    i=0
    while i < len(num):#Itera de 0 a la longitud de num
        nuevoNum=num[i].split(';')#Por cada elemento de num crea una nueva lista dividiendo cada vez que hay un ';'['2', '3\n']
        if nuevoNum==['\n'] or len(nuevoNum)!=2:#Validacion
            nuevoNum=[]
        else:#Validacion
            nuevoNum[1] = nuevoNum[1].replace('\n', '') #Elimina cada '\n' en cada elemento [1]
        i+=1
        lista+=[nuevoNum]
    print('\n La nueva lista es: ',lista)
    i=0
    while i <len(lista):#De 0 a el tamaño de lista
        if lista[i] == []:#Validacion
            print('\nLa linea ',i+1,' no sirve para este programa')
        else:#Validacion
            var1=lista[i][0]#Obtiene elemento [0] de lista de cada lista dentro de lista[] 
            var2=lista[i][1]#Obtiene elemento [1] de lista de cada lista dentro de lista[]
            print('\nEl primer elemento en la linea ',i+1,' es: ',var1)#Imprime en consola los numero de cada linea.
            print('El segundo elemento en la linea ',i+1,' es: ',var2)
        i+=1
  
    
leerPrueba()
