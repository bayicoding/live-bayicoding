// If Else di C++
// Request dari kak ima

#include <iostream>
using namespace std;

int main() {
    // CARA BERPIKIR: cek syarat dari atas ke bawah,
    // syarat pertama yang benar yang dijalankan

    // 1. if else: dua pilihan
    int susu = 0;
    if (susu > 0) {
        cout << "Bayi minum susu" << endl;
    } else {
        cout << "Susu habis, bayi nangis" << endl;
    }

    // 2. if, else if, else: banyak pilihan
    int nilai = 78;
    if (nilai >= 85) {
        cout << "Nilai A, mantap!" << endl;
    } else if (nilai >= 70) {
        cout << "Nilai B, bagus!" << endl;
    } else {
        cout << "Belajar lagi yuk" << endl;
    }

    // 3. syarat gabungan: && artinya DAN
    int umur = 17;
    bool punyaKTP = true;
    if (umur >= 17 && punyaKTP) {
        cout << "Boleh bikin SIM" << endl;
    } else {
        cout << "Belum boleh bikin SIM" << endl;
    }

    return 0;
}
