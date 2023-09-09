# x = 90   # int

# y = int(input("Enter any Number: "))   # str
# z = input("Enter any Number: ")   # str


# print(y+int(z))  # str + str  --> 311 (Addition)

# # Datatypes


x = 90 
print(type(x))  # int


y = 90.56  # Float

z = 'q' # str

d = 'Mauli'  # str

s = 90 + 3j
print(type(s))   # <class 'complex'>  ---> 90 is Real Part, 3j Imaginary Part


print(s + 80)   # (170+3j)   # int + complex ----> complex [Implicit T.C]

x = '90'
y = 67

try:
    print(x+y)   # Error str + int
except SyntaxError:
    print("Syntax Error")
except Exception as e:
    print("str + int Not Possible",e)   # str + int Not Possible can only concatenate str (not "int") to str
  
print('Statement')


x = '90'
print(10 + int(x))   # 100  # [Explicit T.C]

f = 90.90
print(2+f)   # Implicit


x = True   # 1
print(x + 23)  # 24

g = 'None'
g = None
print(type(g))   # <class 'NoneType'>


# int a[10]
list1 = [10,20,30,40, 90.90, "Try", True, [10,20,(10,20,30)], 90+2j]
print(list1)
print(type(list1))  # <class 'list'>

tup1 = ()    # Tuple
tup1 = (10)  # int
tup1 = (10,) # Tuple
print(type(tup1))


dict1 = {}    # dict
dict1 = {10,20,30,40}   # set
print(type(dict1))   # <class 'dict'>


dict2 = {'Name' : "Mauli", 'Roll' : 900, 'list1' : [10,20]}   # dict

x = '23.90'
# print(int(x))   # Error
print(int(float(x)))  # 23
print(round(23.90))   # 24


import math

print(math.floor(45.9999))    # 45
print(math.ceil(45.000001))   # 46
print(math.ceil(45.000000))   # 45

print(45 / 2) # 22.5
print(45 // 2) # 22
print(-45 / 2) # -22.5
print(-45 // 2) # -23

print(25 ** 2)  # 625
print(2 ** 2 ** 3)  # 256



# Operator

# 1. Arithmetic + - * / // % **

# 2. AssignMent O/p  = += -= *= /= //= %= <<= >>= &= |= ^=

x = 10
x += 20   # x = x + 20


print(x)   # 30

x = 40

x+=300    # 340
x %= 3    # 1
x += 900  # 901
x /= 3    # 290.3333333333333
x -= 20   # 280.3333333333333

print(x+10)  # 290.3333333333333
print(x)    # 280.0


# Days

# Year, Months, Rem Days  @ 2414