text = input("Введіть рядок: ")

words = text.split()

lengths = []
for word in words:
    if len(word) not in lengths:
        lengths.append(len(word))


for length in lengths:
    group = []
    for word in words:
        if len(word) == length:
            group.append(word)
    if len(group) > 1:
        print(f"Довжина {length}: {' '.join(group)}")
