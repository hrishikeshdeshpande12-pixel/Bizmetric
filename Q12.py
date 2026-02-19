# 12.	Ask user to enter information about salary of the employee per year and rating received as A, B, C, D
# If salary upto 5 lpa then increament based on ratings are  A = 16% , B=12%, C= 10%, D=6%
# If salary upto 10 lpa then increament based on ratings are  A = 14% , B=10%, C= 8%, D=6%
# If salary upto 15 lpa then increament based on ratings are  A = 8% , B=6%, C= 4%, D = no gincrement
# If salary upto 23 lpa then increament based on ratings are  A = 7% , B=5%, C= 4%, D=no
# Sol'n:-
class Employee:
    def __init__(self,salary,rating):
        self.salary = salary
        self.rating = rating

    def calculate_increment(self):
        increment_percent = 0

        if self.salary <= 5:
            if self.rating == 'A':
                increment_percent = 16
            elif self.rating == 'B':
                increment_percent = 12
            elif self.rating == 'C':
                increment_percent = 10
            elif self.rating == 'D':
                increment_percent = 6

        elif self.salary <= 10:
            if self.rating == 'A':
                increment_percent = 14
            elif self.rating == 'B':
                increment_percent = 10
            elif self.rating == 'C':
                increment_percent = 8
            elif self.rating == 'D':
                increment_percent = 6
        elif self.salary <= 15:
            if self.rating == 'A':
                increment_percent = 8
            elif self.rating == 'B':
                increment_percent = 6
            elif self.rating == 'C':
                increment_percent = 4
            elif self.rating == 'D':
                increment_percent = 0
        
        elif self.salary <= 23:
            if self.rating == 'A':
                increment_percent = 7
            elif self.rating == 'B':
                increment_percent = 5
            elif self.rating == 'C':
                increment_percent = 4
            elif self.rating == 'D':
                increment_percent = 0

        return increment_percent
    
    def new_salary(self):
        increment = self.calculate_increment()
        return self.salary + (self.salary * increment/100)
        
salary = float(input("Enter employee salary in LPA: "))
rating = input("Enter employee rating (A/B/C/D): ")

emp = Employee(salary,rating)
print("Increment Percentage: ",emp.calculate_increment(),"%")
print("New Salary after Increment:",emp.new_salary(),"LPA")

               



