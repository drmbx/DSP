from math import pi, sin, cos
from typing import Callable
import cmath

class FourierInterpolation:
    def __init__(self, function: Callable[[float], float], half_period: float, step: float, n: int):
        self._function = function
        self._half_period = half_period
        self._step = step
        self._N = n
        self._a_0 = (1/self._half_period) * self._integral(self._function)
        self._a = [(1/self._half_period) * self._integral(lambda x: self._function(x) * cos(pi*n*x/self._half_period)) for n in range(1, self._N+1)]
        self._b = [(1/self._half_period) * self._integral(lambda x: self._function(x) * sin(pi*n*x/self._half_period)) for n in range(1, self._N+1)]

    def __call__(self, x: float) -> float:
        value = self._a_0 / 2
        for n in range(1, self._N+1):
            value += self._a[n - 1] * cos(pi * n * x / self._half_period) + self._b[n - 1] * sin(pi * n * x / self._half_period)
        return value

    def _integral(self, function: Callable[[float], float]) -> float:
        x = -self._half_period
        value = 0
        while x < self._half_period:
            value += function(x) * self._step
            x += self._step
        return value
    
def FourierTransform(x: list) -> list:
    N = len(x)
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(-2j * pi * k * n / N)
    return X

def InverseFourierTransform(x: list) -> list:
    N = len(x)
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * cmath.exp(2j * pi * k * n / N)
        X[k] /= N
    return X