# ==========================================
# PROGRAM SIMULASI TRANSAKSI TOKO
# NIM: 2611532028
# ==========================================

print("=== SISTEM TRANSAKSI TOKO ===")


# ==========================================
# 1. INPUT DATA PELANGGAN
# ==========================================

nama_pelanggan_2028 = input("Masukkan Nama Pelanggan : ")

status_pelanggan_2028 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()

total_belanja_2028 = int(input("Masukkan Total Belanja : Rp"))

jumlah_barang_2028 = int(input("Masukkan Jumlah Barang : "))

kode_promo_2028 = input("Masukkan Kode Promo : ").upper()


# ==========================================
# 2. OPERATOR PERBANDINGAN
# ==========================================

syarat_belanja_2028 = (total_belanja_2028 >= 200000)

syarat_barang_2028 = (jumlah_barang_2028 >= 3)

status_member_2028 = (status_pelanggan_2028 == "member")


# ==========================================
# 3. OPERATOR LOGIKA
# ==========================================

# Operator AND
# Member DAN belanja minimal Rp200.000
mendapat_diskon_2028 = (status_member_2028 and syarat_belanja_2028)

# Belanja minimal Rp200.000 DAN jumlah barang minimal 3
syarat_promo_2028 = (syarat_belanja_2028 and syarat_barang_2028)


# Operator OR
# Pelanggan mendapat status tambahan jika member
# ATAU memiliki kode promo yang tersedia
member_atau_promo_2028 = (status_member_2028 or kode_promo_2028 in["HEMAT10", "HEMAT20", "GRATISONGKIR"])


# Operator NOT
# Memeriksa apakah pelanggan bukan member
bukan_member_2028 = not status_member_2028


# ==========================================
# 4. OPERATOR KEANGGOTAAN
# ==========================================

daftar_promo_2028 = [
    "HEMAT10",
    "HEMAT20",
    "GRATISONGKIR"]

# Operator IN
kode_promo_tersedia_2028 = (kode_promo_2028 in daftar_promo_2028)

# Operator NOT IN
kode_promo_tidak_tersedia_2028 = (kode_promo_2028 not in daftar_promo_2028)


# ==========================================
# 5. PERHITUNGAN DISKON
# ==========================================

if mendapat_diskon_2028:
    diskon_2028 = (total_belanja_2028 * 10 / 100)
else:
    diskon_2028 = 0


# ==========================================
# 6. OPERATOR ARITMATIKA
# ==========================================

# Operator pengurangan
# Total pembayaran setelah diskon
total_pembayaran_2028 = (total_belanja_2028 - diskon_2028)

# Operator pembagian
# Rata-rata harga barang
harga_rata_rata_2028 = (total_pembayaran_2028 / jumlah_barang_2028)


# ==========================================
# 7. OPERATOR PENUGASAN
# ==========================================

total_transaksi_2028 = 0

# Operator +=
total_transaksi_2028 += total_pembayaran_2028


# ==========================================
# 8. STATUS PROMO
# ==========================================

mendapat_promo_2028 = (syarat_promo_2028 and kode_promo_tersedia_2028)


# ==========================================
# 9. OPERATOR IDENTITAS
# ==========================================

# Operator IS
# Digunakan untuk memeriksa apakah data kosong
data_kosong_2028 = None

data_tidak_tersedia_2028 = (data_kosong_2028 is None)


# ==========================================
# 10. OPERATOR BITWISE
# ==========================================

# Keterangan kode:
#
# 0001 = Member
# 0010 = Belanja >= Rp200.000
# 0100 = Jumlah Barang >= 3
# 1000 = Kode Promo Tersedia

bit_member_2028 = 0b0001

bit_belanja_2028 = 0b0010

bit_barang_2028 = 0b0100

bit_promo_2028 = 0b1000


# ==========================================
# 11. MEMBUAT KODE HAK AKSES
# ==========================================

kode_hak_akses_2028 = 0


# Operator OR (|)
if status_member_2028:
    kode_hak_akses_2028 |= bit_member_2028

if syarat_belanja_2028:
    kode_hak_akses_2028 |= bit_belanja_2028

if syarat_barang_2028:
    kode_hak_akses_2028 |= bit_barang_2028

if kode_promo_tersedia_2028:
    kode_hak_akses_2028 |= bit_promo_2028


# ==========================================
# 12. PEMERIKSAAN HAK AKSES
# ==========================================

# Operator AND (&)

member_access_2028 = (kode_hak_akses_2028 & bit_member_2028) != 0

promo_access_2028 = (kode_hak_akses_2028 & bit_promo_2028) != 0

free_shipping_access_2028 = (kode_hak_akses_2028 & bit_barang_2028) != 0


