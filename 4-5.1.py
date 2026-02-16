n = int(input("Введіть кількість членів N: "))

s = 0

for i in range(1, n + 1):
    a = i
    b = i + 1
    g = (a*a + b*b) / (a*a + b*b + 4)
    s += g

print("Сума =", s)
