text = input("Введіть рядок: ")

words = text.split()

print("Слова без літер, що повторюються:")
for word in words:
    word_lower = word.lower()
    has_repeat = False
    for i in range(len(word_lower)):
        for j in range(i + 1, len(word_lower)):
            if word_lower[i] == word_lower[j]:
                has_repeat = True
    if not has_repeat:
        print(word)