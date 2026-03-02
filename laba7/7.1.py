import random

print("Введіть кількість елементів n")

n = int(input())

print("Формування списку дійсних чисел від 0 до 1")
a = []
for i in range(n):
    a.append(random.random())
print(a)

print("Формування списку цілих чисел від -10 до 10")
b = []
for i in range(n):
    b.append(random.randint(-10, 10))
print(b)

print("Формування списку цілих чисел від 0 до 50")
c = []
for i in range(n):
    c.append(random.randint(0, 50))
print(c)

print("Введіть значення k для циклічного зсуву вліво")
k = int(input())
k = k % n

d = c[k:] + c[:k]

print("Список після циклічного зсуву вліво")

print(d)