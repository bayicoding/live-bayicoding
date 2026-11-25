// Array di C++
// Request dari kak wondergirl

#include <iostream>
using namespace std;

int main() {
    // CARA BERPIKIR: array itu rak berderet,
    // tiap kotak punya nomor (index) mulai dari 0.

    // 1. bikin array: tipe nama[jumlah] = {isi};
    int nilai[5] = {80, 75, 90, 60, 85};

    // 2. ambil isi pakai index
    cout << "Nilai pertama: " << nilai[0] << endl;
    cout << "Nilai terakhir: " << nilai[4] << endl;

    // 3. ganti isi kotak
    nilai[3] = 70;

    // 4. tampilkan semua pakai for
    for (int i = 0; i < 5; i++) {
        cout << "Kotak " << i << " = " << nilai[i] << endl;
    }

    // 5. hitung total dan rata-rata
    int total = 0;
    for (int i = 0; i < 5; i++) {
        total += nilai[i];
    }
    cout << "Rata-rata: " << total / 5.0 << endl;

    // 6. array string
    string teman[3] = {"Ima", "Winny", "Wondergirl"};
    for (int i = 0; i < 3; i++) {
        cout << "Halo kak " << teman[i] << "!" << endl;
    }

    return 0;
}
