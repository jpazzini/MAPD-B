# 03_multi_threaded_nolock.py
import time
import threading
from threading import Thread
from colorama import Fore, Style

def my_sum_mod(a, b, m):
    """A simple function summing integers from a to b.

    Also check whether the current value is a multiple of `m`; if so:
      - add +1 to a common counter `COMMON_COUNTER`
      - store the current value in a common list `COMMON_LIST`
    """

    # Use the `COMMON_COUNTER` and `COMMON_LIST` variables, common to all threads
    global COMMON_COUNTER
    global COMMON_LIST

    the_sum = threading.local() 

    the_sum = 0    
    for i in range(a, b):
        the_sum += i
        if i % m == 0:
            # Modify the common objects
            COMMON_COUNTER += 1
            COMMON_LIST.append(i)

    print(f'Sum from {a} to {b} = {the_sum}')

if __name__ == '__main__':
    # Common "global" objects
    MIN = 0
    MAX = 100_000_000
    MOD = 1397
    COMMON_COUNTER = 0 
    COMMON_LIST    = [] 

    # Create 2 threads
    t1 = Thread(target=my_sum_mod, args=(MIN, MAX//2, MOD))
    t2 = Thread(target=my_sum_mod, args=(MAX//2, MAX, MOD))

    # Start a timer
    start = time.time()

    # Start both threads  
    t1.start()
    t2.start()

    # Join both threads 
    t1.join()
    t2.join()

    # Stop the timer
    end = time.time()

    # Verify if the `COMMON_COUNTER` is equal to the length of `COMMON_LIST`
    if COMMON_COUNTER != len(COMMON_LIST):
        print(Fore.RED + Style.BRIGHT)
    print()
    print(f'Number of multiples of {MOD} in the sum from {MIN} to {MAX} = {COMMON_COUNTER}')
    print()
    print(f'First 100 items of the list of multiples of {MOD}:')
    print(COMMON_LIST[:100])
    print()
    print(f'Cross-check of the size of the list: {len(COMMON_LIST)}')
    print()
    print(f'Time taken = {end - start:.2f} sec')
    print(Style.RESET_ALL)
