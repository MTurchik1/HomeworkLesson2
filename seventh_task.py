# Компьютер загадывает число от 1 до 100.
# У пользователя три попытки отгадать.
# После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число.
import random
num = random.randrange(1,100)
tryans = 3
ans = None
while tryans != 0:
   ans = int(input("input num 1-100"))
   tryans -=1
   if ans > num:
       print("too hight num")
   elif ans < num:
       print("too small num")
   else:
       print("congratulation")
       break