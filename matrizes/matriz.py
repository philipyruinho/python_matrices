#!/usr/bin/env python3
# coding: utf-8
import sys


def le_matriz():
    """Recebe a dimensao da matriz"""
    lin = int(input("Digite o número de linhas da matriz: "))
    col = int(input("Digite o número de colunas da matriz: "))
    return lin, col


def cria_matriz(lin, col):
    """Cria uma matriz"""
    matriz = []
    for l in range(lin):
        linha = []
        for c in range(col):
            valor = int(input(f"Informe o elemento [{l}][{c}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def cria_matriz_nula(lin, col):
    """Cria matriz nula"""
    MN = []
    for l in range(lin):
        linha = []
        for c in range(col):
            valor = 0
            linha.append(valor)
        MN.append(linha)
    return MN


def soma_matriz(MA, MB):
    """Soma duas matrizes"""
    linA, colA = len(MA), len(MA[0])
    linB, colB = len(MB), len(MB[0])
    if linA != linB or colA != colB:
        print("Matrizes com dimensões diferentes, não é possível somar.")
        sys.exit()
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
        print("Matrizes com dimensões diferentes, não é possível subtrair.")
        sys.exit()
    MC = []
    for l in range(linA):
        linha = []
        for c in range(colA):
            valor = MA[l][c] - MB[l][c]
            linha.append(valor)
        MC.append(linha)
    return MC


def mult_matriz(A, B):
    """Multiplica duas matrizes."""
    lin = len(A)
    col = len(A[0])
    MM = cria_matriz_nula(lin, col)
    for l in range(lin):
        for c in range(col):
            valor = 0
            for k in range(len(B[0])):
                valor = valor + A[l][k] * B[k][c]
            MM[l][c] = valor
    return MM


def transposta_matriz(M):
    """Calcula a transposta de uma matriz."""
    lin = len(M[0])
    col = len(M)
    MT = []
    for l in range(lin):
        linha = []
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


def inverter_matriz(A):
    """Retorna a matriz passada invertida"""
    n = len(A)
    IM = identidade_matriz(n)
    indices = list(range(n))
    for fd in range(n):
        fd_scaler = 1.0 / A[fd][fd]
        for j in range(n):
            A[fd][j] *= fd_scaler
            IM[fd][j] *= fd_scaler
        for i in indices[0:fd] + indices[fd + 1:]:
            cr_scaler = A[i][fd]
            for j in range(n):
                A[i][j] -= cr_scaler * A[fd][j]
                IM[i][j] -= cr_scaler * IM[fd][j]
    return IM


def valida_matriz_determinante(lin, col):
    """verifica se é uma matriz quadrada"""
    if lin != col:
        print("As dimensões da matriz são incompatíveis, somente matrizes quadradas são aceitas!")
        sys.exit()
    else:
        return lin, col


def det_matriz(matriz):
    """Calcula a determinante de uma matriz"""
    lin = len(matriz)
    col = len(matriz[0])
    if lin == 1:
        determinante = matriz[0][0]
        return determinante
    elif lin == 2:
        principal, secundaria = 1, 1
        for i in range(lin):
            for j in range(col):
                if i == j:
                    principal *= matriz[i][j]
                else:
                    secundaria *= matriz[i][j]
        determinante = principal - secundaria
        return determinante
    elif lin == 3:
        principais = 0
        for i in range(lin):
            soma = 1
            for j in range(col):
                k = (i + j) % col
                soma *= matriz[j][k]
            principais += soma
        secundarias = 0
        for i in range(lin):
            subtracao = 1
            for j in range(col):
                k = (i - j) % col
                subtracao *= matriz[j][k]
            secundarias -= subtracao
        determinante = secundarias + principais
        return determinante
    else:
        sub_matriz = []
        for i in range(lin - 1):
            l = []
            for j in range(col - 1):
                l.append(0)
            sub_matriz.append(l)
        aux, determinante = 0, 0
        for i in range(lin):
            l = -1
            for j in range(col):
                c = 0
                for k in range(col):
                    if aux != j and k != i:
                        sub_matriz[l][c] = matriz[j][k]
                        c += 1
                l += 1
            determinante += (-1) ** (aux + i) * \
                matriz[aux][i] * det_matriz(sub_matriz)
        return determinante


def cof_matriz(matriz):
    """Calcula o cofator de uma matriz"""
    lin = int(input("\nInforme a linha do elemento que deseja calcular o cofator: "))
    col = int(input("Informe a coluna do elemento que deseja calcular o cofator: "))
    if len(matriz) >= 2:
        sub_matriz = []
        for i in range(len(matriz) - 1):
            l = []
            for j in range(len(matriz[0]) - 1):
                l.append(0)
            sub_matriz.append(l)
        cofator, l = 0, 0
        for j in range(len(matriz[0])):
            c = 0
            for k in range(len(matriz[0])):
                if lin != j and k != col:
                    sub_matriz[l][c] = matriz[j][k]
                    c += 1
            l += 1 if lin != j else 0
        cofator += (-1) ** (lin + col) * det_matriz(sub_matriz)
        return cofator

    else:
        print("\nNão é possível calcular o cofator.")
        sys.exit()


def imprime_matriz(matriz, nome):
    """Imprime a matriz linha por linha"""
    print(f"Matriz {nome}\n")
    for l in matriz:
        print("{}".format(l))
    print("\n")
