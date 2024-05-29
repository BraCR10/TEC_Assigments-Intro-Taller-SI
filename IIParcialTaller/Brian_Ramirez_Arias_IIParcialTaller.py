def lecturaArchivo():
    archivo = open('IIParcialTaller/Arch1.txt', 'r', encoding="utf8")
    listaArch1=filtradorItems(archivo)
    archivo.close()  
    archivo = open('IIParcialTaller/Arch2.txt', 'r', encoding="utf8")
    listaArch2=filtradorItems(archivo)
    archivo.close()  
    archivo = open('IIParcialTaller/Arch3.txt', 'r', encoding="utf8")
    listaArch3=filtradorItems(archivo)
    archivo.close()  
    archivo = open('IIParcialTaller/Arch4.txt', 'r', encoding="utf8")
    listaArch4=filtradorItems(archivo)
    archivo.close()  
    archivo = open('IIParcialTaller/Arch5.txt', 'r', encoding="utf8")
    listaArch5=filtradorItems(archivo)
    archivo.close()  
    #Agregando identificador
    listaArch1=[1]+listaArch1
    listaArch2=[2]+listaArch2
    listaArch3=[3]+listaArch3
    listaArch4=[4]+listaArch4
    listaArch5=[5]+listaArch5
    
    return[listaArch1,listaArch2,listaArch3,listaArch4,listaArch5]
    
    
def filtradorItems(archivo):
    lista = []
    cadenaTemp = ''
    while True:#Termina hasta que se recorra todo el archivo
        digito = archivo.read(1)#Se recorre una linea a la vez
        if  digito=='':#Si ya se recorrio todo el archivo
            break
        if digito.isdigit()==True:#Si la cadena es un digito
            cadenaTemp += digito
        elif digito != '\n' and digito != ' ':
            if cadenaTemp!='':
                lista+=[cadenaTemp]
                cadenaTemp = ''
            lista+=[digito]#Cualquier cosa diferente de \n o ' ' como (),+,-,*,^....
    if cadenaTemp!='':
        lista+=[cadenaTemp]
    return lista
    
   
def listasPosFijo(lista):#Convierte una operacion a una lista posfijo
    lista=lista[1:]#Se quita la identificacion de archivo
    listaPila=[]#Donde se ponen los operandos
    listaExpresion=[]#Se arma la lista a retornar
    bandera=False#Se utiliza para ver la pila en un while true
    for elemento in lista:
        if elemento.isdigit():
            listaExpresion+=[int(elemento)]
        else:
            if listaPila==[]:
                listaPila+=[elemento]
            elif elemento=='(' :
                listaPila+=[elemento]
            elif elemento=='^' :
                while True:
                    if listaPila[len(listaPila)-1:] ==['^']:#Solo pasa si el elemento mas reciente es en pila es ^
                        listaExpresion+=listaPila[len(listaPila)-1:]
                        listaPila=listaPila[:len(listaPila)-1]
                        bandera=True
                    elif bandera==False:#Si no es ^
                        listaPila+=[elemento]
                        break
                    elif bandera==True:
                        listaPila+=[elemento]
                        break
                bandera=False
            elif elemento=='*' or elemento=='/':
                while True:
                    if listaPila[len(listaPila)-1:] in [['^'],['/'],['*']]:#Solo pasa si el elemnto mas reciente en cola es ^ o / o *
                        listaExpresion+=listaPila[len(listaPila)-1:]
                        listaPila=listaPila[:len(listaPila)-1]
                        bandera=True
                    elif bandera==False:#Si  no es ^ o / o *
                        listaPila+=[elemento]
                        break
                    elif bandera==True:
                        listaPila+=[elemento]
                        break
                bandera=False
            elif elemento=='+' or elemento=='-':
                while True:
                    if listaPila[len(listaPila)-1:] in [['^'],['*'],['/'],['-'],['+']]:#Solo pasa si el elemento mas reciente en la  es ^ o / o * o + o -
                        listaExpresion+=listaPila[len(listaPila)-1:]
                        listaPila=listaPila[:len(listaPila)-1]
                        bandera=True
                    elif bandera==False:#Si no  es ^ o / o * o + o -
                        listaPila+=[elemento]
                        break
                    elif bandera==True:
                        listaPila+=[elemento]
                        break
                bandera=False
            elif elemento==')':#Si se necesita cerrar un parentesis
                for rastreador in range(len(listaPila)):
                    if listaPila[rastreador]=='(':
                        parentesisCerrar=rastreador
                if parentesisCerrar==0:#Si es el ultimo parentesis
                    listaPila=listaPila[1:]
                    for items in range(len(listaPila)-1,-1,-1):
                        listaExpresion+= listaPila[items]
                    listaPila=[]
                else:#Si no es el ultimo parentesis
                    for items in range(len(listaPila[parentesisCerrar+1:])-1,-1,-1):
                        listaExpresion+=listaPila[parentesisCerrar+1:][items]
                    listaPila=listaPila[:parentesisCerrar]
    for i in range(len(listaPila)-1,-1,-1):#Si quedaron cosas para agregar a la listaExpresion diferentes a )   
        if listaPila[i]!=')':
            listaExpresion+= listaPila[i]
    return listaExpresion
    

