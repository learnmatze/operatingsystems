class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.shortest_remaining_time = burst_time  # Initialize shortest_remaining_time

    def run(self, time):
        print(f"Process {self.pid} is executing at time {time}.")

def str_scheduler(processes):
    current_time = 0
    while processes:
        # Find the process with the shortest remaining burst time among the arrived processes
        runnable_processes = [p for p in processes if p.arrival_time <= current_time]
        print(f"At current_time {current_time} the following processes are startable:")
        for pro in runnable_processes:
            print(f"pid {pro.pid}, arrival_time {pro.arrival_time}, burst_time {pro.burst_time}, shortest_remaning_time {pro.shortest_remaining_time}")
        if not runnable_processes:
            current_time += 1
            continue
        shortest_remaining_time_job = min(runnable_processes, key=lambda p: p.shortest_remaining_time)
        # Execute the selected process
        current_time += shortest_remaining_time_job.burst_time
        shortest_remaining_time_job.run(current_time)
        # Update the remaining burst times for other processes
        for p in processes:
            if p != shortest_remaining_time_job and p.arrival_time <= current_time:
                p.shortest_remaining_time = p.shortest_remaining_time - shortest_remaining_time_job.burst_time
        # Remove the executed process from the list
        processes.remove(shortest_remaining_time_job)

if __name__ == "__main__":
    # Create a list of processes with arrival times and burst times
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 6),
        Process(4, 4, 2),
    ]
    # Execute the processes using Shortest Time Remaining (STR) scheduling
    str_scheduler(processes)