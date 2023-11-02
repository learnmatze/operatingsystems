import threading
import time

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start, end):
    primes = [n for n in range(start, end) if is_prime(n)]
    print(f"Found primes from {start} to {end}: {primes}")

if __name__ == "__main__":
    start_range = 1
    # end_range = 1000
    end_range = 4000000
    num_threads = 4
    thread_list = []

    step = (end_range - start_range) // num_threads
    start_time = time.time()
    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step

        thread = threading.Thread(target=find_primes, args=(start, end))
        thread_list.append(thread)
        thread.start()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Ausführungszeit für Primzahlenberechnung mit {num_threads} threads: {execution_time} sekunden")

    for thread in thread_list:
        thread.join()

    print("All threads are done.")