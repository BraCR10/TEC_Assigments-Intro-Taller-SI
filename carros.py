#definicion de las clases
# hacer una clase carros con los siguiente atributos
#placa,marca,modelo,anno,kms, gasolina
#metodo imprimir

#init es equivalente a un constructor, no se llama igual que la clase
#python solo permite un constructor
#metodo especial que permite inicializar los atributos de la clase



class Carros:       #23
    #Constructor
    def _init_(self,placa,marca,modelo,anno,kms):
        self.numPlaca =placa #23
        self.marca =marca
        self.modelo =modelo
        self.anno =anno
        self.kms =kms
        self.gasolina=0

               

    def Imprimir(self):
        print("Placa ",self.numPlaca)
        print("Marca ",self.marca)
        print("Modelo ",self.modelo)
        print("Año ",self.anno)
        print("Kms ",self.kms)
        print("gasolina",self.gasolina)

    def ImprimirGas(self):
        print("gas ",self.gasolina)

    def CargarTanque(self,gasolina):
        self.gasolina = self.gasolina + gasolina #0+20=20

    def Viaje(self,gas,recorrido):
        self.gasolina = self.gasolina - gas #30-20=10
        self.kms=self.kms+recorrido         #10+20=30

        
#constructor es un metodo especial, que permite dar valor a los atributos
#python init
# c++ o java, un monton constructores como se llaman igual que la clase
#los constructores pueden tener varios parametros, diferente cantidad
# se puede hacer una combinacion de diferentes parametros, de diferente tipo
# de diferente orden o diferente cantidad
# carros ( placa, gasolina  int, int
# carros ( modelo, gasolina string, int toyota,34
#x carros ( anno, gasolina int,int NO SE PUEDE igual en cantidad y tipo de parametros
# carros ( gasolina,modelo int,string 34,toyota


#programa
carros = []   #lista de carros

opcion = " "
while opcion.upper() != "S" :   #se sale hasta que "S"
    print("   1.  Ingresar carros")
    print("   2.  Imprimir carros")
    print("   3.  Cargar Tanque")
    print("   4.  Viaje")
    print("   S.  Salir")
    print("")
    
    opcion = input("   Digite la opcion y presione ENTER -->")
    if opcion == "1" :
        p = Carros()#instancia
        numPlaca = input("Digite el numero de placa:")#23
        marca = input("Digite la marca :")
        modelo = input("Digite el modelo :")
        anno = input("Digite el anno :")
        kms = int(input("Digite los kms :"))
        #carros.append(p)#sin init SOLO este
        #***************************
        #USO PARA INIT
        p._init_(numPlaca,marca,modelo,anno,kms)
        carros.append(p)
                  #23
        #23,toyota,yaris,2013,40
        #123,nissan,xxx,2015,45
         
    elif opcion == "2" :
        print("Lista de Carros :")
        print("-------------------")
        for i in range(len(carros)):
            carros[i].Imprimir()
            print("-------------------")
       
        
    elif opcion == "3" :
        #buscar la placa y despues si existe, cargar gasolina
        placaBuscada = input("Ingrese la placa para cargar :")#123
        encontro = -1       # no existe
        for i in range(len(carros)):
            if carros[i].numPlaca==placaBuscada: #23==123x 123=123si (posicion1)
                encontro = i#1
            
        if encontro != -1 :#1
            gasolina=int(input(" Digite la gasolina a cargar: "))#20
            carros[encontro].CargarTanque(gasolina)#20
           
        else :
           print("La placa digitada no existe !!!")
           
    elif opcion == "4" :#[123,10,gas30
        #buscar la placa y despues si existe, realizar viaje
        placaBuscada = input("Ingrese la placa para viajar :")#123
        encontro = -1       # no existe
        for i in range(len(carros)):
            if carros[i].numPlaca== placaBuscada:
                encontro=i
                
        if encontro != -1 :
            consumo=int(input("Digite  el consumo de gasolina"))#20
            if carros[encontro].gasolina <= consumo:
               print("No se puede viajar")
            else:
               Kilometros=int(input("Ingrese cantidad de Kilometros: "))#20
               carros[encontro].Viaje(consumo,Kilometros)
            
        else :
           print("La placa digitada no existe !!!")
            
  
        
    else :
        print("Gracias por usar el programa !!!")
        print("Fin")
