point_diplom = float(input('Enter point of diplom - '))
staz = float(input('Enter experience - '))

if 3 <= point_diplom <= 5:
    if staz == 0:
        if point_diplom * 1 >= 45:
            print(f"Вы не проходите. ваш рейтинг - {point_diplom * 1}. Ваш рейтинг должен быть - 45.")
        else:
            print(f"Вы проходите. ваш рейтинг - {point_diplom * 13} при минимальном 45.")
    elif staz < 2:
        if point_diplom * 13 >= 45:
            print(f"Вы проходите. ваш рейтинг - {point_diplom * 13} при минимальном 45.")
        else:
            print(f"Вы не проходите. ваш рейтинг - {point_diplom * 13}. Ваш рейтинг должен быть - 45.")
    elif 2 <= staz <= 5:
        if point_diplom * 16 >= 45:
            print(f"Вы проходите. ваш рейтинг - {point_diplom * 16} при минимальном 45.")
        else:
            print(f"Вы не проходите. ваш рейтинг - {point_diplom * 16}. Ваш рейтинг должен быть - 45.")
    else:
        print("Такого стажа быть не может")
else:
    print('Вы либо врете, либо ваш балл диплома слишком низок.')