
matriz = []

for i in range(3):
     matriz.append([])
     for j in range(2):
        if i == j:
            matriz[i].append(1)
        else:
            matriz[i].append((i+1)**2)


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print ("\n")
    