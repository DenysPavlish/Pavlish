side_a = float(input("Введіть довжину першої сторони трикутника: "))
side_b = float(input("Введіть довжину другої сторони трикутника: "))
side_c = float(input("Введіть довжину третьої сторони трикутника: "))

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    if side_a == side_b == side_c:
        print("Рівносторонній трикутник")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("Рівнобедрений трикутник")
    else:
        print("Різносторонній трикутник")
else:
    print("Трикутник не існує")
