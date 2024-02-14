import math
age = float(input("Enter your age: "))
age = math.floor(age)
if (age < 5):
  print("You may not attend school.")
elif (age == 5):
  print("You may start school, but you do not have to.")
else:
  print("You must have started school.")
