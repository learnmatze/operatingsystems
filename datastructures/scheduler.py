import time
import random

class Scheduler:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task, taskname):
        self.task_queue.append((task, taskname))

    def run(self):
        print(f"Scheduler started.")
        while self.task_queue:
            task = self.task_queue.pop(0)
            task_function = task[0]
            task_name = task[1]         
            print(f"Task gestartet {task_name}:", task)
            task_function()
            print(f"Task beendet {task_name}:", task)
        print(f"Scheduler finished.")

def task1():
    print("Task 1 gestartet")
    sleep_time  = random.uniform(1,5)
    time.sleep(sleep_time)
    print("Task 1 beendet")

def task2():
    print("Task 2 gestartet")
    sleep_time  = random.uniform(1,5)
    time.sleep(sleep_time)
    print("Task 2 beendet")

def task3():
    print("Task 3 gestartet")
    sleep_time  = random.uniform(1,5)
    time.sleep(sleep_time)
    print("Task 3 beendet")

# Beispielverwendung des Schedulers
scheduler = Scheduler()
scheduler.add_task(task1, "Task1")
scheduler.add_task(task2, "Task2")
scheduler.add_task(task3, "Task3")

scheduler.run()