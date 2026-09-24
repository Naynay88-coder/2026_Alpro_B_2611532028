# Buat file dengan nama multi_if1_2028.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit NIM terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2028 = int(input("Input Umur Anda: "))
sim_2028 = input("Apakah Anda Sudah Punya sim c (y/t): ")[0]

if umur_2028 >= 17 and sim_2028 == 'y' :
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")

if umur_2028 >= 17 and sim_2028 != 'y' :
    print("Anda Sudah Dewasa dan Tidak Boleh Bawa Motor")

if umur_2028 < 17 and sim_2028 == 'y' :
    print("Anda Belum Cukup Umur Punya SIM")

if umur_2028 < 17 and sim_2028 != 'y' :
    print("Anda Belum Cukup Umur Bawa Motor")