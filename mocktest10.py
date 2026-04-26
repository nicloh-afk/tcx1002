#%% Mock test 10
import numpy as np
'''You are given a 1D NumPy array arr. Construct the pair-wise squared-difference matrix D where

D[i,j] = (arr[i] - arr[j])**2
Then, find one pair of indices (i, j) such that:

D[i,j] is minimal, where i < j
If there are multiple such pairs, return any one.
Do NOT use loops. You may want to use np.fill_diagonal(). Here is an example:'''

# Create a 3x3 array
a = np.zeros((3, 3), int)

# Hint: Fill the diagonal with a certain value
np.fill_diagonal(a, 5)

# Output:
# [[5 0 0]
#  [0 5 0]
#  [0 0 5]]

def min_sqdiff_pair(arr):
  arr = np.array(arr)
  n = len(arr)
  # print(arr), print(arr.shape) # eg. shape = (4,)
  
  ex_arr = arr[:,np.newaxis] # shape = (4,1)
  D = (ex_arr-arr)**2 # (extended array - original array)**2  # broadcasting
  np.fill_diagonal(D,np.max(D))
  print(D)
  
  # np.argmin(), np.argmax() -- returns index(min) along 1D array
  i = np.argmin(D) # finds earliest min value
  # eg. in 4x4 array, 
  # min value at 2nd row (idx=1), 3rd col (idx=2), 
  # np.argmin(arr) = 7 = row_idx * 4 + (col_idx + 1)
  row_idx = i//n
  col_idx = i%n
  return (row_idx,col_idx)

arr1 = [1,4,7,10]
min_sqdiff_pair(arr1)