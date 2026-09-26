# ============================================================
# SISTEM LOKET ALPRO ADVENTURE PARK
# Nama : Naysha Putri
# NIM  : 2611532028
# ============================================================

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# ============================================================
# 1. INPUT DATA PENGUNJUNG
# ============================================================

nama_pengunjung_2028 = input("Masukkan Nama Pengunjung       : ")
umur_2028 = int(input("Input umur anda                : "))
sim_2028 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]


# ============================================================
# 2. PEMILIHAN WAHANA MENGGUNAKAN MATCH-CASE
# ============================================================

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba          (Rp 50,000)")
print("  2. Arung Jeram           (Rp 75,000)")
print("  3. Motor ATV Ekstrim     (Rp 120,000)")
print("  4. Roller Coaster Kilat  (Rp 100,000)")
print("  5. All-Access VIP        (Rp 220,000)")

pilihan_paket_2028 = int(input("\nMasukkan nomor paket (1-5) : "))

match pilihan_paket_2028:
    case 1:
        nama_wahana_2028 = "Wahana Safari Rimba"
        harga_satuan_2028 = 50000

    case 2:
        nama_wahana_2028 = "Wahana Arung Jeram"
        harga_satuan_2028 = 75000

    case 3:
        nama_wahana_2028 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2028 = 120000

    case 4:
        nama_wahana_2028 = "Wahana Roller Coaster Kilat"
        harga_satuan_2028 = 100000

    case 5:
        nama_wahana_2028 = "Wahana All-Access VIP"
        harga_satuan_2028 = 220000

    case _:
        print("\nPaket wahana tidak valid!")
        print("Program Selesai")
        exit()

jumlah_tiket_2028 = int(input("Masukkan jumlah tiket          : "))

# If tunggal untuk mengecek jumlah tiket
if jumlah_tiket_2028 <= 0:
    print("Peringatan: Kuota tiket tidak valid.")
    print("Program Selesai")
    exit()
# ============================================================
# 3. INPUT MEMBER DAN KODE PROMO
# ============================================================

is_member_2028 = input("Apakah Anda member? (y/t)     :").strip().lower()

kode_promo_valid_2028 = input("Apakah kode promo valid? (y/t) :").strip().lower()

# ============================================================
# 4. VALIDASI IZIN KENDALI WAHANA
# ============================================================

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

# Khusus Motor ATV Ekstrim
if pilihan_paket_2028 == 3:

    if umur_2028 >= 17 and sim_2028 == 'y':
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")

    elif umur_2028 >= 17 and sim_2028 != 'y':
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV "
              "(wajib didampingi instruktur).")

    elif umur_2028 < 17 and sim_2028 == 'y':
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")

    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")

# Untuk paket selain ATV
else:
    if umur_2028 >= 10:
        print("Status Akses: Anda memenuhi batas usia untuk wahana ini.")
    else:
        print("Status Akses: Anda belum memenuhi batas usia untuk wahana ini.")

# ============================================================
# 5. PERHITUNGAN SUBTOTAL
# ============================================================

subtotal_2028 = harga_satuan_2028 * jumlah_tiket_2028

# ============================================================
# 6. MULTI-IF TERPISAH UNTUK AKUMULASI DISKON
# ============================================================

total_diskon_persen_2028 = 0

# Diskon Belanja Besar
if subtotal_2028 >= 200000:
    total_diskon_persen_2028 += 10

# Diskon Member
if is_member_2028 in ['y', 'ya']:
    total_diskon_persen_2028 += 5

# Diskon Voucher Promo
if kode_promo_valid_2028 in ['y', 'ya']:
    total_diskon_persen_2028 += 15

# Diskon Tambahan Rombongan
if jumlah_tiket_2028 >= 5:
    total_diskon_persen_2028 += 5

# ============================================================
# 7. PERHITUNGAN TOTAL PEMBAYARAN
# ============================================================

nominal_diskon_2028 = subtotal_2028 * (total_diskon_persen_2028 / 100)
total_bayar_2028 = subtotal_2028 - nominal_diskon_2028

# ============================================================
# 8. AUDIT TRANSAKSI MENGGUNAKAN IF-ELSE
# ============================================================

if total_bayar_2028 > 300000:
    catatan_layanan_2028 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_2028 = "Terima kasih telah berkunjung."

# ============================================================
# 9. OUTPUT RINCIAN TRANSAKSI
# ============================================================

print("\n--- RINCIAN PEMBAYARAN ---")
print(f"Nama Pengunjung  : {nama_pengunjung_2028}")
print(f"Wahana           : {nama_wahana_2028}")
print(f"Harga Satuan     : Rp {harga_satuan_2028:,.0f}")
print(f"Jumlah Tiket     : {jumlah_tiket_2028}")
print(f"Subtotal Belanja : Rp {subtotal_2028:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_2028}% "f"(Rp {nominal_diskon_2028:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_2028:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_2028}")

print("\nProgram Selesai")