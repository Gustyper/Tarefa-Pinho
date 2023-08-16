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

############

print("Questão 5", end = "\n\n")

for i in range(arr_random):
    for j in range(arr_random_2):
        if arr_random[i] = arr_random_2:
            ...
            






