# 02_multi_threaded_local_data.py
import time
import threading
from threading import Thread

def my_sum(a, b):
    """A simple function summing integers from a to b."""
    
    # Create an instance of local (per-thread) memory 
    # Now "the_sum" is **explicitly** thread-specific
    the_sum = threading.local() 

    the_sum = 0    
    for i in range(a, b):
        the_sum += i
    print(f'Sum from {a} to {b} = {the_sum}')

if __name__ == '__main__':
    # Common "global" objects
    MIN = 0
    MAX = 100_000_000

    # Create 2 threads
    t1 = Thread(target=my_sum, args=(MIN, MAX//2,))
    t2 = Thread(target=my_sum, args=(MAX//2, MAX,))

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

    print()
    print(f'Time taken = {end - start:.2f} sec')
