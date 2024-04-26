def Pasalista(num):#2345
    if num==0:
        return [0]
    else:
        return Pasalistaux(num,[])
    
def Pasalistaux(num,lista):
    #num     lista
    #2345    []
    #234     [5]
    #23      [4,5]
    #2       [3,4,5]
    #        [2,3,4,5]
    
    if num==0:
        return lista #[2,3,4,5]
    else:
        return Pasalistaux(num//10,[num%10]+lista)
        #return (234,[5]+[])
        #return (23,[4]+[5])
        #return (2, [3]+[4,5])
        #return (0, [2]+[3,4,5])

def ParesCD(num):#23451
    if type(num)==int:
        num=abs(num)
        ListaNueva=Auxiliares.Pasalista(num)#[2,3,4,5,1]
        if ListaNueva==[0]:
            return [0]
        else:
            return ParesCD_aux(ListaNueva,[])
    else:
        print("Parametro incorrecto")

def ParesCD_aux(lista,LNueva):
    #[2,3,4,5,1]      []
    #[3,4,5,1]        [2]
    #[4,5,1]          [2]
    #[5,1]            [2,4]
    #[1]              [2,4]
    #[]               [2,4]
    
    if lista ==[]:
        return LNueva#[2,4]
    elif lista[0]%2==0: #2%2si 3%2x 4%2si 5%2x 1%2x
        return ParesCD_aux(lista[1:],LNueva+[lista[0]])
        #return ParesCD_aux([3,4,5,1],[]+[2])
        #return ParesCD_aux([5,1],[2]+[4])
    else:
        return ParesCD_aux(lista[1:],LNueva)
        #return ParesCD_aux([4,5,1],[2])
        #return ParesCD_aux([1],[2,4])
        #return ParesCD_aux([],[2,4])


def largonum(num): #234=>3 
    if num==0: #validacion 
        return 1
    else:
        cont=0 #contador
        while num!=0:# 9 0
            
       # Ejecuta las instrucciones las 2 instrucciones dentro del while
        #mientras la condicion es verdadera    
            cont=cont+1 #0+1 =1 
            #print("valor del contador:",cont)
            num=num//10 #9//10=0
            #print("cambio del parametro num:",num)
        return cont

