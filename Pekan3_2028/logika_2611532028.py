# Buat file dengan nama logika_nim.py
# Nma variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini mengunakan fungsi input()
# Program operator logika dalam python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_2028 = input("Input nilai boolean-1 (True/False):").strip().lower() == "true"
a2_2028 = input("Input nilai boolean-2 (True/False):").strip().lower() == "true"

print("\nA1 =", a1_2028)
print("A2 =", a2_2028)

# Konjungsi bernilai true jika keduanya true
hasil_2028 = a1_2028 and a2_2028
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_2028)

# Disjungsi bernilai True jika salah satunya True
hasil_2028 = a1_2028 or a2_2028
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_2028)

# Negasi A1: membalik nilai A1
hasil_2028 = not a1_2028
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_2028)

# Negasi A2: membalik nilai A2
hasil_2028 = not a2_2028
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_2028)

# XOR bernilai True jika kedua nilai berbeda
hasil_2028 = a1_2028 != a2_2028
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_2028)
