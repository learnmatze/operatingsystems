import threading
import time

# Globale Variable zur Kontrolle zwischen den Threads
current_thread = 1
switch_interval = 5  # Zeitintervall zum Wechseln der Threads

def worker1():
    while True:
        if current_thread == 1:
            print("Thread 1 is running...")
            time.sleep(2)  # Simuliere Arbeit für 2 Sekunden

def worker2():
    while True:
        if current_thread == 2:
            print("Thread 2 is running...")
            time.sleep(3)  # Simuliere Arbeit für 3 Sekunden

# Haupt-Thread (Scheduler)
if __name__ == "__main__":
    # Erstelle die Worker-Threads
    thread1 = threading.Thread(target=worker1)
    thread2 = threading.Thread(target=worker2)

    # Starte die Worker-Threads
    thread1.start()
    thread2.start()

    try:
        while True:
            # Der Haupt-Thread wechselt zwischen den Threads
            if current_thread == 1:
                time.sleep(switch_interval)  # Warte das definierte Intervall
                current_thread = 2  # Wechsle zur Thread 2
            else:
                time.sleep(switch_interval)  # Warte das definierte Intervall
                current_thread = 1  # Wechsle zur Thread 1

    except KeyboardInterrupt:
        # Falls das Programm mit Strg+C beendet wird, stoppe die Worker-Threads
        thread1.join()
        thread2.join()
