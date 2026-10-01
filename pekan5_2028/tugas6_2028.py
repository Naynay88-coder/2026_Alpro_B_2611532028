tinggi_2028 = int(input("Masukkan tinggi segitiga: "))
for i_2028 in range(1, tinggi_2028 + 1):
    for j_2028 in range(tinggi_2028 - i_2028):
        print(" ", end="")

    for k_2028 in range(i_2028):
        print("*", end=" ")

    print()