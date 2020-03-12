import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

# print("HIII")
stock_data = np.loadtxt('ZBH.csv', delimiter="," , skiprows=1 , usecols=(1, 4))
# print (stock_data)
stock_data=scale(stock_data)

price = stock_data[:, 1].reshape(-1, 1)
date = stock_data[:, 0].reshape(-1, 1)

# plt.plot(date[:, 0],price[:, 0])
# plt.show()

fi=np.polyfit(date[:,0],price[:,0],10)
# print (len(fi))
# print (fi)
t = str(fi[0])
for i in range(1, len(fi)):
    t += "+"+str(str(fi[i])+"*x**"+str(i))

x=np.array(range(-2,2))
plt.plot(x,eval("x**2+2*x+2"))

plt.show()
# print (t)