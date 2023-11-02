import threading
import time

# Eine einfache Funktion, die von den Threads ausgeführt wird
def thread_function(thread_name):
    for i in range(5):
        print(f"Thread {thread_name} - Iteration {i}")
        time.sleep(5)

# Erstellen von Threads
thread1 = threading.Thread(target=thread_function, args=("1",))
thread2 = threading.Thread(target=thread_function, args=("2",))

# Starten der Threads
thread1.start()
thread2.start()

# Warten auf das Ende der Threads
thread1.join()
thread2.join()

print("Both threads have finished.")