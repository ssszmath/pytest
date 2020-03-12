import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from TFANN import ANNR

# print("HIII")
stock_data = np.loadtxt('ZBH.csv', delimiter="," , skiprows=1 , usecols=(1, 4))
# print (stock_data)
stock_data=scale(stock_data)

price = stock_data[:, 1].reshape(-1, 1)
date = stock_data[:, 0].reshape(-1, 1)

plt.plot(date[:, 0],price[:, 0])
plt.show()

# print (date)
# print (date[:,0])

