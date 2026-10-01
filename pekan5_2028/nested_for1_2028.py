# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah dengan 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunaka fungsi input()

batas_2028 = int(input("Masukkan nilai batas: "))
for line_2028 in range(1, batas_2028 + 1):
    for j_2028 in range(1,(-1 * line_2028 + batas_2028) + 1):
        print(".", end="")
    print(line_2028)