# Q1.	If  name = ''' Hi How are you?
# Starterd learning python.
# It's really interesting.''' Then what is the output of following code
# •	name[:] 
# •	name[-10:-5]
# •	name[3:12]
# •	name[12:3]
# •	name[5,6]
# •	name[-4:-12]
# •	name[::2]
# •	name[::-2]
# Sol'n:-
name = ''' Hi How are you?
# Starterd learning python.
# It's really interesting.'''

print("name[:]:", name[:])
print("name[-10:-5]:", name[-10:-5])
print("name[3:12]:", name[3:12])
print("name[12:3]:", name[12:3])
print("name[-4:-12]:", name[-4:-12])
print("name[::2]:", name[::2])
print("name[::-2]:", name[::-2])


# Q2.	 L1 = [‘a’ , ‘b’, 20, 30, ‘t’, 100, 300, 400, ‘Happy’, ‘major’]
# a.	L1[:]
# b.	L1[::3]
# c.	L1[::-2]
# d.	How to extract  value “Happy” based on index and negative index
# e.	How to check type of data in list at 4th position
# f.	Extract values for 100, 300, 400 
# Sol'n:-
L1 = ['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
print("L1[:]:", L1[:])
print("L1[::3]:", L1[::3])
print("L1[::-2]:", L1[::-2])
print("L1[8]:", L1[8]) 
print("L1[-2]:", L1[-2]) 
print("Type at 4th position:", type(L1[3]))
print("L1[5:8]:", L1[5:8])



# Q3.	If l2 =[1,2,3,5,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”] then what is the output of following
# •	L2[4]
# •	L2[1:5]
# •	L2[7]
# •	L2[7][2]
# •	L7[7][2:]
# •	L2[ : 3]
# •	L2[3:]
# Sol'n:-
L2 = [1, 2, 3, 5, ['a', 'b', 'work hard'], 100, 200, "Success"]
print("L2[4]:", L2[4])
print("L2[1:5]:", L2[1:5])
print("L2[7]:", L2[7])
print("L2[7][2]:", L2[7][2])
print("L2[7][2:]:", L2[7][2:])
print("L2[:3]:", L2[:3])
print("L2[3:]:", L2[3:])


# Q4.	From the above l2 value ‘b’ must be changed to ‘BEE’.
# Sol:-
L2 = [1, 2, 3, 5, ['a', 'b', 'work hard'], 100, 200, "Success"]
L2[4][1] = 'BEE'
print(L2)
#Q 5.	From l2 “BEE” has to discard.
# Sol'n:-
L2[4].remove('BEE')
print(L2)

# Q6.	In l2 add a dictionary at the end {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}
# Sol'n:-
L2.append({'insect': ['bee', 'moth'], 'bird': ['parrot', 'sparrow']})
print(L2)

# Q7.	From l2 extract insect information.
# Sol'n:-
print(L2[-1]['insect'])

# Q8.Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2
# Sol'n:-
d1 =  {'a': 10, 'b': 20, 'c': 30}
L2.insert(1, d1)
print(L2)

#Q9.Based on new l2 created here extract the value 10 from l2 dictionary.
# Sol'n:-
print(L2[1]['a'])

#Q10.If l2 =[1,2,3,5, (90,40,50,10), ‘Python’, 400 ,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”, (200,300, “Hundreds”)] then what is the output of following
# •	L2[4][2]
# •	L2[5][:]
# •	L2[2] [:]
# •	L2[1:5]
# •	L2[5]
# •	L2[5][3:-1]
# •	L2[-1]
# •	L2[-4, -3]
# •	L2[-4: -10]
# •	L2[7][2]
# •	L7[-7][[2:]
# •	L2[ :- 3]
# •	L2[-3:]
# Sol"n:-
print(L2[4][2])
print(L2[5][:])
print(L2[1:5])
print(L2[5])
print(L2[5][3:-1])
print(L2[-1])
print(L2[-4:-10])
print(L2[7][2])
print(L2[:-3])
print(L2[-3:])


# Type Casting
# Q.17
a = 100

b = str(a)
print("str:", b, type(b))

# list conversion (will give error)
c = list(a)
print(type(c))
# tuple conversion (will give error)
d = tuple(a)
print(type(d))
# dict conversion (will give error)
e = dict(a)
print(type(e))
# set conversion (will give error)
f = set(a)
print(type(f))

g = float(a)
print("float:", g, type(g))


# Q18.	Create city = “Pune” 
# •	Convert to int     
# •	Convert float 
# •	Convert list  
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 
# •	Obsert errors and note it down for all conversions 

# sol'n
city = "Pune"

# int conversion (error)
a = int(city)

# float conversion (error)
b = float(city)

c = list(city)
print("list:", c, type(c))

d = tuple(city)
print("tuple:", d, type(d))

# dict conversion (error)
e = dict(city)

f = set(city)
print("set:", f, type(f))



#  Q19.	Create a list as marks = [20,18,15,17,18] 
# •	Convert to int 
# •	Convert float 
# •	Convert list 
# •	Convert tuple 
# •	Convert dict 
# •	Convert set 
# •	observe : errors and note it down for all conversions 

marks = [20, 18, 15, 17, 18]

# int conversion (error)
a = int(marks)

# float conversion (error)
b = float(marks)

c = list(marks)
print("list:", c, type(c))

d = tuple(marks)
print("tuple:", d, type(d))

# dict conversion (error)
e = dict(marks)

f = set(marks)
print("set:", f, type(f))



# List operations 
# Q20.	Create the empty list snames 
# •	 Add value 20 in the list using append 
# •	 Add value 30 in the list using extend 
# •	Add values in the list using append 
# •	Add value “WORK" in the list using extend 
# •	 Create a new list combo having the values [1, ‘a’, ‘b’ ,2 , 3] 
# •	Add sname to combo using addition operator 
# •	Add combo to snames using append 
# •	Add combo to snames using extend. 

# Sol'n:-
# Create empty list
snames = []
print("Initial snames:", snames)

# Add value 20 using append
snames.append(20)
print("After append 20:", snames)

# Add value 30 using extend
snames.extend([30])
print("After extend 30:", snames)

# Add values in the list using append
snames.append(40)
snames.append(50)
print("After append 40 and 50:", snames)

# Add value "WORK" using extend
snames.extend("WORK")
print("After extend 'WORK':", snames)

# Create new list combo
combo = [1, 'a', 'b', 2, 3]
print("Combo list:", combo)

# Add snames to combo using + operator
new_list = combo + snames
print("combo + snames:", new_list)

# Add combo to snames using append
snames.append(combo)
print("After append combo to snames:", snames)

# Add combo to snames using extend
snames.extend(combo)
print("After extend combo to snames:", snames)


# Q21.	Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1 
# Sol'n:-
l1 = [10, 20]
l3 = [1, 2, 3, 4, 5, 6, 7]
l3.insert(3, l1)   # index 3 means 4th position
print("Updated l3:", l3)

# 12.	Collection is the list having values [1,2,3,[‘a’, ‘b’, ‘c’], 100, ‘Nisha’, 20.50, 90.10 ] if the data is in integer or float then multiply with 5.  
# •	From the collection delete the record for “Nisha” 
# •	Find the location of 20.50 
# Sol'n:-
collection = [1, 2, 3, ['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10]

# Multiply integers and floats by 5
for i in range(len(collection)):
    if type(collection[i]) == int or type(collection[i]) == float:
        collection[i] = collection[i] * 5

print("After multiplication:", collection)

# Delete "Nisha"
collection.remove('Nisha')
print("After deleting Nisha:", collection)

# Find location of 20.50 (after multiplication it became 102.5)
# Sol'n:-
index_value = collection.index(102.5)
print("Location of 20.50 after multiplication:", index_value)


# Q22.	Create a comprehensive list for square upto 10 
# Sol'n:-
lis = [i**2 for i in range(10)]
print(lis)


# Q23.Create the comprehensive list to find number divisible by 13 till 200
# Sol'n:-
num = [i for i in range(1,201) if i % 13 == 0]
print(num)


# Q24.Create the list which is divisible by 4 from 300 to 400 
# Sol'n:-
Div_list = [x for x in range(300,401) if x % 4 == 0] 
print(Div_list)

# Q25.	Create a comprehensive list to generate list up to x, y as a number. For example if x = 3 list will be x_list = [0,1,2] and y=2 then y_list =[0,1]
# Then generate a new list based on all combination of x and y. For example: if x = 1 and y =2  then x_list = [0] and y_list = [0,1]
# And output will be [[0,0],[0,1]]
# If x=2 and y = 2 then output will be [[0,0],[0,1][1,0],[1,1]]
# Sol'n:-
x = int(input("Enter the number upto which you want your X_list to be: "))
y = int(input("Enter the number upto which you want your Y_list to be: "))
X_list = [i for i in range(x)]
Y_list = [j for j in range(y)]
result = [[i ,j] for i in  X_list for j in Y_list]
print(X_list)
print(Y_list)
print(result)

# Q26.How to create empty set? 
# Sol'n:-
# Method 1
s = set()
print("Empty set:", s, type(s))

# {} creates empty dictionary, not set
d = {}
print("Empty dictionary:", d, type(d))

# Q27.Create the set s1 and s2 and perform set operations like union, intersection, difference, set difference.
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print("s1:",s1)
print("s2:",s2)
#Union
print("Union:",s1.union(s2))
#Intersection
print("Intersection:",s1.intersection(s2))
# Diffrence (s1 - s2)
print("Diffrence s1 - s2 : ",s1.difference(s2))
# Diffrence (s2 - s1)
print("Diffrence s1 - s2 : ",s2.difference(s1))
# Symmetric diffrence
print("Symmetric Difference:", s1.symmetric_difference(s2))

# Q28.Create l2 as a list and perform set operation on s1 with l1 
l2 = [3,4,7,8]
print("List l2:",l2)

set_l2  = set(l2)
print("Union with l2:",s1.union(set_l2))
print("Intersection with l2:",s1.intersection(set_l2))
print("Diffrence s1-l2:",s1.difference(set_l2))
print("Symmetric Diffrence with l2",s1.symmetric_difference(set_l2))



#Q29.Create the format mentioned here.
# *
# * *
# * * *
# * * * *
# Sol'n:-

for i in range(5):
    print("* "*i)

# Q30.Create the format as mentioned below:
# ****
# ***
# **
# *
# Sol'n:-
n = 4
for i in range(5):
    print("*"*(n-i))

# Q31.Str_val = “ABCD” then create the format as mentioned below:
# A
# A B
# A B C
# A B C D

str_val = "ABCD"
for i in range(len(str_val)):
    print(str_val[:i+1])
    
# Q32.Create the format mentioned below:
# A
# BB
# CCC
# DDDD
Str_val = "ABCD"

for i in range(len(Str_val)):
   print(Str_val[i]*(i+1))
   
# 30.Create the format mentioned below:
# 1
# 22
# 333
# 4444
Str_val = "1234"

for i in range(len(Str_val)):
    print(Str_val[i]*(i+1))

# 31.Val = “ABCD”  based on the Val, create the format mentioned below
# D
# DC
# DCB
# DCBA
Val = "ABCD"
rev = Val[::-1]
for i in range(len(rev)+1):
    print(rev[:i])

#32.	Ask user to enter the string. If string is UPGRAD then output must be
# D
# DA
# DAR
# DARG
# DARGP
# DARGPU User may pass any string.

Str = str(input("Enter a string: "))
rev = Str[::-1]
for i in range(len(rev)+1):
    print(rev[:i])

# 33.	Create a list of odd numbers from 1 to 10
# 1.	Using for loop
# 2.	Using comprehensive list
#1.For loop:
lis = []
for i in range(11):
    if i % 2 != 0:
        lis.append(i)
print(lis)
#2. list comprehensive
lis = [i for i in range(11) if i % 2 != 0]
print(lis)

# 34.Create even number list using for loop from 200 to 250
  
lis = []
for i in range(200,251):
    if i % 2 == 0:
        lis.append(i)
print(lis)


# 35.	List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element by 2 and display the answer
para = "para"
List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
result =[]

for i in List2:
    try:
        result.append(i*2)
    except:
        result.append("cannot multiply")
print("Orginal list: ",List2)
print("After multiplying by 2: ",result)

# 36.	List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]

# Multiply each and every element from list2 by 2 and store the answer in list3
para = "para"
List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
List3 =[]

for i in List2:
    try:
        List3.append(i*2)
    except:
        List3.append("cannot multiply")
print("Orginal list: ",List2)
print("After multiplying by 2: ",List3)

# 37.	Create a function to accept marks from user utilize exception concept to validate proper marks.

def get_marks():
    try:
        marks = float(input("Enter marks (0 to 100): "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")
        print("Valid marks entered:",marks)
    except ValueError as e:
        print("Invalid input:",e)

get_marks()

# 38.	Create a function to validate user first name/last name. User first name/last name should contain only characters. No special characters, numbers, space in name 

def validate_name():
    try:
        first = input("Enter first name: ")
        last = input("Enter last name: ")

        if not first.isalpha():
            raise ValueError("First name must contain only letters"
                             )
        if not last.isalpha():
            raise ValueError("Last name must contain only letters")
        
        print("Valid Name: ",first,last)

    except ValueError as e:
        print("Invalid input: ",e)

validate_name()

# 39.	Create a function to accept mobile number. Mobile number should contain 10 digits. No Special character, alphabets and space. 

def validate_mobile():
    try:
        mobile = input("Enter mobile number: ")
        
        if not mobile.isdigtit():
            raise ValueError("Mobile number must contain only digits")
        if len(mobile) != 10:
            raise ValueError("Mobile number must be exactly 10 digits")
        print("Valid mobile number: ",mobile)

    except ValueError as e:
        print("Invalid input:",e)

validate_mobile()

# 40.Create a function to generate auto-password based on specific person details. Ask user to enter name, DOB. And password must be First name 4 characters and year of birth.

def generate_password():
    name = input("Enter first name: ")
    dob = input("Enter DOB (DD-MM-YYYY: ")

    part_name = name[:4]
    year = dob[-4:]

    password = part_name + year

    print("Genrated Password:",password)

generate_password()

# 41.Create a empty dictionary and ask user to enter values as name, DOB, mobile number add all the details in dictionary with customer number as 1 for first time. If user try to enter another value, then number should increase as 2 with new details and previous values should not change.
# For example:
# {}
# {1:{name : "Sachin", "DOB": "21-06-1965" , "mobile": "1234123423"}}

# {1:{name : "Sachine", "DOB": "21-06-1965" , "mobile": "1234123423"},
# 2: {name : "Sumedh", "DOB": "02-02-2002" , "mobile": "1234123433"}}

customer = {}
cust_no = 0

while True:
    name = input("Enter name: ")
    dob = input("Enter DOB (DD-MM-YYYY): ")
    mobile = input("Enter mobile number: ")

    customer[cust_no] = {"name":name,"DOB":dob,"mobile":mobile}

    print("Current customer data:")
    print(customer)

    cus_no += 1

    choice  = input("Do you want to add another customer?(yes/no): ")
    if choice.lower() != "yes":
        break

# 42.	Based on the above example create the dictionary and save the same in a cust_info.txt or cust_info.log

customer = {}
cust_no = 1

while True:
    name = input("Enter name: ")
    dob = input("Enter DOB (DD-MM-YYYY):")
    mobile = input("Enter mobile number: ")

    customer[cust_no] = {"name":name,"DOB":dob,"mobile":mobile}

    cust_no +=1

    choice = input("Add another customer? (yes/no): ")
    if choice.lower() != "yes":
        break

file = open("cust_info.txt","w")
file.write(str(customer))
file.close()

print("Customer data saved in cust_info.txt")

# 43.Based on the above example read the file cust_info.txt . check if dictionary any information is available in the file. If there is information then read the dictionary store into one variable and then append new information of customer if added.

import os

filename = "cust_info.txt"

if os.path.exists(filename):
    file = open(filename,"r")
    content = file.read()
    file.close()

    if content:
        customer = eval(content)
    else:
        customer = { }
else:
    customer = { }

if customer:
    cust_no = max(customer.keys())+1
else:
    cust_no = 1

name = input("Enter name: ")
dob = input("Enter DOB (DD-MM-YYYY): ")
mobile = input("Enter mobile number: ")

customer[cust_no] = {
    "name": name,
    "DOB":dob,
    "mobile": mobile
}

file = open(filename,"w")
file.write(str(customer))
file.close()

print("Customer added successfully")
print("Update customer data:",customer)

# 44.	Create a table  cust_info as sr_no, name, DOB, mobile. Ask user to enter the information from python code. Validate all fields and after validation insert records in the table.

import pyodbc

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=LAPTOP-F993VFLL\\SQLEXPRESS;'
    'Database=PYTHON_PRACTICE;'
    'Trusted_Connection=yes;'
)
cur = conn.cursor()

name = input("Enter name: ")
dob = input("Enter DOB (DD-MM-YYYY): ")
mobile = input("Enter mobile number: ")

if not name.isalpha():
    print("Invalid name")
elif not mobile.isdigit() or len(mobile) !=10:
    print("Invalid mobile number")
else:
    cur.execute("INSERT INTO cust_info(name,DOB,mobile) VALUES (? ? ?),(name,dob,mobile)")
    conn.commit()
    print("Record inserted successfully")
conn.close()

# 45.	Dict1= {“Key”: {“subkey”:20} ,  “k2”:{“sub2” : 5}, “k3” : {“sub4” :16},  “k4” : {“sub4” : 6}}
# Sort elements based on values
# Output must be {,  “k2”:{“sub2” : 5}, “k4” : {“sub4” : 6},  “k3” : {“sub4” : 16}, “Key”:{“subkey”:20}}

# 46.	Create a function to calculate age till now.
from datetime import datetime
def calculate_age(dob):
    birth_year = int(dob[-4:])
    current_year = datetime.now().year
    return current_year - birth_year
print(calculate_age("02-02-2000"))
# 47.	Create a function to check age eligibility for given customer based on DOB. Function will take two input DOB and ELIGIBILITY age.
from datetime import datetime

def check_eligibility(dob, eligibility_age):
    # dob format: "YYYY-MM-DD"
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    
    age = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )
    
    if age >= eligibility_age:
        return f"Eligible (Age: {age})"
    else:
        return f"Not Eligible (Age: {age})"

# Example
print(check_eligibility("2000-05-15", 18))

# 48.	Create a function to check if string is palindrome or not ? For example, if input is NITIN then reverse of the string is same then it is palindrome. If input is ANIL then reverse is LINA which is not same then it is not palindrome.  
def is_palindrome(string):
    string = string.upper()
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

# Example
print(is_palindrome("NITIN"))
print(is_palindrome("ANIL"))

# 49.	Create a function to generate a Fibonacci Series. 0 1 1 2 3 5 8 13 21 34 …..  upto 100 
def fibonacci_upto_100():
    a, b = 0, 1
    while a <= 100:
        print(a, end=" ")
        a, b = b, a + b

# Example
fibonacci_upto_100()

# 50.	Write a code to generate factorial of the number  For example: factorial of 5 = 5! = 5*4*3*2*1
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
print("Factorial of 5:", factorial(5))

# 51.	Write a program to find largest number in the list.
def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Example
numbers = [10, 45, 23, 67, 89, 34]
print("Largest number:", find_largest(numbers))

# 52.	Write a program to check frequency of each element in the list.
def frequency_of_elements(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Example
numbers = [1, 2, 2, 3, 3, 3, 4]
print("Frequency:", frequency_of_elements(numbers))

# 53.	There are two string l1 =[ 1,2,3,4,5] and l2 =[3,2,8,7,9] then write a program to find common elements in the list.
def common_elements(l1, l2):
    return list(set(l1) & set(l2))

# Example
l1 = [1, 2, 3, 4, 5]
l2 = [3, 2, 8, 7, 9]
print("Common elements:", common_elements(l1, l2))


