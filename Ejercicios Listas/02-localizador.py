def buscaAgregaNuevo(nuevo,buscar,lista):
    if(isinstance(nuevo,int) and isinstance(buscar, int) and isinstance(lista,list)):
        if(lista==[]):
            return(0)
        else:
            cont=0
            for i in range(len(lista)):
                if(i==0 and buscar==lista[i]):
                    lista=[nuevo]+lista[0:]
                    cont=cont+2
                elif(buscar==lista[i+cont]):
                    lista=lista[0:i+cont]+[nuevo]+lista[i+cont:]
                    cont=cont+2
                else:
                    lista=lista
                    cont=cont+1
                cont=cont-1
            return(lista)
                    
    else:
        print("Inserte digitos válidos")


print(buscaAgregaNuevo(1,2,[1,2,2]))



























