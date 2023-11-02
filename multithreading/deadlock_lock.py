import threading
import time

# Zwei Ressourcen
resource1 = threading.Lock()
resource2 = threading.Lock()

# Funktion für den ersten Thread
def thread1():
    print("Thread 1: Versuche Ressource 1 zu sperren")
    resource1.acquire()
    print("Thread 1: Ressource 1 gesperrt. Warte 1 Sekunden.")
    time.sleep(1)
    print("Thread 1: Versuche Ressource 2 zu sperren.")
    resource2.acquire()
    print("Thread 1: Beide Ressourcen konnten acquired werden.")
    # Hier wird die Arbeit mit den Ressourcen durchgeführt
    time.sleep(3)
    print("Thread 1: Konnte alle Ressourcen bekommen und den Task abarbeiten.")
    resource2.release()
    resource1.release()

# Funktion für den zweiten Thread
def thread2():
    print("Thread 2: Versuche Ressource 1 zu sperren")
    resource1.acquire()
    print("Thread 2: Ressource 1 gesperrt. Warte 2 Sekunden.")
    time.sleep(2)
    print("Thread 2: Versuche Ressource 2 zu sperren.")
    resource2.acquire()
    print("Thread 2: Beide Ressourcen konnten acquired werden.")
    # Hier wird die Arbeit mit den Ressourcen durchgeführt
    time.sleep(2)
    print("Thread 2: Konnte alle Ressourcen bekommen und den Task abarbeiten.")
    resource2.release()
    resource1.release()

# Erstelle und starte die Threads
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()

t1.join()
t2.join()