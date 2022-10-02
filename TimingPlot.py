from Fitting import const, lin, quad, fit_data
from scipy import optimize
from matplotlib import pyplot as plt
import random
import time
 
x = [i for i in range(0, 1001, 50)]
 
def bubble_sort(L):
    n = len(L)
    for i in range(n):
        for j in range(n):
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
 
def time_function(func, args):
    # get current time from computer
    start_time = time.time()
    # run function
    func(args)
    # return difference
    return time.time() - start_time
 
y_data = []
for i in x:
    L = [random.randint(0,i) for i in range(i)]
    y_data.append(time_function(bubble_sort, L)*1000)
 
linear = fit_data(lin, x, y_data)
yfit1 = linear[2]
for i in yfit1:
    i*=1000
quadratic = fit_data(quad, x, y_data)
yfit2 = quadratic[2]
for i in yfit2:
    i *= 1000
 
 
plt.figure()
plt.scatter(x, y_data)
plt.plot(x, yfit1, label = "fit line")
plt.plot(x, yfit2, label = "fit quad")
 
plt.legend()
plt.xlabel("number of values to sort (n)")
plt.ylabel("time")
plt.ylim(-10, 120)
plt.xlim(-10, 1000)
plt.show()
plt.savefig("bestfit.png")
 
