# from b import B # note this gives error. uncomment and checkout yourself.

class A(object):
    @staticmethod
    def catchme():
        from b import B
        return B()