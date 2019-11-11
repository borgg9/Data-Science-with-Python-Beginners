import math
from matplotlib import pyplot as plt
from functools import partial

def difference_quotient(f, x, h):
    return(f(x + h) - f(x)) / h
    
def square(x):
    return x * x

def derivative(x):
    return 2 * x

derivative_stimate = partial(difference_quotient, square, h=0.0001)
x = range (-10, 10)

plt.title('Acutal derivatibes Vs. Estimates')
plt.plot(x, map(derivative, x), 'rx', label='Actual')
plt.plot(x, map(derivative_stimate, x), 'b+', label='Estimatge')
plt.legend(loc=9)
plt.show()    
