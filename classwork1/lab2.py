from math import sqrt


if __name__ == "__main__":
    sum = 0.0
    step = 0.01
    x = 0
    while x <= 1:
        x += step
        y = 0
        while y <= sqrt(max(1 - x**2, 0)):
            y += step
            z = 0
            while z <= sqrt(max(1 - x**2 - y**2, 0)):
                z += step
                sum += (x + y + z)/sqrt(max(2*(x**2) + 4*(y**2) + 5*(z**2), 0)) * step**3
    print(sum)