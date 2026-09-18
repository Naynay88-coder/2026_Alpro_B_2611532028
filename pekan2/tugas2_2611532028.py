from typing import Final

# ==========================================
# KONSTANTA
# ==========================================
BATAS_LULUS: Final = 75.0


# ==========================================
# INPUT DATA PRAKTIKAN
# ==========================================
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_2028 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_2028 = input("Masukkan Jenis Kelamin (L/P) : ")
umur_2028 = int(input("Masukkan Umur : "))
nilai_2028 = float(input("Masukkan Skor Tes Awal : "))


# ==========================================
# DATA TAMBAHAN
# ==========================================

# Alamat menggunakan multiline string
alamat_2028 = """Jl. Pagambiran Permai,
Kecamatan Lubuk Begalung,
Kota Padang"""

# Token identifikasi menggunakan tipe data complex
id_token_2028 = 100 + 3j


# ==========================================
# VALIDASI STATUS KELULUSAN
# ==========================================
lulus_2028 = nilai_2028 >= BATAS_LULUS

# ==========================================
# MENAMPILKAN DATA DAN TIPE DATA
# ==========================================
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print(f"Nama Mahasiswa : {nama_2028} | Tipe: {type(nama_2028)}")
print(f"Jenis Kelamin  : {jenis_kelamin_2028} | Tipe: {type(jenis_kelamin_2028)}")

print("Alamat Domisili:")
print(f"{alamat_2028} | Tipe: {type(alamat_2028)}")

print(f"Umur           : {umur_2028} tahun | Tipe: {type(umur_2028)}")
print(f"Skor Tes Awal  : {nilai_2028} | Tipe: {type(nilai_2028)}")
print(f"ID Token Sinyal: {id_token_2028} | Tipe: {type(id_token_2028)}")


# ==========================================
# MENAMPILKAN STATUS KELULUSAN
# ==========================================
print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

print(f"Batas Minimum Nilai : {BATAS_LULUS}")
print(f"Apakah Dinyatakan Lulus? : {lulus_2028} | Tipe: {type(lulus_2028)}")

