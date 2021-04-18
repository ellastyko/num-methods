import numpy as np
import math 
import plotly as pt
import copy


class Method:

    def __init__(self):
        pass

    def __determinant(self, matrix):
        pass

    def cramer(self, matrix, vector):      
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

    def gauss(self, matrix, vector):
        pass