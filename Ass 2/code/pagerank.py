import graph
import random
import numpy as np

class PageRank:
    __surfer_node = None
    __graph = None
    __random_jump = False
    __damp = 0
    __vec = None

    def __init__(self, graph):
        self.__graph = graph
        self.__surfer_node = self.__graph.GetRandomNode()
        self.__vec = [1 / self.__graph.GetNodeCount()] * self.__graph.GetNodeCount()
        print(self.__vec)
        print(f"PageRank simulation started with surfer at {self.__surfer_node}!")
    
    def SetRandomJump(self, d):
        self.__damp = d
        print(f"[PageRank] Dampening factor set to {self.__damp}!")
    
    def ToggleRandomJump(self, bool):
        self.__random_jump = bool
        print(f"[PageRank] Random jump set to " + "True" if self.__random_jump else "False" + "!")

    def Step(self):
        edges = curr_node.GetEdges()
        if 0 == len(edges) or (self.__random_jump and random.random() <= (1 - self.__damp)):
            self.__surfer_node = self.__graph.GetRandomNode()
            print(f"Surfer randomly jumped to {self.__surfer_node}!")
            return
        
        p = random.random()
        curr_node = self.__graph.GetNodeFromLabel(self.__surfer_node)
        edge_sum = 0
        for edge in edges:
            edge_sum += edge.GetWeight()
            if p <= edge_sum:
                self.__surfer_node = edge.GetTo()
                break
        self.CalculatePageRank()
        
        print(f"Surfer clicked on {self.__surfer_node}!")
        print(f"New PageRank weights: {self.__vec}")
        
    def StepN(self, n):
        for i in range(n):
            self.Step()
    
    def CalculatePageRank(self):
        np_adj = np.array(self.__graph.GetAdjacencyMatrix())
        np_vec = np.array(self.__vec)

        self.__vec = np.matmul(np_adj, np_vec).tolist()

        if self.__random_jump:
            for i in range(len(self.__vec)):
                self.__vec[i] = (1 - self.__damp) / len(self.vec) + self.__vec[i] * self.__damp
