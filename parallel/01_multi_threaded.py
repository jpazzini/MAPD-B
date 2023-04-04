# multi_threaded.py
import time
from threading import Thread

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
    # 
    # thread start is a _non-blocking_ operation 
    # => the program creates the threads and proceeds onward without blocking its execution
    t1.start()
    t2.start()

    # join both threads 
    # *join* => wait for a thread to have completed its task
    #
    # what would it happen if we removed the join call and execute the script?
    t1.join()
    t2.join()

    # stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')
