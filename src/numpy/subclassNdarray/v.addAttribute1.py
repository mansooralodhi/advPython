
import numpy as np

class Rabbit(np.ndarray):
    """
    initiate a ndarray and add attribute.
    a problem here is that we need a constructor with same signature
    as the built-in np.ndarray, this is avoided in part-2.
    """
    def __new__(subtype, shape, *args, info=None, **kwargs):
        obj = super().__new__(subtype, shape, *args , **kwargs)
        obj.info = info
        return obj

    def __array_finalize__(self, obj, *args, **kwargs):
        if obj is None:
            # class initiated by explicit constructor call
            return
        # class initiated by view casting (np.ndarray) or
        # from template (Rabbit)
        self.info = getattr(obj, "info", None)

# explicit constructor call

# arr = Rabbit(shape=(2,), info="information")
# print(type(arr))
# print(arr.info)

""" Output:
<class '__main__.Rabbit'>
information
"""

# view casting
nparr = np.asarray([2,3])
myarr = nparr.view(Rabbit)
print(type(myarr))
print(myarr.info)

"""Output:
<class '__main__.Rabbit'>
None
"""

# from template
arr = Rabbit(shape=(2,), info="information")
myarr = arr[1:]
print(type(myarr))
print(myarr.info)

"""Output
<class '__main__.Rabbit'>
information
"""
