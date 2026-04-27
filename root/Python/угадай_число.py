import random

num_users = int(input('Сколько игроков будет играть? '))


users = []
for name in range(1, num_users + 1):
  user = input(f'Введите имя {name}-ого игрока - ')
  users.append(user)

game_diff = input('Выберите сложность игры(легко, средне, сложно) - ')

if game_diff == 'легко':
	num = random.randint(1, 10)
	print('Я загадал число от 1 до 10. Сможете угадать?')
if game_diff == 'средне':
	num = random.randint(1, 100)
	print('Я загадал число от 1 до 10. Сможете угадать?')
if game_diff == 'сложно':
	num = random.randint(1, 500)
	print('Я загадал число от 1 до 10. Сможете угадать?')

flag = True
while flag:
	for name in users:
		num_user = int(input(f'{name}, напишите число - '))
		if num != num_user:
			print(f'{name} не угадал число. Ход переходит следующему игроку.')
			if num > num_user:
				print('Загаданное число больше вашего!')
			if num < num_user:
				print('Загаданное число меньше вашего!')
		else:
			print(f'{name} угадал число! Число, которое было загадано - {num}')
			flag = False
