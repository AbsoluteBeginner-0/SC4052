class Edge:
    __weight = None
    __from = None
    __to = None

    def __init__(self, to, weight, src):
        self.__weight = weight
        self.__from = src
        self.__to = to
    
    def GetFrom(self):
        return self.__from.GetLabel()
    
    def GetTo(self):
        return self.__to.GetLabel()
    
    def GetWeight(self):
        return self.__weight
    
    def SetWeight(self, weight):
        self.__weight = weight

class Node:
    __id = None
    __label = None
    __edges = None

    def __init__(self, id, label):
        self.__id = id
        self.__label = label
        self.__edges = []

    def AddEdge(self, to):
        new_edge = Edge(to, 0, self)
        self.__edges.append(new_edge)

        for edge in self.__edges:
            edge.SetWeight(1 / len(self.__edges))
        return new_edge
    
    def GetEdge(self, neighbor_label):
        for edge in self.__edges:
            if neighbor_label == edge.GetTo():
                return edge
        return None

    def GetEdges(self):
        return self.__edges
    
    def GetEdgeSum(self):
        sum = 0
        for edge in self.__edges:
            sum += edge.GetWeight()
        return sum
    
    def GetLabel(self):
        return self.__label

    def GetNeighbours(self):
        neighbors = []
        for edge in self.__edges:
            neighbors.append(edge.__to)
        return neighbors
