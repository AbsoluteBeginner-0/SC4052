import matplotlib.pyplot as plt
import numpy as np
import random

class User:
    _alpha = 0
    _beta = 0
    _window_size = None
    _steps = None
    
    def __init__(self, n, alpha, beta):
        self._alpha = alpha
        while (0 == beta):
            beta = random.random()
        self._beta = beta
        self._window_size = n
        self._steps = [n]
    
    def Increase(self):
        self._window_size += self._alpha
    
    def Decrease(self):
        self._window_size = max(1, int(self._window_size * self._beta))

    def Log(self):
        self._steps.append(self._window_size)

    def GetWindowSize(self):
        return self._window_size

    def GetSteps(self):
        return self._steps

    def GetAlpha(self):
        return self._alpha
    
    def GetBeta(self):
        return self._beta

class Host:
    # _alpha = 0
    # _beta = 0
    _max_window_size = 0
    _clients = []

    def __init__(self, seed, max_window_size=20):  #alpha=1, beta=0.5, max_window_size=20):
        random.seed(seed)
        # self._alpha = alpha
        # self._beta = beta
        self._max_window_size = max_window_size

    def addClients(self, n):
        for i in range(n):
            self._clients.append(User(random.randint(1, 10), random.randint(1, 10), random.random()))

    def Step(self):
        sum_windows = 0
        for client in self._clients:
            sum_windows += client.GetWindowSize()
            
            if (sum_windows > self._max_window_size):
                # Congestion event
                for client in self._clients:
                    client.Decrease()
                    client.Log()
                return
        
        for client in self._clients:
                    client.Increase()
                    client.Log()

    def Plot(self, x, y):
        xpoints = np.array(self._clients[x].GetSteps())
        ypoints = np.array(self._clients[y].GetSteps())

        plt.plot(xpoints, ypoints)
        plt.show()

def GetAsymptote(a, b):
    return a / (1 - b)

if __name__ == "__main__":
    my_host = Host(42069, 5000)
    my_host.addClients(200)

    for i in range(10000):
        my_host.Step()
    print(my_host._clients[0].GetAlpha(), my_host._clients[0].GetBeta())
    print(my_host._clients[1].GetAlpha(), my_host._clients[1].GetBeta())
    # print(my_host._clients[0].GetSteps()[9900:], sum(my_host._clients[0].GetSteps()[9000:]))
    # print(my_host._clients[1].GetSteps()[9900:], sum(my_host._clients[1].GetSteps()[9000:]))
    print(sum(my_host._clients[0].GetSteps()[9900:]) / 100)
    print(sum(my_host._clients[1].GetSteps()[9900:]) / 100)
    a_1 = GetAsymptote(my_host._clients[0].GetAlpha(), my_host._clients[0].GetBeta())
    a_2 = GetAsymptote(my_host._clients[1].GetAlpha(), my_host._clients[1].GetBeta())
    print(a_2/a_1)
    print(sum(my_host._clients[1].GetSteps()[9900:]) / sum(my_host._clients[0].GetSteps()[9900:]))
    # my_host.Plot(0, 1)
