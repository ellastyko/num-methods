import numpy as np


def gauss(matrix, vector):

    roots, row = [0] * len(vector), None
    
    for col in range(len(vector)):

        
        for i in range(col, len(matrix)):
            if row == None or abs(matrix[i][col]) > abs(matrix[row][col]):
                row = i
            
        if row == None:
            return 'Error'

        # print(row, col)
        if row != col:
            matrix[row], matrix[col] = matrix[col], matrix[row]
            vector[row], vector[col] = vector[col], vector[row]
        
        div = matrix[col][col]
        matrix[col] = [a / div for a in matrix[col]]
        vector[col] /= div


        for i in range(col + 1, len(matrix)):
            el = -matrix[i][col]
            matrix[i] = [m + n * el for m, n in zip(matrix[i], matrix[col])]
            vector[i] += el * vector[col] 

    # print(np.matrix(matrix))
    # print(np.matrix(vector))
    # Calculating of roots
    for i in range((len(vector) - 1), -1, -1):
        roots[i] = vector[i] - sum(x * a for x, a in zip(roots[(i + 1):], matrix[i][(i + 1):]))

    return roots



if __name__ == "__main__":
    matrix = [
        [2,  1, 1],
        [1, -1, 0,],
        [3, -1, 2],
    ]
    vector = [2, -2, 2]
    print(f'Result: {gauss(matrix, vector)}')
