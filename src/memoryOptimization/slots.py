
"""
Like any other python object, the instance of class is allocated a dynamic dictionary
that store the class attributes. However, this is inefficient method in terms of
memory. If thousands of objects are to be initiated then that would lead to
excessive amount of useless memory occupation by instances due to infinite number of
possible attributes.

Nevertheless, if we could restrict the possible class attributes then that would
save a lot of memory. This is achieved using the attribute __slot__.
The tuple assigned to it contains possible attributes. It will not be possible to
add any new attribute at any stage (inside or outside class).
"""

class Rabbit:
    __slots__ = ('x', 'y')

    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = 1

rabbit = Rabbit(1, 2, 3)
# rabbit.w = 1