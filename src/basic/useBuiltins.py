"""
This module provides direct access to all ‘built-in’ identifiers of Python;
for example, builtins.map is the full name for the built-in function map().
There is also another builtin method called 'slice' which may wish to explore.
"""
import builtins

def map(x):
    return builtins.map(float, x)

x = [1, 2, 2]
print(f"Original : {x}")                    # Original : [1, 2, 2]
print(f"Mapped : {[i for i in map(x)]}")    # Mapped : [1.0, 2.0, 2.0]
