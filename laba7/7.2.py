import random


print("Введіть кількість рядків m")
m = int(input())

print("Введіть кількість стовпців n")
n = int(input())

print("Матриця з дійсних чисел від 0 до 1")
a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.random())
    a.append(row)
for row in a:
    print(row)

print("Матриця з цілих чисел від -10 до 10")
b = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(-10, 10))
    b.append(row)
for row in b:
    print(row)

print("Матриця з цілих чисел від 0 до 20")
c = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(0, 20))
    c.append(row)
for row in c:
    print(row)

print("Матриця з дійсних чисел від -10 до 10")
d = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.uniform(-10, 10))
    d.append(row)
for row in d:
    print(row)

print("Головна діагональ")
main_diag = []
for i in range(min(m, n)):
    main_diag.append(d[i][i])
print(main_diag)

print("Побічна діагональ")
side_diag = []
for i in range(min(m, n)):
    side_diag.append(d[i][n - 1 - i])
print(side_diag)