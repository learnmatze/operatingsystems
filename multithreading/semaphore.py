import threading
import time

# create a semaphore with count 3 and use 5 threads to work at a shared resource
# Semaphore erstellen mit einer Anfangsanzahl von 3 Permits
semaphore = threading.Semaphore(3)
# lock = threading.Lock()

# Gemeinsam genutzte Ressource
shared_resource = 0

# Funktion für den Zugriff auf die geschützte Ressource
def access_shared_resource(thread_id):
    global shared_resource

    # Versuchen, ein Permit zu erwerben
    with semaphore:
        print(f"Thread {thread_id} hat ein Permit erworben.")
        # with lock:
        # Kritische Sektion: Zugriff auf die gemeinsame Ressource
        current_value = shared_resource
        time.sleep(1)  # Simuliert eine längere Berechnung
        shared_resource = current_value + 1

        print(f"Thread {thread_id} hat die gemeinsame Ressource aktualisiert. Permit wird freigegeben.")

# Fünf Threads erstellen
threads = []

for i in range(5):
    thread = threading.Thread(target=access_shared_resource, args=(i,))
    threads.append(thread)

# Threads starten
for thread in threads:
    thread.start()

# Auf das Ende der Threads warten
for thread in threads:
    thread.join()

print("Endwert der gemeinsamen Ressource:", shared_resource)