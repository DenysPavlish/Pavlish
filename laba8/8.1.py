text = input("Введіть рядок: ")

clean = text.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Рядок є паліндромом")
else:
    print("Рядок не є паліндромом")