class BankAccount:
	def __init__(self, owner: str, balance: float = 0):
		self.owner = owner
		self._balance = balance

	def deposit(self, amount: float):
		if amount > 0:
			self._balance += amount
			print(f"{self.owner} пополнил баланс на: {amount}. Баланс: {self._balance}.")
		else:
			print('Сумма должна быть положительной!')

	def withdraw(self, amount: float):
		if 0 < amount <= self._balance:
			self._balance -= amount
			print(f"{self.owner} снял {amount} с банкомата. Баланс: {self._balance}.")
		else:
			print('У вас недостаточно средств!')

	def get_balance(self):
		return self._balance

own1 = BankAccount('Bro', 0)
own1.deposit(100)
own1.withdraw(50)
print(own1.get_balance())