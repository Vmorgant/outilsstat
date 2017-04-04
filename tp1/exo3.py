import matplotlib.pyplot as plt
import numpy as np

n, p = 10000, 0.5 # mean and standard deviation
s = np.random.binomial(n, p, 1000)

count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(p * np.sqrt(2 * np.pi)) *np.exp( - (bins - n)**2 / (2 * p**2) ),linewidth=2, color='r')

plt.show()
