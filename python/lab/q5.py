'''5.Create two NumPy arrays of shape (3, 3) with random integers ranging from 1 to 10.
 Perform element-wise multiplication and addition of the two arrays. Print the results'''
import numpy as np

arr1 = np.random.randint(1,11, size=(3,3))
arr2 = np.random.randint(1,11, size=(3,3))
print('arr 1:\n',arr1)
print('arr 2:\n',arr2)

multiplication_arr=np.multiply(arr1,arr2)
print(multiplication_arr)
addition_arr=np.add(arr1,arr2)
print(addition_arr)