h = int(input("Введите часы: "))
m = int(input("Введите минуты: "))
s = int(input("Введите секунды: "))

def f_t(h, m, s):

    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        return "Некорректное время"

    return f"{h:02}:{m:02}:{s:02}"

print(f_t(h, m, s))