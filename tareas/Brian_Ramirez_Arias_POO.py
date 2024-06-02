class Pasillo:
    def __init__(self,codPasillo,nombre):#Constructor
        self.codPasillo=codPasillo
        self.nombre=nombre
        
    def insertarPasillo(self,lista):#Inserta a la lista un pasillo nuevo
        for obj in lista:
            if obj.codPasillo==self.codPasillo:
                print( '\nEl codigo ya existe')
                return None
        archivoPasillo = open("Pasillo.txt", "a")
        archivoPasillo.write(f'\n\n###############################################################')
        archivoPasillo.write(f'\nCodigo: {self.codPasillo}')
        archivoPasillo.write(f'\nNombre: {self.nombre}')
        archivoPasillo.close()
        lista+=[self]
        print( '\nSe ha añadido el pasillo')
        
    def imprimirPasillo(self):
        print('\nCodigo: ',self.codPasillo)
        print('Nombre: ',self.nombre)
        
    def buscarPasillo(self,lista):
        for obj in range(len(lista)):         
            if lista[obj].codPasillo==self.codPasillo:
                print('\n El pasillo ha sido encontrado, aqui esta la informacion:')
                return lista[obj].imprimirPasillo()
        print('\nNo se ha encontrado ningun pasillo con ese codigo!')
        return 'No se ha encontrado'
            
                
                
    
class ProductosPasillo:
    def __init__(self,codPasillo,codProducto,nombre):
        self.nombre=nombre
        self.codPasillo=codPasillo
        self.codProducto=codProducto
    
    def insertarProducto(self,lista):
        for obj in lista:
            if obj.codProducto==self.codProducto:
                print( '\nEl codigo ya existe')
                return None
        archivoProductosPasillo = open("ProductosPasillo.txt", "a")
        archivoProductosPasillo.write(f'\n\n###############################################################')
        archivoProductosPasillo.write(f'\nCodigo pasillo: {self.codPasillo}')
        archivoProductosPasillo.write(f'\nCodigo producto: {self.codProducto}')
        archivoProductosPasillo.write(f'\nNombre: {self.nombre}')
        archivoProductosPasillo.close()
        lista+=[self]
        print( '\nSe ha añadido el producto')
        
    def imprimirProducto(self):
        print('\nCodigo pasillo: ',self.codPasillo)
        print('Codigo producto: ',self.codProducto)
        print('Nombre: ',self.nombre)
        
    def buscarProducto(self,lista):
        for obj in range(len(lista)):         
            if lista[obj].codProducto==self.codProducto: 
                print('\n El producto ha sido encontrado, aqui esta la informacion:')
                return lista[obj].imprimirProducto()
        print('\nNo se ha encontrado ningun producto con ese codigo ')
        return 'No se ha encontrado'
        

                
            
            
    
