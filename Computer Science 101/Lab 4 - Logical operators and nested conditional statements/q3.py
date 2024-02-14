import math
test_score = int(input("Enter a test score: "))
if test_score < 60:
  grade = "F"
if test_score < 70:
  grade = "D"
if test_score < 80:
  grade = "C"
if test_score < 90:
  grade = "B"
else:
  grade = "A"
print(grade)
