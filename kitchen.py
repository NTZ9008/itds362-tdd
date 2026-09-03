class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Quantity(self.amount * multiplier)

    def __eq__(self, other):
        if isinstance(other, Quantity):
            return self.amount == other.amount
        return False

    def __repr__(self):
        return f"Quantity({self.amount})"
