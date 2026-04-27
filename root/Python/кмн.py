import random

items = ['камень', 'ножницы', 'бумага']
flag = True

while flag:
	ans = random.randint(0, 2)
	ans_item = items[ans]
	ans_user = input('Выберите чем вам ходить - ')
	if (ans_user == 'камень' and ans_item == 'ножницы') or (ans_user == 'ножницы' and ans_item == 'бумага') or (ans_user == 'бумага' and ans_item == 'камень'):
		print(f'Выбор игрока - {ans_user}. \nВыбор соперника - {ans_item}. \nИгрок победил.')
		flag = False
	if (ans_item == 'камень' and ans_user == 'ножницы') or (ans_item == 'ножницы' and ans_user == 'бумага') or (ans_item == 'бумага' and ans_user == 'камень'):
		print(f'Выбор игрока - {ans_user}. \nВыбор соперника - {ans_item}. \nБот победил.')
		flag = False
	if ans_item == ans_user:
		print(f'Выбор игрока - {ans_user}. \nВыбор соперника - {ans_item}. \nНичья.')
