# Pola Segitiga 54321 pakai Nested Loop
# Request dari kak uliinaa

# Hasil yang dimau:
# 54321
# 4321
# 321
# 21
# 1

# CARA BERPIKIR:
# Loop luar = baris, angka awalnya turun: 5, 4, 3, 2, 1
# Loop dalam = isi baris, hitung mundur dari angka awal sampai 1

# Cara 1: for di dalam for
for awal in range(5, 0, -1):
    baris = ""
    for angka in range(awal, 0, -1):
        baris += str(angka)
    print(baris)

print("---")

# Cara 2: while di dalam while
awal = 5
while awal >= 1:
    angka = awal
    baris = ""
    while angka >= 1:
        baris += str(angka)
        angka -= 1
    print(baris)
    awal -= 1
