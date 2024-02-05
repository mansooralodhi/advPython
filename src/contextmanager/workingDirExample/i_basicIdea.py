import os

"""
Problem:    
        every time we need to switch between child directories, 
        we need to keep record of the current directory.
        this is a tear-down example.
        we want to remember the working directory while switching
        between child directories temporarily.
"""

# os.chdir -> change directory
# os.getcwd -> get current working directory

cwd = os.getcwd()
print(os.getcwd())

os.chdir('sampleDir1')

# note: cwd changes to 'sampleDir1'
print(os.getcwd())

# os.chdir('sampleDir2')
# problem: sampleDir2 can't be found

# solution: change the cwd to previous one
os.chdir(cwd)
os.chdir('sampleDir2')
print(os.getcwd())