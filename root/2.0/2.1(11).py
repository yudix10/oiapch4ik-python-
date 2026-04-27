min = float(input('Enter minutes/mounth - '))
rub = float(input('Enter rubles/mounth - '))
over_min = float(input('Enter over_rubles/mounth - '))
all_min = float(input('Enter all_min/mounth - '))

if all_min > min:
    pay = rub + ((all_min - min) * over_min)
    print(pay)
else:
    print(f'Sum - {rub}')
