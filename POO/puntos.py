#clases
class Punto:
    #Atributos
    x = 0 # se pueden inicializar directamente. En otros hay que utilizar un 
    y = 0 # constructor. Python es el init
    z=0
    
    #Metodo
    #self parametro que necesito python. Siempre se utiliza. No debe ser self
    #obligatoriamente
    
    def Imprima(self):#[2,3]
        print(self.x,self.y,self.z)
    
#programa
puntos = [] 
for i in range(2):
    p = Punto()#instancia, ademas es como dar permiso para que sea utilizada
               #la clase punto
    p.x = int(input("Digite la coordenada X:"))
    p.y = int(input("Digite la coordenada Y:"))
    p.z = int(input("Digite la coordenada Z:"))
    puntos.append(p)
   # puntos=[3,4,1]+puntos

for i in range(len(puntos)):
    puntos[i].Imprima() # la forma de comunicacion es por medio metodos
    #print(puntos[i])#[[2,3],[4,5]]
    #Imprima es un metodo, no recibe parametros. Se llama con .Nombre(puede parametros)
    #aquien le va aplicar el metodo.metodo()
