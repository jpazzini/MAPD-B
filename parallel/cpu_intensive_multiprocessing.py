# cpu_intensive_multiprocessing.py
import time
import math
import random
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
from multiprocessing import Pool

def f(x):
    return (math.sin(1/(x*(2-x))))**2
            
def cpu_function(seed):
    """ a simple function performing an MC integration 
        of a function taking as input a given seed
    """
    time_start = time.time()

    # number of point to generate
    _n = 2_000_000

    # initialize a local random number generator
    local_random = random
    local_random.seed(seed)

    # perform the numerical integration
    _count = 0
    for _ in range(_n):
        x = 2*local_random.random()
        y = local_random.random()
        if y < f(x):
            _count+=1

    print (f'time to perform numerical integration over {_n} entries = {time.time()-time_start:.2f} sec')

    # return the count
    return (_count, _n)
    
    
if __name__ == '__main__':
    
    # start a timer
    start = time.time()

    # define the number of processes 
    N_PROCESSES = 4

    # number of chunks
    n_chunks = 10

    # total number of points and count
    total_n = 0
    total_count = 0

    # """ Pool + map alternative """
    # # create a pool of processes
    # pool = Pool(N_PROCESSES)

    # # submit multiple instances of the function  
    # future_results = pool.map_async(cpu_function, [_ for _ in range(n_chunks)])
    
    # # to get the results all processes must have been completed
    # # the get() function is therefore _blocking_ (equivalent to join) 
    # results = future_results.get()
    # """ --- """

    """ alternative based on concurrent.futures library """
    # create an executor for a number of threads
    executor = ProcessPoolExecutor(max_workers=N_PROCESSES)

    # submit the applications as multiple threads 
    futures = [executor.submit(cpu_function, _) for _ in range(n_chunks)]   

    # wait for all threads to be done
    wait(futures)

    # get the thread results and the total sums
    results = [f.result() for f in futures]
    """ --- """  
    
    
    for res in results:
        total_count += res[0]
        total_n += res[1]
    
    # compute the integral
    integral = 2*total_count/total_n

    # stop the timer
    end = time.time()
    
    print()
    print(f'Integral evaluated over {total_n} points = {integral}')
    print()
    print(f'Time taken = {end - start:.2f} sec')

