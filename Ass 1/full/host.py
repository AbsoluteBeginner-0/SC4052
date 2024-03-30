import random
import full.user as user

import matplotlib.pyplot as plt
import numpy as np

class Host:
    _alpha = 0
    _beta = 0
    _max_window_size = 0
    _clients = []

    def __init__(self, seed, alpha=1, beta=0.5, max_window_size=20):
        random.seed(seed)
        self._alpha = alpha
        self._beta = beta
        self._max_window_size = max_window_size
    
    def addClientW(self, p):
        self._clients.append(user.User(p))
    
    def addClient(self):
        self.addClientW(random.randint(5, 100))

    def addClients(self, n):
        for i in range(n):
            self.addClient()

    def Step(self):
        sum_windows = 0
        for client in self._clients:
            sum_windows += client.GetWindowSize()
            
            if (sum_windows > self._max_window_size):
                # Congestion event
                for client in self._clients:
                    client.Decrease(self._beta)
                    client.Log()
                self._alpha = max(1, int(self._alpha * self._beta))
                return
        
        for client in self._clients:
                    client.Increase(self._alpha)
                    client.Log()
        self._alpha *= 2

    def Plot(self, x, y):
        xpoints = np.array(self._clients[x].GetSteps())
        ypoints = np.array(self._clients[y].GetSteps())

        plt.plot(xpoints, ypoints)
        plt.show()


    def BroadCast(self):
        for i in range(len(self._clients)):
            self.Send(i)

    def Send(self, n):
        target = self._clients[n]

        for i in range(target.GetWindowSize()):
            if (not target.Receive()):
                target.Decrease(self._beta)
                target.Log()
                return
        target.Increase(self._alpha)
        target.Log()