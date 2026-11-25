// Kalkulator bahasa C ala Bayi Coding
#include <stdio.h>

int main() {
    float angka1 = 12;
    float angka2 = 4;
    char operasi = '+';
    float hasil;

    if (operasi == '+') {
        hasil = angka1 + angka2;
    } else if (operasi == '-') {
        hasil = angka1 - angka2;
    } else if (operasi == '*') {
        hasil = angka1 * angka2;
    } else if (operasi == '/') {
        hasil = angka1 / angka2;
    } else {
        printf("Operator tidak dikenal\n");
        return 1;
    }

    printf("Hasilnya: %.2f\n", hasil);
    return 0;
}
