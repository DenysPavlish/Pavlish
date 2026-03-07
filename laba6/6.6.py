str_info = "Денис КН-3 Комп'ютерні науки"

parts = str_info.split()
group = parts[1]
print(f"Група: {group}")

new_str = str_info.replace("Денис", "Павліш")
print(new_str)

words = str_info.split(" ")
print(f"Кількість слів: {len(words)}")
