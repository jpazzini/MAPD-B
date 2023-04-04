# multi_processing_pool_starmapasync.py
import time
from multiprocessing import Pool

def my_sum(a,b):
    """ a simple function summing integers from a to b """
    the_sum = 0    
    for i in range(a,b):
        the_sum += i
    print (f'Sum from {a} to {b} = {the_sum}')
    return the_sum

if __name__ == '__main__':
    # common "global" objects
    MIN = 0
    MAX = 100_000_000

    # define the number of processes
    N_PROCESSES = 4

    # start a timer
    start = time.time()

    # create a pool of processes
    pool = Pool(N_PROCESSES)

    # submit multiple instances of the function my_sum 
    # - starmap_async: allows to run the processes with a (iterable) list of arguments
    # - map_async    : is a similar function, supporting a single argument
    future_results = pool.starmap_async(my_sum, [(MIN+_*(MAX-MIN)//N_PROCESSES , MIN+(_+1)*(MAX-MIN)//N_PROCESSES) \
                                                 for _ in range(N_PROCESSES)])
    
    # the map_async and starmap_async functions are _non-blocking_
    #
    # this means that the main program execution will continue 
    # while the mapped functions are run concurrently
    while future_results.ready() is False:
        """ if the sub-processes are not done, sleep 0.1 second and print something """
        time.sleep(0.1)
        print("Still not ready yet")
    
    # to get the results all processes must have been completed
    # the get() function is therefore _blocking_ (equivalent to join) 
    results = future_results.get()

    # get the results
    print(f'List of process results: {results}')
    print(f'Total sum = {sum(results)}')

    # stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')

