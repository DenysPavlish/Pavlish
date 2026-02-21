users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]

print(f"Tom: {users.count('Tom')}")
print(f"Mark: {users.count('Mark')}")
print(f"Alice: {users.count('Alice')}")
print(f"John: {users.count('John')}")

users.pop(2)
if "Tom" in users:
    users.remove("Tom")

print(users)
