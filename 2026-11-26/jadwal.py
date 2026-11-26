# Bikin Jadwal Kegiatan di Python
# Request dari kak cloverr

jadwal = []

print("=== PEMBUAT JADWAL BAYI CODING ===")
jumlah = int(input("Mau isi berapa kegiatan? "))

# isi kegiatan satu per satu
for i in range(jumlah):
    print("\nKegiatan ke-" + str(i + 1))
    hari = input("Hari (contoh: Senin): ")
    jam = input("Jam (contoh: 08:00): ")
    kegiatan = input("Kegiatan: ")
    jadwal.append({"hari": hari, "jam": jam, "kegiatan": kegiatan})

# urutkan berdasarkan hari, lalu jam
urutan_hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

def kunci(item):
    hari = item["hari"].lower()
    nomor = urutan_hari.index(hari) if hari in urutan_hari else 7
    return (nomor, item["jam"])

jadwal.sort(key=kunci)

# tampilkan jadwal
print("\n========== JADWAL KAMU ==========")
hari_sebelumnya = ""
for item in jadwal:
    if item["hari"] != hari_sebelumnya:
        print("\n" + item["hari"].upper())
        hari_sebelumnya = item["hari"]
    print(" - " + item["jam"] + " | " + item["kegiatan"])

print("\nSemangat jalanin jadwalnya!")

