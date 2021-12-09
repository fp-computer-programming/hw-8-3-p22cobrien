# Author: CMOB 12/9/2021

def sum_odds(num):
    total = 0
    x = 0
    while x < len(num):
        if num[x] % 2 != 0:
            total += num[x]
            x += 1
        else:
            x += 1
    
    return total

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)

print(sum_odds([1, 2, 3, 4, 5, 6]))
print(sum_odds([1, 3, 5, 7, 9]))
print(sum_odds([4, 6, 8, 10]))
