import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть крок h: "))

x = a

while x <= b:
    if x == 0 or x + 3 < 0:
        print("x =", x, "— вихід за область допустимих значень")
        break
    y = 1/x + math.sqrt(x + 3) + 6
    print("x =", x, " y =", y)
    x += h
