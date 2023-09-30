# str1 = "MISSISSIPPI"

# ans = {'M' : 1, 'I' : 4, 'S' : 4, 'P' : 2}


# # Set---> Unordered, Unique Values

# dict1 = {}
# # for i in set(str1):
# #     dict1[i] = str1.count(i)

# # print(dict1)   # {'I': 4, 'S': 4, 'M': 1, 'P': 2}


# for i in str1:
#     if i not in dict1:
#         # dict1[i] = 1
#         x = i
#         dict1.update({ x : 1})
#     else:
#         dict1[i] += 1

# print(dict1)   # {'M': 1, 'I': 4, 'S': 4, 'P': 2}


# list1 = [10,20,30,40,50,60,70,80]
# # ans = [(10,10), (10,20) .... ]
# # list2 = []

# # for k in list1:   # k = 10
# #     for m in list1:   # m = 10
# #         list2.append((k,m))   # (10,10)

# # print(list2)

# main = []
# new = []

# # for k in range(8):
# for k in range(len(list1)):   # k = 0
#     for s in range(k+1, len(list1)+1):   # s = 8
#         main.append((list1[k:s]))  # list1[0:8]
# print(main)   # [[10], [10, 20], [10, 20, 30], [10, 20, 30, 40], [10, 20, 30, 40, 50], [10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60, 70], [10, 20, 30, 40, 50, 60, 70, 80], [20], [20, 30], [20, 30, 40], [20, 30, 40, 50], [20, 30, 40, 50, 60], [20, 30, 40, 50, 60, 70], [20, 30, 40, 50, 60, 70, 80], [30], [30, 40], [30, 40, 50], [30, 40, 50, 60], [30, 40, 50, 60, 70], [30, 40, 50, 60, 70, 80], [40], [40, 50], [40, 50, 60], [40, 50, 60, 70], [40, 50, 60, 70, 80], [50], [50, 60], [50, 60, 70], [50, 60, 70, 80], [60], [60, 70], [60, 70, 80], [70], [70, 80], [80]]




# dict1 = {'I':1, 'II' : 2, 'III' : 3, 'IV' : 4 ,'V':5 , 'VI' : 6, 'VII' : 7, 'VIII' : 8, 'IX' : 9,  'X':10, 'L':50, 'C':100, 
# 'D':500}

# str1 = 'IV'

# while 




# # str1 = 'CDXXXVVVVIV'

# # sum = 0
# # for i in str1:
# #     sum+=dict1[i]

# # str2 = ''

# # val = [i for i in dict1.values()]
# # key1 = [i for i in dict1.keys()]
# # list1 = [[i,j] for i,j in dict1.items()]   # [['I', 1], ['V', 5], ['X', 10], ['L', 50], ['C', 100], ['D', 500], ['M', 1000]]


# # from bidict import bidict
# # dict2 = bidict(dict1)
# # dict3 = dict2.inverse

# # for key,j in dict1.items():
# #         print("sum-----------------------------------------",sum)
# #         # v1 = [s[1] for s in list1]
# #         if sum in val:
# #             str2 += dict3[sum]
# #             print(str2, '------')
# #             break

# #         for i in val[::-1]:
# #             if sum == 1:
# #                 str2 += 'I'
# #                 print(str2)
# #                 break
# #             if sum > i:
# #                 temp = i
# #                 break
# #         if sum == 1:
# #              break
        
# #         ans = sum / temp   # 2

# #         if 1:
# #             ans = sum // temp
# #             # print("temp",temp)
# #             for x,y in dict1.items():
# #                 if y == temp:
# #                     str2+= (x * ans)
# #                     # print('str2',str2)
# #                     # print(f"sum = {sum}, j = {y}, ans = {ans}, temp = {temp}")
# #                     break
           
# #             sum = sum % temp
# #             # print(sum,ans,temp)
# #             if sum == 0:
# #                 print(str2)
# #                 break
# #         if sum == 0:
# #             print(str2)
# #             break


# def factorial(n):
#     mul = 1
#     for j in range(1,n+1):
#         mul *= j
#     return mul


list1 = [50, 60, 70, 40, 45, 35, 55, 61, 62, 48]

min  = list1[0]
day = -1
for j in range(len(list1)):
    if min > list1[j]:
        min = list1[j]
        day = j
print(min, day)    # 35

max  = list1[0]
day1 = 0
for j in range(len(list1)):
    if min < list1[j]:
        max = list1[j]
        day1 = j


print(max, day1)    # 35