numbers = [21, 70, 3, 50, 67, 26]
numbers.insert(1, -5)
min_val = min(numbers)
max_val = max(numbers)
numbers[2:2] = [1, 2, 3]
numbers.append("Павліш Денис")
count_elements = len(numbers)

print(numbers)
print(f"Min: {min_val}, Max: {max_val}")
print(f"Кількість: {count_elements}")
