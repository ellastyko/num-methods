import numpy as np
import math 
import copy


class Method:

    def __init__(self):
        pass

    def degeneracy(self, matrix):
        det = np.linalg.det(matrix)
        if (det != 0): 
            return True
        else: 
            return False


    def checking(self, matrix, vector, roots):
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res += matrix[i][j] * roots[j]

            if res != vector[i]:
                return False
            res = 0

        return True


    def cramer(self, matrix, vector):     

        roots = []
        temp = copy.deepcopy(matrix)
        det = np.linalg.det(matrix)
        for i in range(0, len(temp)):
            for j in range(0, len(temp)):
                temp[j][i] = vector[j]    
            
            d = np.linalg.det(temp)
            d = math.ceil(d)
            root = d / det
            roots.append(root)
            temp = copy.deepcopy(matrix)
        return True, roots


    def gauss(self, matrix, vector):

        roots, row = [0] * len(vector), None
        
        for col in range(len(vector)):

            
            for i in range(col, len(matrix)):
                if row == None or abs(matrix[i][col]) > abs(matrix[row][col]):
                    row = i
                
            if row == None:
                return False, 'Invalid matrix'

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

        for i in range((len(vector) - 1), -1, -1):
            roots[i] = vector[i] - sum(x * a for x, a in zip(roots[(i + 1):], matrix[i][(i + 1):]))

        return True, roots


    def seidel(self, matrix, vector):

        length = len(matrix)
        roots = [0.0 for i in range(length)] # Fill zeros
        e = 0.0
        while True:
            root = copy.deepcopy(roots)

            for i in range(length):

                s1 = sum(matrix[i][j] * root[j] for j in range(i))
                s2 = sum(matrix[i][j] * roots[j] for j in range(i + 1, length))
                root[i] = (vector[i] - s1 - s2) / matrix[i][i]

            e = sum(abs(root[i] - roots[i])  for i in range(length))
            roots = copy.deepcopy(root)
            if e < 0.0001:
                break 
            
        return True, roots


    def jordan_gauss(self, matrix, vector):

        n = len(matrix)
        roots = np.zeros(n)

        # Matrix in extended format
        for i in range(n):
            matrix[i].append(vector[i])

        # Applying Gauss Jordan Elimination
        for i in range(n):
            if matrix[i][i] == 0.0:
                return False, 'Divide by zero detected!'
                
            for j in range(n):
                if i != j:
                    ratio = matrix[j][i]/matrix[i][i]

                    for k in range(n+1):
                        matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

        # Obtaining Solution
        for i in range(n):
            roots[i] = matrix[i][n] / matrix[i][i]

        return True, roots


    def jacobi(self, matrix, vector, N = 100):

        roots = [0 for i in range(len(matrix))]  	
        D = np.diag(matrix)  				
        R = matrix - np.diagflat(D) 		
                                            

        for i in range(N):  		
            roots = (vector - np.dot(R, roots)) / D

        return True, roots