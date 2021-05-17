import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = np.arange(20, 41, 1)
y1 = 1/x1
plt.plot(x1, y1, 'r-', c='purple')
plt.legend(['linia wykresowa'])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([20,41])
plt.ylim([0.02,0.05])
plt.show()

x1 = np.arange(20, 41, 1)
y1 = 1/x1
plt.plot(x1, y1, 'bo--')
plt.title('Wykres funkcji f(x) dla x[20, 40]')
plt.xlabel('x')
plt.ylabel('1/x')
plt.xlim([20,40])
plt.ylim([0.02,0.05])
plt.show()
