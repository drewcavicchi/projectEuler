def check_increase(number):
  number = str(number)
  positive_negative = 1
  for i in range(0, len(number) -1):
    if number[i] <= number[i+1]:
      continue
    else:
      positive_negative = positive_negative * 0
  if positive_negative == 1:
    return 1

def check_decrease(number):
  number = str(number)
  positive_negative = 1
  output = ''
  for i in range(0, len(number) -1):
    if number[i] >= number[i+1]:
      continue
    else:
      positive_negative = positive_negative * 0
  if positive_negative == 1:
    return 1

    
def findbouncy(i):
    if check_increase(i) == 1 or check_decrease(i) == 1:
      return False
    else:
      return True

i = 0; t = 0; bouncy = [] 

while t <.99:
  i+=1
  if findbouncy(i):
    bouncy.append(i)
  t = len(bouncy)/float(i)
print(i)
