# SuperFastPython.com
# example of thread starvation
from time import sleep
from threading import Thread
from threading import Lock

# create shared lock
lock = Lock()
 
# long task
def long_task(lock, identifier):
    # acquire lock
    with lock:
        # execute long task
        for i in range(30):
            # simulate effort
            print(f'Thread {identifier} processing long Task')
            sleep(1)

# long task
def short_task(lock, identifier):
    # acquire lock
    with lock:
        # execute short task
        for i in range(5):
            # simulate effort
            print(f'Thread {identifier} processing short Task')
            sleep(1)            

# create two worker threads
long_thread = Thread(target=long_task, args=(lock, 1))
short_thread = Thread(target=short_task, args=(lock, 2))

long_thread.start()
short_thread.start()

long_thread.join()
short_thread.join()

print(f"The main Programm ended.")