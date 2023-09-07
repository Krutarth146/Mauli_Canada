# Python is Dynamic Lang. High Level Lang, Interpreted Lang.

# High Level----> Human Readable
# Interpreted ----> Line by Line Interpretation
# Dynamic ---> Run time Memory Allocation

x = 90
print(type(x))   # <class 'int'>

x = 'M'
print(type(x))   # <class 'str'>

x = True
print(type(x))   # <class 'bool'>

# main()
# {
#     int x, y, z;
# }

# print("Mauli Shah")
# print("Mauli Shah")
# printaa("Mauli Shah")
# print("Mauli Shah")
# print("Mauli Shah")
# input()

# Single Line Comment
# ctrl + /

'''
Multi
Line
Comment
'''


# from matplotlib import pyplot
# import matplotlib.pyplot as plt


print('Mauli Shah',end=' ----> ')   # default end='\n'
print('Good Morning',end='')    # Mauli Shah ----> Good Morning


print("Aman")   # Mauli Shah ----> Good MorningAman

x = 90
y,z = 89,78


print(x,y,z,sep='\t',end='\n')   # 90 89 78   default --> sep=' '

print('''Aman
                        is 
      Good
      Boy''')


print("Mauli has 500 Rs. only.")

name = "Mauli"
rupees = 900

# print("%s has %d Rupees only.",name, rupees)

print(name,"has",rupees,"Rupees only.")
print(f"{name} has {rupees} Rupees only.")   # fstring 

x = 25
y = 2

print(f'{x} + {y} = {x+y}')   # 900 + 788 = 1688
print(f'{x} - {y} = {x-y}')   # 900 + 788 = 1688
print(f'{x} * {y} = {x*y}')   # 900 + 788 = 1688
print(f'{x} / {y} = {x/y}')   # 900 + 788 = 1688
print(f'{x} // {y} = {x//y}')   # 900 + 788 = 1688
print(f'{x} % {y} = {x%y}')   # 900 + 788 = 1688
print(f'{x} ** {y} = {x**y}')   # 900 + 788 = 1688