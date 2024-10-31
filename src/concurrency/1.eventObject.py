
import time
import threading

"""
event object has a boolean value and is shared amoung threads (tbd later) and could be used for many purpsoe.
"""

stop_flag = threading.Event()
print(f"1 - Stop flag :  {stop_flag.is_set()}")


def read():
    while not stop_flag.is_set():
        print(f"2 - Stop flag :  {stop_flag.is_set()}")
        time.sleep(1)

if __name__ == "__main__":
    tr = threading.Thread(target=read)
    tr.start()
    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Keyboard Interrupt ...")
        print(f"3 - Stop flag :  {stop_flag.is_set()}")
        stop_flag.set()
        print(f"4 - Stop flag :  {stop_flag.is_set()}")


""" Terminal Output:
    1 - Stop flag :  False
    2 - Stop flag :  False
    2 - Stop flag :  False
    2 - Stop flag :  False
    Keyboard Interrupt ...
    3 - Stop flag :  False
    4 - Stop flag :  True
"""