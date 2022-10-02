import math
from scipy import optimize
from matplotlib import pyplot as plt
 
#Task one
def const(c0):
    return c0
 
def lin(c1, x, c0):
    return (c1*x)+c0
 
def quad(c2, c1, x, c0):
    return (c2*(x**2)) + (c1*x) + c0
 
def fit_data(fitting_func, x_data, y_data):
    params, params_cov = optimize.curve_fit(fitting_func, x_data, y_data)
    y = [fitting_func(x_data[i], *params) for i in range(len(x_data))]
    rms = 0
    for i in range(len(x_data)):
        rms += ((y[i] - y_data[i])**2)
    rms = math.sqrt(rms/len(x_data))
    return params, rms, y
 
x = [i for i in range(20)]
y = [i for i in range(20)]
print(fit_data(quad, x, y))
