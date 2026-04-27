class Product:
	def __init__(self, name: str, price: float):
		self.name = name
		self.price = price
	
	def __str__(self):
		return f'{self.name} - {self.price} руб.'



class Food(Product):
	def __init__(self, name: str, price: float, expiry_date: str):
		super().__init__(name, price)
		self.expiry_date = expiry_date

	def __str__(self):
		return f"{self.name} - {self.price}. Годен до: {self.expiry_date}"



class Electronic(Product):
	def __init__(self, name: str, price: float, warranty: int):
		super().__init__(name, price)
		self.warranty = warranty
  
	def __str__(self):
		return f'{self.name} - {self.price}. Гарантия - {self.warranty} мес.'

apple = Food("Яблоки", 99, "2023-12-31")
phone = Electronic("iPhone", 79999, 12)

print(apple)   
print(phone) 