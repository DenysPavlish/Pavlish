num1 = int(input("Введіть перше ціле число: "))
num2 = int(input("Введіть друге ціле число: "))
num3 = int(input("Введіть третє ціле число: "))

if num1 == num2 == num3:
    print(3)
elif num1 == num2 or num2 == num3 or num1 == num3:
    print(2)
else:
    print(0)
