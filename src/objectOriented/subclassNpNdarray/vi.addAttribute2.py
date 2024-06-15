

import numpy as np

class Rabbit(np.ndarray):
    """
    add attribute to an existing ndarray.
    """
    def __new__(cls, array, info=None):
        obj = np.asarray(array).view(cls)
        obj.info = info
        return obj

    def __array_finalize__(self, obj, *args, **kwargs):
        if obj is None:
            return
        self.info = getattr(obj, "info", None)


arr  = Rabbit([3, 4, 5])
print(type(arr))
print(arr.info)
print(arr.shape)

"""Output:
<class '__main__.Rabbit'>
None
(3,)
"""
