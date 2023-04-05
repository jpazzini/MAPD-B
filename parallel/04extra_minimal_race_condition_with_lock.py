# A minimal race condition example with a lock
import threading

# increment function using a common counter
def increment(max_val=100_000):
    global counter
    global lock
    for i in range(max_val):
        lock.acquire()
        counter += 1
        lock.release()

if __name__ == '__main__':
    # common counter
    counter = 0
    lock = threading.Lock()

    # create and start 10 concurrent threads
    threads = []
    for i in range(10):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    # join all threads
    for t in threads:
        t.join()
        
    print(f"Final value of counter: {counter}")
    
