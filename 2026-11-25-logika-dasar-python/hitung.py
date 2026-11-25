# Hitung Mundur 54321 pakai for dan while
# Request dari kak uliinaa

# CARA BERPIKIR, jawab 3 pertanyaan:
# 1. Mulai dari berapa? -> 5
# 2. Berhenti kapan? -> setelah 1
# 3. Tiap putaran gimana? -> kurang 1

# Cara 1: for
# range(mulai, batas, langkah), batas tidak ikut
for angka in range(5, 0, -1):
    print(angka)

print("---")

# Cara 2: while
angka = 5 # 1. mulai dari 5
while angka >= 1: # 2. jalan selama masih >= 1
    print(angka)
    angka -= 1 # 3. kurang 1 tiap putaran

print("Meluncur! Bayi terbang")
