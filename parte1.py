import numpy as np
import numpy.random

def questao1():
    print("Questão 1", end = "\n\n")
    
    array = np.arange(4)
    array_2 = np.arange(1,5)
    print(array, end = "\n\n")
    print(array_2, end = "\n\n")

    array_3 = array + array_2
    print(array_3, end = "\n\n")

    return array_3


###########

def questao2(array_3 = questao1()):
    print("Questão 2", end = "\n\n")

    array_2d = array_3.reshape(2,2)
    print(array_2d, end = "\n\n")

    array_float = array_2d.astype(float)
    print(array_float, end = "\n\n")

    array_float = np.transpose(array_float)
    print(array_float, end = "\n\n")


#############
def questao3(array_3 = questao1()):
        
    print("Questão 3", end = "\n\n")
    
    array_4 = np.array([[1,2], [3,4]])
    print(array_4, end = "\n\n")
    
    array_mult = array_3 * array_4
    print(array_mult, end = "\n\n")
    
    ############