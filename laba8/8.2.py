text = input("Введіть рядок: ")

words = text.split()

print("Слова непарної довжини:")
for word in words:
    if len(word) % 2 != 0:
        print(word)