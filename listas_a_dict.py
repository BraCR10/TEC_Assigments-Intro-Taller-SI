lista=[['1','Juan','M1','1'],['2','Jose','M2','0']]
print(lista)
for i in range(len(lista)):
    for j in range(len(lista[i])//2):
        lista[i]+=[(lista[i][0],lista[i][1])]
        lista[i]= lista[i][2:]
    lista[i]=dict(lista[i])
print(lista)

for i in range(len(lista)):
    lista+=[(i+1,lista[0])]
    lista=lista[1:]

lista=dict(lista)
print(lista)

print(lista[1])
print(lista[1]['M1'])
print(lista[2])
print(lista[2]['M2'])