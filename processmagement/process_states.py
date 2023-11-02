import random
import threading
import time

class Process:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.state = "New"  # Initial state

    def run(self):
        while self.state != "Finished":
            if self.state == "New":
                self.state = "Ready"
            elif self.state == "Ready":
                random_value = random.random()
                # print(random_value)
                if random_value < 0.7:  # Simulate blocking
                    self.state = "Blocked"
                else:
                    self.state = "Finished"
            elif self.state == "Blocked":
                random_value = random.random()
                # print(random_value)
                if random_value < 0.8:  # Simulate unblocking
                    self.state = "Ready"
            elif self.state == "Finished":
                pass
            print(f"Process {self.name} (PID: {self.pid}) is now in the {self.state} state.")
            time.sleep(1)
        print(f"***** Process {self.name} (PID: {self.pid}) has FINISHED. *****")


def process_thread(process):
    process.run()

def main():
    num_processes = 5
    processes = [Process(pid, f"Process-{pid}") for pid in range(1, num_processes + 1)]
    threads = []

    for process in processes:
        thread = threading.Thread(target=process_thread, args=(process,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print(f"All {num_processes} Processes have FINISHED execution.")

if __name__ == "__main__":
    main()