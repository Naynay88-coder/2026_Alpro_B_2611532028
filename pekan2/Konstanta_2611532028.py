# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# Nama variable ditambah 4 digit nim terakhir contoh: jari_2028
from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2028 = float(input('Masukkan nilai jari-jari:'))
luas_2028 = PI * jari_2028 * jari_2028
print("Luas Lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2028, luas_2028))