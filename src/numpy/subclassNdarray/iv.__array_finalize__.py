"""
this method is called in case of all 3 cases:
    1.  view casting
    2.  from template
    3. explicit constructor call

"""
import numpy as np


class Rabbit(np.ndarray):
    def __new__(cls, shape, *args, **kwargs):
        print("Entering __new__")
        print(type(object))
        print(type(cls))
        print("Exiting __new__")
        return super().__new__(cls, shape, *args, **kwargs)

    def __init__(self, shape):
        # super().__init__(shape)
        print("Inside __init__")

    def __array_finalize__(self, obj, *args, **kwargs):
        print("Entering __array_finalize__")
        print(type(self))
        print(type(obj))  # observe its behavior ...
        print("Exiting __array_finalize__")


# explicit constructor call

arr = Rabbit((3,))

""" Output:
Entering __new__
<class 'type'>
<class 'type'>
Exiting __new__
Entering __array_finalize__
<class '__main__.Rabbit'>
<class 'NoneType'>
Exiting __array_finalize__
Inside __init__
"""

# view casting

z = np.asarray([10, 1])
cast_a = z.view(Rabbit)

""" Output:
Entering __array_finalize__
<class '__main__.Rabbit'>
<class 'numpy.ndarray'>
Exiting __array_finalize__
"""

# from template

tv = arr[1:]

""" Output:
Entering __array_finalize__
<class '__main__.Rabbit'>
<class '__main__.Rabbit'>
Exiting __array_finalize__
"""