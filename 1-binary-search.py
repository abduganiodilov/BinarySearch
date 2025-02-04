import math
import random

def binary_search(lst, item):
    low = 0
    high = len(lst)-1

    while low <= high:
        mid = math.floor((low+high)/2)
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lst = [i+1 for i in range(1000000)]
print(binary_search(lst, random.choice(lst)))


