import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def creatFurmula(z):
    t = ""
    for i in range(0, len(z)):
        t += '+' + str(z[i]) + '*x**' + str(len(z) - 1 - i)
    return t


data = pd.read_csv('etkam.csv')
x1 = data['Date value']
y1 = data['Close']
x = np.array(x1)
y = np.array(y1)
z = np.polyfit(x, y, 6)
p = np.array(range(len(x)+2,len(x)+22))
x = np.append(x,p)


plt.plot(x1, y1)
plt.plot(x, eval(creatFurmula(z)))
plt.show()
