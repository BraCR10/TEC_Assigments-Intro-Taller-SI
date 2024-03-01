def leerPaises():
    
    paises = open('Lectura de archivos Python\Paises.txt', 'r')
    listaPaises=paises.readlines()
    '''for linea in paises:
        pais = linea.split(";")#['999', 'Costa Rica']
        pais[1] = pais[1].replace("\n", "")
        listaPaises+=[pais]'''
    paises.close()
    print(listaPaises)

print()
print()
print()
leerPaises()
print()
print()
print()




