'''2.Create a NumPy array of shape (5, 5) with random integers ranging from 1 to 10. 
Find the maximum value in the array and its corresponding index.'''
import numpy as np

arr= np.random.randint(1,11,size=(5,5))
max=np.max(arr)
max_index_row=np.argmax(arr,axis=0)
max_index_col=np.argmax(arr,axis=1)
print(arr)
print('max:',arr.max())
print('max-index:',max_index_row,max_index_col)

