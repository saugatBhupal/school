"""
#1 print softwarica 10 times
[print("softwarica") for i in range(10)]
"""
"""
#2 sum of list
i =[1,2,3,4]
sum_ = 0
for x in i :
    sum_ += i
print(sum_)
"""
"""
#3 print each caharacter using indexing
arr = [1,2,3,4]
[print(f"{i} is {arr[i]}" ) for i in range(len(arr))]
"""
"""
#4 each element of a list
arr = [1,2,3,4]
[print(i) for i in arr]
"""
"""
#5 multiplication of weach element
arr = [1,2,3,4]
mul = 1
for i in arr:
    mul *= arr
print(arr)
"""
"""
#6 multiplication table of a given number
num = int(input("number"))
[print(f"{num} x {i} = ", num * i)for i in range(11)]
"""
"""
#7 reverse a list
arr = [1,2,3,4,5]
arr2 = []
for i in range(len(arr)-1,-1,-1):
    arr2.append(arr[i])
print(arr2)
"""
"""
#8
total number of digits in a number
num = int(input("Enter a number"))
num = str(num)
dig = 0
for i in num:
    dig +=1
print(dig)
"""
"""
#9prime number
num = int(input("number"))
count = 0
for i in range(1,num+1):
    if(num % i == 0 ):
        count +=1
if(count == 2 ):
    print("true")
else:
    print("false")
"""
"""
#10 even odd count
arr = [1,2,3,4,5]
even = 0
odd = 0
for i in arr:
    if(arr%2 == 0):
        even += 1
    else:
        odd += 1
print(even, odd)
"""
"""
#11 accepts string calcucate digits and num
word = input("word")
num = 0
alpha = 0
for i in word:
    if (i.isnumeric()):
        num += 1
    elif(i.isalpha()):
        alpha += 1
    else:
        pass
print(f"dig : {num}, alpha: {alpha}")     
"""
"""
#12 check password and username
user = "admin"
password = "admin123"
username, pwd = input("username"), input("password")
if(user == username and password == pwd ):
    print("logged in")
else:
    print("wrong info")
"""

"""
#13 odd or even
num = int(input("number"))
if(num% 2 == 0 ):
    print("even")
else:
    print("odd")
"""

"""
#14 Factorial
num = int(input("number"))
fact = 1
for i in range(1, num+1):
    fact *= i
print(fact)
"""

"""
#15 number paliondrome
num = input("Enter a number")
rev = ""
for i in range(len(num)-1, -1,-1):
    rev += i
if(int(num) == int(rev)):
    print(True)
else:
    print(False)
"""
"""
#16 check armstrong
num = input("number")
exp = len(num)
sum_ = 0
for i in num:
    sum_ += int(i)**exp
if(sum_ == int(num)):
    print(True)
else:
    print(False)
"""

"""
#17 perfect square
sq = int (input("Enter square"))
base = int(input("Enter base"))

sq_ = base ** 2

if(sq_ == sq):
    print(True)
else:
    print(False)
"""
"""
#18 perfect number 
num = int(input("number"))
count = 0
for i in range(1,num):
    if(num%i == 0):
        count += i
if(count == num):
    print(True)
else:
    print(False)
"""
"""
#19 multiplication table of 1,2,3,4,5,6,7,8
for i in range (1, 10):
    [print(f"{i} x {x} = ", i*x) for x in range(1,11)]
"""
"""
#20 10 natural numbers
[print(i) for i in range(1, 11)]
"""

""""
#21 sum of all numbers in a range
ran = int(input("enter range"))
sum_ = 0
for i in range(1, ran):
    if(i % 2 != 0):
        sum_ += i
print(sum_)
"""
"""
#22  sum of even in range
ran = int(input("enter range"))
sum_ = 0
for i in range(1, ran):
    if(i % 2 == 0):
        sum_ += i
print(sum_)
"""

"""
#23 count spaces
inp = input("Input spaces")
count = 0
for i in inp:
    if(i == " "):
        count += 1
print(count)
"""
"""
#24 calculate digits numbers and space
word = input("word")
num = 0
alpha = 0
space = 0
for i in word:
    if (i.isnumeric()):
        num += 1
    elif(i.isalpha()):
        alpha += 1
    elif(i == " "):
        space +=1
        
print(f"dig : {num}, alpha: {alpha}, space: {space}")   
"""