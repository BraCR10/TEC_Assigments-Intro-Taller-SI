
def largoNum(num):#Funcion del largo
    if isinstance(num,int):
        if num==0:#Validacion
            return 1
        else:
            num=abs(num)
            cont=0
            while num!=0:
                num=num//10#Elimina el ultimo numero
                cont+=1#Contador
            return cont
    else:
        return 'Deben ser enteros'


def PasalistaDI(num):#3456 [5,6] 0
    num=abs(num)
    if type(num)==int:
        if num==0:
            return [0]
        else:
            listaNueva=[]#definiendo una lista vacia, para almacenar los elementos del numero
            #listaNueva  num
            # []        3456
            # [6]       345
            # [5,6]     34
            # [4,5,6]   3
            #[3,4,5,6]  0
            
            while num!=0:#3456si 345si 34si 3si 0x
                listaNueva=[num%10]+listaNueva#Insercion al inicio
                #listaNueva=[6]+[]=[6]
                #listaNueva=[5]+[6]=[5,6]
                #listaNueva=[4]+[5,6]=[4,5,6]
                #listaNueva=[3]+[4,5,6]=[3,4,5,6]
                num=num//10#3456 345 34 3 0
            return listaNueva#[3,4,5,6]
    else:
        print("El parametro no es un numero")
def funcionQuiz(num1,num2):
    if type(num2)==int and type(num1)==int:
        if largoNum(num1)==largoNum(num2):
            num1=abs(num1)
            num2=abs(num2)
            num2=PasalistaDI(num2)
            num1=PasalistaDI(num1)
            nuevaLista=[]
            for i in range(len(num1)):#Lista con numeros
                nuevaLista+=[num1[i]]
                nuevaLista+=[num2[i]]
            for i in range(len(nuevaLista)):#Lista con str
                nuevaLista[i]=str(nuevaLista[i])
            cadena=''
            for i in nuevaLista:#Solo una str
                cadena+=i
            print(cadena)
        else:
            print('Datos incorrectos')
    else:
        print('Datos incorrectos')

