
import math
def r_to_d(r):
    d = r * (180 / math.pi)
    m = (d - int(d)) * 60
    s = (m - int(m)) * 60
    return int(d), int(m), round(s)
r = float(input("Введите угол в радианах: "))
d, m, s = r_to_d(r)
print(f"Угол: {d}° {m}' {s}''")

