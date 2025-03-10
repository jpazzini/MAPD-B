# 01_multi_threaded.py
import time
from threading import Thread

def my_sum(a, b):
    """A simple function summing integers from a to b."""
    the_sum = 0    
    for i in range(a, b):
        the_sum += i
    print(f'Sum from {a} to {b} = {the_sum}')

if __name__ == '__main__':
    # Common "global" objects
    MIN = 0
    MAX = 100_000_000

    # Create 2 threads
    #
    # Both acting on the same function
    # Each summing half of the values
    t1 = Thread(target=my_sum, args=(MIN, MAX//2,))
    t2 = Thread(target=my_sum, args=(MAX//2, MAX,))

    # Start a timer
    start = time.time()

    # Start both threads 
    #
    # Thread #1 and Thread #2 are started ~ at the same time 
    # and will be executed concurrently or in parallel (depending on the architecture)
    # 
    # `thread.start()` is a **non-blocking** operation 
    # i.e. the Python interpreter creates and starts the threads 
    # and proceeds onward the execution of this script without blocking its execution
    t1.start()
    t2.start()

    # Join both threads 
    #
    # `thread.join()` is a **blocking** call 
    # i.e. it waits for a thread to have completed its task before proceeding onward
    #
    # ??? What would happen if we removed the join call and execute the script ???
    t1.join()
    t2.join()

    # Stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')
