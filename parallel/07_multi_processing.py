# multi_processing.py
import time
from multiprocessing import Process

def my_sum(a,b):
    """ a simple function summing integers from a to b """
    the_sum = 0    
    for i in range(a,b):
        the_sum += i
    print (f'Sum from {a} to {b} = {the_sum}')

if __name__ == '__main__':
    # common "global" objects
    MIN = 0
    MAX = 100_000_000

    # create 2 processes (actually... sub-processes)
    # both acting on the same function
    # each summing half of the values
    p1 = Process(target=my_sum, args=(MIN,MAX//2,))
    p2 = Process(target=my_sum, args=(MAX//2,MAX,))

    # start a timer
    start = time.time()

    # start both processes
    # process #1 and process #2 are started ~ at the same time 
    # and will be executed concurrently or in parallel (depending on the architecture)
    p1.start()
    p2.start()

    # join both processes 
    # *join* => wait a process to have completed its task
    p1.join()
    p2.join()

    # stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')

