# multi_processing_pool_starmap.py
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
    # - starmap: allows to run the processes with a (iterable) list of arguments
    # - map    : is a similar function, supporting a single argument
    results = pool.starmap(my_sum, [(MIN+_*(MAX-MIN)//N_PROCESSES , MIN+(_+1)*(MAX-MIN)//N_PROCESSES) \
                                    for _ in range(N_PROCESSES)])
    
    # the map and starmap functions are _blocking_
    #
    # this means that the main program execution will not 
    # get past them until all sub-processes are completed
    
    # get the results
    print(f'List of process results: {results}')
    print(f'Total sum = {sum(results)}')

    # stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')

