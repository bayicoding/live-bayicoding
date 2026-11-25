// Looping Do While di C
// Request dari kak alik

#include <stdio.h>

int main() {
    // CARA BERPIKIR: do while = "kerjain dulu, baru cek".
    // Jadi isinya PASTI jalan minimal sekali.

    // 1. do while biasa: hitung 1 sampai 5
    int i = 1;
    do {
        printf("Putaran ke-%d\n", i);
        i++;
    } while (i <= 5);

    // 2. bedanya sama while
    int susu = 0;

    while (susu > 0) {
        printf("while: minum susu\n"); // tidak jalan sama sekali
    }

    do {
        printf("do while: cek botol dulu, ternyata kosong\n");
    } while (susu > 0); // tetap jalan sekali

    // 3. contoh nyata: hitung mundur roket
    int hitung = 3;
    do {
        printf("%d...\n", hitung);
        hitung--;
    } while (hitung > 0);
    printf("Meluncur!\n");

    return 0;
}
