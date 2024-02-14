t1 = ["January", "March", "May", "July", "August", "October", "December"]
te = ["February"]
td = ["April", "June", "September", "November"]
month = input("Enter the month: ")
if (month in t1):
  print(f"{month} has 31 days.")
elif (month in te):
  print(f"{month} has 28 days.")
elif (month in td):
  print(f"{month} has 30 days.")
else:
  print("Invalid month.")
