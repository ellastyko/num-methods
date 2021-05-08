

def func(x):
    return x*x - 4

def center_rect(function, begin, end, iterations):

	step = (end - begin) / iterations
	sum, x = 0.0, begin
	for i in range(iterations):
		sum += function(x + 0.5*step)
		x += step
	return sum * step

    

if __name__ == "__main__":
    print(center_rect(func, float(2), float(4), 100))