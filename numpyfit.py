import numpy as np
import matplotlib.pyplot as plt


def creatFurmula(z):
    t = ""
    for i in range(0, len(z)):
        t += '+' + str(z[i]) + '*x**' + str(len(z) - 1 - i)
    return t


# x = np.array(range(0, 100))
# y = np.array(range(0, 100))

x = np.array(range(-10, 10))
y = []
for i in range(0, len(x)):
    y.append(x[i]**3)

# print (len(x))
# print (len(y))
z = np.polyfit(x, y, 3)
print (z)
print (creatFurmula(z))
# plt.plot(x, eval(str(z[0])+'*x*'+str(z[1])))
# plt.plot(x, eval(str(z[0]) + '*x**1+' + str(z[0])))
plt.plot(x, eval(creatFurmula(z)))
plt.show()

