def sumasinceros_cola(n1,n2):#2309,1002 =>239+12= 251
    if type(n1)==int or type(n2)==int:
        return sumasinceros_colaux(abs(n1),abs(n2),0,0,0,0)
    else:
        return "los numeros deben ser enteros"
    
def sumasinceros_colaux(n1,n2,a,b,c,d):

    if n1==0 and n2==0:# finalizacion
        return c+d #
    elif n1%10==0 and n2%10==0:
        
       return sumasinceros_colaux(n1//10,n2//10,a,b,c,d)
       #                         
       
    elif n1%10==0 and n2%10!=0:
       
        return sumasinceros_colaux(n1//10,n2//10,a,b+1,c,(d+(n2%10*10**b)))
    
    elif n1%10!=0 and n2%10==0:
       
        return sumasinceros_colaux(n1//10,n2//10,a+1,b,(c+(n1%10*10**a)),d)
       
    
    else:
        
        return sumasinceros_colaux(n1//10,n2//10,a+1,b+1,(c+(n1%10*10**a)),(d+(n2%10*10**b)))



    
#**********************************
    
# cambia numero
def CambiaNumero(n):#3456 1010
    if isinstance(n,int):
        
        #0=>0 0
        return Cambia_aux(0,0,abs(n))
        
    else:
        print("numero no entero")
        


#**************************************************   
#Ejemplo  16,4,[5,6,7,8,4,6,7,89,4]  salida [5,6,7,8,16,4,6,7,89,16,4]
def ejemplonuevo(nuevo,buscar,lista):
    
    if lista==[]:
        return []
    else:
        return ejemplonuevoaux(nuevo,buscar,lista,0,lista)

def ejemplonuevoaux(nuevo,buscar,nlista,cont, otralista):

    
    if otralista==[]:
       
        return(nlista)#
    elif nlista[cont]== buscar:
       
        return ejemplonuevoaux(nuevo,buscar,nlista[0:cont]+[nuevo]+nlista[cont:],cont+2,otralista[1:])
    else:
        return ejemplonuevoaux(nuevo,buscar,nlista,cont+1, otralista[1:])
       
    
    




