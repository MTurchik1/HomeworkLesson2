# Пользователь вводит сумму вклада в банк и годовой процент.
# Найдите сумму вклада через 5 лет
deposit = int(input("enter the amount of the deposit"))
percent = float(input("enter the annual percentage"))
oneyearsdep = deposit + deposit * (percent / 100)
twoyearsdep = oneyearsdep + oneyearsdep * (percent / 100)
threeearsdep = twoyearsdep + twoyearsdep * (percent / 100)
fouryearsdep = threeearsdep + threeearsdep * (percent / 100)
fiveyearsdep = fouryearsdep + fouryearsdep * (percent / 100)
print(round(fiveyearsdep, 2))