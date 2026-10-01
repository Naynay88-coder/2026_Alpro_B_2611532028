# Buat file dengan nama perulangan_for3_2028.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah dengan 4 digit nim terakhir contoh: ulang_1234 
# Programm ini menggunaka fungsi input()

ulang_2028 = int(input("Masukkan jumlah perulangan:"))

jumlah_2028 = 0
for i_2028 in range(1, ulang_2028 + 1):
    print(i_2028, end=" ")
    jumlah_2028 = jumlah_2028 + i_2028

    if i_2028 < ulang_2028:
        print("+", end=" ")
    else:
        print(" = ", jumlah_2028, end="")
print()
print("Jumlah =", jumlah_2028)