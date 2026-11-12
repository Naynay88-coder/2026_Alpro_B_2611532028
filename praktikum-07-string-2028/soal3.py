# Name: Naysha Putri
# NIM: 2611532028
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:])

text = "Naysha Putri"
count = 0

for char in text.lower():
    if char in "aiueo":
        count += 1
print("vowels:", count)