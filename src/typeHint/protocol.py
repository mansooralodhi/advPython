from typing import Protocol
from typing_extensions import runtime_checkable

class Drawable(Protocol):
    """
    If an argument hints type Drawable than it is expected
    to have the implemented function as those in the class
    Drawable.
    This is not a constraint/restriction and will not
    through error unless and until there is a logical error.
    """
    def draw(self) -> None:
        pass

class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Square:
    def draw(self) -> None:
        print("Drawing a square")

def draw_shape(shape: Drawable) -> None:
    shape.draw()

circle = Circle()
square = Square()

print(isinstance(circle, Drawable))
print(isinstance(circle, Drawable))
draw_shape(circle)  # Output: Drawing a circle
draw_shape(square)  # Output: Drawing a square
