import os

class ChangeDir:

    def __init__(self, newDir):
        self.newDir = newDir
        self.currDir = os.getcwd()

    def __enter__(self):
        os.chdir(self.newDir)
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.currDir)
        pass

with ChangeDir('sampleDir1'):
    print(os.getcwd())

print(os.getcwd())
"""Comment the 'os.chdir(self.currDir)' line in __exit__ and note the difference """
