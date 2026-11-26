// Program Data Nilai Mahasiswa: 5 Fitur
// Pakai string, array, fungsi, dan STL (vector, sort, find_if)
// Request dari kak sandyaaraa

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct Mahasiswa {
    string nama;
    int nilai;
};

vector<Mahasiswa> daftar; // STL vector: ukurannya bisa bertambah

// array berisi nama-nama menu
string menu[5] = {"Tambah data", "Tampilkan data", "Cari nama", "Urutkan nilai", "Statistik"};

void tambah() {
    Mahasiswa m;
    cout << "Nama : ";
    cin >> m.nama;
    cout << "Nilai: ";
    cin >> m.nilai;
    daftar.push_back(m);
    cout << "Data tersimpan!\n";
}

void tampilkan() {
    if (daftar.empty()) {
        cout << "Data masih kosong.\n";
        return;
    }
    for (int i = 0; i < daftar.size(); i++) {
        cout << i + 1 << ". " << daftar[i].nama << " - " << daftar[i].nilai << "\n";
    }
}

void cari() {
    string target;
    cout << "Cari nama: ";
    cin >> target;
    auto hasil = find_if(daftar.begin(), daftar.end(), [&](Mahasiswa m) {
        return m.nama == target;
    });
    if (hasil != daftar.end()) {
        cout << "Ketemu! Nilai " << hasil->nama << " = " << hasil->nilai << "\n";
    } else {
        cout << "Nama tidak ditemukan.\n";
    }
}

void urutkan() {
    sort(daftar.begin(), daftar.end(), [](Mahasiswa a, Mahasiswa b) {
        return a.nilai > b.nilai;
    });
    cout << "Diurutkan dari nilai tertinggi:\n";
    tampilkan();
}

void statistik() {
    if (daftar.empty()) {
        cout << "Data masih kosong.\n";
        return;
    }
    int total = 0;
    for (Mahasiswa m : daftar) {
        total += m.nilai;
    }
    cout << "Jumlah data : " << daftar.size() << "\n";
    cout << "Rata-rata : " << (double)total / daftar.size() << "\n";
}

int main() {
    int pilih;
    do {
        cout << "\n=== DATA NILAI BAYI CODING ===\n";
        for (int i = 0; i < 5; i++) {
            cout << i + 1 << ". " << menu[i] << "\n";
        }
        cout << "0. Keluar\nPilih: ";
        cin >> pilih;

        if (pilih == 1) tambah();
        else if (pilih == 2) tampilkan();
        else if (pilih == 3) cari();
        else if (pilih == 4) urutkan();
        else if (pilih == 5) statistik();
    } while (pilih != 0);

    cout << "Dadah, semangat belajar C++!\n";
    return 0;
}
