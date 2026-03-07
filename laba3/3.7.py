A = int(input("Введіть значення A: "))
B = int(input("Введіть значення B: "))

if A != B:
    A = A + B
    B = A
else:
    A = 0
    B = 0

print("Нове значення A:", A)
print("Нове значення B:", B)
