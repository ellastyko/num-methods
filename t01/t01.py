import math
import numpy as np 
import copy

def determinant(matrix):
    pass

def cramer(matrix, vector):
    
    det = np.linalg.det(matrix)
    if (det != 0):
        roots = []
        temp = copy.deepcopy(matrix)

        for i in range(0, len(temp)):
            for j in range(0, len(temp)):
                temp[j][i] = vector[j]    
            
            d = np.linalg.det(temp)
            d = math.ceil(d)
            root = d / det
            roots.append(root)

            temp = copy.deepcopy(matrix)
        return roots
    else:
        return 0


if __name__ == '__main__':
    matrix = [
        [2,  1, 1],
        [1, -1, 0,],
        [3, -1, 2],
    ]
    vector = [2, -2, 2]
    print(f'det: {cramer(matrix, vector)}')