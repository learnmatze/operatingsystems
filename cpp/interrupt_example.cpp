#include <Windows.h>
#include <iostream>
#include <string>

using namespace std;

int main() {
    cout << "Interrupt Programm started";
    Sleep(1000);
    MessageBox(NULL,  "This is an interrupt!", "Interrupt Example", 0x20);
    cout << "Interrupt Programm endet";
    cout << endl;    
    return 0;      
}

