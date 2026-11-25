# Logika Dasar Python + Cara Berpikirnya
# Request dari kak uliinaa

# CARA BERPIKIR: pecah masalah jadi langkah kecil,
# tulis dulu pakai bahasa manusia, baru ubah jadi kode.

# 1. if elif else: memilih jalan
# Pikir: "nilai berapa dapat huruf apa?"
nilai = 78
if nilai >= 85:
    print("Nilai A, mantap!")
elif nilai >= 70:
    print("Nilai B, bagus!")
else:
    print("Belajar lagi yuk")

# 2. for: ulang yang jumlahnya sudah tahu
# Pikir: "sapa 3 teman satu per satu"
teman = ["Pai", "Ikaa", "uliinaa"]
for nama in teman:
    print(f"Halo kak {nama}!")

# 3. while: ulang selama syaratnya benar
# Pikir: "minum terus selama susu masih ada"
susu = 3
while susu > 0:
    print(f"Glek! Sisa susu {susu}")
    susu -= 1
print("Susu habis")

# 4. def return: bikin mesin kecil
# Pikir: "masukkan dua angka, keluarkan rata-ratanya"
def rata_rata(a, b):
    hasil = (a + b) / 2
    return hasil

print("Rata-rata:", rata_rata(80, 90))
