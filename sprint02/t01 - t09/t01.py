import numpy as np

# FORMULE
# S = step*[f(x1) + f(x2) + ...]

l = [
	lambda x: x*x - 4,
	(lambda x: x*4 - 3)
] 

def left_rect(function, begin, end, iterations):

	step = (end - begin) / iterations
	sum, x = 0.0, begin
	for i in range(iterations):
		sum += function(x)
		x += step
	return sum * step

    

if __name__ == "__main__":
    print(left_rect(l[1], float(2), float(4), 100))