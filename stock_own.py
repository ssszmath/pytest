import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('zbh2.csv')

x = data['Date value']
y = data['Close']

# print (x)
# print (y)

z = np.polyfit(x, y,5)
# print (z)
t = ""
for i in range(0, len(z)):
    t += "+"+str(z[i])+"*x**"+str(len(z)-1-i)
print (t)
print(z)
plt.plot(x, y)
x=np.array(range(0, 250))
# plt.plot(x, eval(t))
plt.show()
