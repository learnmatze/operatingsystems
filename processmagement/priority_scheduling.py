class Process:
    def __init__(self, pid, priority, burst_time):
        self.pid = pid
        self.priority = priority
        self.burst_time = burst_time

    def run(self, time):
        while self.burst_time > 0:
            print(f"Process {self.pid} is executing at time {time}.")
            self.burst_time -= 1
            time += 1
        return time

def priority_scheduler(processes):
    current_time = 0
    while processes:
        # Find the process with the highest priority
        highest_priority_process = min(processes, key=lambda p: p.priority)
        # Execute the process with the highest priority
        current_time = highest_priority_process.run(current_time)
        # Remove the executed process from the list
        processes.remove(highest_priority_process)

if __name__ == "__main__":
    # Create a list of processes with priorities and burst times
    processes = [
        Process(1, 3, 5),
        Process(2, 1, 3),
        Process(3, 2, 6),
        Process(4, 4, 4),
    ]
    # Execute the processes using Priority Scheduling
    priority_scheduler(processes)