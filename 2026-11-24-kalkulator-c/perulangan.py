# Perulangan Python ala Bayi Coding

# 1. for: ulang sesuai jumlah
for i in range(1, 6):
    print(f"Langkah ke-{i}")

# 2. while: ulang selama kondisinya benar
susu = 3
while susu > 0:
    print(f"Bayi minum susu, sisa {susu}")
    susu = susu - 1
print("Susu habis, bayi bobo!")

# 3. nested loop + fungsi berparameter
def tabel_perkalian(baris, kolom):
    for i in range(1, baris + 1):
        isi = ""
        for j in range(1, kolom + 1):
            isi += str(i * j) + "\t"
        print(isi)

tabel_perkalian(3, 4)
