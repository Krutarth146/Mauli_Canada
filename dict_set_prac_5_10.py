dict1 = {'Name' : 'Mauli', 'Roll' : 900, 'address' : [10,20,30,40]}

print(dict1)   # {'Name': 'Mauli', 'Roll': 900, 'address': [10, 20, 30, 40]}

t = ()
print(type(t))  # Tuple

t = (10)
print(type(t))  # int

t = (10,)
print(type(t))  # tuple

f = {}
print(type(f))  # dict


f = {19}
print(type(f))  # set

f = {'Name' : 90}
print(type(f))  # dict

mauli = set()
print(type(mauli))   # <class 'set'>

dict1 = {'Name' : 'Mauli', 'Roll' : 900, 'address' : [10,20,30,40]}

for j in dict1:
    print(j)   # Name  Roll  address

for j in dict1.keys():
    print(j)   # Name  Roll  address

for j in dict1.values():
    print(j)   # Mauli   900   [10,20,30,40]

for k in dict1.items():
    print(k)
# ('Name', 'Mauli')
# ('Roll', 900)
# ('address', [10, 20, 30, 40])

for key, val in dict1.items():
    print(key,'---->',val)
# ('Name', 'Mauli')
# ('Roll', 900)
# ('address', [10, 20, 30, 40])

# Dictionary : Keys Unique (Don't Allow Duplicates), Ordered

dict1 = {'Name' : 'Krutarth', 'Name' : 'Manoj', 'ROll' : ('Manoj', 'Manoj')}
print(dict1)   # {'Name': 'Manoj', 'ROll': ('Manoj', 'Manoj')}

print(dict1['Name'])   # Manoj
# print(dict1['Manoj'])   # Error


for k,v in dict1.items():
    if v == 'Manoj': 
        print(k)   # Name
        break

dict1 = {'Name' : 'Krutarth', 'Name' : 'Manoj', 'ROll' : ('Manoj', 'Manoj')}

from bidict import bidict

dict2 = bidict(dict1)
print(type(dict2))   # <class 'bidict.bidict'>

print(dict2)   # bidict({'Name': 'Manoj', 'ROll': ('Manoj', 'Manoj')})

dict3 = dict2.inverse

print(dict3)   # bidict({'Manoj': 'Name', ('Manoj', 'Manoj'): 'ROll'})
print(dict3['Manoj'])   # Name


dict8 = {'Name' : 'Ramesh', 'ROll' : 90, 'address' : [{'City' : [{'Ahm' : {'Area' : 'Income Tax', 'money' : [10,20,]}}, {'Gnr' : 80}]}]}

print(dict8['address'])   # [{'City': [{'Ahm': {'Area': 'Income Tax', 'money': [10, 20]}}, {'Gnr': 80}]}]
print(len(dict8['address']))   # 1
print(len(dict8['address'][0]))    # {'City': [{'Ahm': {'Area': 'Income Tax', 'money': [10, 20]}}, {'Gnr': 80}]}
print(dict8['address'][-1])   # {'City': [{'Ahm': {'Area': 'Income Tax', 'money': [10, 20]}}, {'Gnr': 80}]}
print(dict8['address'][-1])   # {'City': [{'Ahm': {'Area': 'Income Tax', 'money': [10, 20]}}, {'Gnr': 80}]}
print(dict8['address'][-1]['City'])   # [{'Ahm': {'Area': 'Income Tax', 'money': [10, 20]}}, {'Gnr': 80}]
print(dict8['address'][-1]['City'][0])   # {'Ahm': {'Area': 'Income Tax', 'money': [10, 20]}}
print(dict8['address'][-1]['City'][-2])   # {'Ahm': {'Area': 'Income Tax', 'money': [10, 20]}}
print(dict8['address'][-1]['City'][-2]['Ahm'])   # {'Area': 'Income Tax', 'money': [10, 20]}
print(dict8['address'][-1]['City'][-2]['Ahm']['money'])   # [10, 20]
print(dict8['address'][-1]['City'][-2]['Ahm']['money'][-1])   # 20  # int
print(dict8['address'][-1]['City'][-2]['Ahm']['money'][-1:])   # [20]  # list


str1 = 'Mauli'

ans = {'M' : 'mmm', 'A' : 'aaa', 'U' : 'uuu', 'L' : 'lll', 'I' : 'iii'}


# ans['K'] = "kkk"
# ans['U'] = "yyy"

# ans.update({'K' : 'kkk'})
# print(ans)

res = {k.upper() : k.lower() * 3 for k in str1}
print(res)   # {'M': 'mmm', 'A': 'aaa', 'U': 'uuu', 'L': 'lll', 'I': 'iii'}

list1 = [10,14,24,23,12,56]

# ans1 = {10 : [1,2,5,10], 14 : [1,2,7,14] ....}  1. Simple   2. Comprehension

# list1 = [10,20,94,34,12]
# temp = []
# dict2 = {}
# for x in list1:
#     for k in range(1,x+1):
#         if x % k == 0:
#             temp.append(k)

#     dict2[x] = temp
#     # print(temp, dict2)
#     temp = []
#     # print(temp, dict2)

# print(dict2)

# Dictionary Comprehension    

print({x : [k for k in range(1,x+1) if x % k == 0] for x in list1 })