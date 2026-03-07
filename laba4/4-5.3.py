n = int(input("Введіть число N: "))

a = 0
b = 1

print(a, b, end=" ")

while True:
    c = a + b
    if c % n == 0:
        print(c)
        break
    print(c, end=" ")
    a = b
    b = c
