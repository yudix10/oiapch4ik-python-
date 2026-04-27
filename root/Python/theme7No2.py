import math
list = [2,0, -2,0, 0,4]

#a
def a(list):
	radius = math.sqrt(list[0]**2 + list[1]**2)
	for i in range(2, len(list), 2):
		new_radius = math.sqrt(list[i]**2 + list[i + 1]**2)
		if new_radius > radius:
			radius = new_radius
	return radius


#b
def b(list):
	radius = math.sqrt(list[0]**2 + list[1]**2)
	for i in range(2, len(list), 2):
		new_radius = math.sqrt(list[i]**2 + list[i + 1]**2)
		if new_radius == radius:
			continue
		else:
			return False
	return True


#c
def c(list):
	list_x = [ list[i] for i in range(0, len(list), 2)]
	list_y = [ list[i] for i in range(1, len(list), 2)]
	len_on_x = abs(list_x[0] - list_x[1])
	len_on_y = abs(list_y[0] - list_y[1])
	hypotenuse = math.sqrt(len_on_x**2 + len_on_y**2)

	for i in range(2, len(list_x), 2):
		next_len_on_x = abs(list_x[i] - list_x[i + 1])
		next_len_on_y = abs(list_y[i] - list_y[i + 1])
		new_hypotenuse = math.sqrt(next_len_on_x**2 + next_len_on_y**2)
		if hypotenuse  ==  new_hypotenuse:
			continue
		else:
			return False
	return True


#d
def d(list):
	count = 0
	list_x = [ list[i] for i in range(0, len(list), 2)]
	#2 -2 0
	list_y = [ list[i] for i in range(1, len(list), 2)]
	#0 0 4

	len_on_x = abs(list_x[0] - list_x[1])
	len_on_y = abs(list_y[0] - list_y[1])
	hypotenuse = math.sqrt(len_on_x**2 + len_on_y**2)

	for i in range(0, len(list_x)):#0 1 2
		for j in range(i + 1, len(list_x)):# 1 2
			len_on_x = abs(list_x[i] - list_x[j])
			len_on_y = abs(list_y[i] - list_y[j])
			new_hypotenuse = math.sqrt(len_on_x**2 + len_on_y**2)

			if hypotenuse  ==  new_hypotenuse:
					count += 1
			else:
				hypotenuse = new_hypotenuse
	if count != 1:
		print(count)
		return True
	else:
		print(count)
		return False
print(d(list))


#e
def e(list):
	max_len = 0
	min_len = 0
	list_x = [ list[i] for i in range(0, len(list), 2)]
	#2 -2 0
	list_y = [ list[i] for i in range(1, len(list), 2)]
	#0 0 4

	len_on_x = abs(list_x[0] - list_x[1])
	len_on_y = abs(list_y[0] - list_y[1])
	min_len = math.sqrt(len_on_x**2 + len_on_y**2)
	max_len = math.sqrt(len_on_x**2 + len_on_y**2)


	for i in range(0, len(list_x)):#0 1 2
		for j in range(i + 1, len(list_x)):# 1 2
			len_on_x = abs(list_x[i] - list_x[j])
			len_on_y = abs(list_y[i] - list_y[j])
			new_hypotenuse = math.sqrt(len_on_x**2 + len_on_y**2)

			if min_len  >  new_hypotenuse:
					min_len = new_hypotenuse
			if max_len < new_hypotenuse:
					max_len = new_hypotenuse
			else:
				continue
	return min_len
	

print(e(list))