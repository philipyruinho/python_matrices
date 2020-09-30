from matrizes.matriz import soma_matriz, multiplica_matriz, imprimir_matriz

# cria as matrizes
A = [[2, 1], [-3, 4]]
B = [[0, -1], [2, 5]]
C = [[3, 0], [6, 1]]

# soma as matrizes A * B
soma = soma_matriz(A, B)

# multiplica a matriz AB * C
multiplica = multiplica_matriz(soma, C)

# imprime a matriz A+B * C
imprimir_matriz(multiplica, "Matriz (A + B) * C")