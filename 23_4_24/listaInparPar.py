def parImpares(lista):
    if type(lista)==list:
        if lista==[]:
            return []
        else:
            return parImpares_aux(lista,[],[])
def parImpares_aux(lista,par,impar):
    if len(lista)==0:
        return par,impar
    elif lista[0]%2==0:
        return parImpares_aux(lista[1:],par+[lista[0]],impar)
    elif lista[0]%2!=0:
        return parImpares_aux(lista[1:],par,impar+[lista[0]])
    
print(parImpares([1,2,9,6,3,4]))
      