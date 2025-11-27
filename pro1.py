import sys
if len(sys.argv) ==6:
  script_name=sys.argv[0]
  n1=sys.argv[1]
  n2=sys.argv[2]
  n3=sys.argv[3]
  n4=sys.argv[4]
  n5=sys.argv[5]
else:
  n1=80
  n2=20
  n3=50
  n4=40
  n5=90
  print("No input given-using default values:")

average = (n1+n2+n3+n4+n5)/5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Average Marks:", average)
print("Grade:", grade)
print("Script Name", script_name)
