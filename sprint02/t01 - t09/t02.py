
def func(x):
    return x*x - 4

def right_rect(function, begin, end, iterations):

	step = (end - begin) / iterations
	sum, x = 0.0, end
	for i in range(iterations):
		sum += function(x)
		x -= step
	return sum * step

    

if __name__ == "__main__":
    print(right_rect(func, float(2), float(4), 100))