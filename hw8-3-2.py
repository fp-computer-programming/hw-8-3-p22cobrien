# Author: CMOB 12/8/2021

def sum_no_odd(num):
    total = 0
    trig = True
    while trig == True:
        for x in num:
            if x % 2 != 0:
                break
            else:
               total += x
    return total

print(sum_no_odd([2, 4, 5]))