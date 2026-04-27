n = str(input('Enter n - '))

otv = ''
list_n = list(n)
max = int(list_n[0])

for i in range(len(list_n)):
		max = 0
		for j in list_n:
				if int(j) > max:
						max = int(j)
		otv += str(max)
		list_n.remove(str(max))
print(otv)