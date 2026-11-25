# Kompleksitas Waktu & Ruang di Python
# Request dari Kak aya, makasih ya!
# Waktu = berapa banyak langkah, Ruang = berapa banyak memori
import sys

# 1. O(1): langkahnya tetap, berapa pun datanya
def ambil_pertama(data):
    return data[0]

# 2. O(n): langkah naik sebanding jumlah data
def cari(data, target):
    langkah = 0
    for x in data:
        langkah += 1
        if x == target:
            break
    return langkah

# 3. O(n^2): loop di dalam loop, langkah naik drastis
def semua_pasangan(data):
    langkah = 0
    for a in data:
        for b in data:
            langkah += 1
    return langkah

for n in [10, 100, 1000]:
    data = list(range(n))
    ambil_pertama(data)
    print(f"n={n}: O(1)=1 langkah, O(n)={cari(data, n - 1)}, O(n^2)={semua_pasangan(data)}")

# 4. Ruang: O(1) hemat vs O(n) boros
def total_hemat(data):
    total = 0 # cuma 1 variabel -> ruang O(1)
    for x in data:
        total += x
    return total

def total_boros(data):
    salinan = [x for x in data] # bikin list baru -> ruang O(n)
    return sum(salinan)

print("Total hemat:", total_hemat(range(1000)))
print("Total boros:", total_boros(range(1000)))
print("Memori 1 angka:", sys.getsizeof(0), "byte")
print("Memori list 1000:", sys.getsizeof(list(range(1000))), "byte")
