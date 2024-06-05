#Esta funcion agrega un numero en una lista, tomando como referencia un numero ya presente y lo agraga alante
def agreganum(nuevo,buscar,lista):
    if type(nuevo)==int and type(buscar)==int and type(lista)==list:#Validacion
        if lista==[]:#Validacion
            return []
        else:
            i=0
            while i<=(len(lista)-1):
                if i==0 and buscar==lista[i]:#Busca en picion 0 y si buscar es igual a ese elemento en 0
                    lista=[nuevo]+lista#Lo agraga adelante del ultimo num
                    i+=1#Suam uno
                elif buscar==lista[i]:#En cuanquier otra posicion que no es 0
                    lista=lista[0:i]+[nuevo]+lista[i:]#Parte la lista y pone el nuevo adelante del numero buscar
                    i+=1
                else:#Si buscar no existe enlista
                    lista=lista
                i+=1
            return lista
    else:
        return 'Parametros incorrectos'

print(agreganum(1,2,[3,2,5,1,2]))