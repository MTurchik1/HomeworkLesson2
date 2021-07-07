# Пользователь вводит четыре числа. Найдите наибольшее четное число среди них.
# Если оно не существует, выведите фразу "not found"
numone = int(input("enter first integers"))
numtwo = int(input("enter second integers"))
numthree = int(input("enter third integers"))
numfour = int(input("enter fours integers"))
allnum = [numone, numtwo, numthree, numfour]
maxeven = 0
if numone % 2 != 0 and numtwo % 2 != 0 and numthree % 2 != 0 and numfour % 2 != 0:
   print("not found")
else:
   for n in allnum:
       if n % 2 == 0 and n > maxeven:
           maxeven = n
   print(maxeven)
