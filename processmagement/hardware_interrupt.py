#pip install keyboard
import threading
import time
import keyboard

# Variable, um den Zustand des Tastendrucks zu speichern
key_pressed = False

# Funktion, die im Thread ausgeführt wird (Prozesssimulation)
def process_simulation():
    while True:
        print("Prozess läuft...")
        time.sleep(2)  # Simulierte Ausführung des Prozesses

# Interrupt Service Routine (ISR) für den Tastendruck
def isr_keypress(e):
    global key_pressed
    print(f"Keyboard Interrupt ausgelöst. Tastendruck erkannt: {e.name}")
    # Hier können Sie Aktionen basierend auf dem Tastendruck ausführen
    key_pressed = True  # Markieren Sie den Tastendruck

# Interrupt Service Routine (ISR) für den Timer Interrupt
aktuelle_systemzeit = time.time()
def isr_timer():
    global aktuelle_systemzeit
    clock_timer = time.time()
    print(f"Timer Interrupt ausgelöst. Aktualisiere die Systemzeit von {time.ctime(aktuelle_systemzeit)} auf {time.ctime(clock_timer)}")
    aktuelle_systemzeit = clock_timer

def start_timer():
    while True:
        time.sleep(10)  # Simuliere das Ablaufen des Timers alle 5 Sekunden
        isr_timer()    # ISR wird aufgerufen, wenn der Timer abläuft

# Hauptfunktion
def main():
    global key_pressed
    # Erstellen und starten des Threads (Prozesssimulation)
    process_thread = threading.Thread(target=process_simulation)
    process_thread.start()

    # Registrieren der ISR für den Tastendruck (z.B., die Tasten 'a','e')
    keyboard.on_press_key('a', isr_keypress)
    keyboard.on_press_key('e', isr_keypress)

    timer_thread = threading.Thread(target=start_timer)
    timer_thread.start()

    while True:
        if key_pressed:
            # Tastendruck wurde behandelt, setzen Sie den Zustand zurück
            key_pressed = False

            # Fortsetzen der Prozesssimulation
            print("Prozesssimulation fortgesetzt.")

        time.sleep(1)  # Warten auf Interrupts und gleichzeitig weiterhin Prozesssimulation

if __name__ == "__main__":
    main()