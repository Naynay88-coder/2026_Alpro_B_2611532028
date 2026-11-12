# Name: Naysha Putri
# NIM: 2611532028
# Question 5

username = input("username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")

elif not username.isalnum():
    print("Invalid: letters and digits only")

elif not username[0].isalpha():
    print("Invalid: must start with a letter")

else:
    print("Valid")
    
# Check the rules in a safe order and print the first rule that fails.
# Messages:
# "Invalid: at least 5 characters"
# "Invalid: letters and digits only"
# "Invalid: must starts with a letter"
# "valid"

nim = input("Masukkan NIM: ")

if len(nim) == 10 and nim.isdigit():
    thn = "20" + nim[:2]
    print("Valid, intake year", thn)
else:
    print("Invalid NIM")