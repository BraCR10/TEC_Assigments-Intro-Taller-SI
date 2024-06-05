def pasaListaRC(num):
    if type(num)==int:
        if num ==0:
            return [0]
        else:
            return pasaListaRC_aux(num,[])
def pasaListaRC_aux(num,lista):
    if num==0:
        return lista
    else:
        return pasaListaRC_aux(num//10,[num%10]+lista)
#Pruebas
#print(pasaListaRC(6633))
def pasaListaRP(num):
    if type(num)==int:
        if num ==0:
            return [0]
        else:
            return pasaListaRP_aux(abs(num))
    
def pasaListaRP_aux(num):
    if num==0:
        return []
    else:
        return pasaListaRP_aux(num//10)+[num%10]
#Pruebas
#print(pasaListaRP(7)) 
