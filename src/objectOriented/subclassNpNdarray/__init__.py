
print("Hello World !")

"""

Also refer to a more broader term, "interoperability of numpy":
    https://numpy.org/doc/stable/user/basics.interoperability.html#basics-interoperability

Three method of initiating subclass object
1.  Explicit constructor call.
2.  View casting.
3.  New from template.

When to use subclassing?
-   personal project
-   no maintainability
-   faster implementation
-   no protocols to follow

Implications of subclassing
-   ndarray.__new__ method for the 
    main work of object initialization, 
    rather then the more usual __init__ method.
-   The second is the use of the 
    __array_finalize__ method to allow 
    subclasses to clean up after the 
    creation of views and new instances from templates. 
"""