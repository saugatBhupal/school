"""
#1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

a,b = int(input("a")),int(input("b"))
if(a ==b):
    print(1)
elif(a > b):
    print(2)
else:
    print(3)
"""
   
"""
#2.  Print "Hello" if a is equal to b, or if c is equal to d.

a,b,c,d = int(input("a")),int(input("b")),int(input("c")),int(input("d"))
if(a == b or c == d):
    print("Hello")
"""

"""
#3. Print "Hello" if a is equal to b, and c is equal to d.

a,b,c,d = int(input("a")),int(input("b")),int(input("c")),int(input("d"))
if(a == b & c == d):
    print("Hello")
"""

"""
#4. For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0. 

x = int(input("Number"))
if(x > 0 ):
    print("True")
elif(x < 0):
    print("False")
else:
    print("Zero")
"""

"""
# 5. Check whether the user input number is even or odd and display it to user.

x = int(input("Number"))
if(x%2 == 0):
    print("Even")
else:
    print("Odd")
"""

"""
#6. WAP which accepts marks of four subjects and display total marks, percentage and 
#grade.
#Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, 
#less than 40% –> fail

m1,m2,m3,m4 = int(input("Marks 1")),int(input("Marks 2")),int(input("Marks 3")),int(input("Marks 4"))
total = m1 + m2 + m3 + m4
per = total/4
grade = ''
if(per > 70):
    grade = 'Distinction'
elif(per>60 & per< 70):
    grade = 'First'
elif(per > 40 & per < 60):
    grade = 'Pass'
else:
    grade = 'fail'
print(total, per, grade)
"""

"""

#7. What is the output of ‘APPLE’ > ‘apple’?
print('APPLE' > 'apple')
"""

"""

#8. Write a Python program to display your details like name, age, address in three different lines.
print("Name", "Age", "Address", sep='\n')

"""
"""
#9. Write a python program which accepts the radius of circle from user and compute the area.

radius = int(input("Radius"))
area = 3.14*(radius**2)
print(area)
"""

"""

# 10 A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. The program should read three integers: the number of students in each of the three 
#classes, a, b and c respectively. Hint. In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.

a,b,c = int(input("A")),int(input("B")),int(input("C"))
desks = a + b + c
if(desks%2 != 0 ):
    desks = (desks // 2) + 1
else:
    desks = desks/2
print(desks)
"""

""""
# 11 Write a python program which calculates tax of an employee with given condition:
salary = int(input("Salary"))
if(salary<20000):
    tax = 0.15
elif(salary>20000 and salary<50000):
    tax = 0.25
elif(salary>50000 and salary<100000):
    tax = 0.30
elif(salary>100000):
    tax = 0.35
print(tax*salary)
"""

"""
#12.  Given three integers, print the smallest one. (Three integers should be user input)
a,b,c = int(input("a")),int(input("b")),int(input("c"))
if(a < b and a < c):
    print(a)
elif(b < a and b < c):
    print(b)
elif(c < a and c < b):
    print(c)
else:
    print("equal")
"""

"""
#13. N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.
N,K = int(input("students")),int(input("apples"))
print("Each student gets: ",K//N)
print("Remaining: ", K%N)
"""

"""
#14. Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]
natNum = [1,2,3,4,5]
if(5 in natNum):
    print(True)
else:
    print(False)
"""

"""
#15. Write a program that asks the user for a number in the range of 1 to 12. The program should display the corresponding month, where 
#1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 8=august,9=september,10=october,11=november,12=december. The program should display an error message if the user enters a numberthat is outside the range of 1 to 12.
month = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
ind = int(input('enter number'))
if(ind > 1 or ind < 12):
    print(month[1])
else:
    print("Invalid number")
"""

"""
#16. Given x = 5, what will be the value of x after we run x+=3?
x = 8
"""

"""
#17.A school has following rules for grading system:
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

"""
#18. Take input of age of 3 people by user and determine oldest and youngest among them
age = [int(input("age"))for i in range(0,3)]
age.sort()
print("greatest:", age[-1], "smallest:", age[0])
"""

"""
#19. Write a program to check whether a person is eligible for voting or not. (accept age from user)
age = int(input('Age'))
if(age >= 18):
    print(True)
