import numpy as np

"""
View casting means you have created a new
instance of your array type from any potential 
subclass of ndarray.
"""

class C(np.ndarray):
    # class is a datatype
    pass


arr = np.zeros((3,))
c_arr = arr.view(dtype=C)
print(c_arr)  # [0. 0. 0.]
print(type(c_arr))  # <class '__main__.C'>
