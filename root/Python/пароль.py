import random
def password(count):
	end_pas = []
	for i in range(count):
		end_pas.append(random.randint(0, 9))
	print(''.join(map(str, end_pas)))

print(password(10))