# multi_threaded_pool_lock.py
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
import threading
from threading import Lock

def my_sum_mod(the_lock,a,b,m):
    """ a simple function summing integers from a to b 
        also check whether the current value is a multiple of m; if so:
          - add +1 to a common counter 
          - store the current value in a common list
    """
    # use the COMMON_COUNTER and COMMON_LIST variables, common to all threads
    global COMMON_COUNTER
    global COMMON_LIST

    # create an instance of local (per-thread) memory 
    # now "the_sum" is *explicitely* thread-specific
    the_sum = threading.local() 

    the_sum = 0    
    for i in range(a,b):
        the_sum += i
        if i%m == 0:
            the_lock.acquire()
            COMMON_COUNTER += 1
            COMMON_LIST.append(i)
            the_lock.release()

    print (f'summing from {a} to {b} = {the_sum}')
    
    # concurrent.futures includes also an easy way to handle return values
    return the_sum

if __name__ == '__main__':
    # common "global" objects
    MIN = 0
    MAX = 100_000_000
    MOD = 1397
    COMMON_COUNTER = 0 
    COMMON_LIST    = [] 

    # create a thread lock
    LOCK = Lock()

    # define the number of threads 
    N_THREADS = 4

    # create an executor for a number of threads
    executor = ThreadPoolExecutor(max_workers=N_THREADS)

    # start a timer
    start = time.time()

    # submit the applications as multiple threads 
    futures = [executor.submit(my_sum_mod,
                                LOCK,
                                MIN+     _*(MAX-MIN)//N_THREADS,
                                MIN+ (_+1)*(MAX-MIN)//N_THREADS,
                                MOD) for _ in range(executor._max_workers)]   

    # wait for all threads to be done
    wait(futures)

    # stop the timer
    end = time.time()

    # get the thread results and the total sum
    results = [f.result() for f in futures]
    total_sum = sum(results)
        
    print()
    print(f'Total sum = {total_sum}')
    print()
    print(f'Number of multiples of {MOD} in the sum from {MIN} to {MAX} = {COMMON_COUNTER}')
    print()
    print(f'First 100 items of the list of multiples of {MOD}:')
    print(COMMON_LIST[:100])
    print()
    print(f'Cross-check of the size of the list: {len(COMMON_LIST)}')
    print()
    print(f'Time taken = {end - start:.2f} sec')
