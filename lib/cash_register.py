class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.items = []
        self.last_transaction = None

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

    def get_total(self):
        return self.total

    def get_items(self):
        return self.items.copy()

#Usage
register = CashRegister()
print(register.add_item('eggs', 2.50))  # Adding eggs
print(register.add_item('tomato', 1.00))  # Adding tomato
print(register.get_total())  # Should print total
print(register.get_items())  # Should print items added
print(register.void_last_transaction())  # Removing last item (tomato)
print(register.get_total())  # Updated total
print(register.remove_all_items())  # Clear all items
print(register.get_total())  # Should be 0.0

   

       
