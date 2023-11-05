#include <iostream>

// Data-Segment: Initialisierte globale Variable
int globalVar = 42;

// Eine einfache Funktion (simple Funktion) ist im Code-Segment
void simpleFunktion() {
    std::cout << "simple Funktion (in Code-Segment)." << std::endl;
}

// Code-Segment: Die Funktion main ist im Code-Segment.
int main() {
    
    // Funktionszeiger auf die Funktion simpleFunktion
    void (*funktionsZeiger)() = simpleFunktion;

    // Aufruf der Funktion simpleFunktion über den Funktionszeiger
    funktionsZeiger();

    // Stack-Segment: Lokale Variable auf dem Stack
    int localVar = 10;

    // Heap-Segment: Dynamische Speicherzuweisung
    int *heapVar = new int;
    *heapVar = 100;

    std::cout << "main method (in Code-Segment): " << std::endl;
    std::cout << "Adresse von simpleFunktion (in Code-Segment): " << &funktionsZeiger << std::endl;
    std::cout << "Adresse von globalVar (in Data-Segment): " << &globalVar << std::endl;
    std::cout << "Adresse von localVar (in Stack-Segment): " << &localVar << std::endl;
    std::cout << "Adresse von heapVar (in Heap-Segment): " << heapVar << std::endl;

    // Freigabe des Heap-Segments
    delete heapVar;

    return 0;
}
