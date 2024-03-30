from node import *
import random

class Graph:
    __node_count = 0
    __nodes = None
    __edges = None

    def __init__(self):
        self.__nodes = []
        self.__edges = []
    
    def AddEdge(self, label_from, label_to):
        node_from = self.GetNodeFromLabel(label_from)
        node_to = self.GetNodeFromLabel(label_to)

        # check for existing edge
        potential_edge = node_from.GetEdge(node_to.GetLabel())
        if potential_edge:
            raise Exception(f"Existing edge from '{label_from}' to '{label_to}'!")

        self.__edges.append(node_from.AddEdge(node_to))
 
    def AddNode(self, label):
        for node in self.__nodes:
            if label == node.GetLabel():
                raise Exception(f"Vertex with label {label} already exists!")

        self.__node_count += 1
        self.__nodes.append(Node(self.__node_count, label))
    
    def GetAdjacencyMatrix(self):
        adjacency_matrix = []
        for node in self.__nodes:
            row = []
            for neighbor in self.__nodes:
                edge = neighbor.GetEdge(node.GetLabel())
                if edge:
                    row.append(edge.GetWeight())
                else:
                    row.append(0)
            adjacency_matrix.append(row)
        return adjacency_matrix
    
    def GetNodeCount(self):
        return self.__node_count
    
    def GetNodeFromLabel(self, label):
        for node in self.__nodes:
            if label == node.GetLabel():
                return node
        raise Exception("No node with label '" + label + "' exists!")
    
    def GetRandomNode(self):
        return self.__nodes[random.randint(1, self.__node_count)].GetLabel()
    
    def Print(self):
        print("Vertices:")
        for node in self.__nodes:
            print(node.GetLabel())
        print("Edges: ")
        for edge in self.__edges:
            print(f"{{{edge.GetFrom()}, {edge.GetTo()}, {edge.GetWeight()}}}")
        print("Adjacency Matrix:")
        print(self.GetAdjacencyMatrix())
    