#include <iostream>
#include <Windows.h>
// Function to be called when the timer interrupt occurs
VOID CALLBACK TimerInterruptCallback(PVOID lpParam, BOOLEAN TimerOrWaitFired) {
    std::cout << "Timer interrupt occurred!" << std::endl;
}
int main() {
    HANDLE hTimer;
    // Create a timer queue and a timer
    if (!CreateTimerQueueTimer(&hTimer, NULL, TimerInterruptCallback, NULL, 1000, 1000, 0)) {
        std::cerr << "Error creating timer: " << GetLastError() << std::endl;
        return 1;
    }
    std::cout << "Press Enter to stop the timer interrupt..." << std::endl;
    std::cin.get();
    // Delete the timer
    DeleteTimerQueueTimer(NULL, hTimer, NULL);
    return 0;
}