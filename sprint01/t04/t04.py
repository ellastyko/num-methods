import numpy as np



def jordan_gauss(matrix, vector):

    n = len(matrix)
    x = np.zeros(n)

    # Matrix in extended format
    for i in range(n):
        matrix[i].append(vector[i])

    # Applying Gauss Jordan Elimination
    for i in range(n):
        if matrix[i][i] == 0.0:
            return 'Divide by zero detected!'
            
        for j in range(n):
            if i != j:
                ratio = matrix[j][i]/matrix[i][i]

                for k in range(n+1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    # Obtaining Solution
    for i in range(n):
        x[i] = matrix[i][n] / matrix[i][i]

    return x

if __name__ == '__main__':
    matrix = [
        [2,  1, 1],
        [1, -1, 0],
        [3, -1, 2],
    ]
    vector = [2, -2, 2]
    print(f'Result: {jordan_gauss(matrix, vector)}')