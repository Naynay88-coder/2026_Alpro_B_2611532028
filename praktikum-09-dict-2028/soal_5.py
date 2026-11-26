n = int(input())

cash = {}

for i in range(n):
    data = input().split()
    name = data[0]
    amount = int(data[1])

    if name in cash:
        cash[name] += amount
    else:
        cash[name] = amount

total_cash = sum(cash.values())

for name, total in cash.items():
    print(f"{name}: {total}")

print(f"Total cash: {total_cash}")

top_name = max(cash, key=cash.get)
print(f"Top contributor: {top_name} ({cash[top_name]})")