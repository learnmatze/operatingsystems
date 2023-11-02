#include <iostream>
#include <thread>
#include <vector>
#include <chrono>

// Diese Funktion wird in einem separaten Thread ausgeführt
void thread_function(int thread_id) {
    std::cout << "Thread " << thread_id << " gestartet." << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(5));
    std::cout << "Thread " << thread_id << " beendet." << std::endl;
}

int main() {
    const int num_threads = 4;
    std::vector<std::thread> threads;
    for (int i = 0; i < num_threads; ++i) {
        // Jeder Schleifendurchlauf erstellt einen neuen Thread und weist ihm die Funktion zu
        threads.push_back(std::thread(thread_function, i));
    }
    std::cout << "Hauptthread wartet auf die Beendigung der Nebenthreads..." << std::endl;
    // Auf die Beendigung der Threads warten
    for (std::thread& t : threads) {
        t.join();
    }
    std::cout << "Alle Threads wurden beendet." << std::endl;
    return 0;
}