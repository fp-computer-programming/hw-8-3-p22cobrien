# Author: CMOB 12/8/2021

def sum_no_odd(num):
    total = 0
    x = 0
    z = 0
    while x < len(num):
        if num[x] % 2 == 0:
            total += num[x]
            x += 1
        else:
            x += len(num) + 9
    return total

print(sum_no_odd([2, 4, 5]))
print(sum_no_odd([2, 4, 6, 8, 9]) == 20)
print(sum_no_odd([13, 12, 10]) == 0)
print(sum_no_odd([14, 16, 32]) == 62)