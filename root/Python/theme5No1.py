k = int(input('Enter k - '))

list_nums = []

num = 0
count = 0
while k != count:
	num += 1
	number = num
	while number != 0:
		len_num = len(str(number))
		print(len_num)
		f_num = 10 ** int(len_num) / 10 
		list_nums.append(number // f_num)
		number //= 10
print(list_nums)