def lenNum(num):
    if num==0:
        print(1)
    else:
        cont=0
        while num!=0:
            temp=num%10
            num=num//10
            cont+=1
    print(f'La cantidad de digitos son: {cont}')

lenNum(12)