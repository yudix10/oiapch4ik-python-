class Animal:
	def make_sound(self):
		raise NotImplementedError("Должен быть определён в дочернем классе!")

class Dog(Animal):
	def make_sound(self):
		return 'Гав Гав!'

class Cat(Animal):
	def make_sound(self):
		return 'мяу мяу!'

class Cow(Animal):
	def make_sound(self):
		return 'му му!'

animals = [Dog(),Cat(),Cow()]

for animal in animals:
	print(animal.make_sound())