class Marcas:
    def __init__(self,codPasillo,codProducto,codMarca,nombre,CantidadGondola,precio):
        self.codPasillo=codPasillo
        self.codProducto=codProducto
        self.codMarca=codMarca
        self.nombre=nombre
        self.CantidadGondola=CantidadGondola
        self.precio=precio
        
    def insertarMarca(self,lista):
        for obj in lista:
            if obj.codMarca==self.codMarca:
                print( '\nEl codigo ya existe')
                return None
            
        archivoMarcas = open("Marcas.txt", "a")
        archivoMarcas.write(f'\n\n###############################################################')
        archivoMarcas.write(f'\nCodigo pasillo: {self.codPasillo}')
        archivoMarcas.write(f'\nCodigo producto: {self.codProducto}')
        archivoMarcas.write(f'\nCodigo marca: {self.codMarca}')
        archivoMarcas.write(f'\nNombre: {self.nombre}')
        archivoMarcas.write(f'\nCantidad Gondola: {self.CantidadGondola}')
        archivoMarcas.write(f'\nPrecio: {self.precio}')
        archivoMarcas.close()
        lista+=[self]
        print( '\nSe ha añadido la marca')
    def imprimirMarca(self):
        print('\nCodigo pasillo: ',self.codPasillo)
        print('Codigo producto: ',self.codProducto)
        print('Codigo marca: ',self.codMarca)
        print('Nombre: ',self.nombre)
        print('Cantidad Gondola: ',self.CantidadGondola)
        print('Precio: ',self.precio)
        
    def buscarMarca(self,lista):
        for obj in range(len(lista)):         
            if lista[obj].codMarca==self.codMarca: 
                print('\n La marca ha sido encontrado, aqui esta la informacion:')
                return lista[obj].imprimirMarca()
        print('\nNo se ha encontrado ninguna marca con ese codigo  ')
        return 'No se ha encontrado' 
    
    def buscarPrecio(self,lista):
        for obj in range(len(lista)):         
            if lista[obj].codMarca==self.codMarca: 
                print('\n El precio de la marca es de :',lista[obj].precio)
                return lista[obj].precio
        print('\nNo se ha encontrado ninguna marca con ese codigo  ')
        return 'No se ha encontrado' 
    def cantidadMarca(self,lista):
        for obj in range(len(lista)):         
            if lista[obj].codMarca==self.codMarca: 
                print('\n La cantidad de la marca es de :',lista[obj].CantidadGondola)
                return lista[obj].precio
        print('\nNo se ha encontrado ninguna marca con ese codigo  ')
        return 'No se ha encontrado' 
