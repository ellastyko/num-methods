

def func(x):
    return x*x - 4

def trapezoidal(function, begin, end, iterations):

	step = (end - begin) / iterations
	sum, x = 0.0, begin
	for i in range(iterations):
		sum += ((function(x) + function(x + step)) / 2) * step
		x += step
	return sum

    

if __name__ == "__main__":
    print(trapezoidal(func, float(2), float(4), 100))