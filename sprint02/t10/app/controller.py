import plotly
import plotly.graph_objects as go 
import matplotlib.pyplot as plt 
from PIL import Image
import numpy as np
import json

from app.methods import Method
method = Method()

func = [    # Integral
            (lambda x: x*x + 2),
            (lambda x: x*x - 4),
            (lambda x: x**3 - 6*x), 
            (lambda x: np.exp(-x)),
            (lambda x: np.sin(-x)), 
            (lambda x: np.exp(pow(-x, 2))),
            (lambda x: np.exp((-4 * x) - pow(x, 3))),
            # Differential equations
            (lambda x, y: -x*y), 
            (lambda x, y: y + x),
            (lambda x, y: (3*x - (12*x)**2) * y), 
            (lambda x, y: x*x + y),
            (lambda x, y: x**3 + 2*y)
        ]

class Controller():

    def __init__(self):
        pass


    def definite_integral(self, body):
        
        i = int(body['example'])
        body['begin'] = float(body['begin'])
        body['end'] = float(body['end'])
        body['n'] = int(body['n'])

        if body['compare'] == True:
            result = []
            result.append(method.left_rect(func[i], body['begin'], body['end'], body['n']))
            result.append(method.right_rect(func[i], body['begin'], body['end'], body['n']))
            result.append(method.center_rect(func[i], body['begin'], body['end'], body['n']))
            result.append(method.trapezoidal(func[i], body['begin'], body['end'], body['n']))
            result.append(method.simpson(func[i], body['begin'], body['end'], body['n']))
            return result
        else:
            if body['method'] == 'left_rect':
                return method.left_rect(func[i], body['begin'], body['end'], body['n'])
            elif body['method'] == 'right_rect':
                return method.right_rect(func[i], body['begin'], body['end'], body['n'])
            elif body['method'] == 'center_rect':
                return method.center_rect(func[i], body['begin'], body['end'], body['n'])
            elif body['method'] == 'trapezoidal':
                return method.trapezoidal(func[i], body['begin'], body['end'], body['n'])
            elif body['method'] == 'simpsons':
                return method.simpson(func[i], body['begin'], body['end'], body['n'])
                
    
    def differential_equation(self, body):
        i = int(body['example'])
        body['begin'] = float(body['begin'])
        body['end'] = float(body['end'])
        body['y0'] = float(body['y0'])
        body['n'] = int(body['n'])

        if body['method'] == 'euler':
            return method.euler(func[i], body['begin'], body['end'], body['y0'], body['n'])
        elif body['method'] == 'rung-kutte-2':
            return method.runge_kutta_second(func[i], body['begin'], body['end'], body['y0'], body['n'])
        elif body['method'] == 'rung-kutte-3':
            return method.runge_kutta_third(func[i], body['begin'], body['end'], body['y0'], body['n'])
        elif body['method'] == 'rung-kutte-4':
            return method.runge_kutta_fourth(func[i], body['begin'], body['end'], body['y0'], body['n'])