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

food = Category("Food", 1000)
food.depost_fund(1000)
food.withdraw_fund(100)
print(food.compute_balance())

clothing = Category("Clothing", 2500)
food.transfering_balance(150, clothing)
clothing.withdraw_fund(75)

entertainment = Category("Entartainment", 500)
entertainment.depost_fund(200)
entertainment.withdraw_fund(120)

print(food)
print(clothing)
print(entertainment)

