class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{brand} {model}"
hp = Laptop('BMW', 'X5', 57000) # price in $
print(hp.laptop_name)