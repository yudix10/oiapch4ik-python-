ticket = 999999
counter = 0

for num in range(1, ticket + 1):
	f_num = num // 1000
	l_num = num % 1000
	f_sum = 0
	l_sum = 0
	while f_num != 0:
		f_sum += f_num % 10
		f_num //= 10

	while l_num != 0:
		l_sum += l_num % 10
		l_num //= 10

	if f_sum == l_sum == 13:
		counter += 1

print(counter)