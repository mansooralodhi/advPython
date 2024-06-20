


from functools import partial

"""
-   The significance of transforming original function using partial is the fact that
    you can easily ignore the required argument once you set their values.
-   These arguments are made constant like anyother default keyword argument. 
-   The only difference is that now you set the default/constant value rather then the producer.
-   Lambda does similar thing however, it only returns single values and it might be difficult
    to read and understand and also debug.
-   In mathematics (gradient computation), it can be used to turn some parameters as static/passive while
    other as active. Specifically it can be used to make_jaxpr of jax.vjp by setting primal argument as
    scalar and later using the jaxexpr with interval inputs for interval-adjonit computation. 
"""

def f(x, m, c):
    return m*x + c

def line(x,m=5, c=1):
    return m*x + c


fx = partial(f, 1, 10)             # sets values for x, m
lx = partial(line, m=1, c=10)      # sets values for x, c

print(fx(c=10))                 # 20
print(lx(x=10))                 # 20