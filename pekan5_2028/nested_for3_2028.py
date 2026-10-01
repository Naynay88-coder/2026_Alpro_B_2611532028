# Buat file dengan nama nested_for3_NIM.py
# Buat program perulangan dor dalam pyhton
# Nama variabel ditambah dengan 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunaka fungsi input()

batas_2028 = int(input("Masukkan nilai batas: "))
for i_2028 in range(batas_2028+1):
    for j_2028 in range(batas_2028+1):
        print(i_2028+j_2028, end=" ")
    print() # pindah ke baris berikutnya