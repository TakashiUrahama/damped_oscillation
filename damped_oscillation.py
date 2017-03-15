import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid', {'grid.linestyle': '--'})

x = np.linspace(0, 10, 1000)
y = np.cos(np.pi*x)
z = np.exp(-x)

plt.plot(x, y*z, color = 'magenta', label = '$ y = e^{-x}\cos \pi x $')
plt.plot(x, z, color = 'lime', label = '$ y = e^{-x} $')
plt.plot(x, -z, color = 'greenyellow', label = '$ y = -e^{-x} $')
plt.legend()
plt.title('damped oscillation')
plt.xlim(0, 10)
plt.ylim(-1, 1)
plt.savefig('damped_oscillation.png')
plt.show()
