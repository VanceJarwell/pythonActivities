#Set the counter and total to 0
counter = 0
total = 0
avg = 0
maximum = None
minimum = None

while True:
  number = input("Enter a number: ")
  try:
    number = float(number)
    if minimum is None or number < minimum:
      minimum = number
    if maximum is None or number > maximum:
      maximum = number
  except:
    if number == 'Done' or number == 'done':
      break
    else:
      print ('Invalid Input')
      continue
print(maximum, minimum)
