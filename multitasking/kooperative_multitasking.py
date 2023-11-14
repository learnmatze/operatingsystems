import threading
import time

# Variable to control cooperative switching
cooperative_switch = threading.Event()
cooperative_switch.set()  # Allow the first thread to run

lock = threading.Lock()

# Function for the cooperative threads
def cooperative_task(thread_id):
    while True:
        cooperative_switch.wait()
        with lock:
            print(f"Thread {thread_id} is running.")
        time.sleep(1)
        cooperative_switch.clear()  # Voluntarily yield control
        cooperative_switch.wait()  # Wait for next round

# Create cooperative threads
threads = []
num_threads = 4

for i in range(num_threads):
    thread = threading.Thread(target=cooperative_task, args=(i,))
    threads.append(thread)

# Start the cooperative threads
for thread in threads:
    thread.daemon = True
    thread.start()

try:
    while True:
        # Perform some work in the main thread
        time.sleep(2)
       
        # Allow the next cooperative thread to run
        cooperative_switch.set()
except KeyboardInterrupt:
    print("Program ended.")