def evaluacionListaPosFijo(listaExpresion):#Genera la evalucion de una lista en posfijo
    listaNumeros=[]#Lista donde se almacena las operaciones
    for items in listaExpresion:
        if type(items)==int:
            listaNumeros+=[items]
        else:
            num1=listaNumeros[len(listaNumeros)-2]
            num2=listaNumeros[len(listaNumeros)-1]
            listaNumeros=listaNumeros[:len(listaNumeros)-2]
            if items=='^':
                listaNumeros+=[num1**num2]
            elif items=='*':
                listaNumeros+=[num1*num2]
            elif items=='/':
                if num2!=0:
                    listaNumeros+=[num1/num2]
                else:
                    return 'Error por divicion entre 0'
            elif items=='+':
                listaNumeros+=[num1+num2]
            elif items=='-':
                listaNumeros+=[num1-num2]
    return listaNumeros[0]
                
        
        
        
            
    
def impresor():#Genera todas las listas para imprimir
    ListaArchivos=lecturaArchivo()#Genera la lista de archivos
    
    #LLamada a las funciones de posfijo y evaluacion de cada archivo
    listaExpresionArch1=listasPosFijo(ListaArchivos[0])
    evaluacionArch1=evaluacionListaPosFijo(listaExpresionArch1)
    
    listaExpresionArch2=listasPosFijo(ListaArchivos[1])
    evaluacionArch2=evaluacionListaPosFijo(listaExpresionArch2)
    
    listaExpresionArch3=listasPosFijo(ListaArchivos[2])
    evaluacionArch3=evaluacionListaPosFijo(listaExpresionArch3)
    
    listaExpresionArch4=listasPosFijo(ListaArchivos[3])
    evaluacionArch4=evaluacionListaPosFijo(listaExpresionArch4)
    
    listaExpresionArch5=listasPosFijo(ListaArchivos[4])
    evaluacionArch5=evaluacionListaPosFijo(listaExpresionArch5)
    
    #Imprime todo lo necesario
    print('Lista original del archivo 1: ',ListaArchivos[0])
    print('Lista postfijo del archivo 1: ',listaExpresionArch1)
    print('Resultado del archivo 1: ',evaluacionArch1)
    print()
    
    print('Lista original del archivo 2: ',ListaArchivos[1])
    print('Lista postfijo del archivo 2: ',listaExpresionArch2)
    print('Resultado del archivo 2: ',evaluacionArch2)
    print()
    
    print('Lista original del archivo 3: ',ListaArchivos[2])
    print('Lista postfijo del archivo 3: ',listaExpresionArch3)
    print('Resultado del archivo 3: ',evaluacionArch3)
    print()
    
    print('Lista original del archivo 4: ',ListaArchivos[3])
    print('Lista postfijo del archivo 4: ',listaExpresionArch4)
    print('Resultado del archivo 4: ',evaluacionArch4)
    print()
    
    print('Lista original del archivo 5: ',ListaArchivos[4])
    print('Lista postfijo del archivo 5: ',listaExpresionArch5)
    print('Resultado del archivo 5: ',evaluacionArch5)
    print()

impresor()