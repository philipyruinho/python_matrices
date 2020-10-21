from matrizes.matriz import mult_matriz, imprime_matriz, inverter_matriz

# cria matriz A, inverte matriz A
A = [[2, 1], [-3, 4]]
AI = inverter_matriz(A)

# multiplica A x AI
MATRIZ_PRODUTO = mult_matriz(A, AI)

# imprime matriz
imprime_matriz(MATRIZ_PRODUTO, "Matriz A * A^-1 = In")
