'''3.Create a NumPy array of shape (6, 6) with random integers ranging from 0 to 9. 
Find the even numbers in the array and replace them with -1. Print the modified array.'''
import numpy as np

arr = np.random.randint(0,9,size=(6,6))
print(arr)
print(arr.shape[0])
for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):
        if arr[x][y]%2==0:
            arr[x][y]=-1

print(arr)
