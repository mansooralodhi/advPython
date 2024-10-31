

import time
import threading

"""
Ways of sharing data:
    1. threading.Event -> boolean variable
    2. threading.Lock -> protecting shared variable
    3. queue.Queue -> share data
    
"""
event = threading.Event()

def read():
    while not event.is_set():
        print("Reading ...")
        time.sleep(1)

def write():
    while not event.is_set():
        print("Writing ...")
        time.sleep(1)
        
if __name__ == "__main__":
    tr_write = threading.Thread(target=write)
    tr_read = threading.Thread(target=read)
    tr_write.start()
    tr_read.start()
    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        event.set() 
        print("Exiting threads ...")