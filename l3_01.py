from matrizes.matriz import mult_matriz, imprime_matriz

# cria as matrizes A e B
A = [[2, 1], [-3, 4]]
B = [[0, -1], [2, 5]]

# multiplica as matrizes A e B
resultado = mult_matriz(A, B)

# imprime a matriz A*B
imprime_matriz(resultado, "Matriz A * B")
