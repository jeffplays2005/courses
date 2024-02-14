num1 = 100
num2 = 150
num3 = 5
output = ""
if num1 < num2 and num3 > num2:
  output += "A"
  if num1 + num2 > 100:
    output += "B"
    output += "C"
elif num3 < num1:
  if num1 + num2 > 200:
    output += "D"
  else:
    output += "E"
  output += "F"
else:
  if num2 > num1:
    output += "G"
  elif num3 < num2:
    output += "H"
  else:
    output += "I"
output += "J"
print(output)
