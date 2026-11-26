# 4 Pilar OOP di Python
# Request dari kak Maisyaaaa (semangat UAS Senin!)


# 1. CLASS & OBJECT: class itu cetakan, object itu hasilnya
class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.__umur = umur # 2. ENKAPSULASI: __ artinya private

    # getter: cara aman membaca data private
    def get_umur(self):
        return self.__umur

    # setter: cara aman mengubah data private
    def set_umur(self, umur_baru):
        if umur_baru > 0:
            self.__umur = umur_baru
        else:
            print("Umur tidak boleh minus!")

    def bersuara(self):
        print(self.nama + " bersuara...")


# 3. PEWARISAN: Kucing dan Anjing mewarisi semua isi Hewan
class Kucing(Hewan):
    # 4. POLIMORFISME: method sama, isi berbeda
    def bersuara(self):
        print(self.nama + " bilang: Meong!")


class Anjing(Hewan):
    def bersuara(self):
        print(self.nama + " bilang: Guk guk!")


# membuat object dari class
kucing = Kucing("Oyen", 2)
anjing = Anjing("Bleki", 3)

print("=== Polimorfisme ===")
for hewan in [kucing, anjing]:
    hewan.bersuara()

print("\n=== Enkapsulasi ===")
print("Umur Oyen:", kucing.get_umur())
kucing.set_umur(-5)
kucing.set_umur(4)
print("Umur Oyen sekarang:", kucing.get_umur())
