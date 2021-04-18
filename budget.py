class Category:
    def __init__(self, category, amount):
        self.amount = 0
        self.category = category
        
    def depost_fund(self, amount):
        self.amount += amount

    def withdraw_fund(self, amount):
        self.amount -= amount

    def compute_balance(self):
        return self.amount

    def transfering_balance(self, amount, category):
        self.amount -= amount

