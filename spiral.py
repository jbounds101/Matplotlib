import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0., 16*np.pi, 1000)
a, b = 0, 2.
plt.polar(theta, a+b*theta)
plt.grid(False)
plt.show()
