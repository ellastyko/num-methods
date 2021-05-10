import numpy as np


class Method():

    

    def __init__(self):
        pass


    def left_rect(self, function, begin, end, iterations):

        step = (end - begin) / iterations
        sum, x = 0.0, begin
        for i in range(iterations):
            sum += function(x)
            x += step
        return sum * step    
    

    def right_rect(self, function, begin, end, iterations):

        step = (end - begin) / iterations
        sum, x = 0.0, end
        for i in range(iterations):
            sum += function(x)
            x -= step
        return sum * step
    

    def center_rect(self, function, begin, end, iterations):

        step = (end - begin) / iterations
        sum, x = 0.0, begin
        for i in range(iterations):
            sum += function(x + 0.5*step)
            x += step
        return sum * step
    

    def trapezoidal(self, function, begin, end, iterations):

        step = (end - begin) / iterations
        sum, x = 0.0, begin
        for i in range(iterations):
            sum += ((function(x) + function(x + step)) / 2) * step
            x += step
        return sum
    

    def simpson(self, function, begin, end, iterations):

        step = (end - begin) / (iterations * 2)
        sum = float(function(begin)) + float(function(end))
        for i in range(1, iterations * 2):
            if i % 2 == 0:
                sum += 2 * float(function(begin + (i * step)))		    
            else:
                sum += 4 * float(function(begin + (i * step)))
                
        return sum * step / 3
    

    def euler(self, function, begin, end, y0, iterations):
        xx = np.zeros(iterations + 1)
        y = np.zeros(iterations + 1)
        step = (end - begin) / iterations
        x, y[0] = begin, y0
        for i in range(1, iterations + 1):
            y[i] = y[i-1] + (step * function(x, y[i-1]))
            xx[i] = x
            x = begin + (i * step)    
        return y[1:], xx[1:]
    

    def runge_kutta_second(self, function, begin, end, y0, iterations):

        xx = np.zeros(iterations + 1)
        y = np.zeros(iterations + 1)
        step = (end - begin) / iterations
        x, y[0] = begin, y0
        for i in range(1, iterations + 1):
            R1 = step * function(x, y[i-1])
            R2 = step * function(x + (step / 2), y[i-1] + (R1 / 2))
            y[i] = y[i-1] + R2
            xx[i] = x
            x = begin + (i * step)
        return y[1:], xx[1:]
    

    def runge_kutta_third(self, function, begin, end, y0, iterations):

        step = (end - begin) / iterations
        xx = np.zeros(iterations + 1)
        y = np.zeros(iterations + 1)
        x, y[0] = begin, y0

        for i in range(1, iterations + 1):
            R1 = step * function(x, y[i-1])
            R2 = step * function(x + (step / 2), y[i-1] + (R1 / 2))
            R3 = step * function(x + step, y[i-1] + (2 * R2) - R1)

            y[i] = y[i-1] + ((1 / 6) * (R1 + (4 * R2) + R3))
            xx[i] = x
            x = begin + (i * step)
        return y[1:], xx[1:]
    

    def runge_kutta_fourth(self, function, begin, end, y0, iterations):

        step = (end - begin) / iterations
        xx = np.zeros(iterations + 1)
        y = np.zeros(iterations + 1)
        x, y[0] = begin, y0

        for i in range(1, iterations + 1):
            R1 = step * function(x, y[i-1])
            R2 = step * function((x + (step / 2)), (y[i-1] + (R1 / 2)))
            R3 = step * function(x + (step /2), y[i-1] + (R2 / 2))
            R4 = step * function(x + step, y[i-1] + R3)

            y[i] = y[i-1] + (R1 + 2 * R2 + 2 * R3 + R4) / 6
            xx[i] = x
            x = begin + (i * step)

        return y[1:], xx[1:]