# 2 ** 6  ----> 2*2*2*2*2*2

num = 4
mul = 1
k = 1
while k <= 3:    # k = 3
    mul = mul * num  # 64 = 16 * 4
    k+=1

print(mul)   # 64

# ----------------------------------------------------------------
for num in range(1,10001):
    x1 = num
    x2 = num

    digit = 0

    while num > 0:
        num = num // 10   # num = 0
        digit+=1   # digit = 4

    # print(digit)   # 4
    sum = 0

    while x1 > 0:   # 8208
        rem = x1 % 10   # rem = 8
        h = 1
        mul = 1
        while h <= digit:
            mul = mul * rem   # 4096 = 8 * 8  
            h+=1
        # sum = sum + rem ** digit
        sum = sum + mul   # 0 + (8**4)   # sum = 4096 + 0 + 16 + 4096   # 8 ** 4   153 ---> 3*3*3 + 5*5*5 + 1*1*1
        x1 = x1 // 10  # x1 = 0

    print(sum)
    num = x2