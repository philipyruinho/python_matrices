#!/usr/bin/env python3
# coding: utf-8


def cria_matriz():
    """Recebe a dimensao e cria uma matriz"""
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    matriz = []
    for l in range(lin):
        linha = []
        for c in range(col):
            valor = int(input(f"Informe o elemento [{l}][{c}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def cria_matriz_nula(num_linhas, num_colunas):
    """Cria matriz nula"""
    MN = []
    for l in range(num_linhas):
        linha = []
        for c in range(num_colunas):
            valor = 0
            linha.append(valor)
        MN.append(linha)
    return MN


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


def sub_matriz(MA, MB):
    """Subtrai duas matrizes"""
    linA, colA = len(MA), len(MA[0])
    linB, colB = len(MB), len(MB[0])
    if linA != linB or colA != colB:
        raise "Matrizes com dimensões diferentes, não é possível subtrair."
    MC = []
    for l in range(linA):
        linha = []
        for c in range(colA):
            valor = MA[l][c] - MB[l][c]
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


def identidade_matriz(N):
    """Cria matriz quadrada identidade"""
    MI = []
    for l in range(N):
        linha = []
        for c in range(N):
            if l == c:
                valor = 1
            else:
                valor = 0
            linha.append(valor)
        MI.append(linha)
    return MI


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


def inverter_matriz(A):
    """Retorna a matriz passada invertida"""
    n = len(A)
    IM = identidade_matriz(n)
    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1.0 / A[fd][fd]
        for j in range(n):
            A[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd+1:]: 
            crScaler = A[i][fd]
            for j in range(n):
                A[i][j] -= crScaler * A[fd][j]
                IM[i][j] -= crScaler * IM[fd][j]
    return IM


def imprimir_matriz(matriz, nome):
    """Imprime a matriz linha por linha"""
    print(f"Matriz {nome}\n")
    for l in matriz:
        print("{}".format(l))
    print("\n")