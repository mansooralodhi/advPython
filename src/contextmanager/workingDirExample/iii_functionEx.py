import os
from contextlib import contextmanager

"""
Note: 
    we use the 'contextmanager' decorator to decorate a generator function
"""

@contextmanager
def changeDir(newDir):
    """
    compared to OpenFile class example (ii)
    1. __enter__: every thing before yield statement
    2. __exit__: every thing after yield statement
    """
    try:
        cwd = os.getcwd()
        os.chdir(newDir)
        yield
    finally:
        os.chdir(cwd)


print(os.getcwd())

with changeDir('sampleDir1'):
    print(os.getcwd())

with changeDir('sampleDir2'):
    print(os.getcwd())


print(os.getcwd())
"""Comment the 'os.chdir(self.currDir)' line in __exit__ and note the difference """
