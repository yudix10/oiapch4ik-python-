myfile = 'text.txt'

def write_file():
	with open(myfile, 'a') as file:
		message = input('Ввeдите сообщение: ')
		file.write(message + '\n')

def read_file():
	with open(myfile, 'r') as file:
		read_file = file.read()
		print(read_file, end='')
		file.close()

def del_file():
	with open(myfile, 'wb') as file:
		pass

while True:
	ans = int(input((f"1. Запись файла\t2. Чтение файла\t3. Выход\t4. Удаление содержимого")))
	match ans:
		case 1: write_file()
		case 2: read_file()
		case 3: break
		case 4: del_file()
