# A minimal race condition example
import threading

# increment function using a common counter
def increment(max_val=1_000_000):
    global counter
    for i in range(max_val):
        counter += 1
    
if __name__ == '__main__':
    # common counter
    counter = 0

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
    
