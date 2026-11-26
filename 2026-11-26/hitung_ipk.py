# Program Hitung IPK Mahasiswa
# Request dari kak dede diyen


# tabel konversi nilai huruf ke angka (dictionary)
bobot = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}


def predikat(ipk):
    if ipk >= 3.51:
        return "Cumlaude"
    elif ipk >= 3.01:
        return "Sangat Memuaskan"
    elif ipk >= 2.76:
        return "Memuaskan"
    else:
        return "Semangat, semester depan pasti naik!"


print("=== HITUNG IPK BAYI CODING ===")
jumlah = int(input("Berapa mata kuliah? "))

total_sks = 0
total_nilai = 0

for i in range(jumlah):
    print("\nMata kuliah ke-" + str(i + 1))
    nama = input("Nama matkul : ")


    while True:
        try:
            sks = int(input("Jumlah SKS : "))
            break
        except ValueError:
            print("SKS harus angka ya, Contoh 3")

    huruf = input("Nilai (A/B/C/D/E): ").upper()

    if huruf not in bobot:
        print("Nilai tidak dikenal, dianggap E")
        huruf = "E"

    total_sks += sks
    total_nilai += bobot[huruf] * sks

ipk = total_nilai / total_sks

print("\n========== HASIL ==========")
print("Total SKS :", total_sks)
print("IPK kamu :", round(ipk, 2))
print("Predikat :", predikat(ipk))
