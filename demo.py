import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

a = 3
b = 7
x = np.arange(0.01, 1, 0.01)
y = stats.beta.pdf(x, a, b)
plt.plot(x, y)
plt.title('Beta: a=%.1f, b=%.1f' % (a, b))
plt.xlabel('x')
plt.ylabel('Probability density')
plt.savefig('beta-dist.png')
plt.show()
