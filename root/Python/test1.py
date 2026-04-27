num = int(input('Enter number - '))
divider = 2
while num != 1:
	while num % divider == 0:
		print(divider)
		num //= divider
	else:
		divider += 1