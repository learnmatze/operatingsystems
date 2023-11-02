class Process:    
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

    def run(self, time):
        print(f"Process {self.pid} is executing at time {time}.")        

def sjn_scheduler(processes):
    process_list = []
    current_time = 0
    while processes:
        runnable_processes = [p for p in processes if p.arrival_time <= current_time]
        print(f"At current_time {current_time} the following processes are startable:")
        for pro in runnable_processes:
            print(f"pid {pro.pid}, arrival_time {pro.arrival_time}, burst_time {pro.burst_time}")        
        if not runnable_processes:
            current_time += 1
            continue
        shortest_job = min(runnable_processes, key=lambda p: p.burst_time)
        current_time += 2  # Execute for a quantum of 2
        shortest_job.remaining_time -= 2
        shortest_job.run(current_time)
        process_list.append(f"Process {shortest_job.pid} executed at {current_time}")

        if shortest_job.remaining_time <= 0:
            processes.remove(shortest_job)
    return process_list

def str_scheduler(processes):
    process_list = []
    current_time = 0
    while processes:
        runnable_processes = [p for p in processes if p.arrival_time <= current_time]
        print(f"At current_time {current_time} the following processes are startable:")
        for pro in runnable_processes:
            print(f"pid {pro.pid}, arrival_time {pro.arrival_time}, burst_time {pro.burst_time}, remaning_time {pro.remaining_time}")        
        if not runnable_processes:
            current_time += 1
            continue
        shortest_remaining_time_job = min(runnable_processes, key=lambda p: p.remaining_time)
        current_time += 2  # Execute for a quantum of 2
        shortest_remaining_time_job.remaining_time -= 2
        shortest_remaining_time_job.run(current_time)
        process_list.append(f"Process {shortest_remaining_time_job.pid} executed at {current_time}")

        if shortest_remaining_time_job.remaining_time <= 0:
            processes.remove(shortest_remaining_time_job)
    return process_list

if __name__ == "__main__":
    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 6),
        Process(4, 4, 4),
    ]

    print("SJN Scheduler:")
    processes_sjn = processes.copy()
    process_list = sjn_scheduler(processes_sjn)
    print("Process execution list for SJN:")
    for process in process_list:
        print(process)    

    processes = [
        Process(1, 0, 5),
        Process(2, 1, 3),
        Process(3, 2, 6),
        Process(4, 4, 4),
    ]
    print("\n")
    print("STR Scheduler:")
    processes_str = processes.copy()
    process_list = str_scheduler(processes_str)
    print("Process execution list for STR:")
    for process in process_list:
        print(process)    
