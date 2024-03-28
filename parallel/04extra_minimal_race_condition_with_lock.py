# 04extra_minimal_race_condition_with_lock.py
import threading

# Increment function using a common counter
def increment(max_val=1_000_000):
    global counter
    for _ in range(max_val):
        lock.acquire()
        counter += 1
        lock.release()
    
if __name__ == '__main__':
    # Common counter
    counter = 0
    lock = threading.Lock()

    # Create and start 10 concurrent threads
    threads = []
    for i in range(10):
        t = threading.Thread(target=increment)
        threads.append(t)
        t.start()

    # Join all threads
    for t in threads:
        t.join()
        
    print(f"Final value of counter: {counter}")