'''
import keyword
print(len(keyword.kwlist))


False123=10
print(False123)


a=50
b=50
print(id(a))
print(id(b))


name = "A"
Name = "B"
naMe = "C"
NAME = "D"
n_a_m_e = "E"
_name = "F"
name_ = "G"
_name_="H"
na56me = "I"
print(name,Name,naMe,NAME,n_a_m_e,_name, name_,_name_, na56me)


p=q=r=60
print(p)
print(q)
print(r)

a=10
b=20
c=30
d=a+b
print(id(d))
print(id(c))

a='pc'
b='da'
c='pcda'
print (id(c))
print (id(a+b))


'''


'''
print("hello\nPython")
print('what\'s up')

print("hello Python")
print("\tworld")
print("\tworld".expandtabs(16)) # expandtabs(n)

print("hello\bworld")

print(r"hello\nPython")

print("hello\\\\world") # no of \ = \ divide by 2 so 4 \ then 2 \ in output
'''



'''
a="hello  "
ans1=a.replace("l","f")
print (ans1)
ans2=a.replace("l","f",1)
print (ans2)
print (len(ans2))


a="   hello  "
ans1=a.rstrip()
print (ans1)
ans2=a.strip()
print (ans2)


#regex substitution
import re
a="   hello  "
ans1=re.sub(" ","l",a)
print (ans1)
print (len(ans1))


a="hello"
b='p'+ a
print (b)


#slicing
a="hello"
print(a[0:3])
print(a[:3])
print((a[0:3])+'p'+(a[1:]))


# capital and lower letter
a="hello world"
b=a.upper()
c=a.lower()
d=a.swapcase()
e=a.title()
f=a.capitalize()
print (b,c,d,e,f)


#isalnum isalpha isdigit

a="hello123"
b=a.isalnum()
print (b)
c=a.isalpha()
print (c)
d=a.isdigit()
print (d)


# isidentifier isprintable isspace
a="for"
b=a.isidentifier()
c=a.isprintable()
d=a.isspace()
print (b,c,d)


# isupper islower istitle iscapitalize
a="hello"
b= a.isupper()
c=a.islower()
d=a.istitle()
print(b,c,d,)

##fill zero in gap

a="hello"
print(len(a))
b=a.zfill(8)
print (b)

# count character
a="hello0o"
b=a.count('o')
print (b)

a = ""
print(dir(a))

fruits = ['apple','banana','orange','avocado']
[ print (fruit, end=', ') for fruit in fruits]


print("Hello {}, your balance is {}.". format ("Adam", 230))
# positional arguments
print ("Hello {0}, your balance is {1}.". format ("Adam", 230))
# keyword arguments
print("Hello {name}, your balance is {b1c}.". format (name= "Adam", b1c=230))
# mixed arguments
print("Hello {0}, your balance is {blc}". format ("adam",blc =230))
name = "Adam"
blc = 230
print(f"Hello {name}, your balance is {blc}")

a = 0.1+0.1+0.1
print(f"{0.1:.60f}")
print(f"{0.3:.60f}")
print(f"{a:.60f}")
'''

