import numpy as np
# Formules https://planetcalc.ru/8400/?thanks=1

def func(x, y):
    return x ** 2 + y

def runge_kutta_second(function, begin, end, y0, iterations):

    y = np.zeros(iterations + 1)
    step = (end - begin) / iterations
    x, y[0] = begin, y0
    for i in range(1, iterations + 1):
        R1 = step * function(x, y[i-1])
        R2 = step * function(x + (step / 2), y[i-1] + (R1 / 2))
        y[i] = y[i-1] + R2
        x = begin + (i * step)
    return y[1:]
    

if __name__ == "__main__":
    print(runge_kutta_second(func, float(2), float(4), float(1), 10))