from math import sqrt
import numpy as np
from numpy import array
 

def seidel(matrix, vector):

	length = len(matrix)
	roots = [0.0 for i in range(length)] # Fill zeros
	e = 0.0
	while True:
		root = np.copy(roots)

		for i in range(length):

			s1 = sum(matrix[i][j] * root[j] for j in range(i))
			s2 = sum(matrix[i][j] * roots[j] for j in range(i + 1, length))
			root[i] = (vector[i] - s1 - s2) / matrix[i][i]

		e = sum(abs(root[i] - roots[i])  for i in range(length))
		roots = root
		if e < 0.0001:
			break 
		

	return roots
	

 

if __name__ == '__main__':
    matrix = [
        [2,  1, 1],
        [1, -1, 0,],
        [3, -1, 2],
    ]
    vector = [2, -2, 2]
    print(f'Roots: {seidel(matrix, vector)}')