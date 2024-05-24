#defincion de una clase
import os
class Cuenta:
    NumeroCuenta=" "
    saldo=0
    Tipo="AC"
    referenciacliente=""
    referenciasucursal=""

    #metodos
    def Depositar(self,p):
        self.saldo=self.saldo+p


    def ImprimirSaldo(self):
        print(" El saldo de la cuenta es: ", self.saldo)


class Cliente:
    Identificacion=""
    nombre=""
    direccion=""
    telefono=""

    #metodos
    def Imprimircliente(self):
        print(" Identificacion: ",self.Identificacion)
        print(" Nombre: ", self.nombre)
        print(" Direccion: ", self.direccion)
        print(" Telefono: ", self.telefono)

#Programa
Cuentas=[]    #lista de cuenta
Clientes=[]   #lista de clientes

#menu
opcion=" "
os.system('cls')
while opcion.upper()!="S":
    print("1. Ingresar clientes")
    print("2. Imprimir clientes")
    print("3. Crear cuenta")
    print("4. Deposito")
    print("5. Imprimir saldo")
    print("6. Imprimir lista de cuentas")
    print("S. Salir")
    print(" ")
    print("---------------------------------------")
    opcion=input(" Digite la opcion y presione ENTER  ")
    if opcion=="1":
        #instancia
        p=Cliente()# Tipo de la clase
        p.Identificacion=input(" Digite la identificacion: ")
        p.nombre=input(" Digite el nombre: ")
        p.direccion=input(" Digite la direccion: ")
        p.telefono=input(" Digite el telefono: ")
        Clientes.append(p)
    elif opcion=="2":
        print("Lista de Clientes")
        print("---------------------------------------")
        for i in range(len(Clientes)):
            Clientes[i].Imprimircliente()
    elif opcion=="3":
        #instancia
        c=Cuenta()
        c.NumeroCuenta=input(" Digite el numero de cuenta")
        c. referenciacliente=input("Digite el cliente dueño de la cuenta")
        Cuentas.append(c)
        print("---------------------------------------")
    elif opcion=="4":
        
        print("---------------------------------------")
    elif opcion=="5":
        
    elif opcion=="6":
       
    else:
        break
    input()
        
        
        
   
    
        









        









        
