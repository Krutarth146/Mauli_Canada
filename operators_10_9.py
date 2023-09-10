# Comparison O/p  / Relational O/p     < > <= >= == !=

x = 90
y = 980

if x > y:
    print("980 is Max")
else:
    print("90 is Min")   # 90 is Min

if -78:
    print("Manoj")   # Manoj

# Truthy Values: 90, -45, [10,20,30], "Mauli", True
# Falsy Values: False, 0, [], ""

if '':
    print("Ashok")

if 78 >= 78:
    print(True)   # True
else:
    print("True")


x = 90
if x == 90:
    print(True)


x = 90   

list1 = [10,90,78,34]
list2 = [10,90,34,78]


print(id(list1))   # 8144
print(id(list2))   # 2576
list1.sort(reverse=True)

print(list1)   # [90, 78, 34, 10]

if list1.sort(reverse=True) == list2.sort(reverse=True):
    print('Both lists are Same')
else:
    print("Differ")

# -------------------------------------------------
# Identity Operator    is / is not

if list1 is list2:
    print("Both Lists are Very Same")

list1 = list2
print(id(list1))
print(id(list2))

if list1 is list2:
    print("Both List's reference are Same")

x = 90
y = 90

y += 10

if x is y:
    print("x is y")   # x is y



# ----------------------------------------------
# Logical Operator  and or not

num = 78563211

if num % 2 == 0 or num % 3 == 0:
    print("Div. By 2 or 3")


num1 = 70

if num1 % 3 == 0 or num1 % 5 == 0 and num1 % 10 == 0:
    print(True)

if not 45:
    print("False")


num1 = 901
num2 = 67
num3 = 9011

if num1 > num2:
    print('Num1 is Max')
else:
    print('Num2 is Max')

print(num1 if num1 > num2 else num2)


if num1 > num2:
    if num1 > num3:
        print('Num1 is Max')
    else:
        print("Num3 is Max")
else:
    if num2 > num3:
        print('Num2 is Max')
    else:
        print('num3 is Max')


print(num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2 > num3 else num3)


list1 = [10 ,90, 78, 67, 34, 23]

num = 90
count = 0


for i in list1:
    count += 1
    if i == num:
        print("Element is Found")
        break
else:
    print("Not Found")
    

print(count)


# --------------------------

if num in list1:    # Membership O/p  ---> in / not in
    print("Elment is Found")
else:
    print(False)