import multiprocessing
import time
import random

# Function to be run by each child process
def worker_function(process_num, shared_value):
    print(f"Process {process_num} started")
    sleep_time  = random.uniform(100,200)
    time.sleep(sleep_time)
    shared_value.value += process_num  # Modify the shared value    
    print(f"Process {process_num} finished")

if __name__ == "__main__":
    num_processes = 4
    shared_value = multiprocessing.Value("i", 0)  # Shared integer value
    # Create and start child processes
    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker_function, args=(i, shared_value))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
    print(f"Final shared value: {shared_value.value}")