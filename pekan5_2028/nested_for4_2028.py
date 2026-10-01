# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah dengan 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunaka fungsi input()

tinggi_2028 = int(input(" Masukka tinggi pola (bilangan genap, misal 10): "))

if tinggi_2028 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2028 = tinggi_2028
    c_2028 = a_2028
    lebar_2028 = (2 * tinggi_2028) - 2

    for i_2028 in range(1, tinggi_2028 + 1):
        b_2028 = c_2028+ 1

        for j_2028 in range(1, lebar_2028 + 1):

            # Barisan atas dan bawah
            if i_2028 == 1 or i_2028 == tinggi_2028:
                if j_2028 == 1 or j_2028 == lebar_2028:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j_2028 == 1 or j_2028 == lebar_2028:
                    print("|", end="")
                elif j_2028 == b_2028:
                    print(">", end="")
                elif j_2028 == (lebar_2028 - c_2028 + 1):
                    print(">", end="")
                elif j_2028 > b_2028 and j_2028 < (lebar_2028 - c_2028):
                    print(".", end="")
                else:
                    print(" ", end="")

        print()

        # logika asli java
        a_2028 -= 2

        if a_2028 <= 0:
            c_2028 = a_2028 + 2
        else:
            c_2028 = a_2028