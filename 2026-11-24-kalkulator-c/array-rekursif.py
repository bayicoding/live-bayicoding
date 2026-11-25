# Array (list) & rekursif di Python ala Bayi Coding

# 1. Array: kumpulan data dalam satu variabel
mainan = ["bola", "boneka", "mobil"]
print("Mainan pertama:", mainan[0])

mainan.append("robot")
print("Semua mainan:", mainan)
print("Jumlah mainan:", len(mainan))

for m in mainan:
    print("Bayi main", m)

# 2. Rekursif: fungsi yang memanggil dirinya sendiri
def hitung_mundur(n):
    if n == 0:
        print("Bayi bobo!")
        return
    print(n)
    hitung_mundur(n - 1)

hitung_mundur(3)

def faktorial(n):
    if n == 1:
        return 1
    return n * faktorial(n - 1)

print("5! =", faktorial(5))
