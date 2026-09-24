# Buat file dengan nama multi_if2_nim.py
# Buat program untuk komdisional if
# Nama Variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Program menghitung diskon belanja
 
# Input  dari user
total_belanja_2028 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
is_member_2028 = input("Apkah Anda Member? (y/t): ").strip().lower()

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2028 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2028 = input_promo_2028 in ["y", "ya"]

total_diskon_persen_2028 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus
if total_belanja_2028 > 1000000:
    total_diskon_persen_2028 += 10 #Diskon belanja besar

if is_member_2028:
    total_diskon_persen_2028 += 5 # Diskon member

if kode_promo_valid_2028:
    total_diskon_persen_2028 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2028 = total_belanja_2028 * (total_diskon_persen_2028 / 100)
total_bayar_2028 = total_belanja_2028 - nominal_diskon_2028

# Output hasil
print("\n--- Rincian Pembayara ---")
print(f"Total Diskon  : {total_diskon_persen_2028}% (Rp (nominal_diskon_2028:,.0f))")
print(f"Total Bayar   : Rp {total_bayar_2028:,.0f}")

print(f"Total Diskon yang Anda Dapatkan: {total_diskon_persen_2028}%")
# Output total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid