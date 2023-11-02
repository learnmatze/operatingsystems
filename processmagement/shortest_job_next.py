class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    def run(self, time):
        print(f"Process {self.pid} is executing at time {time}.")

def sjn_scheduler(processes):
    current_time = 0
    while processes:
        # Find the process with the shortest burst time among the arrived processes
        runnable_processes = [p for p in processes if p.arrival_time <= current_time]
        # print(f"At current_time {current_time} the following processes are startable:")
        # for pro in runnable_processes:
        #     print(f"pid {pro.pid}, arrival_time {pro.arrival_time}, burst_time {pro.burst_time}")
        if not runnable_processes:
            current_time += 1
            continue
        shortest_job = min(runnable_processes, key=lambda p: p.burst_time)
        print(f"the process with the shortest burst_time {shortest_job.pid}, {shortest_job.arrival_time}, {shortest_job.burst_time}")
        # Execute the selected process
        current_time += shortest_job.burst_time
        # print(f"Found Process {shortest_job.pid} with arrival time {shortest_job.arrival_time} with burst time {shortest_job.burst_time} started at: {current_time} ")
        shortest_job.run(current_time)
        # Remove the executed process from the list
        processes.remove(shortest_job)

if __name__ == "__main__":
    # Create a list of processes with arrival times and burst times
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 6),
        Process(4, 4, 2),
    ]
    # processes = [
    #     Process(1, 0, 4),
    #     Process(2, 1, 5),
    #     Process(3, 2, 6),
    #     Process(4, 3, 4),
    # ]
    # Execute the processes using SJN (SJF) scheduling
    sjn_scheduler(processes)