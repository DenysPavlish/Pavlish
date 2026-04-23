class Document:
    def __init__(self, number, date):
        self.number = number
        self.date = date

    def show(self):
        print(f"Документ №{self.number} від {self.date}")


class Receipt(Document):
    def __init__(self, number, date, payer, amount):
        super().__init__(number, date)
        self.payer = payer
        self.amount = amount

    def show(self):
        print(f"Квитанція №{self.number} від {self.date} | Платник: {self.payer} | Сума: {self.amount} грн")


class Invoice(Document):
    def __init__(self, number, date, sender, receiver):
        super().__init__(number, date)
        self.sender = sender
        self.receiver = receiver

    def show(self):
        print(f"Накладна №{self.number} від {self.date} | Від: {self.sender} -> Кому: {self.receiver}")


class Check(Document):
    def __init__(self, number, date, shop, total):
        super().__init__(number, date)
        self.shop = shop
        self.total = total

    def show(self):
        print(f"Чек №{self.number} від {self.date} | Магазин: {self.shop} | До сплати: {self.total} грн")


Receipt("001", "23.04.2026", "Іваненко І.І.", 500).show()
Invoice("002", "23.04.2026", "ТОВ Постачальник", "ФОП Покупець").show()
Check("003", "23.04.2026", "Сільпо", 201).show()