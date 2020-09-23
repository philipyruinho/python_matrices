#!/usr/bin/env python3
# coding: utf-8

from os import system
from matrizes.matriz import le_matriz, soma_matriz, imprimir_matriz

# Limpa a tela
system("clear || cls")

# Constroi as matrizes
matriz_a = le_matriz()
matriz_b = le_matriz()
matriz_c = le_matriz()

# Soma as matrizes
AB = soma_matriz(matriz_a, matriz_b)
AC = soma_matriz(matriz_a, matriz_c)
ABC = soma_matriz(AB, matriz_c)

# Limpa a tela

# Imprime as matrizes
imprimir_matriz(AB, "Matriz A + B")
imprimir_matriz(AC, "Matriz A + C")
imprimir_matriz(ABC, "Matriz A + B + C")