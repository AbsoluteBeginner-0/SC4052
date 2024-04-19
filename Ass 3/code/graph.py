from node import *
import random

class Graph:
    __node_count = 0
    __nodes = None
    __edges = None

    def __init__(self):
        self.__nodes = []
        self.__edges = []
    
    def AddEdge(self, id_from, id_to, weight=0):
        node_from = self.GetNodeFromID(id_from)
        node_to = self.GetNodeFromID(id_to)
        self.__edges.append(node_from.AddEdge(node_to, weight))
 
    def AddNode(self, label):
        self.__nodes.append(Node(self.__node_count, label))
        self.__node_count += 1
    
    def GetAdjacencyMatrix(self):
        adjacency_matrix = []
        for node in self.__nodes:
            row = []
            for neighbor in self.__nodes:
                edge = neighbor.GetEdge(node.GetID())
                if edge:
                    row.append(edge.GetWeight())
                else:
                    row.append(0)
            adjacency_matrix.append(row)
        return adjacency_matrix
    
    def GetDiagonalMatrix(self):
        n = len(self.__nodes)
        diag_matrix = []

        for i in range(n):
            curr_node = self.__nodes[i]
            curr_row = [0] * n
            curr_row[i] = 1 / curr_node.GetEdgeSum()
            diag_matrix.append(curr_row)
        return diag_matrix
  
    def GetNodeCount(self):
        return self.__node_count
    
    def GetNodeFromID(self, id):
        try:
            return self.__nodes[id]
        except e:
            raise Exception("No node with id '" + id + "' exists!")
    
    def GetRandomNode(self):
        return self.__nodes[random.randint(0, self.__node_count - 1)].GetID()
    
    def Print(self):
        print("Vertices:")
        for node in self.__nodes:
            print(f"[ID: {node.GetID()}, Label: {node.GetLabel()}]")
            print(f"[ID: {node.GetID()}, Tokens: {node.GetTokens()}]")
        # print("Edges: ")
        # for edge in self.__edges:
        #     print(f"{{{edge.GetFrom()}, {edge.GetTo()}, {edge.GetWeight()}}}")
        # print("Adjacency Matrix:")
        # print(self.GetAdjacencyMatrix())
        # print("Diagonal Matrix:")
        # print(self.GetDiagonalMatrix())
    