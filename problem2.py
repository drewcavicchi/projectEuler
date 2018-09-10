first_number = 0
second_number = 1 
total = 0
output = 0

def calculate_fibonacci(first_number, second_number):
  output = first_number + second_number
  return output

while output < 4000000:
  output = calculate_fibonacci(first_number, second_number)
  if output % 2 == 0:
    total += output
  first_number = second_number
  second_number = output
print(total)
