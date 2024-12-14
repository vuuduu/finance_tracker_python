import uuid

class Expense:
    def __init__(self, date=None, vendor=None, amount=None, category=None, card_used=None, note=None):
        self.id = str(uuid.uuid4)
        self.date = date
        self.vendor = vendor
        self.amount = amount
        self.category = category
        self.card_used = card_used
        self.note = note

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date
    
    def set_vendor(self, vendor):
        self.vendor = vendor

    def get_vendor(self):
        return self.get_vendor
    
    def set_amount(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount
    
    def set_category(self, category):
        self.category = category

    def get_category(self):
        return self.category
    
    def set_card_used(self, card_used):
        self.card_used = card_used

    def get_card_used(self):
        return self.card_used
    
    def set_note(self, note):
        self.note = note

    def get_note(self):
        return self.note
    
    def show_data(self):
        print("\nExpense id:", self.id)
        print("date:", self.date)
        print("vendor:", self.vendor)
        print("amount:", self.amount)
        print("category:", self.category)
        print("card_used:", self.card_used)
        print("note:", self.note)