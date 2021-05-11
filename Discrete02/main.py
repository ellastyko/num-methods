


class Line():

    edge = []
    vertexes = []

    def __init__(self):
        pass

    def add(self, begin, end):
        self.edge.append([begin, end])


    # Образ and Прообраз   
    def proto(self):
        vertexes = []
        for i in range(len(self.edge)):
            for j in range(len(self.edge[i])):
                vertexes.append(self.edge[i][j])

        vertexes = sorted(list(set(vertexes)))
        self.vertexes = vertexes

        G = [list() for i in range(len(vertexes))]  # Образ
        NG = [list() for i in range(len(vertexes))]  # Прообраз

        for i in range(len(vertexes)):
            for j in range(len(self.edge)):
                # Для всех вершин мы ищем ребра которые в нее входят и выходят 
                if vertexes[i] == self.edge[j][0] and vertexes[i] != self.edge[j][1]:
                    G[i].append(self.edge[j][1])
                
                if vertexes[i] != self.edge[j][0] and vertexes[i] == self.edge[j][1]:
                    NG[i].append(self.edge[j][0])

        return G, NG 


    # Смежность    
    def adjacency(self):

        G, NG = self.proto()
        string = f"  {' '.join(self.vertexes) }"
        for i in range(len(self.vertexes)):
            string += '\n' + self.vertexes[i]
            for j in range(len(self.vertexes)):
                if self.vertexes[j] in G[i]:
                    string += ' 1'
                else: 
                    string += ' 0'     

        return string

    def incidence(self):
        string = ''
        for i in range(len(self.vertexes)):

            string += self.vertexes[i]
            for j in range(len(self.edge)):
                if self.vertexes[i] in self.edge[j]:
                    if self.vertexes[i] == self.edge[j][0]:
                        string += ' 1'
                    elif self.vertexes[i] == self.edge[j][1]:
                        string += ' -1'
                else:
                    string += ' 0'
            string += '\n'
        return string


def main():

    arr = [0 for i in range(9)]

    graph = Line()

    graph.add('А', 'Б')
    graph.add('А', 'В')   
    graph.add('В', 'А')   
    graph.add('Б', 'Е')   
    graph.add('Е', 'В')   
    graph.add('В', 'Г')   
    graph.add('Г', 'Е')
    graph.add('Е', 'Д')   
    graph.add('Г', 'Д')    

    G, NG = graph.proto()
    print(f'Образы {G}')
    print(f'Пробразы {NG}')

    print('Adjacency matrix')
    print(graph.adjacency() + '\n')
    print('Incidence matrix')
    print(graph.incidence())



if __name__ == '__main__':
    main()