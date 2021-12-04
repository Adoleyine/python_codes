# check even or odd number
num = int(input("PLEASE ENTER NUMBER: "))
if num % 2 == 0:
    print("THE NUMBER ", num, " is even")
elif num % 2 != 0:
    print("THE NUMBER ", num, " IS ODD")
else:
    print("ERROR")

# check for positive or negative number
num = int(input("PLEASE ENTER NUMBER:"))
if num < 0:
    print("PLEASE THE NUMBER ", num, " IS NEGATIVE")
elif num > 0:
    print("PLEASE THE NUMBER ", num, " IS POSITIVE")
else:
    print("THE NUMBER IS ZERO")

# check factorial of a number
num = int(input("PLEASE ENTER NUMBER: "))
fact = 1
if num < 0:
    print("ERROR")
elif num == 0:
    print("THE FACTORIAL OF ", num, " IS 0")
else:
    for i in range(1, num+1, 1):
        fact = fact * i
print(fact)

# reversing a number
num = int(input("PLEASE ENTER NUMBER: "))
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = reverse * 10 + remainder
    num = num // 10
print(reverse)
