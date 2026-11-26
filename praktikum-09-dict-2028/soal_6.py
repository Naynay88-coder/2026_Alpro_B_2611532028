schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"]
}

# 6a. Mencari hari dengan mata kuliah terbanyak
busiest_day = max(schedule, key=lambda day: len(schedule[day]))
course_count = len(schedule[busiest_day])

print(f"Busiest day: {busiest_day} ({course_count} courses)")

# 6b. Menghitung jumlah hari mata kuliah muncul
course = input("Course name: ")

count = 0
for day in schedule:
    if course in schedule[day]:
        count += 1

print(f"{course}: {count} days")