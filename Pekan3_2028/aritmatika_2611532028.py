# Buat file dengan nama aritmatika_2611532028.py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2611532028
# Program ini menggunakan fungsi input 
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2028 = int(input("Input angka-1: "))
angka2_2028 = int(input("Input angka-2: "))

#penjumlahan
hasil_2028 = angka1_2028 + angka2_2028
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2028)

#pengurangan
hasil_2028 = angka1_2028 - angka2_2028
print("\nOperator Pengurangan")
print("Hasil =", hasil_2028)

# Perkalian
hasil_2028 = angka1_2028 * angka2_2028
print("\nOperator Perkalian")
print("Hasil =", hasil_2028)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2028 != 0:
    hasil_2028 = angka1_2028 / angka2_2028
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2028)

    hasil_2028 = angka1_2028 // angka2_2028
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2028)

    hasil_2028 = angka1_2028 % angka2_2028
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2028)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2028 = angka1_2028 ** angka2_2028
print("\nOperator Pangkat")
print("Hasil =", hasil_2028)
