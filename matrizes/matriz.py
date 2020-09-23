#!/usr/bin/env python3
# coding: utf-8


def le_matriz():
    """Recebe a dimensao da matriz"""
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return cria_matriz(lin, col)


def cria_matriz(num_linhas, num_colunas):
    """Cria uma matriz"""
    matriz = []
    for l in range(num_linhas):
        linha = []
        for c in range(num_colunas):
            valor = int(input(f"Informe o elemento [{l}][{c}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def cria_matriz_nula(num_linhas, num_colunas):
    """Cria matriz nula"""
    matriz_nula = []
    for l in range(num_linhas):
        linha = []
        for c in range(num_colunas):
            valor = 0
            linha.append(valor)
        matriz_nula.append(linha)
    return matriz_nula

def soma_matriz(MA, MB):
    """Soma duas matrizes"""
    linA, colA = len(MA), len(MA[0])
    linB, colB = len(MB), len(MB[0])
    if linA != linB or colA != colB:
        raise "Matrizes com dimensões diferentes, não é possível somar."
    MC = []
    for l in range(linA):
        linha = []
        for c in range(colA):
            valor = MA[l][c] + MB[l][c]
            linha.append(valor)
        MC.append(linha)
    return MC


def transposta_matriz(M):
    """Calcula a transposta de uma matriz."""
    lin = len(M[0])
    col = len(M)
    MT=[]
    for l in range(lin):
        linha=[]
        for c in range(col):
            linha.append(M[c][l])
        MT.append(linha)
    return MT


def multiplica_matriz(A,B):
    """Multiplica duas matrizes."""
    lin = len(A)
    col = len(A[0])
    MM = cria_matriz_nula(lin, col)
    for l in range(lin) :
        for c in range(col):
            valor = 0
            for k in range(len(B[0])):
                valor = valor + A[l][k]*B[k][c]
            MM[l][c]=valor
    return MM


def imprimir_matriz(matriz, nome):
    print(f"Matriz {nome}\n")
    for l in matriz:
        print("{}".format(l))
    print("\n")