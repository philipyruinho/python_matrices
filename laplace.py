#!/usr/bin/env python3
# coding: utf-8
from os import system
import sys
from matrizes.matriz import (
    le_matriz,
    valida_matriz_determinante,
    cria_matriz,
    cof_matriz,
    det_matriz,
    imprime_matriz,
)


def menu():
    system("cls || clear")
    print(
        """
    ███╗   ███╗ █████╗ ████████╗██████╗ ██╗███████╗    ██╗   ██╗██████╗
    ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚══███╔╝    ██║   ██║╚════██╗
    ██╔████╔██║███████║   ██║   ██████╔╝██║  ███╔╝     ██║   ██║ █████╔╝
    ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ███╔╝      ╚██╗ ██╔╝ ╚═══██╗
    ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║███████╗     ╚████╔╝ ██████╔╝
    ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝      ╚═══╝  ╚═════╝
    
    [ 1 ] Calcular a determinante de uma matriz
    [ 2 ] Calcular o cofator de uma matriz
    [ 3 ] Vazar na brachiaria
    """
    )
    escolha = int(input("Escolha uma opção: "))
    return exec_menu(escolha)


def exec_menu(escolha):
    system("cls || clear")
    if escolha == 1:
        lin, col = le_matriz()
        lin, col = valida_matriz_determinante(lin, col)
        ma = cria_matriz(lin, col)
        det_ma = det_matriz(ma)
        imprime_matriz(ma, "Informada")
        print(f"O determinante é {det_ma}")
    elif escolha == 2:
        lin, col = le_matriz()
        lin, col = valida_matriz_determinante(lin, col)
        ma = cria_matriz(lin, col)
        cof_ma = cof_matriz(ma)
        imprime_matriz(ma, "Informada")
        print(f"O cofator é {cof_ma}")
    else:
        sys.exit()


if __name__ == "__main__":
    menu()
