# Пользователь вводит номер месяца, вывести название месяца. (попробуйте решить с применением цикла)


num_month = int(input('''enter the month number from 1 to 12,
 if you want to exit enter 0'''))
while num_month != 0:
    if num_month == 1:
        print('January')
    elif num_month == 2:
        print('February')
    elif num_month == 3:
        print('March')
    elif num_month == 4:
        print('April')
    elif num_month == 5:
        print('May')
    elif num_month == 6:
        print('June')
    elif num_month == 7:
        print('July')
    elif num_month == 8:
        print('August')
    elif num_month == 9:
        print('September')
    elif num_month == 10:
        print('October')
    elif num_month == 11:
        print('November')
    elif num_month == 12:
        print('December')
    elif num_month > 12 or num_month < 0:
        print('''Please enter the month number from 1 to 12,
     if you want to exit enter 0''')
    num_month = int(input())
else:
    print('Goodbye')













