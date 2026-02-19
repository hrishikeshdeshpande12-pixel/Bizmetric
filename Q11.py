# 11.	Ask user to enter the marks and define if the user got distinction, first class, second class, pass, Fails
# If marks are more than 80 output must be “You got distinction”
# For marks more than 60 output must be “You got First class”
# Marks more than 40 will display “You got second class”
# Marks more than or equal to 35 “PASS” Otherwise Fail

# Sol'n:-

class Result:
  def __init__(self,marks):
    self.marks = marks

  def get_result(self):
    if self.marks >80:
      return "You got Distinction"
    elif self.marks > 60:
      return "You got First class"
    elif self.marks > 40:
      return "You got Second class"
    elif self.marks >= 35:
      return "PASS"
    else:
      return "Fail"
    
marks = float(input("Enter your marks: "))

student_result = Result(marks)

print(student_result.get_result())


