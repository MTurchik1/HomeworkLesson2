# Дано два числа. Вывести yes, если они отличаются на 100, иначе вывести No.
numone = int(input("enter first number"))
numtwo = int(input("enter second number"))
diff = numone - numtwo
diff = abs(diff)
if diff == 100:
   print("yes")
else:
   print("no")