students = input().split()
submitted = input().split()

students_set = set(students)
submitted_set = set(submitted)

not_submitted = students_set - submitted_set

print(f"Submitted: {len(submitted_set)} students")
print(f"Not submitted: {len(not_submitted)} students")

for student in students:
    if student in not_submitted:
        print(student)