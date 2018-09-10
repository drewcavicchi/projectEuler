def multiple_3(number):
  if number % 3 == 0:
    return True
  else:
     return False

def multiple_5(number):
  if number % 5 == 0:
    return True
  else:
    return False

multiples_5_3 = []

for i in range(0, 1000):
  if multiple_3(i) or multiple_5(i):
    multiples_5_3.append(i)

print(sum(multiples_5_3))
