import time
import random

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def run(self):
        print(f"Process {self.pid} is executing.")
        sleep_time  = random.uniform(1,10)
        time.sleep(sleep_time)
        print(f"Process {self.pid} has finished.")

def fcfs_scheduler(processes):
    current_time = 0
    for process in processes:
        if process.arrival_time > current_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        process.run()

if __name__ == "__main__":
    # Create a list of processes with arrival times and burst times
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 6),
        Process(4, 4, 4),
    ]
    # Execute the processes using FCFS scheduling
    fcfs_scheduler(processes)