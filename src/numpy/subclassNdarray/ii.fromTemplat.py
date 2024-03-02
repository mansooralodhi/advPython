
import numpy as np

"""
Creating new from template means you have created
a new instance of your class from a pre-existing 
instance, allowing you - for example - to copy 
across attributes that are particular to your subclass.

The 'slice' is a 'view' onto the original c_arr 
data. When we take a view from the ndarray, 
we return a new ndarray, of the same class, 
that points to the data in the original.
e.g. of usage of view()
    -   c_arr.copy()
    -   c_arr.mean()
"""

class C(np.ndarray):
    # class is a datatype
    pass


arr = np.zeros((3,))
c_arr = arr.view()[1:]

print(c_arr)  # [0. 0.]
print(type(c_arr)) # <class 'numpy.ndarray'>
print(arr is arr) # True
print(c_arr is arr) # False

