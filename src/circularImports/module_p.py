# module_p.py
from lazy_import import lazy_module
my_module = lazy_module("src.circularImports.module_q")

class P(object):
    def func(self):
        # Fixme:
        #       AttributeError: module 'src.circularImports.module_q' has no attribute 'Q'.
        #       the below strategy works in baseNode.py in principleMathematics repository.
        print(my_module.Q)
        pass
P().func()