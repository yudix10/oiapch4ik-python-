try:
	while True:
		work = int(input('0 - закончить программму\n1 - продолжить: '))
		if work == 0:
			break
		if work == 1:
			num1 = int(input('Введите первое число: '))
			num2 = int(input('Введите второе число: '))
			action = input('Введите действие (+  -  /  * ) - ')
			if action == '+':
				print(f'Ответ: {num1 + num2}')
			if action == '-':
				print(f'Ответ: {num1 - num2}')
			if action == '/':
				print(f'Ответ: {num1 / num2}')
			if action == '*':
				print(f'Ответ: {num1 * num2}')
		else:
			print('Вы ввели не действие!', end='')
except ValueError:
	print('Введите число!')
except ZeroDivisionError:
	print('Делить на 0 нельзя!!!')

