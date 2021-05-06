

def checking(matrix, vector, roots):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            res += matrix[i][j] * roots[j]

        if res != vector[i]:
            return False
        res = 0

    return True



if __name__ == '__main__':
    matrix = [
        [2,  1, 1],
        [1, -1, 0,],
        [3, -1, 2],
    ]
    vector = [2, -2, 2]
    roots = [-1.0, 1.0, 3.0]
    print(checking(matrix, vector, roots))