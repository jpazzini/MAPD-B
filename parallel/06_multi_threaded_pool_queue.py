# 06_multi_threaded_pool_queue.py
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
import threading
import queue 

def my_sum_mod(the_queue, a, b, m):
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
            # Add (put) the new element into the queue
            #
            # This will block other threads from accessing the same resource 
            # for the duration of the put operation
            #
            # ** Thread-safe **
            the_queue.put(i)
    # Signal that the task is completed in order to 
    # let the queue know that it will receive no other elements
    the_queue.task_done()

    print(f'summing from {a} to {b} = {the_sum}')
    
    return the_sum

if __name__ == '__main__':
    # Common "global" objects
    MIN = 0
    MAX = 100_000_000
    MOD = 1397
    COMMON_COUNTER = 0 
    COMMON_LIST    = [] 

    # Create a thread-safe queue object
    QUEUE = queue.Queue()

    # Define the number of threads 
    N_THREADS = 4

    # Create an executor for a number of threads
    executor = ThreadPoolExecutor(max_workers=N_THREADS)

    # Start a timer
    start = time.time()

    # Submit the applications as multiple threads 
    futures = [executor.submit(my_sum_mod,
                                QUEUE,
                                MIN + _*(MAX - MIN)//N_THREADS,
                                MIN + (_+1)*(MAX - MIN)//N_THREADS,
                                MOD) for _ in range(executor._max_workers)]   

    # Wait for all threads to be done
    wait(futures)

    # Stop the timer
    end = time.time()

    # Get the thread results and the total sum
    results = [f.result() for f in futures]
    total_sum = sum(results)
        
    print()
    print(f'Total sum = {total_sum}')
    print()
    print(f'Size of the Queue object = {QUEUE.qsize()}')
    print()
    print(f'First 100 items of the Queue object:')
    print([QUEUE.get() for _ in range(100)])
    print()
    print(f'Time taken = {end - start:.2f} sec')
