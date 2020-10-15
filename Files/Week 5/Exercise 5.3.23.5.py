import math


def add_vectors(vector1, vector2):
    sum_vector = []
    for i in range(2):
        sum_vector.append(vector1[i]+vector2[i])
    return sum_vector


def scalar_mult(scalar, vector2):
    product_vector = []
    for i in range(len(vector2)):
        product_vector.append(scalar*vector2[i])
    return product_vector


def dot_product(vector1, vector2):
    dot_vector = 0
    if len(vector1) != len(vector2):
        print("Not the same dimension")
    else:
        for i in range(len(vector1)):
            dot_vector += vector1[i]*vector2[i]
        return dot_vector


#test of dimensions
def check_dim(array1, array2):
    if len(array1[0]) == len(array2[0]):
        if len(array1) == len(array2):
            indic = "true"
        else:
            indic = "false"
    else:
        if len(array1) == len(array2[0]):
            indic = "true"
        else:
            indic = "false"
    return indic









# zeros matrix

def zeros_matrix(m, n):
    row = [0]
    row *= m
    zeros = [row]
    zeros *= n
    return zeros











#matrix multiplication
def matrix_mult(array1, array2):
    indic = check_dim(array1, array2)
    if indic == "true":
        mult_matrix = zeros_matrix(len(array1), len(array2[0]))
        print(mult_matrix)
        for i in range(len(array1)):
            for j in range(len(array2[0])):
                for k in range(len(array2)):
                    mult_matrix[i][j] += array1[i][k] * array2[k][j]
        return mult_matrix
    else:
        print("Cannot multiply matrices")


a = [1, 1]
b = [2, 2]
c = 2

d = [[2, 7], [5, 2]]
e = [[3, 4], [5, 2]]

print(add_vectors(a, b))
print(scalar_mult(c, a))
print(dot_product(a, b))

print(matrix_mult(d, e))
