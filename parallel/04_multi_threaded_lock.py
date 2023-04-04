# multi_threaded_lock.py
import time
import threading
from threading import Thread
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
            # the thread acquires the lock
            the_lock.acquire()
            
            # code that could result in race condition
            #--------------------- 
            COMMON_COUNTER += 1
            COMMON_LIST.append(i)
            #---------------------
            
            # the thread releases the lock
            # remember to release the lock in order to avoid deadlock conditions
            the_lock.release()

    print (f'Sum from {a} to {b} = {the_sum}')

if __name__ == '__main__':
    # common "global" objects
    MIN = 0
    MAX = 100_000_000
    MOD = 1397
    COMMON_COUNTER = 0 
    COMMON_LIST    = [] 

    # create a thread lock
    LOCK = Lock()

    # create 2 threads
    # both acting on the same function
    # each summing half of the values
    t1 = Thread(target=my_sum_mod, args=(LOCK,MIN,MAX//2,MOD))
    t2 = Thread(target=my_sum_mod, args=(LOCK,MAX//2,MAX,MOD))

    # start a timer
    start = time.time()

    # start both threads  
    # thread #1 and thread #2 are started ~ at the same time 
    # and will be executed concurrently or in parallel (depending on the architecture)
    t1.start()
    t2.start()

    # join both threads 
    # *join* => wait a thread to have completed its task  
    t1.join()
    t2.join()

    # stop the timer
    end = time.time()

    print()
    print(f'Number of multiples of {MOD} in the sum from {MIN} to {MAX} = {COMMON_COUNTER}')
    print()
    print(f'First 100 items of the list of multiples of {MOD}:')
    print(COMMON_LIST[:100])
    print()
    print(f'Cross-check of the size of the list: {len(COMMON_LIST)}')
    print()
    print(f'Time taken = {end - start:.2f} sec')
