class Quantity:
    def __init__(self, amount, unit=None):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def __eq__(self, other):
        if isinstance(other, Quantity):
            return self.amount == other.amount and self.unit == other.unit
        return False

    def __repr__(self):
        return f"Quantity({self.amount}, {repr(self.unit)})"
