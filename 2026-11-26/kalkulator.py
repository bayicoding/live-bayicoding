# Kalkulator Python Bayi Coding
# Request dari kak Islami


# fungsi untuk menghitung sesuai operator
def hitung(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "x":
        return a * b
    elif operator == ":":
        if b == 0:
            return "Tidak bisa dibagi nol!"
        return a / b
    else:
        return "Operator tidak dikenal"


print("=== KALKULATOR BAYI CODING ===")
print("Operator: + (tambah), - (kurang), x (kali), : (bagi)")

# perulangan: terus menghitung sampai pengguna mau berhenti
while True:
    angka1 = float(input("\nAngka pertama : "))
    operator = input("Operator : ")
    angka2 = float(input("Angka kedua : "))

    hasil = hitung(angka1, angka2, operator)
    print("Hasilnya:", hasil)

    lagi = input("Hitung lagi? (y/n): ")
    if lagi != "y":
        break

print("Makasih udah pakai kalkulator bayi!")
