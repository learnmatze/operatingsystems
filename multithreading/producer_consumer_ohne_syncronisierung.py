import threading
import time
import random

buffer = []
buffer_size = 5
def producer():
    while True:
        if len(buffer) < buffer_size:
            item = random.randint(1, 100)
            buffer.append(item)
            print(f"Produced {item}, Buffer: {buffer}")
            time.sleep(random.uniform(0.1, 0.5))

def consumer():
    while True:
        if len(buffer) > 0:
            item = buffer.pop(0)
            print(f"Consumed {item}, Buffer: {buffer}")
            time.sleep(random.uniform(0.1, 0.5))

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()