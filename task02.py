import numpy as np
import copy, math

def gauss(matrix, vector):

    temp = copy.deepcopy(matrix)
    for i in range(0, len(matrix)):
        matrix[i].append(vector[i])
    # print(np.matrix(matrix))



def main():
    matrix = [
        [2,  1, 1],
        [1, -1, 0],
        [3, -1, 2],
    ]
    vector = [2, -2, 2]
    print(f'det: {gauss(matrix, vector)}')


if __name__ == '__main__':
    main()