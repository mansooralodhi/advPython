

class A: pass

class B(A): pass


print(  type(A()) ==  A )       # True
print(  type(B()) ==  B )       # True
print(  type(B()) ==  A )       # False
print(  isinstance(B(),  A) )   # True -> note the difference from 'type'
print(  isinstance(B(),  B) )   # True

"""
NB: 'type' only check latest type while 'isinstance' also checks the parent types.
"""