import random

class User:
    # _drop_probability = None
    _max_window_size = None
    _window_size = None
    _steps = None
    
    def __init__(self, n):
        self._max_window_size = n
        self._window_size = n
        self._steps = [n]

    def Receive(self):
        return self._window_size <= self._max_window_size
        # return random.random() < self._drop_probability
    
    def Increase(self, alpha):
        self._window_size += alpha
    
    def Decrease(self, beta):
        self._window_size = max(1, int(self._window_size * beta))

    def Log(self):
        self._steps.append(self._window_size)

    def GetWindowSize(self):
        return self._window_size

    def GetSteps(self):
        return self._steps