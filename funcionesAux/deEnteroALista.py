def Pasalista(num): #234  [2,3,4] 0 [0]  
    num=abs(num)#234
    if isinstance (num,int):
        if num==0:
            return [0]
        else:
            listaNueva=[]#definiendo un lista vacia,almacenar los elementos
            while num!=0:#234 23 2 0
                #             #4 [4]+[]=[4] 3 [3]+[4]=[3,4] 2 [2]+[3,4]=[2,3,4]
                listaNueva= [num%10]+listaNueva
                num=num//10#234 23 2 0
            return(listaNueva)#[2,3,4]
    else:
         print(" No es entero")