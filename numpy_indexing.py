import numpy as np 

arr = np.arange(0, 11)
arr[1:5]
arr[:6]
arr[3:]
arr[0:3] = 10  # udpate data between given index

slice_of_arr = arr[0:3]
slice_of_arr[:] = 44  # update slice variable as well as original array as its just giving another view

arr_copy = arr.copy() # not effect original array
arr_copy[:] = 50

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2d

arr_2d[0][0] # double bracket way
arr_2d[1]

arr_2d[0,0] # Single bracket way

arr_2d[:2, 1:] ## Get Everything until row 2 and get everything from column 2
arr_2d[1:, 1:]

# Comparision
arr = np.arange(0, 11)
bool_arr = arr > 4
arr[bool_arr]

arr[arr > 5]
arr[arr < 3]