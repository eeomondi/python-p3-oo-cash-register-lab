class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.last_transaction = None
        self.discount = discount  # Initialize discount

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price
        self.last_transaction = (item, price)
        return f"Added {item} for ${price:.2f}. Total is now ${self.total:.2f}."

    def void_last_transaction(self):
        if self.last_transaction is not None:
            item, price = self.last_transaction
            self.items.remove(item)
            self.total -= price
            self.last_transaction = None
            return f"Removed last transaction: {item}. Total is now ${self.total:.2f}."
        else:
            raise AttributeError("No transaction to void.")

    def remove_all_items(self):
        self.items.clear()
        self.total = 0.0
        return "All items have been removed. Total is now $0.00."

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"Discount applied: {self.discount}%. New total: ${self.total:.2f}."
        else:
            return "No discount to apply."

    def get_total(self):
        return self.total

    def get_items(self):
        return self.items.copy()

# Example Usage
register = CashRegister(20)  # Now accepts a discount
print(register.add_item('eggs', 2.50))
print(register.add_item('tomato', 1.00))
print(register.apply_discount())  # Applying discount
print(register.get_total())
print(register.get_items())
print(register.void_last_transaction())
print(register.get_total())
print(register.remove_all_items())
print(register.get_total())

   

       
