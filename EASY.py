import numpy as np
import numpy.random as npr


print("Questão 1", end = "\n\n")

array = np.arange(4)
array_2 = np.arange(1,5)
print(array, end = "\n\n")
print(array_2, end = "\n\n")

array_3 = array + array_2
print(array_3, end = "\n\n")


###########

print("Questão 2", end = "\n\n")

array_2d = array_3.reshape(2,2)
print(array_2d, end = "\n\n")

array_float = array_2d.astype(float)
print(array_float, end = "\n\n")

array_float = np.transpose(array_float)
print(array_float, end = "\n\n")


#############

print("Questão 3", end = "\n\n")

array_4 = np.array([[1,2], [3,4]])
print(array_4, end = "\n\n")

array_mult = array_2d * array_4
print(array_mult, end = "\n\n")

############

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


###################

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


###################

print("Questão 6", end = "\n\n")

A = np.array([0, 2, 3])
B = np.array([4, 5, 6])

produto_vetorial = np.cross(A, B)

print("Vetor A:", A)
print("Vetor B:", B)
print("Produto vetorial AxB:", produto_vetorial, end = "\n\n")


###################

print("Questão 7", end = "\n\n")

matriz_3x3 = np.array([[1, 0, 3], [0, 3, 2], [6, 2, 0]])
print("Matriz 3x3:")
print(matriz_3x3,  end = "\n\n")

identity = np.identity(3).astype(int)
print("Identidade:")
print(identity,  end = "\n\n")

determinante = np.linalg.det(matriz_3x3).round()
print("Determinante da matriz:")
print(determinante,  end = "\n\n")

inversa = np.linalg.inv(matriz_3x3)
print("Matriz Inversa:")
print(inversa,  end = "\n\n")

produto = np.matmul(matriz_3x3, inversa)
print("Produto da matriz pela sua inversa:")
print(np.round(produto).astype(int),  end = "\n\n")

if np.allclose(produto, identity):
    print("O produto é igual à identidade.")
else:
    print("O produto não é igual à identidade.")







