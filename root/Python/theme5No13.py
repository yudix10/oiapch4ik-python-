n = int(input('Enter n - '))

if n ** 3 == int(str(n**3)[::-1]) or n ** 5 == int(str(n**5)[::-1]) or n ** 4 == int(str(n**4)[::-1]):
  print(f"{n} => {n ** 3} ")
else:
  print('{n} NO')
