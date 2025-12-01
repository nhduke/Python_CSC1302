import numpy as np
import matplotlib.pyplot as plt

#---------------------
#line chart
x1 = np.linspace(1, 200, 400)    
y1 = x1 + np.log(x1) 
#33

plt.figure(figsize=(12, 8))
plt.plot(x1, y1, label='f(x) = x + log(x)')

#annotate
pointX = 100
pointY = pointX + np.log(pointX)

plt.scatter(pointX, pointY, color='red')
plt.annotate(f"({pointX}, {pointY:.2f})",
             (pointX, pointY),
             textcoords="offset points",
             xytext=(10, 10),
             arrowprops=dict(arrowstyle="->"))

plt.title("Line Plot of f(x) = x + log(x), 1 <= x <= 200")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
plt.savefig("Line Chart")

#------------------------------
#bar chart
x2 = np.arange(1, 11)
y2 = 2 * x2 + 1

plt.figure(figsize=(10, 5))
plt.bar(x2, y2)

plt.title("Bar Chart of f(x) = 2x + 1, 1 <= x <= 10")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
plt.savefig("Bar Chart")

