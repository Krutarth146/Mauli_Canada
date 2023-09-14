# # # Match case

# # # switch(choice)
# # # {
# # #     case 1: print('You have Selected Case 1')
# # #             break
# # # }
# # choice = input()

# # match choice:
# #     case 'M' : print('Monday')

# #     case 'True': print("True Statement Selected")

# #     case 56: print("True Statement Selected")

# #     case other : print("Invalid")



# # Loops   
# # 1. Entry Control Loops   ----> 1. while    2. For


# # 1. Start    2. End (Condition)   3. Flow (Incre. / Decre.)


# k = 25    # Start Position
# count = 0

# while k <= 35:
#     print('Mauli Shah',k)
#     count+=1
#     k+=1

# print('count',count)   # count 11

# # Mauli Shah
# # Mauli Shah
# # Mauli Shah
# # Mauli Shah
# # Mauli Shah


# # ---------------------------------------

# j = 90
# while j>=1:
#     if j % 5 == 0 or j % 7 == 0 and j % 10 == 0:
#         print(j,end=' ')
#     j-=1

# # num

# num = 90

# print()
# print()
# num = str(num)   # '90'
# if num[-1] in ['0','2','4','6','8']:
#     print('Even')   # Even

# # print(num / 2)   # 45.0


# # ------------------------------------------

# num = 9342


# # while num != 0:
# # while num > 0:
# #     rem = num % 10     # rem = 9
# #     print(rem,end='')  # 439
# #     num = num // 10    # 0

# c = 0
# num = 93425
# while num != 0:
#     num = num // 10
#     c+=1

# print(c)   # 4


num = 9342   # 18

total = 0

while num != 0:
    rem = num % 10   # rem = 9
    if rem % 2 != 0:
        total = total + rem   # 18 = 9 + 9
    num = num // 10   # 0
    

print(total)   # 12


# ------------------------------
num = 101

rev = 0
xerox = num

while num != 0:
    rem = num % 10   # rem = 3
    rev = rev * 10 + rem   # 243
    num = num // 10   # 0
    

print(rev)   # 101


if xerox == rev:    # 101 == 101
    print('Palindrome Number')


# 1 to 9, 11,22,33,44,55    # 1 to 10000


# Armstrong Number   
# 153 ---> (3*3*3  +  5*5*5  +  1*1*1)   = 153
# 8208 ---> (8*8*8*8 +  2*2*2*2  +  0  +  8*8*8*8)   = 8208


num = 8208

rev = 0
xerox = num

while num != 0:
    rem = num % 10   # rem = 3
    rev = rev + (rem ** 4)   # 243
    num = num // 10   # 0
    

print(rev)   # 101


if xerox == rev:    # 101 == 101
    print('Armstrong Number')

# 1 to 10000 ----> Palindrome, Armstrong...