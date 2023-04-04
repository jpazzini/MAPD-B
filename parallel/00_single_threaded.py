# single_threaded.py
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

    # start a timer
    start = time.time()

    # run the sum function
    my_sum(MIN, MAX)

    # stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')