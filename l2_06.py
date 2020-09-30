#!/usr/bin/env python3
# coding: utf-8

from os import system
from matrizes.matriz import cria_matriz, multiplica_matriz, imprimir_matriz

# Limpa tela
system("cls || clear")

# Construa as Matrizes A e B
matriz_a = cria_matriz()
matriz_b = cria_matriz()

# Multiplica Matriz A x B
matriz_a_x_b = multiplica_matriz(matriz_a, matriz_b)


# Limpa tela
system("cls || clear")

# Imprime a matriz transposta
imprimir_matriz(matriz_a_x_b, "Matriz A x B")
