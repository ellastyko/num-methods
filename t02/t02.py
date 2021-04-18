import numpy as np
import copy
import math

def divide_lists(l1, l2):
    result = []
    for i in range(0, len(l1)):       
        if (l1[i] == 0 or l2[i] == 0):
            result.append(0)
        else:
            result.append(l1[i] / l2[i])
    return result

# Удаляем одинаковые и пропорциональные строки
def delete_similar(temp):
    for i in range(0, len(temp)):
            for j in range(0, len(temp)):
                if (i != j):              
                    proportion = divide_lists(temp[i], temp[j])
                    if len(set(proportion)) == 1: # Если все єлементы списка равны то списки пропорциональны
                        if proportion[0] < 1: # Оставляем список с меньшими коэфициентами 
                            temp.remove(temp[j])
                        else:
                            temp.remove(temp[i])
                        # print(np.matrix(temp))
                        return delete_similar(temp)


def solve(matrix, row, col):

    # Находим нужный столбец  
    for i in range(0, len(matrix[0])):  
        zeros = 0 
        for j in range(0, len(matrix)):   
            if matrix[j][i] == 0:
                zeros += 1
        if zeros == len(matrix) - 1:
            col += 1

    row = col
    # Находим нужный элемент
    for i in range(col, len(matrix)):   
        for j in range(col, len(matrix)):   
            if matrix[j][col] != 0 and i != j and matrix[j][col] < matrix[i][col]:           
                row = j
    # if (math.fabs(matrix[j][col]) < math.fabs(temp)):
    print(row)
    print(col)
    print(matrix[row][col])
    # print(row)  
    # print(col)

                
    return matrix, row, col

def gauss(matrix, vector):

    # Add vector to matrix
    for i in range(0, len(matrix)):
        matrix[i].append(vector[i])
    # print(np.matrix(matrix))

    # Удаляем одинаковые и пропорциональные строки
    delete_similar(matrix)

    # while True:
    row, col = 0, 0    
    _list_, row, col = solve(matrix, row, col) # Ряд из которого будут вычитаться остальные
    # break
        
        

                
    print(np.matrix(matrix))
    return matrix


def main():
    matrix = [
        [2,  -1, 1],
        [0,  4, 0],
        [0, 0, 2],
    ]
    # matrix = [
    #     [2,  -1, 1, 3],
    #     [4, -2, 2, 6],
    #     [3, -1, 2, 3],
    #     [3, -1, 2, 3]
    # ]
    vector = [2, -2, 2]
    print(f'Roots : {gauss(matrix, vector)}')


if __name__ == '__main__':
    main()