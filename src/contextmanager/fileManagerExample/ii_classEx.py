


class OpenFile():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        # runs with 'with' statement
        self.file = open(self.filename, self.mode)
        # returning object in context manager
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # runs when 'with' block exits
        self.file.close()
        pass



with OpenFile('bin.txt', 'w') as f:
    f.write("Bullshit !")


print(f.closed)
"""
comment the 'self.file.close()' line in __exit__ and rerun the file.
"""