#Creacion de lista  
PasilloLista=[]
ProductosPasilloLista=[]
MarcasLista=[]
#Creacion de archivos
archivoPasillo = open("Pasillo.txt", "w")
archivoPasillo.write('Los pasillos registrados: ')
archivoPasillo.close()
archivoProductosPasillo = open("ProductosPasillo.txt", "w")
archivoProductosPasillo.write('Los productos registrados: ')
archivoProductosPasillo.close()
archivoMarcas = open("Marcas.txt", "w")
archivoMarcas.write('Las marcas registrados: ')
archivoMarcas.close()
while True:
    print('\nEscoja una opcion para ver mas acciones!')
    print('1-Pasillos')
    print('2-Productos en un pasillos')
    print('3-Marcas')
    print('4-Salir')
    opcion=input('\nEscriba el digito correspondiente: ')
    if opcion=='1':
        print('Escoja una opcion!')
        print('1-Insertar un pasillo')
        print('2-Imprimir pasillos')
        print('3-Buscar un pasillo')
        print('4-Salir')
        opcion=input('\nEscriba el digito correspondiente: ')
        if opcion=='1':
            codPasillo=input('\nEscriba el codigo de pasillo: ')
            nombre=input('Escriba el nombre del pasillo: ')
            nuevoPasillo=Pasillo(codPasillo,nombre)
            nuevoPasillo.insertarPasillo(PasilloLista)
            temp=input('\nPresione enter para continuar ')
        elif opcion=='2':
            for obj in range(len(PasilloLista)):#Itera por cada objeto en la lista
                PasilloLista[obj].imprimirPasillo()
            if len(PasilloLista)==0:
                print('\nNo se ha almacenado ningun pasillo')
            temp=input('\nPresione enter para continuar ')
        elif opcion=='3':
            pasilloBuscado=input('\nEscriba el codigo de pasillo a buscar: ')
            buscar= Pasillo(pasilloBuscado,'buscar')#Obj para usar el metodo buscar
            buscar.buscarPasillo(PasilloLista)
            temp=input('\nPresione enter para continuar ')
    elif opcion=='2':
        print('Escoja una opcion!')
        print('1-Insertar producto')
        print('2-Imprimir productos')
        print('3-Buscar un producto')
        print('4-Salir')
        opcion=input('\nEscriba el digito correspondiente: ')
        if opcion=='1':
            codPasillo=input('\nEscriba el codigo del pasillo a insertar el producto: ')
            buscar= Pasillo(codPasillo,'buscar')#Obj para usar el metodo buscar
            if buscar.buscarPasillo(PasilloLista)=='No se ha encontrado':
                print('\nNo se puede insertar el producto')
            else:
                codProducto=input('\nEscriba el codigo del producto: ')
                nombre=input('Escriba el nombre del producto: ')
                nuevoProduto=ProductosPasillo(codPasillo,codProducto,nombre)
                nuevoProduto.insertarProducto(ProductosPasilloLista)
            temp=input('\nPresione enter para continuar ')
        elif opcion=='2':
            for obj in range(len(ProductosPasilloLista)):#Itera por cada objeto en la lista
                ProductosPasilloLista[obj].imprimirProducto()
            if len(ProductosPasilloLista)==0:
                print('\nNo se ha almacenado ningun producto')
            temp=input('\nPresione enter para continuar ')
        elif opcion=='3':
            codProducto=input('\nEscriba el codigo del producto: ')
            buscar=ProductosPasillo('00',codProducto,'buscar')#Obj para usar el metodo buscar
            buscar.buscarProducto(ProductosPasilloLista)
            temp=input('\nPresione enter para continuar ')
    elif opcion=='3':
        print('Escoja una opcion!')
        print('1-Insertar marca')
        print('2-Imprimir marca')
        print('3-Buscar un marca')
        print('4-Buscar precio')
        print('5-Buscar cantidad')
        print('4-Salir')
        opcion=input('\nEscriba el digito correspondiente: ')
        if opcion=='1':
            codPasillo=input('\nEscriba el codigo del pasillo a insertar la marca: ')
            codProducto=input('\nEscriba el codigo del producto a insertar la marca: ')
            buscarPasillo= Pasillo(codPasillo,'buscar')#Obj para usar el metodo buscar
            buscarProducto= ProductosPasillo(codPasillo,codProducto,'buscar')#Obj para usar el metodo buscar
            if buscarPasillo.buscarPasillo(PasilloLista)=='No se ha encontrado' or buscarProducto.buscarProducto(ProductosPasilloLista)=='No se ha encontrado':
                print('\nNo se puede insertar la marca!')
            else:
                codMarca=input('\nEscriba el codigo de la marca: ')
                nombre=input('Escriba el nombre de la marca: ')
                CantidadGondola=input('Escriba la cantidad gondola: ')
                precio=float(input('Escriba el precio: '))
                nuevaMarca=Marcas(codPasillo,codProducto,codMarca,nombre,CantidadGondola,precio)
                nuevaMarca.insertarMarca(MarcasLista)
            temp=input('\nPresione enter para continuar ')
        elif opcion=='2':
            for obj in range(len(MarcasLista)):#Itera por cada objeto en la lista
                MarcasLista[obj].imprimirMarca()
            if len(MarcasLista)==0:
                print('\nNo se ha almacenado ningun producto')
        elif opcion=='3':
            codMarca=input('\nEscriba el codigo de la marca: ')
            buscar=Marcas('00','00',codMarca,'buscar','00','00')#Obj para usar el metodo buscar
            buscar.buscarMarca(MarcasLista)
            temp=input('\nPresione enter para continuar ')
        elif opcion=='4':
            codMarca=input('\nEscriba el codigo de la marca: ')
            buscar=Marcas('00','00',codMarca,'buscar','00','00')#Obj para usar el metodo buscar
            buscar.buscarPrecio(MarcasLista)
            temp=input('\nPresione enter para continuar ')
        elif opcion=='5':
            codMarca=input('\nEscriba el codigo de la marca: ')
            buscar=Marcas('00','00',codMarca,'buscar','00','00')#Obj para usar el metodo buscar
            buscar.cantidadMarca(MarcasLista)
            temp=input('\nPresione enter para continuar ')          
    elif opcion=='4':
        print('Gracias por usar el programa!')
        break