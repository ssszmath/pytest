import numpy as np
import matplotlib.pyplot as plt


def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.show()


graph('x**2+2*x-4', range(-200, 200))
