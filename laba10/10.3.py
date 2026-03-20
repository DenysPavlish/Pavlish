count = int(input("Введіть кількість символів для порівняння (N): "))
 
file = open("input3.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
 
output_file = open("output3.txt", "w", encoding="utf-8")
 
print("\nРядки, де перші", count, "символів збігаються з останніми", count, "символами:")
found = False
 
for line in lines:
    line = line.rstrip("\n")
    if len(line) >= count * 2:
        start = line[:count]
        end = line[-count:]
        if start == end:
            print(line)
            output_file.write(line + "\n")
            found = True
 
output_file.close()
 
if not found:
    print("Таких рядків не знайдено.")
else:
    print("Збережено у файл: output3.txt")