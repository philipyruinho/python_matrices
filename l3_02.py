from matrizes.matriz import soma_matriz, mult_matriz, imprime_matriz

# cria as matrizes
A = [[2, 1], [-3, 4]]
B = [[0, -1], [2, 5]]
C = [[3, 0], [6, 1]]

# soma as matrizes A * B
soma = soma_matriz(A, B)

# multiplica a matriz AB * C
multiplica = mult_matriz(soma, C)

# imprime a matriz A+B * C
imprime_matriz(multiplica, "Matriz (A + B) * C")
