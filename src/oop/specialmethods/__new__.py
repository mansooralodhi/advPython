
class Rabbit:
    """
    Here we don't return anything from __new__
    """
    def __new__(cls, name='mans'):
        return
    def __init__(self, name = "manso"):
        print("__init__")

print(Rabbit()) # None

class EvenInteger(int):
    def __new__(cls, val):
        if val % 2 == 0: val = val + 1
        return super().__new__(cls, val)

print(EvenInteger(10.34)) # 10 (NB: though we passed a float but we got an int).

"""
Theory:
------
When we create an instance of a class, Python internally calls the default
__new__ method to create a new instance of class. The default __new__ method
allocates memory for the instance and returns it. After the instance is
created, Python calls the __init__ method (if defined) to initialize the instance.

Since the default __new__ method is automatically provided by Python and is
part of the object creation process, you don't need to define it explicitly
in most cases. However, you can override it if you need to customize the
instance creation process, such as when subclassing  types like int, str, or tuple.

Take Away:
1.  __new__ and __init__ signatures must match.
2.  __new__ must return the class instance if we want __init__ to execute.
3.  __new__ can not initialize instance attributes.

"""
