class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def run(self, time, quantum):
        if self.remaining_time <= quantum:
            print(f"Process {self.pid} is executing at time {time}.")
            time += self.remaining_time
            self.remaining_time = 0
        else:
            print(f"Process {self.pid} is executing at time {time}. Time quantum expired.")
            time += quantum
            self.remaining_time -= quantum
        return time

def round_robin_scheduler(processes, quantum):
    current_time = 0
    while processes:
        for process in processes.copy():
            if process.remaining_time > 0:
                current_time = process.run(current_time, quantum)
                if process.remaining_time == 0:
                    processes.remove(process)
            else:
                processes.remove(process)

if __name__ == "__main__":
    # Create a list of processes with burst times
    processes = [
        Process(1, 10),
        Process(2, 5),
        Process(3, 8),
        Process(4, 2),
    ]
    quantum = 3  # Set the time quantum for Round Robin
    # Execute the processes using Round Robin scheduling
    round_robin_scheduler(processes, quantum)