from math import sin, cos, pi
import random
from typing import Callable

import numpy as np
from Fourier import FourierInterpolation, FourierTransform, InverseFourierTransform
from matplotlib import pyplot as plt

def test_fun(x: float) -> float:
    if x.__floor__() % 2 == 0:
        return 2
    else:
        return -2
    
def print_function(function: Callable[[float], float], start: float, end: float, step: float):
    x_values = []
    y_values = []
    x = start
    while x < end:
        x_values.append(x)
        y_values.append(function(x))
        x += step
    plt.plot(x_values, y_values)

def task_1a():
    fourier = FourierInterpolation(function=test_fun, half_period=1, step=0.01, n=13)
    print_function(test_fun, -5, 5, 0.01)
    print_function(fourier, -5, 5, 0.01)
    plt.show()

def task_1b():
    fourier = FourierInterpolation(function=test_fun, half_period=1, step=0.01, n=13)
    print_function(lambda x: test_fun(x) - fourier(x), -5, 5, 0.01)
    plt.show()

def task_2a():
    fun = lambda x: 0.5*cos(2*pi*x*100) 
    fourier = FourierInterpolation(function=fun, half_period=0.005, step=0.0005, n=13)
    print_function(fun, -0.02, 0.02, 0.0001)
    print_function(fourier, -0.02, 0.02, 0.0001)
    plt.show()
    x = np.linspace(-0.02, 0.02, 200)
    y = [fun(x[i]) for i in range(len(x))]
    ft = FourierTransform(y)
    frequencies = np.fft.fftfreq(200, d=1/200)
    ft_abs = np.abs(ft)
    plt.plot(frequencies, ft_abs)
    plt.show()
    ift = InverseFourierTransform(ft)
    plt.plot(ift)
    plt.show()

def task_3():
    x = np.linspace(-5, 5, 1000)
    y = np.vectorize(test_fun)(x)
    ft = np.fft.fft(y)
    ft_slow = FourierTransform(y)
    frequencies = np.fft.fftfreq(1000, d=1/1000)
    plt.plot(frequencies, np.abs(ft))
    plt.show()
    plt.plot(frequencies, np.abs(ft_slow))
    plt.show()

def task_4():
    fun = lambda x: 0.5 * cos(2*pi*x*100) + random.uniform(-1, 1) * 0.1
    x = np.linspace(-0.02, 0.02, 200)
    y = [fun(x[i]) for i in range(len(x))]
    plt.plot(x, y)
    plt.show()
    ft = np.fft.fft(y)
    frequencies = np.fft.fftfreq(200, d=1/200)
    ft_abs = np.abs(ft)
    plt.plot(frequencies, ft_abs)
    plt.show()

if __name__ == "__main__":
    task_1a()
    #task_1b()
    #task_2a()  
    task_3()
    task_4()

