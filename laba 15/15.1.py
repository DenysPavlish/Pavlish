class NumberSystem:
    def __init__(self, value, base):
        self.value = value
        self.base = base

    def to_decimal(self):
        return int(str(self.value), self.base)

    def __str__(self):
        return f"{self.value} -> {self.to_decimal()}"


class Binary(NumberSystem):
    def __init__(self, value):
        super().__init__(value, 2)

    def __str__(self):
        return f"{self.value} = {self.to_decimal()}"


class Hexadecimal(NumberSystem):
    def __init__(self, value):
        super().__init__(value, 16)

    def __str__(self):
        return f"{self.value} = {self.to_decimal()}"


print(Binary("10101"))
print(Hexadecimal("E1F"))
print(NumberSystem("10101", 2))