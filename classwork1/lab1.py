from math import factorial
import matplotlib.pyplot as plt

def sin(x: float, iterations: int) -> float:
    sum = 0
    for k in range (iterations):
        sum += (-1)**k * (x**(2*k + 1))/factorial(2*k+1)
    return sum



if __name__ == "__main__":
    x_values = []
    y_values = []
    for i in range(100):
        x = i * 0.1 - 5
        x_values.append(x)
        y_values.append(sin(x, 7))
    plt.plot(x_values, y_values)
    plt.show()