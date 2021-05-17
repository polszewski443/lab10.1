import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = np.arange(20, 41, 1)
y1 = 1/x1
plt.legend()
plt.plot(x1, y1, 'r-', c='g')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([20,41])
plt.ylim([0.02,0.05])
plt.show()