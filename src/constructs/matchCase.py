

def checkDtype(obj):
    match obj:
        case int(obj) | float(obj):
            print("A number")
        case str(obj):
            print("A string")
        case _:
            # default (else) case
            print("Unknown object type")
        # NB, case doesn't accept 'and' 'or' but only '|'
        # case int(obj) or float(obj):
        #     print("A number")


checkDtype(42.0)
checkDtype('man')
