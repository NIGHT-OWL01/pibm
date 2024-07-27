'''6.Create a 2-dimensional array of shape (5, 5) with random integers ranging from 1 to 100.
 Find the sum of each row and store the results in a 1-dimensional array. Print the sum array.'''
import numpy as np

arr = np.random.randint(1,101,size=(5,5))
print(arr)
sum_array=np.array([x.max() for x in arr])
#for row in arr:
 #   sum_array=np.append(sum_array,np.max(row))
print(sum_array)
print(type(sum_array))
