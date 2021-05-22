import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = np.arange(20, 41, 1)
y1 = 1/x1
plt.plot(x1, y1, 'r-', c='purple')
plt.legend(['linia wykresowa'])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([20, 41])
plt.ylim([0.02, 0.05])
plt.show()

x1 = np.arange(20, 41, 1)
y1 = 1/x1
plt.plot(x1, y1, 'bo--')
plt.title('Wykres funkcji f(x) dla x[20, 40]')
plt.xlabel('x')
plt.ylabel('1/x')
plt.xlim([20, 40])
plt.ylim([0.02, 0.05])
plt.show()

x2 = np.arange(0, 45, 0.1)
s = np.sin(x2)
c = np.cos(x2)
plt.plot(x2, s, label="sin(x)")
plt.plot(x2, c, label="cos(x)")
plt.title("Wartosc sinusa i cosinusa dla x")
plt.xlabel("x")
plt.legend()
plt.show()

x3 = np.arange(0, 45, 0.1)
s1 = np.sin(x2+np.pi)
s2 = np.sin(x2)+2
plt.plot(x3, s2, label="sin(x)")
plt.plot(x3, s1, label="sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend(loc="center left")
plt.show()

df = pd.read_csv('iris.data', sep=',', decimal='.', header=None)
print(df)
data = {'c': np.random.randint(0, 150, 150),
        'x': df[0],
        'y': df[1],
        's': abs(df[0]-df[1])}
plt.scatter('x', 'y', c='c', s='s', data=data)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()

xlsx = pd.ExcelFile('imiona.xlsx')
df1 = pd.read_excel(xlsx, header=0)
print(df1)
plt.subplot(1, 3, 1)
urodzenia = df1.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
urodzenia.plot.bar(color=['y', 'b'])
plt.xlabel('Płeć')
plt.subplot(1, 3, 2)
x3 = df1['Rok'].unique()
y3 = df1[(df1['Plec'] == 'K')].groupby('Rok').agg({'Liczba': ['sum']}).values
y4 = df1[(df1['Plec'] == 'M')].groupby('Rok').agg({'Liczba': ['sum']}).values
plt.plot(x3, y3, label='Dziewczynki')
plt.plot(x3, y4, label='Chłopcy')
plt.ylabel('Rok')
plt.legend()
plt.show()
