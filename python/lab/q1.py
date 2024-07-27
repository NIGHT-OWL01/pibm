'''1.Create a NumPy array of shape (3, 4) with values ranging from 1 to 12. Reshape it to a (4, 3) array and print the result.'''

import numpy as np

arr = np.arange(1,13).reshape((3,4))
print(arr)