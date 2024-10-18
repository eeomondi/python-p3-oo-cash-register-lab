class CashRegister:
    def __init__(self):
        self.total = 0
        self.discount = 0
        self.last_transaction = 0

    def add_item(self, price, quantity=1):
        self.last_transaction = price * quantity
        self.total += self.last_transaction

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.total * self.discount / 100)
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0  

