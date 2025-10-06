def linear_search(list,val):
    for i in range(len(list)):
        if list[i] == val:
            return i
    return None

nums = list(range(1,11))

print(linear_search(nums,6))