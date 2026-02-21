import random

main_list = [random.randint(-50, 50) for _ in range(25)]
A1 = [x for x in main_list if x > 0]
A2 = [x for x in main_list if x < 0]

print(f"Основний список: {main_list}")
print(f"Додатні (A1): {A1}")
print(f"Від'ємні (A2): {A2}")
