target_char = input("Введіть символ для пошуку: ")
target_pos = int(input("Введіть позицію (починаючи з 1): "))
 
file = open("input1.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
 
print("\nРядки, де на позиції", target_pos, "стоїть символ", repr(target_char), ":")
 
found = False
for line in lines:
    line = line.rstrip("\n")
    if len(line) >= target_pos:
        if line[target_pos - 1] == target_char:
            print(line)
            found = True
 
if not found:
    print("Таких рядків не знайдено.")