import math

x = float(input('Введіть число:'))

y = math.sin((x + 2.3 * math.log10(x + 1)) / math.sqrt(2 * math.log(x) + math.cos(x)))

print('Результат рівняння: ' + str(y))