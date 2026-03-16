
text = input("Введіть рядок зі словами: ")

words = text.split()

if not words:
    print("Рядок не містить слів")
else:
    digit_sets = []

    print("\nМножини цифр для кожного слова:")
    for word in words:
        digits = set(ch for ch in word if ch.isdigit())
        digit_sets.append(digits)
        print(f"  '{word}' -> {digits}")

    intersection = digit_sets[0].copy()
    for s in digit_sets[1:]:
        intersection &= s

    print(f"\nПеретин усіх множин: {intersection}")
    if intersection:
        print(f"Спільні цифри: {', '.join(sorted(intersection))}")
    else:
        print("Спільних цифр немає")