#!/usr/bin/env python3
# coding: utf-8

from os import system
from matrizes.matriz import le_matriz, soma_matriz, transposta_matriz, imprimir_matriz

# Limpa tela
system("cls || clear")

# Construa as Matrizes A e B
matriz_a = le_matriz()
matriz_b = le_matriz()

# Soma as matrizes
matriz_soma = soma_matriz(matriz_a, matriz_b)

# Aplica a Transposta à matriz_soma
matriz_transposta = transposta_matriz(matriz_soma)

# Limpa tela
system("cls || clear")

# Imprime a matriz transposta
imprimir_matriz(matriz_transposta, "Matriz A+B Transposta")
