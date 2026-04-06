import math

def y(n):
    if n == 1:
        return math.sqrt(1)
    return y(n - 1) + math.sqrt(n)

n = int(input("Введіть значення n: "))

if n < 1:
    print("n має бути більше 0!")
else:
    result = y(n)
    print(f"y({n}) = {result:.4f}")