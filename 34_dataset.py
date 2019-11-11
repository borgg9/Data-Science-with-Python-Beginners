from matplotlib import pyplot as plt
import numpy as np

class1 = [(3, 4), (4.2, 5.3), (4, 3), (6, 5), (4, 6), (3.7, 5.8), (3.2, 4.6), (5.2, 5.9),(5, 4), (7, 4), (3, 7), (4.3, 4.3)]
class2 = [(-3, -4), (-2, -3.5), (-1, -6), (-3, -4.3), (-4, -5.6), (-3.2, -4.8), (-2.3, -4.3), (-2.7, -2.6),(-1.5, -3.6), (-3.6, -5.6), (-4.5, -4.6), (-3.7, -5.8)]

X, Y = zip(* class1)
plt.scatter(X, Y, c='r')
X, Y = zip(* class2)
plt.scatter(X, Y, c='b')

plt.show()