def func(num1, num2):
    counter_num1 = 0
    counter_num2 = 0
    while num1 != 0 or num2 != 0:
        if num1 != 0:
            num1 = num1 // 10
            counter_num1 += 1
        else:
            return counter_num1

        if num2 != 0:
            num2 = num2 // 10
            counter_num2 += 1
        else:
            return counter_num2

print(func(3, 211))