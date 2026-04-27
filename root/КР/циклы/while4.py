num = 120
counter = 0
for i in range(0, num + 1):
    num = i
    rev_num = 0
    while i != 0:
        last_num = i % 10
        rev_num = rev_num * 10 + last_num
        i //= 10
    if rev_num == num:
        print(rev_num)
        counter += 1
print(f'Counter - {counter}')