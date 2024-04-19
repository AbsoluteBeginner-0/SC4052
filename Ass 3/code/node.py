import nltk
import re

class Edge:
    __weight = None
    __from = None
    __to = None

    def __init__(self, src, to, weight):
        self.__from = src
        self.__to = to
        self.__weight = weight
    
    def GetFrom(self):
        return self.__from.GetID()
    
    def GetTo(self):
        return self.__to.GetID()
    
    def GetWeight(self):
        return self.__weight
    
    def SetWeight(self, weight):
        self.__weight = weight

class Node:
    __id = None
    __label = None
    __tokens = None
    __edges = None

    def __init__(self, id, label):
        self.__id = id
        self.__label = label
        self.__tokens = self.Tokenize(self.__label)
        self.__edges = []

    def AddEdge(self, to, weight=0):
        new_edge = Edge(self, to, weight)
        self.__edges.append(new_edge)
        return new_edge
    
    def GetEdge(self, neighbor_ID):
        for edge in self.__edges:
            if neighbor_ID == edge.GetTo():
                return edge
        return None

    def GetEdges(self):
        return self.__edges
    
    def GetEdgeSum(self):
        sum = 0
        for edge in self.__edges:
            sum += edge.GetWeight()
        return sum
    
    def GetID(self):
        return self.__id
    
    def GetLabel(self):
        return self.__label

    def GetNeighbours(self):
        neighbors = []
        for edge in self.__edges:
            neighbors.append(edge.__to)
        return neighbors

    def GetTokens(self):
        return self.__tokens
    
    def Tokenize(self, str):
        lemmatizer = nltk.stem.WordNetLemmatizer()
        stop_words = set(nltk.corpus.stopwords.words('english'))

        ret = nltk.word_tokenize(str.lower())
        # ret = list(filter(lambda x: x not in stop_words, ret))
        ret = list(filter(lambda x: x not in ['"', ',', '\'', '.', '(', ')', '/', '\\'], ret))
        ret = list(map(lambda x: lemmatizer.lemmatize(x), ret))

        return ret