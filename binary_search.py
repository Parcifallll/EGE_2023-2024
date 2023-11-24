from math import floor, ceil
import time
my_list = list(range(100_000_000))


def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = ceil((high + low) / 2)
        guess = lst[mid]
        if guess == item:
            return [mid]
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
start_bin = time.time()
binary_search(my_list, 100_000_000)
end_bin = time.time() - start_bin

def linear_search(lst, item):
    for x in lst:
        if x == item:
            return x
            break
start_line = time.time()
linear_search(my_list, 100_000_000)
end_line = time.time() - start_line
print(end_bin, end_line)
