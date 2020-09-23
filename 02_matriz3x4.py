print()
print("Matriz A")
print()

matriz_a = []

for i in range(3):
    matriz_a.append([])
    for j in range(4):
        if i == j:
            matriz_a[i].append(i+j)
        else:
            matriz_a[i].append(2*i - 2*j)
        
for i in range(len(matriz_a)):
    for j in range(len(matriz_a[i])):
        print(f"{matriz_a[i][j]:^3}", end="")
    print ("\n")

print()
print("Matriz B")
print()


matriz_b = []

for i in range(2):
    matriz_b.append([])
    for j in range(2):
        if i == j:
            matriz_b[i].append(i+j)
        else:
            matriz_b[i].append(2*i - 2*j)
        
for i in range(len(matriz_b)):
    for j in range(len(matriz_b[i])):
        print(f"{matriz_b[i][j]:^3}", end="")
    print ("\n")
    
print("Para que possamos somar duas matrizes A e B, elas devem ser de mesma ordem.\n\n\n")