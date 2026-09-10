#buat file dengan nama Boolean_NIM.py
# Nama Variabel ditambah 4 digit nim terakhir contoh: nilai_2028
# Deklrasikan variabel dengan tipe data Boolean
is_lulus = True
is_cumlaude = True

# Menggunakann Boolean
nilai_2028 = 85
batas_lulus_2028 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai_2028 >= batas_lulus_2028 #hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_2028)
print("Apakah Lulus?", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat!, Anda lulus dengan prediket Cum Laude!")
