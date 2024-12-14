import uuid

class Income:
    def __init__(self, date=None, source=None, amount=None, category=None, account_to=None, note=None):
        self.id = str(uuid.uuid4())  # Unique identifier for income
        self.date = date
        self.source = source
        self.amount = amount
        self.category = category
        self.account_to = account_to
        self.note = note

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_source(self, source):
        self.source = source

    def get_source(self):
        return self.source

    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category

    def set_account_to(self, account_to):
        self.account_to = account_to

    def get_account_to(self):
        return self.account_to

    def set_note(self, note):
        self.note = note

    def get_note(self):
        return self.note

    def show_data(self):
        print("\nIncome id:", self.id)
        print("date:", self.date)
        print("source:", self.source)
        print("amount:", self.amount)
        print("category:", self.category)
        print("account_to:", self.account_to)
        print("note:", self.note)
