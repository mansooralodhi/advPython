

import re

def bitSec_to_byteSec(val: str) -> int:
    val = val.upper().strip()
    if re.search('KB[P,/]S', val):
        return int(float(re.sub('KB[P,/]S', '', val))  * 1024) // 8
    elif re.search('MB[P,/]S', val):
        return int(float(re.sub('MB[P,/]S', '', val))  * 1048576) // 8  
    elif re.search('GB[P,/]S', val):
        return int(float(re.sub('GB[P,/]S', '', val))  * 1073741824) // 8  
    else:
        raise Exception(f"Unknow units encountered in '{val}'")
    
def bit_to_byte(val: str) -> int:
    if re.search('bits', val.lower().strip()):
        return int(re.sub('bits', '', val.lower().strip())) // 8
    else:
        raise Exception(f"Unknow units encountered in '{val}'.")
