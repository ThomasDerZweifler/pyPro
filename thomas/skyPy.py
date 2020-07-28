# python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

from scipy.ndimage import gaussian_filter

a = np.arange(50, step=2).reshape((5,5))

fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side
ascent = misc.ascent()
result = gaussian_filter(ascent, sigma=5)
ax1.imshow(ascent)
ax2.imshow(result)
plt.show()