import math

r = float(input('Enter R - '))
l = float(input('Enter L - '))
c = float(input('Enter C - '))
w = 0.2
d = w * l - 1/(w*c)
print(math.sqrt(r**2 + d**2))