from matrizes.matriz import soma_matriz, sub_matriz, multiplica_matriz, transposta_matriz, imprimir_matriz, identidade_matriz

# cria as matrizes
A = [[2, 1], [-3, 4]]
B = [[0, -1], [2, 5]]
C = [[3, 0], [6, 1]]
I = identidade_matriz(2)

# aplica a transposta a C
CT = transposta_matriz(C)

# subtrai matriz B - C transposta
BCT = sub_matriz(B, CT)

# soma matriz A + (B-CT)
A_BCT = soma_matriz(A, BCT)

# multiplica a matriz
resultado = multiplica_matriz(A_BCT, I)

# imprime a matriz
imprimir_matriz(resultado, "Resultado")