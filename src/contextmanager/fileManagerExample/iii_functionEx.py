
from contextlib import contextmanager

"""
Note: 
    we use the 'contextmanager' decorator to decorate a generator function
"""

@contextmanager
def openFileV1(file, mode):
    """
    compared to OpenFile class example (ii)
    1. __enter__: every thing before yield statement
    2. __exit__: every thing after yield statement
    """
    f = open(file, mode) # setup of contextmanager
    yield f
    f.close()

@contextmanager
def openFileV2(file, mode):
    try:
        f = open(file, mode) # setup of contextmanager
        yield f
    finally:
        # tear down code
        f.close()


with openFileV2('bin.txt', 'w') as f:
    f.write("Bullshit !")

print(f.closed)