# ==========================================
# 13. KODE TRANSAKSI DAN REFERENSI
# ==========================================

kode_transaksi_2028 = kode_hak_akses_2028

kode_referensi_2028 = 0b1011


# ==========================================
# 14. OUTPUT DATA TRANSAKSI
# ==========================================

print("\n=== DATA TRANSAKSI ===")

print("Nama Pelanggan        :", nama_pelanggan_2028)

print("Status Pelanggan      :", status_pelanggan_2028)

print("Total Belanja         : Rp", total_belanja_2028)

print("Jumlah Barang         :", jumlah_barang_2028)

print("Kode Promo            :", kode_promo_2028)


# ==========================================
# 15. HASIL VALIDASI
# ==========================================

print("\n=== HASIL VALIDASI ===")

print("Belanja >= Rp200000       :", syarat_belanja_2028)

print("Jumlah Barang >= 3        :", syarat_barang_2028)
 
print("Status Member             :", status_member_2028)

print("Kode Promo Tersedia       :", kode_promo_tersedia_2028)

print("Kode Promo Tidak Tersedia :", kode_promo_tidak_tersedia_2028)

print("Mendapatkan Diskon        :", mendapat_diskon_2028)

print("Mendapatkan Promo         :", mendapat_promo_2028)

print("Member atau Promo         :", member_atau_promo_2028)

print("Bukan Member              :", bukan_member_2028)


# ==========================================
# 16. HASIL PERHITUNGAN
# ==========================================

print("\n=== HASIL PERHITUNGAN ===")

print("Diskon                 : Rp", int(diskon_2028))

print("Total Pembayaran       : Rp", int(total_pembayaran_2028))

print("Rata-rata Harga Barang : Rp", int(harga_rata_rata_2028))


# ==========================================
# 17. HAK AKSES PELANGGAN
# ==========================================

print("\n=== HAK AKSES PELANGGAN ===")

print("Kode Hak Akses         :", format(kode_hak_akses_2028, "04b"))

print("Kode Hak Akses Decimal :", kode_hak_akses_2028)

print("Member Access          :", member_access_2028)

print("Promo Access           :", promo_access_2028)

print("Free Shipping Access   :", free_shipping_access_2028)


# ==========================================
# 18. OPERASI BITWISE
# ==========================================

print("\n=== OPERASI BITWISE ===")


# ==========================================
# KODE STATUS TRANSAKSI
# ==========================================

print("\n=== Kode Status Transaksi ===")

print("\n0001 | 0010 | 0100 | 1000")

print("Kode Biner  :", format(kode_hak_akses_2028, "04b"))

print("Kode Desimal :", kode_hak_akses_2028)


# ==========================================
# PEMERIKSAAN STATUS
# ==========================================

print("\n=== Pemeriksaan Status ===")


# ==========================================
# CEK MEMBER
# ==========================================

print("\nCek Member")

print("",format(kode_hak_akses_2028, "04b"),"&", format(bit_member_2028, "04b"))

hasil_member_bit_2028 = (kode_hak_akses_2028 & bit_member_2028)

print("Hasil Biner  :", format(hasil_member_bit_2028, "04b"))

print("Hasil Desimal :", hasil_member_bit_2028)


# ==========================================
# CEK PROMO
# ==========================================

print("\nCek Promo")

print("", format(kode_hak_akses_2028, "04b"),"&", format(bit_promo_2028, "04b"))

hasil_promo_bit_2028 = ( kode_hak_akses_2028 & bit_promo_2028)

print("Hasil Biner  :", format(hasil_promo_bit_2028, "04b"))

print("Hasil Desimal :", hasil_promo_bit_2028)


# ==========================================
# PERBANDINGAN STATUS
# ==========================================

print("\n=== Perbandingan Status ===")

print("Kode Transaksi :", format(kode_transaksi_2028, "04b"))

print("Kode Referensi :", format(kode_referensi_2028, "04b"))

print("", format(kode_transaksi_2028, "04b"),"^", format(kode_referensi_2028, "04b"))

# Operator XOR (^)
hasil_xor_2028 = (kode_transaksi_2028 ^ kode_referensi_2028)

print("Hasil Biner  :", format(hasil_xor_2028, "04b"))

print("Hasil Desimal :", hasil_xor_2028)


# ==========================================
# SHIFT
# ==========================================

print("\n=== Shift ===")

print("", format(kode_transaksi_2028, "04b"),"<< 1")

# Operator Shift Left (<<)
hasil_shift_2028 = (kode_transaksi_2028 << 1)

print("Hasil Biner  :", format(hasil_shift_2028, "05b"))

print("Hasil Desimal :", hasil_shift_2028)


# ==========================================
# SELESAI
# ==========================================

print("\n=== SELESAI ===")