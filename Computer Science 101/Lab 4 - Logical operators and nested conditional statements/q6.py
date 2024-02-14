spring = ["September", "October", "November"]
summer = ["December", "January", "February"]
autumn = ["March", "April", "May"]
winter = ["June", "July", "August"]

i_m = input("Enter the month: ")
if (i_m in spring):
  print(f"{i_m} is in Spring.")
elif (i_m in summer):
  print(f"{i_m} is in Summer.")
elif (i_m in autumn):
  print(f"{i_m} is in Autumn.")
elif (i_m in winter):
  print(f"{i_m} is in Winter.")
else:
  print("Unknown month.")
