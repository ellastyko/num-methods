import numpy as np

# FORMULE
# S = step*[f(x1) + f(x2) + ...]

def func(x):
    return x*x - 4

def left_rect(function, begin, end, iterations):

	step = (end - begin) / iterations
	sum, x = 0.0, begin
	for i in range(iterations):
		sum += function(x)
		x += step
	return sum * step

    

if __name__ == "__main__":
    print(left_rect(func, float(2), float(4), 100))