# Kalkulator sederhana ala Bayi Coding
angka1 = 100
angka2 = 4
operator = "-"

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    hasil = angka1 / angka2
else:
    hasil = "Operator tidak dikenal"

print("Hasilnya:", hasil)
