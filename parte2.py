import numpy as np
import numpy.random


def questao4():
    
    print("Questão 4", end = "\n\n")

    arr_random = np.random.randint(10, size=10)
    print(arr_random, end = "\n\n")

    arr_random_2 = np.random.randint(10, size=10)
    print(arr_random_2, end = "\n\n")

    arr_junto = np.intersect1d(arr_random, arr_random_2)
    print(arr_junto, end = "\n\n")


    indices_1 = []
    indices_2 = []

    for i in range(len(arr_random)):
        for j in range(len(arr_random_2)):
            if arr_random[i] == arr_random_2[j]:
                indices_1.append(i)
                indices_2.append(j)


    indices_1 = np.unique(indices_1)
    indices_2 = np.unique(indices_2)


    print("Índices da primeira:", indices_1)
    print("Índices da segunda:", indices_2, end="\n\n")


    novo_array = arr_random

    for i in arr_junto:
        novo_array = np.delete(novo_array, np.where(novo_array == i))

    print(novo_array)

    return arr_random, arr_random_2


    ###################

def questao5(arr_random, arr_random_2 = questao4()):
    print("Questão 5", end = "\n\n")
    
    array_horizontal = np.hstack((arr_random, arr_random_2))
    print(array_horizontal)
    
    print("Média: ", np.average(array_horizontal))
    print("Desvio padrão: ", np.std(array_horizontal))
    print("Variância: ", np.var(array_horizontal))
    
    for i in range(len(array_horizontal)):
        if array_horizontal[i] % 2 == 1:
            array_horizontal[i] = -1
        else:
            array_horizontal[i] = 1
            
    print(array_horizontal)