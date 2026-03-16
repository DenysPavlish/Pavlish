text = input("Введіть рядок: ")

S1 = set()  
S2 = set()  

for i, ch in enumerate(text):
    if i % 2 == 0 and ch.islower() and ch.isalpha() and ch.isascii():
        S1.add(ch)
    elif i % 2 == 1 and ch.isupper() and ch.isalpha() and ch.isascii():
        S2.add(ch)

print(f"\nРядок: {text}")
print(f"S1 (маленькі на парних позиціях): {S1}")
print(f"S2 (великі на непарних позиціях): {S2}")
print(f"Кількість елементів S1: {len(S1)}")
print(f"Кількість елементів S2: {len(S2)}")

if len(S1) > len(S2):
    print("S1 містить більше елементів")
elif len(S2) > len(S1):
    print("S2 містить більше елементів")
else:
    print("Множини містять однакову кількість елементів")