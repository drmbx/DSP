from math import cos
import time
import scipy
import numpy as np
import matplotlib.pyplot as plt
import scipy.fft

def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def task_1():
    N = 600
    fmax = 300
    T = 1.0/fmax
    f1 = 50
    f2 = 150

    x = np.linspace(0, N*T, N)
    y = np.cos(f1*2*np.pi*x) + np.cos(f2*2*np.pi*x)

    plt.plot(x[:N//5], y[:N//5])
    plt.show()

    """Задание А"""
    xf = np.linspace(0.0, fmax/2, N//2)
    time_start = time.time()
    yf = DFT_slow(y)
    time1 = time1 = time.time()
    yff = scipy.fft.fft(y)
    time2 = time.time()

    fig = plt.figure(figsize=(8,8)) # размер полотна
    plt.subplots_adjust(wspace=0.4, hspace=0.4) # отступ между графиками

    plt.subplot(221)
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.xlabel('Частота, Гц')
    plt.ylabel('Амплитуда')

    plt.subplot(222)
    plt.plot(xf, 2.0/N * np.abs(yff[0:N//2]))
    plt.grid()
    plt.xlabel('Частота, Гц')
    plt.ylabel('Амплитуда')

    print(time1 - time_start)
    print(time2 - time1)
    plt.show()
    
    """Задание Б"""
    yif = scipy.fft.ifft(yf)
    yiff = scipy.fft.ifft(yff)

    plt.plot(x[:N//5], yif[:N//5])
    plt.show()

    plt.plot(x[:N//5], yiff[:N//5])
    plt.show()

    """Задание В"""
    y+=np.random.normal(0, 1, x.shape)

    plt.plot(x[:N//5], y[:N//5])
    plt.show()

    yff = scipy.fft.fft(y)
    plt.plot(xf, 2.0/N * np.abs(yff[0:N//2]))
    plt.grid()
    plt.show()













if __name__ == "__main__":
    task_1()