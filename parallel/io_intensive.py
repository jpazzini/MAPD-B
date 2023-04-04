# io_intensive.py
import time
import urllib.request
import hashlib
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, wait
from multiprocessing import Pool
import os 

def io_function(the_url):
    """ a simple function performing an url request 
        it fetches a remote file and dumps its content
    """
    time_start = time.time()

    # request to access a remote file
    _u = urllib.request.urlopen(the_url, timeout=20)
    data = _u.read()
    
    # create a filename by hashing the file content
    md5 = hashlib.md5()
    md5.update(data)
    file_name = md5.hexdigest()

    # save remote file locally
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

    # list of urls 
    urls = ['https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/IIT_VPU_die.jpg/512px-IIT_VPU_die.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Intel_A80386DX-20_CPU_Die_Image.jpg/512px-Intel_A80386DX-20_CPU_Die_Image.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/IBM_Blue_Gene_P_supercomputer.jpg/512px-IBM_Blue_Gene_P_supercomputer.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Intel_80486DX2_top.jpg/587px-Intel_80486DX2_top.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/80486dx2-large.jpg/512px-80486dx2-large.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Multiple_Server_.jpg/512px-Multiple_Server_.jpg',
            'https://unsplash.com/photos/JMwCe3w7qKk/download?force=true',
            'https://unsplash.com/photos/ZavLsrP4CDI/download?force=true',
            'https://unsplash.com/photos/CANL3bzp6wU/download?force=true',
            'https://unsplash.com/photos/-9jmFkN-_U4/download?force=true',
            'https://unsplash.com/photos/qOx9KsvpqcM/download?force=true',
            ]

    # checking if the directory pics exist and create it if doesn't
    if not os.path.exists("./pics"):
        os.makedirs("./pics")

    # start a timer
    start = time.time()

    # fetch from all urls 
    for url in urls:
        io_function(url)

    # stop the timer
    end = time.time()

    print()
    print(f'Time taken = {end - start:.2f} sec')

