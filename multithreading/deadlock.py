import threading
import time

# Zwei Ressourcen
resource1 = threading.Lock()
resource2 = threading.Lock()

# Funktion für den ersten Thread
def thread1():
    print("Thread 1: Versuche Ressource 1 zu sperren")
    resource1.acquire()
    time.sleep(1)  # Warte eine Sekunde, um den anderen Thread zu starten
    print("Thread 1: Ressource 1 gesperrt. Versuche Ressource 2 zu sperren.")
    resource2.acquire()
    print("Thread 1: Beide Ressourcen gesperrt.")

# Funktion für den zweiten Thread
def thread2():
    print("Thread 2: Versuche Ressource 2 zu sperren")
    resource2.acquire()
    time.sleep(1)  # Warte eine Sekunde, um den anderen Thread zu starten
    print("Thread 2: Ressource 2 gesperrt. Versuche Ressource 1 zu sperren.")
    resource1.acquire()
    print("Thread 2: Beide Ressourcen gesperrt.")

# Erstelle und starte die Threads
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)
t1.start()
t2.start()

# Warte auf das Ende der Threads
t1.join()
t2.join()