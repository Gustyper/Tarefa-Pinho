import numpy as np
import numpy.random

import parte1
import parte2

parte1.questao1()
parte1.questao2()
parte1.questao3()

parte2.questao4()
parte2.questao5()


def questao6():
    ###################
    
    print("Questão 6", end = "\n\n")
    
    A = np.array([0, 2, 3])
    B = np.array([4, 5, 6])
    
    produto_vetorial = np.cross(A, B)
    
    print("Vetor A:", A)
    print("Vetor B:", B)
    print("Produto vetorial AxB:", produto_vetorial)
    
    
    ###################

def questao7():
    print("Questão 7", end = "\n\n")

    matriz_3x3 = np.array([[1, 0, 3], [0, 3, 2], [6, 2, 0]])
    print("Matriz 3x3:")
    print(matriz_3x3)

    identity = np.identity(3)
    print("Identidade:")
    print(identity)

    determinante = np.linalg.det(matriz_3x3).round()
    print("Determinante da matriz:")
    print(determinante)

    # Calculando a inversa da matriz
    inversa = np.linalg.inv(matriz_3x3)
    print("Matriz Inversa:")
    print(inversa)

    # Multiplicando a matriz original pela sua inversa
    produto = np.matmul(matriz_3x3, inversa)
    print("Produto da matriz pela sua inversa:")
    print(produto)

    # Verificando se o produto é igual à matriz identidade
    if np.allclose(produto, identity):
        print("O produto é igual à identidade.")
    else:
        print("O produto não é igual à identidade.")




questao6()
questao7()













