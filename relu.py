# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def relu(x):
    return np.maximum(0, x)

x = np.arange(-6.0, 6.0, 0.1)
y = relu(x)

plt.plot(x, y,'b')
plt.ylim(-1, 5)
plt.xlabel("x")  # x轴的标签
plt.ylabel("y")  # y轴的标签
plt.title("relu function")
plt.show()
