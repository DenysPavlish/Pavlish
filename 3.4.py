parenthesis = input("Введіть символ-дужку: ")

if parenthesis == "(" or parenthesis == ")":
    print("Кругла дужка")
elif parenthesis == "[" or parenthesis == "]":
    print("Квадратна дужка")
elif parenthesis == "{" or parenthesis == "}":
    print("Фігурна дужка")
else:
    print("Невідомий символ")
