def nuevaListaCentro(lista1,lista2):
    if(len(lista1)==len(lista2) and len(lista1)!=0 and len(lista1)%2!=0):
        centrol2=0
        centrofl2=len(lista2)-1
        centrol1=(len(lista1)//2)-1
        centrodl1=(len(lista1)//2)+1
        lnueva=[]
        centro1=len(lista1)//2
        centro2=len(lista2)//2
        i=1
        while(i<=len(lista1)//2):
            lnueva=lnueva+[lista1[centro1]+lista2[centrol2]]+[lista1[centro1]+lista2[centrofl2]]+[lista2[centro2]+lista1[centrol1]]+[lista2[centro2]+lista1[centrodl1]]
            i=i+1
            centrol2=centrol2+1
            centrofl2=centrofl2-1
            centrol1=centrol1-1
            centrodl1=centrodl1+1
        print(lnueva)
    else:
        print("Inserte listas válidas")
nuevaListaCentro([1,0,2],[1,2,3])