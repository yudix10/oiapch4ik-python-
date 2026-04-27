class Room:
	def __init__(self, number: int, capacity: int):
		self.number = number
		self.capacity = capacity
		self.is_booked = False

	def book(self):
		if not self.is_booked:
			self.is_booked = True
			return f'{self.number} комната забронирована!'
		return f'Комната {self.number} уже занята!'

class Hotel(Room):
	def __init__(self, name: str):
		self.name = name
		self.rooms = []
	
	def add_room(self, room: Room):
		self.rooms.append(room)

	def book_room(self, book_number: int):
		for room in self.rooms:
			if room.number == book_number:
				return room.book()
		return "Комната не найдена!"

hotel = Hotel("Grand Hotel")
hotel.add_room(Room(101, 2))
hotel.add_room(Room(102, 4))

print(hotel.book_room(101))  # Комната 101 забронирована!
print(hotel.book_room(101))