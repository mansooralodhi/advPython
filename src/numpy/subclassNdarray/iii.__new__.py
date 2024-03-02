import numpy as np


class C:
    def __new__(cls, *args, **kwargs):
        print("C __new__")
        return object.__new__(cls)

    def __init__(self, *args):
        print("C __init__")
        pass


class D(C):
    """
        __new__:
            1.  return C.__new__(D, *args) OR return C.__new__(cls, *args)
                calls __init__ method of class C, D and return an object of
                class D. hence, the class type (D) is preserved.
                equivalent to
                            subtype_obj = ndarray.__new__(subtype, shape, ...

            2.  return C.__new__(C, *args)
                doesn't calls __init__ methods of class C, D and returns
                object of class C.

            Q.  from 2, how come an object of type C is generated from
                class D without even calling the __init__ method ???
            A.  possible explanation:
                In general, when the __new__ method returns an object
                of class other than the class in which it is defined,
                the __init__ method of that class is not called.
    """

    def __new__(cls, *args, **kwargs):
        print("D __new__")
        return C.__new__(D, *args)

    def __init__(self, *args):
        print("D __init__")
        super().__init__(*args)


print(type(C("Hello")))
# output:
#   C __new__
#   C __init__
#   <class '__main__.C'>

print("*" * 30)


class N(np.ndarray):
    def __new__(cls, shape, *args, **kwargs):
        """
        this method is only called in case of explicit constructor call
        and not while performing viewCasting or fromTemplate.
        """
        return super().__new__(cls, shape, *args, **kwargs)


arr = np.ndarray.__new__(N, shape=(2,))
print(type(arr))  # <class '__main__.N'>  (NB: the __new__ of N is not called)
print(arr.shape)  # (2,)

arr = N(shape=(3,))
print(type(arr))  # <class '__main__.N'>  (NB: the __new__ of N is called)
print(arr.shape)  # (3,)
