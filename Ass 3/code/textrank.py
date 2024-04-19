import random
import math
import numpy as np

class TextRank:
    __surfer_node = None
    __graph = None
    __random_jump = False
    __damp = 0
    __vec = None
    __verbose = True

    def __init__(self, graph):
        self.__graph = graph
        self.__surfer_node = self.__graph.GetRandomNode()
        self.__vec = [1 / self.__graph.GetNodeCount()] * self.__graph.GetNodeCount()
        self.SetEdges()
        print(self.__vec)
        print(f"[TextRank]: Simulation started with surfer at {self.__surfer_node}!")

    def Relation(self, n1, n2):
        # token overlap
        token_hash = {}
        total_overlap = 0
        for i in n1.GetTokens():
            token_hash[i] = 0
        
        for j in n2.GetTokens():
            if j in token_hash:
                total_overlap += 1
        
        return total_overlap / (math.log(len(n1.GetTokens())) + math.log(len(n2.GetTokens())))

    def SetEdges(self):
        n = self.__graph.GetNodeCount()
        for i in range(n):
            for j in range(n):
                n1 = self.__graph.GetNodeFromID(i)
                n2 = self.__graph.GetNodeFromID(j)
                self.__graph.AddEdge(i, j, self.Relation(n1, n2))
    
    def SetRandomJump(self, d):
        self.__damp = d
        print(f"[TextRank]: Dampening factor set to {self.__damp}!")
    
    def ToggleRandomJump(self, bool):
        self.__random_jump = bool
        print(f"[TextRank]: Random jump set to " + "True" if self.__random_jump else "False" + "!")
    
    def SetVerbose(self, bool):
        self.__verbose = bool

    def Step(self):
        curr_node = self.__graph.GetNodeFromID(self.__surfer_node)
        edges = curr_node.GetEdges()
        if 0 == len(edges) or (self.__random_jump and random.random() <= (1 - self.__damp)):
            self.__surfer_node = self.__graph.GetRandomNode()
            if self.__verbose:
                print(f"[TextRank]: Surfer randomly jumped to {self.__surfer_node}!")
            return
        
        p = random.random() * curr_node.GetEdgeSum()
        edge_sum = 0
        for edge in edges:
            edge_sum += edge.GetWeight()
            if p <= edge_sum:
                self.__surfer_node = edge.GetTo()
                break
        self.CalculateTextRank()
        
        if self.__verbose:
            print(f"[TextRank]: Surfer clicked on {self.__surfer_node}!")
            print(f"[TextRank]: New TextRank weights: {self.__vec}")
        
    def StepN(self, n):
        for i in range(n):
            self.Step()
        
        if not self.__verbose:
            print(f"[TextRank]: TextRank ran for {n} iterations!")
            print(f"New surfer node: {self.__surfer_node}")
            print(f"New TextRank weights: {self.__vec}")
    
    def CalculateTextRank(self):
        np_adj = np.array(self.__graph.GetAdjacencyMatrix())
        np_diag = np.array(self.__graph.GetDiagonalMatrix())
        np_vec = np.array(self.__vec)

        np_vec = np.matmul(np_diag, np_vec)
        np_vec = np.matmul(np_adj, np_vec)

        self.__vec = np_vec.tolist()

        if self.__random_jump:
            for i in range(len(self.__vec)):
                self.__vec[i] = (1 - self.__damp) / len(self.__vec)  +  self.__damp * self.__vec[i]

    def GetTopN(self, n):
        sorted = np.argsort(self.__vec)
        top_n = np.sort(sorted[-n:])

        ret = ""
        for i in range(n):
            ret += " " + self.__graph.GetNodeFromID(top_n[i]).GetLabel()
        return ret
        
