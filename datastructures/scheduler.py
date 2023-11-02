import time

class Scheduler:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task, taskname):
        self.task_queue.append((task, taskname))

    def run(self):
        while self.task_queue:
            task = self.task_queue.pop(0)
            task_function = task[0]
            task_name = task[1]         
            print(f"Task gestartet {task_name}:", task)
            task_function()
            print(f"Task beendet {task_name}:", task)

def task1():
    print("Task 1 gestartet")
    time.sleep(3)
    print("Task 1 beendet")

def task2():
    print("Task 2 gestartet")
    time.sleep(2)
    print("Task 2 beendet")

def task3():
    print("Task 3 gestartet")
    time.sleep(5)
    print("Task 3 beendet")

# Beispielverwendung des Schedulers
scheduler = Scheduler()
scheduler.add_task(task1, "Task1")
scheduler.add_task(task2, "Task2")
scheduler.add_task(task3, "Task3")

scheduler.run()