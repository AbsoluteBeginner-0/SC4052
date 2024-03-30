from node import *
import random

class Graph:
    __node_count = 0
    __nodes = None
    __edges = None

    def __init__(self):
        self.__nodes = []
        self.__edges = []
    
    def GetNodeCount(self):
        return self.__node_count
    
    def GetNodeByID(self, id):
        return self.__nodes[id - 1].GetLabel()
    
    def GetRandomNode(self):
        return self.__nodes[random.randint(1, self.__node_count)].GetLabel()

    def AddNode(self, label):
        for node in self.__nodes:
            if label == node.GetLabel():
                raise Exception(f"Vertex with label {label} already exists!")

        self.__node_count += 1
        self.__nodes.append(Node(self.__node_count, label))
    
    def GetNodeFromLabel(self, label):
        for node in self.__nodes:
            if label == node.GetLabel():
                return node
        raise Exception("No node with label '" + label + "' exists!")
    
    def AddEdge(self, label_from, label_to):
        node_from = self.GetNodeFromLabel(label_from)
        node_to = self.GetNodeFromLabel(label_to)

        # if weight < 0.0:
        #     raise Exception(f"Invalid weight! Weight cannot be negative.")

        # if node_from.GetEdgeSum() + weight > 1.0:
        #     raise Exception(f"Available weight exceeded. Current sum of edge weights of {label_from} is {node_from.GetEdgeSum()}.")

        # check for existing edge
        potential_edge = node_from.GetEdge(node_to.GetLabel())
        if not potential_edge:
            self.__edges.append(node_from.AddEdge(node_to))
            return
        
        # old_weight = potential_edge.GetWeight()
        # potential_edge.SetWeight(weight)
        # raise Exception(f"Existing edge of weight {old_weight} from '{label_from}' to '{label_to}' replaced with weight {weight}.")

    def Print(self):
        print("Vertices:")
        for node in self.__nodes:
            print(node.GetLabel())
        print("Edges: ")
        for edge in self.__edges:
            print(f"{{{edge.GetFrom()}, {edge.GetTo()}, {edge.GetWeight()}}}")
        print("Adjacency Matrix:")
        print(self.GetAdjacencyMatrix())
    
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
