# 07_multi_processing.py
import time
from multiprocessing import Process

def my_sum(a, b):
    """A simple function summing integers from a to b."""
    the_sum = 0    
    for i in range(a, b):
        the_sum += i
    print(f'Sum from {a} to {b} = {the_sum}')

if __name__ == '__main__':
    # Common "global" objects
    MIN = 0
    MAX = 100_000_000

    # Create 2 processes (actually... "sub-processes")
    #
    # Both acting on the same function
    # Each summing half of the values
    p1 = Process(target=my_sum, args=(MIN, MAX//2,))
    p2 = Process(target=my_sum, args=(MAX//2, MAX,))

    # Start a timer
    start = time.time()

    # Start both processes
    #
    # Process #1 and Process #2 are started ~ at the same time 
    # and will be executed concurrently or in parallel (depending on the architecture)
    # 
    # `process.start()` is a **non-blocking** operation 
    p1.start()
    p2.start()

    # Join both processes 
    p1.join()
    p2.join()

    # Stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')
