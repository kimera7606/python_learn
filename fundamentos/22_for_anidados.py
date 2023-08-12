matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz[1])
print(matriz[2][0])

for i in matriz:
    print(i)
    for x in i:
        print(x)

for fila in matriz:
    print(fila)
    for columna in fila:
        print(columna)


