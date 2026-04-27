n = int(input('Enter num - '))
f_num = n // 100
mid_num = (n // 10) % 10
last_num = n % 10

print((f_num + last_num) / mid_num == 2)