# multi_threaded_local_data.py
import time
import threading
from threading import Thread

def my_sum(a,b):
    """ a simple function summing integers from a to b """
    
    # create an instance of local (per-thread) memory 
    # now "the_sum" is *explicitely* thread-specific
    the_sum = threading.local() 

    the_sum = 0    
    for i in range(a,b):
        the_sum += i
    print (f'Sum from {a} to {b} = {the_sum}')

if __name__ == '__main__':
    # common "global" objects
    MIN = 0
    MAX = 100_000_000

    # create 2 threads
    # both acting on the same function
    # each summing half of the values
    t1 = Thread(target=my_sum, args=(MIN,MAX//2,))
    t2 = Thread(target=my_sum, args=(MAX//2,MAX,))

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
    print(f'Time taken = {end - start:.2f} sec')
