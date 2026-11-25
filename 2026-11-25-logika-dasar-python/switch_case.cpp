// Switch Case di C++
// Request dari kak winnysatang

#include <iostream>
using namespace std;

int main() {
    // CARA BERPIKIR: switch itu kayak lift,
    // pencet nomor lantai, langsung ke lantai itu.
    // Cocok kalau pilihannya angka/huruf yang pasti.

    // 1. switch dengan angka: nama hari
    int hari = 3;
    switch (hari) {
        case 1:
            cout << "Senin" << endl;
            break;
        case 2:
            cout << "Selasa" << endl;
            break;
        case 3:
            cout << "Rabu" << endl;
            break;
        default:
            cout << "Hari lain" << endl;
    }

    // 2. switch dengan huruf: menu kantin
    char menu = 'B';
    switch (menu) {
        case 'A':
            cout << "Kamu pesan nasi goreng" << endl;
            break;
        case 'B':
            cout << "Kamu pesan mie ayam" << endl;
            break;
        default:
            cout << "Menu tidak ada" << endl;
    }

    // break = keluar dari switch.
    // Lupa break? case di bawahnya ikut jalan!
    return 0;
}
