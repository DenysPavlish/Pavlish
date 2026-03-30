import math

def compare_positive_halves(sequence):
    n = len(sequence)
    if n == 0:
        return "Послідовність порожня"
 
    first_size = math.ceil(n / 2)
    second_size = math.floor(n / 2)
 
    first_half  = sequence[:first_size]
    second_half = sequence[first_size:] 
 
    count_first  = sum(1 for x in first_half  if x > 0)
    count_second = sum(1 for x in second_half if x > 0)
 
    result = (
        f"Перша половина  ({first_size} ел.): {first_half}  → {count_first} додатних\n"
        f"Друга половина  ({second_size} ел.): {second_half}  → {count_second} додатних\n"
    )
    if count_first > count_second:
        result += "Більше додатних у ПЕРШІЙ половині"
    elif count_second > count_first:
        result += "Більше додатних у ДРУГІЙ половині"
    else:
        result += "Кількість додатних ОДНАКОВА в обох половинах"
 
    return result
 
seq1 = [3, -1, 5, -2, 7, -4, 2]  
seq2 = [-1, -2, 3, 4, -5, 6]      
 
print(f"Послідовність: {seq1}")
print(compare_positive_halves(seq1))
 
print()
print(f"Послідовність: {seq2}")
print(compare_positive_halves(seq2))