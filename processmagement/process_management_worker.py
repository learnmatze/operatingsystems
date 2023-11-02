import multiprocessing
import os
import time

def worker_function(process_num):
    print(f"Process {process_num} started, PID: {os.getpid()}")
    # Simulate a CPU-intensive task
    for _ in range(10**9):
        pass
    print(f"Process {process_num} finished")

if __name__ == "__main__":
    num_processes = 4

    # Create and start child processes
    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target=worker_function, args=(i,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have completed.")