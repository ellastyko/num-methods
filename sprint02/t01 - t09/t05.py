
def func(x):
	return x*x - 4

def simpson(function, begin, end, iterations):

	step = (end - begin) / (iterations * 2)
	sum = float(function(begin)) + float(function(end))
	for i in range(1, iterations * 2):
		if i % 2 == 0:
			sum += 2 * float(function(begin + (i * step)))		    
		else:
			sum += 4 * float(function(begin + (i * step)))
		    
	return sum * step / 3
	

	

if __name__ == "__main__":
	print(simpson(func, float(2), float(4), 100))