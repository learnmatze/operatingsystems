import threading
import time
import random

# demonstrating the use of a lock to protect shared ressources
# Gemeinsam genutzte Ressource
shared_resource = 0

# Mutex erstellen
mutex = threading.Lock()

# Funktion für den Zugriff auf die geschützte Ressource
def access_shared_resource(thread_id):
    global shared_resource
    time.sleep(1)

    # for _ in range(5):  # Fünf Iterationen für jedes Thread
    #     # Mutex sperren
    #     with mutex:
    #         print(f"Thread {thread_id} sperrt den Mutex.")
    #         current_value = shared_resource
    #         time.sleep(0.1)  # Simuliert eine längere Berechnung
    #         shared_resource = current_value + 1
    #         print(f"Thread {thread_id} entsperrt den Mutex. Gemeinsame Ressource: {shared_resource}")

    for _ in range(5):  # Fünf Iterationen für jedes Thread
        # Mutex sperren
        mutex.acquire()
        print(f"Thread {thread_id} sperrt den Mutex.")
       
        current_value = shared_resource
        time.sleep(0.2)
        shared_resource = current_value + 1
       
        print(f"Thread {thread_id} entsperrt den Mutex. Gemeinsame Ressource: {shared_resource}")
        # Mutex entsperren
        mutex.release()
        random_value = random.uniform(0.1, 0.9)
        time.sleep(random_value)  # Simuliert eine längere Berechnung

# Zwei Threads erstellen
thread1 = threading.Thread(target=access_shared_resource, args=(1,))
thread2 = threading.Thread(target=access_shared_resource, args=(2,))
thread3 = threading.Thread(target=access_shared_resource, args=(3,))

# Threads starten
thread1.start()
thread2.start()
thread3.start()

# Auf das Ende der Threads warten
thread1.join()
thread2.join()
thread3.join()

print("Endwert der gemeinsamen Ressource:", shared_resource)