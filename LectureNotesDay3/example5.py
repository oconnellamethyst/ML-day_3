# example program

import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return x**2

x = np.linspace(-3,3,40)

print(x)

y = np.vectorize(f)(x)

print(y)

plt.plot(x,y)
plt.scatter(x[7],y[7])
plt.scatter(x[21],y[21])
plt.show()
# you have to close this plot first and then the next plot will appear

plt.plot(x**3)
plt.show()
# x to the third

plt.plot(np.vectorize(math.sin)(x))
plt.show()
# sine

print(math.e)
# e is a magical number in math...

a = 1.414
b = 0
c = 1
def gaussian(x):
    return a * math.e ** -((x-b)**2)/(2*c**2)

# math looks scary but it's all just formulas, take the gaussian

gaussian(0)
input = np.linspace(-3,3,50)
plt.plot(input,np.vectorize(gaussian)(input))

# not so scary now is it

plt.ylim(0,1)
plt.show()

# derivatives
# in machine learning, we try to find where the derivative is zero
# problem is multiple optima, makes things hard and take a while

# linear regression is bae
