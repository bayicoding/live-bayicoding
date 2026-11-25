# Struktur data pohon (tree) ala Bayi Coding

class Simpul:
    def __init__(self, nama):
        self.nama = nama
        self.anak = []

    def tambah(self, simpul_anak):
        self.anak.append(simpul_anak)
        return simpul_anak

# root: kakek, lalu anak dan cucunya
kakek = Simpul("Kakek")
papa = kakek.tambah(Simpul("Papa"))
om = kakek.tambah(Simpul("Om"))
papa.tambah(Simpul("Bayi"))
papa.tambah(Simpul("Kakak"))
om.tambah(Simpul("Sepupu"))

# tampilkan pohon pakai rekursif
def tampilkan(simpul, level=0):
    print("    " * level + "- " + simpul.nama)
    for a in simpul.anak:
        tampilkan(a, level + 1)

tampilkan(kakek)

# daun (leaf) = simpul yang tidak punya anak
def hitung_daun(simpul):
    if not simpul.anak:
        return 1
    return sum(hitung_daun(a) for a in simpul.anak)

print("Jumlah daun:", hitung_daun(kakek))
