def largo(num):
    if type(num)==int:
        if num==0:
            return
        else:
            return largo_aux(num,0)
    else:
        print('Incorrecto')
        
def largo_aux(num,cont):
    if num==0:
        return cont 
    else:
        return largo_aux(num//10,cont+1)
    
def inv(num):
    if isinstance(num,int):
        if num==0:
            return 0
        else:
            return ((num%10)*(10**(largo(num)-1)))+inv_aux(num//10)
        
    else:
        print('Incorrecto')
        
def inv_aux(num):
    if largo(num)==1:
        return(num%10)*(10**(largo(num)-1))
    else:
        return ((num%10)*(10**(largo(num)-1)))+inv_aux(num//10)
#print(inv(8965))

def factorial(n):
    if isinstance(n,int):
        if n>=0:
            return factorial_aux(n,1)
        else:
            return('Errpr')
            
    else:
        print('Error')
        
def factorial_aux(n,resultado):
    if n==0:
        return resultado
    else:
        return factorial_aux(n-1,resultado*n)

def sumatoria1(i):
    if type(i)==int:
        if i==0:
            return factorial(0)+(0*2)*factorial(0)
        else:
            return sumatoria1_aux(i,i)
        
def sumatoria1_aux(n,i):
    if i<0:
        return 0
    else:
        return (factorial(i)+(n*2)*factorial(i))+sumatoria1_aux(n,i-1)
#print(sumatoria1(2))

def sumatoria2(n):
    if isinstance(n,int):
        if n==0:
            return 1
        else:
            return sumatoria2_aux(n,n,0)
        
def sumatoria2_aux(n,i,resultado):
    if i<0:
        return resultado 
    else:
        return sumatoria2_aux(n,i-1,resultado+(factorial(i)+(n*2)*factorial(i)))
#print(sumatoria2(2))