# Name: Naysha Putri
# NIM: 2611532028
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

# 
full_name = "Naysha Putri"
nim = "2611532028"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

full_name_nim = first_name.lower() + nim[-3:]

print(full_name_nim)
# Build the username: first name in lowercase + last 3 digits of the NIM
# Do not use split().