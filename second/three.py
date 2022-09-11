import numpy as np


def matrix_unfolder(a, b):
    array = []
    matrix = np.random.rand(a, b)
    for row in matrix:
        for i in row:
            array.append(i)
    print(matrix)
    print(array)


def abc_dictionary():
    arr_a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    arr_b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    dictionary = {}
    for i in range(len(arr_a)):
        if dictionary.get(arr_b[i]) is None:
            dictionary.update({arr_b[i]: arr_a[i]})
        else:
            dictionary.update({arr_b[i]: dictionary.get(arr_b[i]) + arr_a[i]})
    print(dictionary)


if __name__ == '__main__':
    matrix_unfolder(3, 3)
    abc_dictionary()
