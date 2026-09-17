print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2028 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2028 = [int(angka.strip()) for angka in input_data_2028.split(",")]

nilai_dicari_2028 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2028 = nilai_dicari_2028 in data_2028
print("\nOperator keanggotaan IN")
print(nilai_dicari_2028, "in", data_2028, "=", hasil_2028)

# Operator not in
hasil_2028 = nilai_dicari_2028 not in data_2028
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2028, "NOT IN", data_2028, "=", hasil_2028)

print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1_2028 menggunakan list dari input pengguna
objek1_2028 = data_2028

# objek2_2028 merujuk pada objek yang sama dengan objek1_2028
objek2_2028 = objek1_2028

# objek3_2028 memiliki isi sama, tetapi merupakan objek baru
objek3_2028 = data_2028.copy()

print("objek1 =", objek1_2028)
print("objek2 =", objek2_2028)
print("objek3 =", objek3_2028)

# Operator is
hasil = objek1_2028 is objek2_2028
print("\nOperator identitas IS")
print("objek is objek2 =", hasil_2028)

# Operator is not 
hasil_2028 = objek1_2028 is not objek3_2028
print("\nOperator identitas IS NOT")
print("objek1_2028 is not objek3_2028 =", hasil_2028)

# Membandingkan identitas dan nilai 
print("\nPerbandingan identitas dan nilai")
print("objek is objek3 =", objek1_2028 is objek3_2028)
print("objek1 == objek3 =", objek1_2028 == objek3_2028)
print("objek1 is objek2 =", hasil)

# Membandingkan identitas dan nilai
print("\nOperator identitas dan nilai")
print("objek1 is objek3 =", objek1_2028 is objek3_2028)
print("objek1 is objek3 =", objek1_2028 == objek3_2028)