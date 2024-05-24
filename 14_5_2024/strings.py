cadena='ana'
cadena=cadena.capitalize()
#print(cadena)

cadena='casa'
cadena=cadena.upper()
#print(cadena)

cadena='CASA'
cadena=cadena.lower()
#print(cadena)

cadena='Este es un ejemplo'
cadena=cadena.lower()
#print(len(cadena))

pos=cadena.find('es')
#print(pos)
#print(cadena.count('es',40,45))
def funCadenaNums(cadena):
    if type(cadena)==str:
        num=0
        for i in cadena:
            i=int(i)
            if i%2==0:
                i=1
                num=num*10+i
            else:
                num=num*10+i
        print(num)
def funCadenaNums(cadena):
    if type(cadena)==str:
        num=0
        for i in range(len(cadena)):
            temp=''.join(cadena[i])
            temp=int(temp)
            if temp%2==0:
                cadena=cadena.replace(cadena[i],'1')
        print(cadena)


#funCadenaNums('123598')

def verificadorNumeros(cadena):
    if type(cadena)==str:
        cont=0
        for i in cadena:
            if i.isdigit():
                cont+=1
        print(cont)
#verificadorNumeros('ty3s2rt')

def Sepraracion(cadena):
    cont=0
    list=[]
    lista=cadena.split(' ')
    print(lista)
    for i in lista:
        if i.isdigit():
            cont+=1
    print(cont)

#Sepraracion('56y 5 6 2 6')

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



def funCadenaNums(num):
    if type(num)==int:
        num=abs(num)
        num=PasalistaDI(num)
        cont=0
        for i in num:
            if i%2==0:
                i=1
                num[cont]=i
                cont+=1
            else:
                num[cont]=i
                cont+=1
        cadena=''
        for i in num:
            cadena+=str(i)
        print(cadena)
#funCadenaNums(123)

def vocales(cadena):
    if str==type(cadena):
        vocales=['a','A','e','E','i','I','o','O','u','U']
        cont=0
        cadenaNueva=''
        for i in range(len(cadena)):
            if cadena[i] in vocales:
                cadenaNueva+=cadena[i].capitalize()
                cont+=1
            else:
                cadenaNueva+=cadena[i]
        print(cadenaNueva,cont)

vocales('AnA va A la playA y Estamos Unidos a Ana')