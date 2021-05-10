import numpy as np

def func(x, y):
    return x ** 2 + y

def runge_kutta_fourth(function, begin, end, y0, iterations):

    step = (end - begin) / iterations
    y = np.zeros(iterations + 1)
    x, y[0] = begin, y0

    for i in range(1, iterations + 1):
        R1 = step * function(x, y[i-1])
        R2 = step * function((x + (step / 2)), (y[i-1] + (R1 / 2)))
        R3 = step * function(x + (step /2), y[i-1] + (R2 / 2))
        R4 = step * function(x + step, y[i-1] + R3)

        y[i] = y[i-1] + (R1 + 2 * R2 + 2 * R3 + R4) / 6
        x = begin + (i * step)

    return y[1:]
    

if __name__ == "__main__":
    print(runge_kutta_fourth(func, float(2), float(4), float(1), 10))