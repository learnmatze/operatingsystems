#include <windows.h>
#include <iostream>

int main() {
    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    DWORD len = MAX_PATH;     

    ZeroMemory(&si, sizeof(STARTUPINFO));
    si.cb = sizeof(STARTUPINFO);
    ZeroMemory(&pi, sizeof(PROCESS_INFORMATION));

    LPCSTR applicationPath = "C:\\Windows\\notepad.exe";

    if (CreateProcess(
        applicationPath,   // Anwendungspfad (in diesem Fall Notepad)
        NULL,                         // Befehlszeilenparameter (keine)
        NULL,                         // Sicherheitsbeschreibung (Standard)
        NULL,                         // Sicherheitsbeschreibung (Standard)
        FALSE,                        // Erstellen im Erbschaftsmodus (nein)
        0,                            // Flags (keine speziellen Flags)
        NULL,                         // Umgebungsvariable (Standard)
        NULL,                         // Arbeitsverzeichnis (Standard)
        &si,                          // STARTUPINFO
        &pi                           // PROCESS_INFORMATION
    )) {
        std::cout << "Notepad erfolgreich gestartet." << std::endl;
        // Hier können Sie auf den neuen Prozess zugreifen.
        DWORD processId = pi.dwProcessId;
        DWORD threadId = pi.dwThreadId;
        std::cout << "Process Id: " << processId << " Thread Id: " << threadId << std::endl;  
        Sleep(1000);      
    } else {
        std::cerr << "Fehler beim Starten von Notepad." << std::endl;
    }
    return 0;
}