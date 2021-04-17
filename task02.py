import numpy as np
import copy, math

# Удаляем одинаковые и пропорциональные строки
def delete_similar(temp):
    for i in range(0, len(temp)):
            for j in range(0, len(temp)):
                if (i != j):                 
                    a = [n / m for n, m in zip(temp[i], temp[j])]
                    if len(set(a)) == 1: # Если все єлементы списка равны то списки пропорциональны
                        if a[0] < 1: # Оставляем список с меньшими коэфициентами 
                            temp.remove(temp[j])
                        else:
                            temp.remove(temp[i])
                        print(np.matrix(temp))
                        return delete_similar(temp)


def gauss(matrix, vector):

    temp = copy.deepcopy(matrix)
    # Add vector to matrix
    for i in range(0, len(matrix)):
        matrix[i].append(vector[i])
    print(np.matrix(temp))

    # Удаляем одинаковые и пропорциональные строки
    print(delete_similar(temp))

                        

                
    print(np.matrix(temp))



def main():
    # matrix = [
    #     [2,  1, 1],
    #     [1, -1, 0],
    #     [3, -1, 2],
    # ]
    matrix = [
        [2,  -1, 1, 3],
        [4, -2, 2, 6],
        [3, -1, 2, 3],
        [3, -1, 2, 3]
    ]
    vector = [-2, -4, 2, 2]
    print(f'det: {gauss(matrix, vector)}')


if __name__ == '__main__':
    main()