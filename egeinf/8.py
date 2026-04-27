from itertools import *
letters = list('СЕНТЯБРЬ')
letters.sort()
counter = 0

for i, w in enumerate(product(letters, repeat=5), 1):
    if w.count('Ь') == 0 and w[0] == 'Р' and i % 2 == 0:
        counter = i
print(counter)

#16384