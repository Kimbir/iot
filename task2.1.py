import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 1000)
plt.figure(figsize=(8,3))
plt.grid(lw=0.5, ls='--')
plt.plot(x,np.power((np.sin(2*x)), 2)*np.exp(((x+2)/10) ** 2), lw = 5.0, color='red', zorder=0)
plt.show()
