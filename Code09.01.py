class Graph() :
    def __init__(self,size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)]for _ in range(size)]

G1 = Graph(4)
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1

# ~~~~