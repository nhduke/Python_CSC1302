import numpy as np
import  matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2,1,1)  # nrows=2, ncols=1, index=1
plt.plot(x, y1, label='sin(x)')
plt.legend()

plt.subplot(2,1,2)  # index=2
plt.plot(x, y2, label='cos(x)', color='red')
plt.legend()

plt.show()