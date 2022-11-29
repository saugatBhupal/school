"""
a = 'python'
[print(f"{i} = ",a[i]) for i in range(0,len(a))]

#multiplication table of a given number

num = int(input("number"))
[print(f"{num} x {i} = ", num * i)for i in range(11)]
#reverse
[print(f"{num} x {i} = ", num * i)for i in range(10, -1, -1)]
"""

"""
-- 49 49 --1
[print(i, " -- ", (50 -i)) for i in range(1, 51)]
"""
"""
#add input
i = int(input("number"))
i = str(i)
sum_ = 0
for r in i:
    sum_ += int(r)
print(sum_)
"""
"""
i = int(input("number"))
i = str(i)
mul = 1
for r in i:
    mul *= int(r)
print(mul)
"""
"""
#check prime
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
#reverse string
word = input("word")
a = [print (word[a]) for a in range(len(word)-1, -1, -1) ]
"""
"""
num = int(input("number"))
fact = 1
for i in range(1, num+1):
    fact *= i
print(fact)
"""
"""
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
#palindorome
word = input("word")
reverse = ''
for i in range(len(word)-1,-1,-1) :
    reverse += word[i]
if(word == reverse):
    print(True)
else:
    print(False)
"""
#check password 3 times
password = "abcd"
log = False
for i in range(0,3):
    pwd = input("enter password")
    if(pwd == password):
        log = True
        break
    
if(log == False):
    print("No attemots left")
else:
    print("Logged in")