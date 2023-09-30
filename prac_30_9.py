# list1 = [10,90,88,33,44,55,10,88]
# new = []


# # Method - 1
# for element in list1:
#     if element not in new:
#         new.append(element)

# print(new)  # [10, 90, 88, 33, 44, 55]


# # Method - 2

# print(list(set(list1)))

# # Method - 3

# new1 = []

# for k in set(list1):
#     if list1.count(k) == 1:
#         new1.append(k)

# print(new1)   # [33, 44, 55, 90]

# # Method - 4

# # new2 = []
# list1.remove(10)
# print(list1)


# for j in list1:
#     if j == 10:
#         list1.remove(j)


# print(list1)    # [90, 88, 33, 44, 55, 88]
print('-----------------')
list1 = [10,20,30,10,10,10,20,10,10,10]
c = 0
copy = list1.copy()   # Shallow Copy

for j in set(list1):
    x = list1.count(j)
    print(x)
    if x != 1:
        for m in range(x-1):
            print(copy)
            copy.remove(j)
print(copy)  # [30, 20, 10]


# print(list1)    # [20, 30, 20, 10]


list1 = [[10,20,30], 
         [90,34,22],
         [22,90,11]]    

# Que - 1   10 + 34 + 11 = ?  ,  30 + 34 + 22 = ?

# Que - 2   
# 10  20  30
# 22  34  90
# 22  90  11  

# Que - 3
# 10 20 30 22 11 90 22 90 34