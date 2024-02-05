


################# One way of writing something in file ###################

f = open('bin.txt', 'w')
f.write("This is bullshit !")
f.close()

################# Another way of writing something in file################

with open('bin.txt', 'w') as f:
    f.write("This is bullshit!")


######################### Take Away  #####################
"""
- The recommended way of writing a file is the second method.
- The second method is the context manager because of with statement
- Benefit of using second method or the context manager:
    - Don't need to remember to close down the file
    - If error is encountered during writing, the file gets closed properly
    - Handles tear down of resources
    
Other usage of context manager:
    - Connect to and close databases automatically.
    - acquire and release locks

"""