else:
    print(False)
"""

"""
#20. Write a program to check whether a number is divisible by 7 or not.
num = int(input("Enter a number"))
if(num%7 == 0):
    print(True)
else:
    print(False)
"""

"""
#21. Accept any city from the user and display monument of that city.
data = {'delhi': 'Red Fort', 'agra':'Taj Mahal', 'jaipur':'Jal Mahal'}
city = input("Enter a city")
print(data[city.lower()])
"""

"""
#22. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
num = int(input('Enter a number'))
if(num%2 == 0 and num%3 == 0):
    print(True)
else:
    print(False)
"""

"""
#23. Write a program to accept two numbers and mathematical operators and perform operation accordingly.
num1 = input('Enter first number')
num2 = input('Enter seconf number')
operator = input('Enter operator')
ans = num1 + operator + num2
print(eval(ans))
"""

"""
#24. Write the syntax of simple if statement.
if():
    pass
else:
    pass
"""

"""
#25. Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
num = int(input("Enter a number"))
if(num%5 == 0):
    print("Hello")
else:
    print("Bye")
"""

"""
#26. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for sunday, 2 for monday and so on.
data = {1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday', 7:'Saturday'}
num = int(input("Enter a number"))
print(data[num])
"""

"""
#27. Write the logical expression for the following:
#A>B and C>D
"""

"""
#28. Write a program to check whether a number entered is three digit number or not.
num = int(input("Number"))
if(num//100 > 0):
    print(True)
else:
    print(False)
"""

"""
#29. Write a program to check whether a person is senior citizen or not.
age = int(input('Enter Age'))
if(age > 65):
    print(True)
else:
    print(False)
"""

"""
#30. Write a program to find the lowest number out of two numbers expected from user.
num1,num2 = int(input('num1')), int(input('num2'))
if(num1<num2):
    print(num1)
else:
    print(num2)
"""

"""
#31. Out of "elif" and "else if",  which is the correct statement in python? -> elif
"""

"""
#32. Accept the following from the user and calculate the percentage of class attended:
working = int(input('Enter working days'))
absent = int(input('Enter absent days'))
per = absent/working *100
if(per < 75):
    print("Not allowed to sit in exams")
else:
    print("Allowed to sit in exams")
"""

"""
#33. Write a program to accept percentage and display the category according to the following criteria:
per = int(input("percentage"))
if(per<40):
    grade = 'Failed'
elif(per>=40 and per<55):
    grade = 'Fair'
elif(per>=55 and per<65):
    grade = 'Good'
elif(per>65):
    grade = 'Excellent'
print(per)
"""

"""
#34. Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
age,sex,days = int(input("age")),input("sex"),input("days")
if((age >=18 and age < 30) and (sex == 'M')):
    wage = 700
elif((age >=18 and age < 30) and (sex == 'F')):
    wage = 750
elif((age >=30 and age < 40) and (sex == 'M')):
    wage = 800
elif((age >=30 and age < 40) and (sex == 'F')):
    wage = 850
print(days * wage)
"""

"""
#35. Accept three numbers from the user and display the second largest number.
nums = [int(input(f"num {i}: ")) for i in range(1,4)]
nums.sort()
print(nums[1])
"""

"""
#36. Accept the number of days from the user and calculaye the charge for library according to following:

days = int(input("days"))
if(days<6):
    charge = 2
elif(days>=6 and days<11):
    charge = 3
elif(days>=11 and days<15):
    charge = 4
elif(days>15):
    charge = 5
print(days*charge)
"""

"""
#37. Evaluate the following statements:
a=True
b=True
c=True
d=True

print(c)
print(d)
print(not a)
print(not b)
print(not c)
print(not d)
print(a and b)
print(a or b)
print(a and b or c)
print(not a or b or c)
print(not a or not b or not c)
print(not(not a or not b or not c))
"""