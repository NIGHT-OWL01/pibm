'''4.Create a NumPy array of shape (5, 5) with random floats ranging from 0 to 1.
 Normalize the array so that the values range from 0 to 1.
 Print the normalized array'''

import numpy as np

arr = np.random.rand(5,5)
print(arr)
normalized_arr = (arr-arr.min())/(arr.max()-arr.min())
print(normalized_arr)