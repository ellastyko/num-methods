import math
import numpy as np

# http://www.hpcc.unn.ru/?dir=1052
def jacobi(matrix, vector, N = 100):

    roots = [0 for i in range(len(matrix))]  	
    D = np.diag(matrix)  				# создаем D и заполняем его диагональю из matrix
    R = matrix - np.diagflat(D) 		# удаляем(вычитаем) диагональ(D) из А 
								        # A = D + R

    for i in range(N):  		# цикл для вычисления корня(корней) по формуле: x^(k+1)= (b − Rx^(k) )D^−1
        roots = (vector - np.dot(R, roots)) / D

    return roots
    

if __name__ == '__main__':
    matrix = [
        [2,  1, 1],
        [1, -1, 0],
        [3, -1, 2],
    ]
    vector = [2, -2, 2]
    print(f'Result: {jacobi(matrix, vector)}')
