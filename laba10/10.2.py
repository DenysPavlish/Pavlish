file = open("input2.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
 
numbers = []
for line in lines:
    line = line.strip()
    if line != "":
        numbers.append(int(line))
 
minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
 
print("Числа у файлі:", numbers)
print("Мінімальне число:", minimum)