# Name: Naysha Putri
# NIM: 2611532028
# Question 7

full_name = "Naysha Putri"
nim = "2611532028"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

full_name_nim = first_name.lower() + nim[-3:]
intake = "20" + nim[-3:]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10} : {full_name}")
print(f"{'NIM':<10} : {nim}")
print(f"{'Username':<10} : {full_name_nim}")
print(f"{'Intake':<10} : {intake}")
print("=" * 30)