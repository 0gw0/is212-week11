class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._discount_rate = 0
        self._tax_rate = 0
        self._category = "Generic"

    def apply_discount(self):
        discounted_price = self.price - (self.price * self._discount_rate)
        print(
            f"Discounted price for {self.name} ({self._category}): {discounted_price}"
        )
        return discounted_price

    def calculate_tax(self):
        tax = self.price * self._tax_rate
        print(f"Tax for {self.name} ({self._category}): {tax}")
        return tax

    def get_final_price(self):
        return self.apply_discount() + self.calculate_tax()


class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self._discount_rate = 0.10  # 10% discount
        self._tax_rate = 0.15  # 15% tax
        self._category = "Electronics"


class Clothing(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self._discount_rate = 0.20  # 20% discount
        self._tax_rate = 0.08  # 8% tax
        self._category = "Clothing"


class Grocery(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        self._discount_rate = 0.05  # 5% discount
        self._tax_rate = 0.02  # 2% tax
        self._category = "Grocery"
