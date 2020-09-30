#!/usr/bin/env python3
# coding: utf-8

from os import system
from matrizes.matriz import cria_matriz, soma_matriz, transposta_matriz, imprimir_matriz

# Limpa tela
system("cls || clear")

# Construa as Matrizes A e B
matriz_a = cria_matriz()

# Aplica a Transposta à matriz A
matriz_at = transposta_matriz(matriz_a)

# Soma as matrizes
matriz_aat_soma = soma_matriz(matriz_a, matriz_at)

# Limpa tela
system("cls || clear")

# Imprime a matriz transposta
imprimir_matriz(matriz_a, "Matriz A")
imprimir_matriz(matriz_at, "Matriz B")
imprimir_matriz(matriz_aat_soma, "Matriz A + A Transposta")
