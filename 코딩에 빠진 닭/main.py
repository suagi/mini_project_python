
daily_sales = []
monthly_sales = 0

with open('chicken.txt', 'r', encoding='UTF-8') as tong:
    for t in tong:
        daily_sales.append(t.strip().split(': '))

for i in range(len(daily_sales)):
    monthly_sales += int(daily_sales[i][1])

print(monthly_sales // len(daily_sales))

print("---------------------- 다른풀이 ----------------------")

monthly = 0
days = 0

with open('chicken.txt', 'r', encoding='UTF-8') as tong:
    for t in tong:
        daily = t.strip().split(": ")
        monthly += int(daily[1])
        days += 1

print(monthly // days)