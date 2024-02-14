import math
test_score = int(input("Enter a test score: "))
if test_score >= 90:
  grade = "A"
if test_score >= 80:
  grade = "B"
if test_score >= 70:
  grade = "C"
if test_score >= 60:
  grade = "D"
else:
  grade = "F"
print(grade)
