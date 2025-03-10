# io_intensive_threading.py
import time
import urllib.request
import hashlib
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
from multiprocessing import Pool
import os

def io_function(the_url):
    """ 
    A simple function performing an url request. 
    It fetches a remote file and dumps its content on disk.
    """

    time_start = time.time()

    # Request to access a remote file
    _u = urllib.request.urlopen(the_url, timeout=20)
    data = _u.read()
    
    # Create a filename by hashing the file content
    md5 = hashlib.md5()
    md5.update(data)
    file_name = md5.hexdigest()

    # Save remote file locally
    file = open("./pics/"+file_name+".jpg",'bw')
    file.write(data)
    file.close()

    print (f'time for request and store from url [...]{the_url[-50:]} = {time.time()-time_start:.2f} sec')
    
    
if __name__ == '__main__':
    
    # BTW, for those interested, take a look at the 
    # stack of technologies used by unsplash here:
    #  https://unsplash.com/blog/the-data-stack-at-unsplash/
    # and wikimedia here:
    #  https://wikitech.wikimedia.org/wiki/Data_Engineering

    # List of urls 
    urls = ['https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/IIT_VPU_die.jpg/512px-IIT_VPU_die.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Intel_A80386DX-20_CPU_Die_Image.jpg/512px-Intel_A80386DX-20_CPU_Die_Image.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/IBM_Blue_Gene_P_supercomputer.jpg/512px-IBM_Blue_Gene_P_supercomputer.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Intel_80486DX2_top.jpg/587px-Intel_80486DX2_top.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/80486dx2-large.jpg/512px-80486dx2-large.jpg',
            'https://unsplash.com/photos/JMwCe3w7qKk/download?force=true',
            'https://unsplash.com/photos/ZavLsrP4CDI/download?force=true',
            'https://unsplash.com/photos/CANL3bzp6wU/download?force=true',
            'https://unsplash.com/photos/-9jmFkN-_U4/download?force=true',
            'https://unsplash.com/photos/qOx9KsvpqcM/download?force=true',
            ]

    # Checking if the directory pics exist and create it if it doesn't
    if not os.path.exists("./pics"):
        os.makedirs("./pics")

    # Start a timer
    start = time.time()

    # Define the number of threads 
    N_THREADS = 4

    # Create an executor for a number of threads
    executor = ThreadPoolExecutor(max_workers=N_THREADS)

    # Submit the applications as multiple threads 
    futures = [executor.submit(io_function, url) for url in urls]   

    # Wait for all threads to be done
    wait(futures)

    # Stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')

