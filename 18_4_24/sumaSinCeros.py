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
print(sumasinceros_cola(10,10))