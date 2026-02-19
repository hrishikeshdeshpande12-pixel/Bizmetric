# 13.	Ask user to opt for courses for master degree based on the following  
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. For example- HR is having HR core and HR analytics and Marketing is having core and Marketing analytics. Analytics is the optional subject and having added extra fees. DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# # Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.  
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual)

# Sol'n:-
class MastersCourse:
    def __init__(self,subject,analytics,hostel,food_months,transport_type):
        self.subject = subject
        self.analytics = analytics.upper()
        self.hostel = hostel.upper()
        self.food_months = food_months
        self.transport_type = transport_type.lower()
        self.base_fee = 200000

    def course_fee(self):
        fee = self.base_fee

        if self.analytics == 'Y' and self.subject in ["HR","Finance","Marketing"]:
            fee += self.base_fee*0.10

        return fee
    
                
    def hostel_fee(self):
        if self.hostel == "Y":
            return 200000
        return 0
    
    def food_fee(self):
        return self.food_months *2000
    
    def transport_fee(self):
        if self.transport_type == "semester":
            return 13000*2
        elif self.transport_type == "annual":
            return 13000
        return 0
    
    def total_annual_cost(self):
        return(
            self.course_fee()
            + self.hostel_fee()
            + self.food_fee()
            + self.transport_fee()
        )

subject = input("Enter subject (HR/Finance/Marketing?DS): ")
analytics = input("Do you want analytics? (Y/N): ")
hostel = input("Do you want hostel ? (Y/N): ")
food_months = input(input("Enter number of months for food: "))
transport = input("Transportion type (semester/annual: )")

student = MastersCourse(subject,analytics,hostel,food_months,transport)

print("Course Fee: ",student.course_fee())
print("Hostel Fee: ",student.hostel_fee())
print("Food Fee: ",student.food_fee())
print("Transport Fee: ",student.transport_fee())
print("Total Annual Cost: ",student.total_annual_cost())




