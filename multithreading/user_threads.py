# pip install gevent
import gevent

# Eine einfache Funktion, die von den Threads ausgeführt wird
def thread_function(thread_name):
    for i in range(5):
        print(f"Thread {thread_name} - Iteration {i}")
        gevent.sleep(5)  # Benutzen Sie gevent.sleep anstelle von time.sleep

# Erstellen von User Threads (Greenlets)
thread1 = gevent.spawn(thread_function, "1")
thread2 = gevent.spawn(thread_function, "2")

# Warten auf das Ende der Threads
gevent.joinall([thread1, thread2])

print("Both threads have finished.")