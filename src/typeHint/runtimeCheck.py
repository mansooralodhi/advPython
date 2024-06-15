
import abc
from typing import Protocol
from typing_extensions import runtime_checkable

"""
If an argument hints type Drawable than it is expected
to have the implemented function as those in the class
Drawable.
This is not a constraint/restriction and will not
through error unless and until there is a logical error.
However, if you want to check that the Circle and
Square class objects follow the same methods as Drawable
then you can check do it using isinstance(..., Drawable)
once you have decorated the class Drawable with
@runtime_checkable.
NB: the methods may not have to be same signature.
If you want the methods to be of same signature then
you need to create another type hint.
NB: you don't need to decorate the method as abstractmethod
because the Drawable class is never inherited, however, it 
would be a good practise to do so.. 
"""


@runtime_checkable
class Drawable(Protocol):
    @abc.abstractmethod
    def draw(self, x) -> None:
        pass

    # def paint(self)-> None:
    #     pass

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def lets_draw(self) -> None:
        print("Drawing a square")


# Now we can perform runtime checks
circle = Circle()
square = Square()

print(isinstance(circle, Drawable))  # Output: True
print(isinstance(square, Drawable))  # Output: False