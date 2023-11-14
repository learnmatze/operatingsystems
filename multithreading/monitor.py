import threading
import time

# demonstrating the use of a monitor to signal a second thread that he can continue working
# Monitor erstellen
monitor = threading.Condition()

# Flag für die Benachrichtigung
notify_flag = False

# Funktion für Thread 1, der Thread 2 benachrichtigt
def thread1_function():
    global notify_flag
    time.sleep(0.2)

    # Monitor sperren
    with monitor:
        print("Thread 1 sperrt den Monitor.")
        time.sleep(1)  # Simuliert eine längere Berechnung

        # Benachrichtigung setzen
        notify_flag = True
        print("Thread 1 setzt die Benachrichtigungsflag und benachrichtigt andere Threads.")
        monitor.notify()

        # Erneut auf den Monitor warten, um die endgültige Arbeit zu beenden
        print("Thread 1 wartet erneut auf den Monitor.")
        monitor.wait()
        print("Thread 1 hat die Benachrichtigung erhalten und setzt seine Arbeit fort.")

    # Optional: Weiterarbeit von Thread 1 außerhalb des Monitors
    print("Thread 1 setzt seine endgültige Arbeit außerhalb des Monitors fort.")

# Funktion für Thread 2, der auf Benachrichtigung wartet
def thread2_function():
    global notify_flag

    # Monitor sperren
    with monitor:
        print("Thread 2 sperrt den Monitor und wartet auf Benachrichtigung.")
       
        # Warten auf Benachrichtigung
        while not notify_flag:
            monitor.wait()
       
        # Benachrichtigung verarbeiteten
        print("Thread 2 hat die Benachrichtigung erhalten und setzt seine Arbeit fort.")
       
        # Signalisieren, dass Thread 1 seine endgültige Arbeit beenden kann
        monitor.notify()
    print("Thread 2 setzt seine endgültige Arbeit außerhalb des Monitors fort.")

# Zwei Threads erstellen
thread1 = threading.Thread(target=thread1_function)
thread2 = threading.Thread(target=thread2_function)

# Threads starten
thread1.start()
thread2.start()

# Auf das Ende der Threads warten
thread1.join()
thread2.join()

print("Programm beendet.")