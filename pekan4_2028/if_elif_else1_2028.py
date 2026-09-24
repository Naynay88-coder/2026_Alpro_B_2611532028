# Buat file dengan nama if_elif_else1_nim.py
# Buat program dengan kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2028 = int(input("Input Umur Anda: "))
sim_2028 = input("Apakah Anda Sudah Punya sim c: ")[0]

if umur_2028 >= 17 and sim_2028 == 'y' :
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")
elif umur_2028 >= 17 and sim_2028 != 'y' :
    print("Anda Sudah Dewasa tetapi Tidak Boleh Bawa Motor")
elif umur_2028 < 17 and sim_2028 == 'y' :
    print("Anda Belum Cukup Umur Punya SIM")
else:
    print("Anda Belum Cukup Umur dan Tidak Boleh Bawa Motor")
print("Program Selesai")