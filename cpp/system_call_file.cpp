#include <windows.h>
#include <iostream>

int main() {
    // Dateipfad
    const char* filePath = "C:\\example.txt";

    // Versuchen, die Datei zu öffnen
    HANDLE hFile = CreateFile(
        filePath,                 // Dateipfad
        GENERIC_READ,             // Zugriffsrechte (lesen)
        0,                        // Freigabe
        NULL,                     // Sicherheitsattribut
        OPEN_EXISTING,             // Öffnet eine vorhandene Datei
        FILE_ATTRIBUTE_NORMAL,     // Dateiattribut
        NULL                      // Dateihandlevorlage (nicht verwendet)
    );

    if (hFile != INVALID_HANDLE_VALUE) {
        std::cout << "Datei erfolgreich geöffnet." << std::endl;
        // Hier können Sie Operationen auf der Datei ausführen, z.B. Lesen oder Schreiben.
        char buffer[1024];

        DWORD byteRead;
        if(ReadFile(hFile, buffer, sizeof(buffer), &byteRead, NULL))
        {
            std::cout << "Gelesen: " << byteRead << " Bytes" << std::endl;
            std::cout << "Inhalt: " << std::string(buffer, byteRead) << std::endl;            
        }
        else {
            std::cerr << "Fehler beim lesen der Datei" << std::endl;
        }
        // Datei schließen
        CloseHandle(hFile);
    } else {
        std::cerr << "Fehler beim Öffnen der Datei." << std::endl;
    }

    return 0;
}