file = open("matrix_input.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
 
matrix = []
for line in lines:
    line = line.strip()
    if line != "":
        values = line.split()
        row = []
        for value in values:
            row.append(int(value))
        matrix.append(row)
 
print("Вхідна матриця:")
for row in matrix:
    for element in row:
        print(str(element).rjust(5), end="")
    print()
print()
 
negative_rows = []
positive_rows = []
 
for i in range(len(matrix)):
    has_negative = False
    for element in matrix[i]:
        if element < 0:
            has_negative = True
    if has_negative:
        negative_rows.append(i)
    else:
        positive_rows.append(i)
 
result = []
for row in matrix:
    result.append(row[:])
 
pairs_count = len(negative_rows)
if len(positive_rows) < pairs_count:
    pairs_count = len(positive_rows)
 
print("Кількість пар для обміну:", pairs_count)
for i in range(pairs_count):
    neg_index = negative_rows[i]
    pos_index = positive_rows[i]
    print("  Міняємо рядок", neg_index + 1, "(з від'ємними) і рядок", pos_index + 1, "(без від'ємних)")
    result[neg_index], result[pos_index] = result[pos_index], result[neg_index]
 
print()
print("Результуюча матриця B:")
for row in result:
    for element in row:
        print(str(element).rjust(5), end="")
    print()
 
file = open("matrix_output.txt", "w", encoding="utf-8")
for row in result:
    str_values = []
    for element in row:
        str_values.append(str(element))
    file.write(" ".join(str_values) + "\n")
file.close()
 
print("\nРезультат збережено у файл: matrix_output.txt")