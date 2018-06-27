import numpy as np

data = [[1,2,3],[4,5,6], [7,8,9]]
np.array(data)  #cast to Array
np.arange(0, 11, 2) # same as range feature

np.zeros((2, 2)) # two dimensional array of 0's
np.zeros((10))  #one diemensional Array of 0's
np.ones((10))  #one diemensional Array of 1's
np.ones((3,3)) # two dimensioanl array of 1's

# separate out number in equal manner (0,5,10) -> 0 start, 5 end, 10 equal disturbed numbers between start and stop
np.linspace(0, 5, 10) 

np.eye(3)  # to get idenetity Materics

# creates random array in between 0 to 1 based on given number
np.random.rand(5) # prints one dimensional array of 5 item between 0 to 1
np.random.rand(5,5) # prints 5*5  array of 5 item between 0 to 1

np.random.randn(5, 5)

# prints only random int number from range
np.random.randint(1, 100)
#print given size int numbers from range
np.random.randint(1, 100, 5)

# reshape data into given dimesional array if its fits for that 
data = np.arange(4)
data.reshape(2,2)

data = np.random.rand(50)
data.max() # max item in array
data.min() # min item in array
data.argmax() # index of max item in array
data.argmin() # index of min item in array
data = data.reshape(10,5)
data.shape # shape of array
data.dtype  # type of value in array
