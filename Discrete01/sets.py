

class Sets():

    # Объеденение
    def union(self, A, B):
        A.extend(B)
        return list(set(A))

    # Пересечение
    # Общее
    def intersection(self, A, B):
        res = []
        for i in A:
            if i in B:
                res.append(i)
        return res     

    # Разница
    # Уникальные элементы А
    def difference(self, A, B):
        res = []
        for i in A:
            if i not in B:
                res.append(i)
        return res     

    # Симметричная Разница
    # Уникальные элементы каждого множества
    def symmetrical_difference(self, A, B): 
        res = []
        for i in A:
            if i not in B:
                res.append(i)
        for i in B:
            if i not in A:
                res.append(i)
        return res     

    def include(self, A, B): 
        for i in A:
            if i not in B:
                return False
        return True