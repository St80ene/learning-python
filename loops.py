# using while loop to execute a set of command as long as the statement is true

index = 1

while index < 6:
  print(index)
  index += 1
  
# using the 'break' statement to stop the loop
while index > 10:
  print(index)
  if index == 5:
    break
  index += 1
  
# using the 'continue' keyword to continue the current iteration
while index < 15:
  index += 1
  if index == 7:
    continue
  print(index)
  
# adding else statement to the while loop
while index < 9:
  print(index)
  index += 1
else:
  print('Index is not more than 9')
  
car_list = ['volve', 'mercedes', 'hyundai']
  
for x in car_list:
  print(x)