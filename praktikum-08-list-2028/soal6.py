LAST_DIGIT = 8  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
total = 0
above_limit = 0

for day in range(1, 8):
    expense = int(input(f"Day {day}: "))
    expenses.append(expense)

    total += expense

    if expense > daily_limit:
        above_limit += 1

    if day == 1 or expense > highest:
        highest = expense
        highest_day = day

average = total / 7

print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", round(average, 1))
print(f"Highest: day {highest_day} ({highest})")
print("Days above limit:", above_limit)