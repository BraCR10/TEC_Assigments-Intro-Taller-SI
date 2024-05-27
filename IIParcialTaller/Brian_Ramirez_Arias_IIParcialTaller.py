def lecturaArchivo():
    archivo = open('IIParcialTaller/Arch1.txt', 'r', encoding="utf8")
    listaArch1=eliminador(archivo)
    archivo.close()  
    archivo = open('IIParcialTaller/Arch2.txt', 'r', encoding="utf8")
    listaArch2=eliminador(archivo)
    archivo.close()  
    archivo = open('IIParcialTaller/Arch3.txt', 'r', encoding="utf8")
    listaArch3=eliminador(archivo)
    archivo.close()  
    archivo = open('IIParcialTaller/Arch4.txt', 'r', encoding="utf8")
    listaArch4=eliminador(archivo)
    archivo.close()  
    archivo = open('IIParcialTaller/Arch5.txt', 'r', encoding="utf8")
    listaArch5=eliminador(archivo)
    archivo.close()  
    #Agregando identificador
    listaArch1=[1]+listaArch1
    listaArch2=[2]+listaArch2
    listaArch3=[3]+listaArch3
    listaArch4=[4]+listaArch4
    listaArch5=[5]+listaArch5
    
    return[listaArch1,listaArch2,listaArch3,listaArch4,listaArch5]
    
    
def eliminador(archivo):
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
    
   
def listaPostFijo(lista):
    lista=lista[1:]
    listaPila=[]
    listaExpresion=[]
    for elemento in lista:
        if elemento.isdigit():
            listaExpresion+=[int(elemento)]
        else:
            if listaPila==[]:
                listaPila+=[elemento]
            elif elemento=='(' :
                listaPila+=[elemento]
            elif elemento=='^' :
                if listaPila[len(listaPila)-2:] =='^':
                    listaExpresion+=[listaPila[len(listaPila)-2:]]
                    listaPila=listaPila[:len(listaPila)-2]
                    listaPila+=[elemento]
                else:
                    listaPila+=[elemento]

            elif elemento=='*' or elemento=='/':
                if listaPila[len(listaPila)-1:] in [['^'],['/'],['*']]:
                    listaExpresion+=listaPila[len(listaPila)-1:]
                    listaPila=listaPila[:len(listaPila)-1]
                    listaPila+=[elemento]
                else:
                    listaPila+=[elemento]
            elif elemento=='+' or elemento=='-':
                if listaPila[len(listaPila)-1:] in [['^'],['*'],['/'],['-'],['+']]:
                    listaExpresion+=listaPila[len(listaPila)-1:]
                    listaPila=listaPila[:len(listaPila)-1]
                    listaPila+=[elemento]
                else:
                    listaPila+=[elemento]
            elif elemento==')':
                for rastreador in range(len(listaPila)):
                    if listaPila[rastreador]=='(':
                        parentesisCerrar=rastreador
                if parentesisCerrar==0:
                    listaPila=listaPila[1:]
                    for items in range(len(listaPila)-1,-1,-1):
                        listaExpresion+= listaPila[items]
                    listaPila=[]
                else:
                    for items in range(len(listaPila[parentesisCerrar+1:])-1,-1,-1):
                        listaExpresion+=listaPila[parentesisCerrar+1:][items]
                    listaPila=listaPila[:parentesisCerrar]
    for i in range(len(listaPila)-1,-1,-1):#Si quedaron cosas para agregar a la listaExpresion    
        if listaPila[i]!=')':
            listaExpresion+= listaPila[i]
    return listaExpresion
    

def evaluacion(listaExpresion):
    listaNumeros=[]
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
                listaNumeros+=[num1/num2]
            elif items=='+':
                listaNumeros+=[num1+num2]
            elif items=='-':
                listaNumeros+=[num1-num2]
            print(listaNumeros)
    return listaNumeros[0]
                
        
        
        
            
    
def principal():
    ListaArchivos=lecturaArchivo()
    
    listaExpresionArch1=listaPostFijo(ListaArchivos[0])
    evaluacionArch1=evaluacion(listaExpresionArch1)
    
    listaExpresionArch2=listaPostFijo(ListaArchivos[1])
    evaluacionArch2=evaluacion(listaExpresionArch2)
    
    listaExpresionArch3=listaPostFijo(ListaArchivos[2])
    evaluacionArch3=evaluacion(listaExpresionArch3)
    
    listaExpresionArch4=listaPostFijo(ListaArchivos[3])
    evaluacionArch4=evaluacion(listaExpresionArch4)
    
    listaExpresionArch5=listaPostFijo(ListaArchivos[4])
    evaluacionArch5=evaluacion(listaExpresionArch5)
    
    print(ListaArchivos[0])
    print(listaExpresionArch1)
    print(evaluacionArch1)
    print()
    
    print(ListaArchivos[1])
    print(listaExpresionArch2)
    print(evaluacionArch2)
    print()
    
    print(ListaArchivos[2])
    print(listaExpresionArch3)
    print(evaluacionArch3)
    print()
    
    print(ListaArchivos[3])
    print(listaExpresionArch4)
    print(evaluacionArch4)
    print()
    
    print(ListaArchivos[4])
    print(listaExpresionArch5)
    print(evaluacionArch5)
    print()
principal()