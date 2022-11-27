"""
#1. Write a program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
price = int(input("Enter price"))
if(price > 10000):
    tax = 0.15
elif(price>50000 and price <= 100000 ):
    tax = 0.1
elif(price<=50000):
    tax = 0.05
print("tax is", tax*price)
"""

"""
#2. Accept the age of 4 people and display the youngest one.
age = [int(input("Age")) for i in range(1,5)]
age.sort()
print(0)

#3. Accept the age of 4 people and display the oldest one.
age = [int(input("Age")) for i in range(1,5)]
age.sort()
print(-1)
"""
"""
#4. Accept the percentage from the user and display the grade according to the following criteria:
marks = int(input("marks"))
if(marks<25):
    grade = 'D'
elif(marks>25 and marks<45):
    grade = 'C'
elif(marks>45 and marks<50):
    grade = 'B'
elif(marks>50 and marks<60):
    grade = 'B+'
elif(marks>60 and marks<80):
    grade = 'A'
elif(marks>80):
    grade = 'A+'
print(grade)
"""

"""
#5. A company decided to give bonus to employee according to following criteria:
time = int(input('Enter time'))
if(time > 10):
    bonus = 10
elif(time >=6 and time <= 10):
    bonus = 8
elif(time < 6):
    bonus = 5
print(bonus)
"""

"""
#6. Accept three numbers from the user and display the second largest number.
age = [int(input("Age")) for i in range(1,5)]
age.sort()
print(1)
"""

"""
#7. Accept the number of days from the user and calculate the charge for library according to following:
days = int(input("enter days"))
if(days<= 5):
    charge = 2
elif(days >= 6 and days < 10):
    charge = 3
elif(days >= 11 and days < 15):
    charge = 4
else:
    charge = 5
print(charge * days)
"""

"""
#8 A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. Ask user for their salary and year of service and print the net bonus amount.
time = int(input("time"))
salary = int(input("salary"))
if(time>5):
    print("bonus", (0.05* salary) + salary)
"""
"""
#9. Write a program to check two strings are anagram or not.
a,b = input("Enter first string"), input("Enter second string")
c = ''
for x in range(len(a)-1, -1,-1):
    c +=a[x]
if(a == b):
    print("anagram")
else:
    print("not anagram")
"""
"""
#A school has following rules for grading system:
marks = int(input("marks"))
if(marks<25):
    grade = 'F'
elif(marks>25 and marks<45):
    grade = 'E'
elif(marks>45 and marks<50):
    grade = 'D'
elif(marks>50 and marks<60):
    grade = 'C'
elif(marks>60 and marks<80):
    grade = 'B'
elif(marks>80):
    grade = 'A'
print(grade)
"""