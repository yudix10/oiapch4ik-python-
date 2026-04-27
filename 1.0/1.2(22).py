import math
x = float(input('Enter radians - '))

grad = 180 * x/math.pi
min = grad * 60
sec = min * 60
print(f"Grad - {grad} Min - {min} Sec - {sec}")