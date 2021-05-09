import numpy as np

def func(x, y):
    return x ** 2 + y


def euler(function, begin, end, y0, iterations):

    y = np.zeros(iterations + 1)
    step = (end - begin) / iterations
    x, y[0] = begin, y0
    for i in range(1, iterations + 1):
        y[i] = y[i-1] + step * function(x, y[i-1])
        x = begin + (i * step)    
    return y[1:]

    

if __name__ == "__main__":
    print(euler(func, float(2), float(4), float(1), 10))