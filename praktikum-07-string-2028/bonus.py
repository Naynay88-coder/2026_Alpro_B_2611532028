# Name: Naysha Putri
# NIM: 2611532028
# Question bonus

kalimat = input("Masukkan kalimat: ")
clean = kalimat.replace(" ", "").lower()

if clean == clean[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")
