'''7.Create a 3-dimensional array of shape (3, 4, 5) with random integers ranging from 1 to 100.
 Find the minimum value along the axis 0 and store the result in a 2-dimensional array of shape (4, 5).
   Print the minimum array.'''
import numpy as np

arr_3d=np.random.randint(1,101, size =(3,4,5))
print(arr_3d)
result=np.min(arr_3d, axis=0)
#!result=np.array([np.min(row) for arr_2d in arr_3d for row in arr_2d]).reshape(4,5)
print(result)