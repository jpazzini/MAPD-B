# 00_single_threaded.py
import time

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

    # Start a timer
    start = time.time()

    # Run the sum function
    my_sum(MIN, MAX)

    # Stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')
