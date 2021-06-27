import numpy as np

def matrixMult(first, second):
    """
       param first: list of "size" lists, each contains "size" floats
       param second: list of "size" lists, each contains "size" floats

       :return: multiplication of first and second
    """
    # result = [first[i][j] * second[i][j] for i, j in zip(range(len(first)), len(range(second[0])))]
    result = [[0 for i in range(len(second[0]))] for j in range(len(first))]
    for i in range(len(first)):
        for j in range(len(second[0])):
            for m in range(len(first[0])):
                result[i][j] += first[i][m] * second[m][j]
    res2 = np.matmul(first, second)
    return result, res2

def diag_2k(a):
    """
    :param a: np.array[size, size]
    :return: Sum of even elements on main diagonal of a
    """
    result = np.sum([x for x in a.diagonal() if x % 2 == 0])

    return result

def cumsum(A):
    """

    :param A: np.array[m,n]
    :return:
    """
    result = np.cumsum(A, axis = 1)

    return result

## tests
a = [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]]
b = [[3, 2, 1],
     [4, 5, 6],
     [7, 8, 9]]
A = [[3, 2, 1],
     [4, 5, 6],
     [7, 8, 9]]

print(cumsum(A))
# print(matrixMult(a, b))

