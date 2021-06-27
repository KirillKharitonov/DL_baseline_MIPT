import numpy as np

def matrixMult(first, second):
    """
       param first: list of "size" lists, each contains "size" floats
       param second: list of "size" lists, each contains "size" floats
    """
    # result = [first[i][j] * second[i][j] for i, j in zip(range(len(first)), len(range(second[0])))]
    result = [[0 for i in range(len(second[0]))] for j in range(len(first))]
    for i in range(len(first)):
        for j in range(len(second[0])):
            for m in range(len(first[0])):
                result[i][j] += first[i][m] * second[m][j]
    res2 = np.matmul(first, second)
    return result, res2

a = [[1, 2, 3],
     [1, 2, 3],
     [1, 2, 3]]
b = [[3, 2, 1],
     [4, 5, 6],
     [7, 8, 9]]

print(matrixMult(a, b))