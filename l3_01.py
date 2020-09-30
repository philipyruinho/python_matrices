from matrizes.matriz import multiplica_matriz, imprimir_matriz

# cria as matrizes A e B
A = [[2, 1], [-3, 4]]
B = [[0, -1], [2, 5]]

# multiplica as matrizes A e B
resultado = multiplica_matriz(A, B)

# imprime a matriz A*B
imprimir_matriz(resultado, "Matriz A * B")
