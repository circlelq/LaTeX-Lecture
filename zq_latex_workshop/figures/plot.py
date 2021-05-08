import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0, 2*math.pi, 100)
y = [math.sin(i) for i in x]
plt.plot(x, y)
plt.savefig("./sin.png")
plt.cla()

y = [math.cos(i) for i in x]
plt.plot(x, y)
plt.savefig("./cos.png")
plt.cla()

x = np.linspace(-1, 1, 100)
y = [i**2 for i in x]
plt.plot(x, y)
plt.savefig("./square.png")
plt.cla()

y = [math.exp(i) for i in x]
plt.plot(x, y)
plt.savefig("./exp.png")