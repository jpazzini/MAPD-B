# 09_multi_processing_pool_starmapasync.py
import time
from multiprocessing import Pool

def my_sum(a, b):
    """A simple function summing integers from a to b."""
    the_sum = 0    
    for i in range(a, b):
        the_sum += i
    print(f'Sum from {a} to {b} = {the_sum}')
    return the_sum

if __name__ == '__main__':
    # Common "global" objects
    MIN = 0
    MAX = 100_000_000

    # Define the number of processes
    N_PROCESSES = 4

    # Start a timer
    start = time.time()

    # Create a pool of processes
    pool = Pool(N_PROCESSES)

    # Submit multiple instances of the function `my_sum` 
    # - starmap_async: allows running the processes with a (iterable) list of arguments
    # - map_async    : is a similar function, supporting a single argument
    future_results = pool.starmap_async(my_sum, [(MIN + _*(MAX - MIN)//N_PROCESSES, MIN + (_+1)*(MAX - MIN)//N_PROCESSES) \
                                                 for _ in range(N_PROCESSES)])
    
    # The `map_async` and `starmap_async` functions are **on-blocking**
    #
    # This means that the main program execution will continue 
    # while the mapped functions are run concurrently
    while future_results.ready() is False:
        """ If the sub-processes are not done, sleep 0.1 second and print something """
        time.sleep(0.1)
        print("Still not ready yet")
    
    # To get the results, all processes must have been completed
    # The `get()` function is therefore **blocking** (equivalent to `join`) 
    results = future_results.get()

    # Get the results
    print(f'List of process results: {results}')
    print(f'Total sum = {sum(results)}')

    # Stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')
