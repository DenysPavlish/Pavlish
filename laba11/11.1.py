import math
import random
 
# 1. Швидке сортування
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left   = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right  = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 2. Пошук елементу за значенням 
def search_by_value(lst, value):
    for i, elem in enumerate(lst):
        if elem == value:
            return i
    return -1
 
# 3. Пошук перших п'яти мінімальних елементів
def first_five_min(lst):
    sorted_lst = quick_sort(lst)
    return sorted_lst[:5]
 
# 4. Пошук середнього арифметичного
def arithmetic_mean(lst):
    if not lst:
        return None
    return sum(lst) / len(lst)
 
# 5. Список без повторів 
def remove_duplicates(lst):
    seen = []
    for elem in lst:
        if elem not in seen:
            seen.append(elem)
    return seen
 
data = [5, 3, 8, 1, 9, 2, 7, 4, 6, 3, 1, 8, 5, 2, 10]
print(f"Початковий список : {data}")
print(f"Після сортування  : {quick_sort(data)}")
print(f"Пошук значення 7  : індекс {search_by_value(data, 7)}")
print(f"Пошук значення 99 : індекс {search_by_value(data, 99)}")
print(f"5 мінімальних     : {first_five_min(data)}")
print(f"Середнє арифметич.: {arithmetic_mean(data):.4f}")
print(f"Без повторів      : {remove_duplicates(data)}")